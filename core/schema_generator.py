import json

from models.project_model import ProjectModel


class SchemaGenerator:

    @staticmethod
    def generate(project: ProjectModel) -> str:

        method = project.methods[0]

        attributes = []

        for attribute in method.output_attributes:

            attributes.append(
                {
                    "name": attribute.display_name,
                    "internalName": attribute.dto_field_name,
                    "type": attribute.data_type,
                    "required": False,
                }
            )

        schema = {
            "name": method.return_type,
            "description": f"Schema defining attributes for {method.return_type}",
            "attributes": attributes,
        }

        return json.dumps(schema, indent=2)
