import json

from models.project_model import ProjectModel


class SchemaGenerator:

    @staticmethod
    def generate(project: ProjectModel) -> str:

        method = project.methods[0]

        properties = []

        for attribute in method.output_attributes:

            properties.append(
                {
                    "name": attribute.dto_field_name,
                    "type": attribute.data_type,
                    "isCollection": False,
                    "isNullable": True,
                }
            )

        schema = {"name": method.return_type, "properties": properties}

        return json.dumps(schema, indent=4)
