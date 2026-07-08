from models.project_model import ProjectModel


class DTOGenerator:

    @staticmethod
    def generate(project: ProjectModel) -> str:

        method = project.methods[0]

        fields = []

        getters_setters = []

        for attribute in method.output_attributes:

            fields.append(f"    private String {attribute.display_name.lower()};")

            name = attribute.display_name

            field = attribute.display_name.lower()

            getters_setters.append(f"""
    public String get{name}() {{
        return {field};
    }}

    public void set{name}(String {field}) {{
        this.{field} = {field};
    }}
""")

        fields_text = "\n".join(fields)

        getters_text = "\n".join(getters_setters)

        return f"""package {project.java_package}.model;

public class SPSModificationList{project.project_name} {{

{fields_text}

{getters_text}

}}
"""
