from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from config.windchill_objects import OBJECTS
from core.project_builder import ProjectBuilder
from core.project_generator import ProjectGenerator
from core.retrieval.registry import STRATEGIES
from web.templating import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def index(request: Request):

    default_root_object = next(iter(OBJECTS))

    return templates.TemplateResponse(
        request,
        "index.html",
        {
            "objects": OBJECTS,
            "strategies": STRATEGIES,
            "selected_root_object": default_root_object,
        },
    )


@router.get("/attributes", response_class=HTMLResponse)
def attributes(request: Request, root_object: str):

    return templates.TemplateResponse(
        request,
        "partials/attributes.html",
        {
            "objects": OBJECTS,
            "selected_root_object": root_object,
        },
    )


@router.post("/generate", response_class=HTMLResponse)
async def generate(request: Request):

    form = await request.form()

    project_name = str(form.get("project_name", "")).strip()
    root_object = str(form.get("root_object", ""))
    retrieval_strategy = str(form.get("retrieval_strategy", ""))
    output_attribute_names = form.getlist("output_attributes")

    if not project_name:
        return templates.TemplateResponse(
            request,
            "partials/result.html",
            {"success": False, "message": "Please enter a Project Name."},
        )

    try:
        windchill_object = OBJECTS[root_object]

        selected_attributes = [
            windchill_object.get_attribute(name) for name in output_attribute_names
        ]

        project = ProjectBuilder().build(
            project_name=project_name,
            root_object=root_object,
            retrieval_strategy=retrieval_strategy,
            output_attributes=selected_attributes,
        )

        ProjectGenerator.generate(project)

    except Exception as error:
        return templates.TemplateResponse(
            request,
            "partials/result.html",
            {"success": False, "message": f"Generation failed: {error}"},
        )

    return templates.TemplateResponse(
        request,
        "partials/result.html",
        {"success": True, "message": f'Project "{project_name}" generated successfully!'},
    )
