from models.project_model import ProjectModel


class DTOGenerator:

    @staticmethod
    def _generate_imports() -> str:
        pass

    @staticmethod
    def _generate_constructor(project: ProjectModel) -> str:
        pass

    @staticmethod
    def _generate_fields(project: ProjectModel) -> str:

        method = project.methods[0]

        fields = []

        for attribute in method.output_attributes:

            fields.append(
                f"    private {attribute.data_type} {attribute.dto_field_name};"
            )

        return "\n".join(fields)

    @staticmethod
    def _generate_getters_setters(project: ProjectModel) -> str:
        pass

    @staticmethod
    def _generate_to_odata(project: ProjectModel) -> str:
        pass

    @staticmethod
    def generate(project: ProjectModel) -> str:

        method = project.methods[0]

        fields = []

        getters_setters = []

        to_odata = []

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

            to_odata.append(f"""        resultComplexValue.getValue().add(
                        new Property(
                            null,
                            "{attribute.dto_field_name}",
                            {attribute.odata_type},
                            get{attribute.dto_field_name[0].upper() + attribute.dto_field_name[1:]}()
                        )
                    );""")

        fields_text = DTOGenerator._generate_fields(project)

        getters_text = "\n".join(getters_setters)

        to_odata_text = "\n\n".join(to_odata)

        to_odata_method = f"""
            public Property toOData() {{

                ComplexValue resultComplexValue = new ComplexValue();

        {to_odata_text}

                return new Property(
                    oDataObjectType,
                    null,
                    ValueType.COMPLEX,
                    resultComplexValue
                );
            }}
        """

        constructor = f"""
            private final String oDataObjectType;

            public SPSModificationList{project.project_name}(String oDataObjectType) {{

                this.oDataObjectType = oDataObjectType;

            }}
        """

        to_odata_method = f"""
            public Property toOData() {{

                ComplexValue resultComplexValue = new ComplexValue();

        {to_odata_text}

                return new Property(
                    oDataObjectType,
                    null,
                    ValueType.COMPLEX,
                    resultComplexValue
                );
            }}
        """

        return f"""package {project.java_package}.model;

        import org.apache.olingo.commons.api.data.ComplexValue;
        import org.apache.olingo.commons.api.data.Property;
        import org.apache.olingo.commons.api.data.ValueType;

        public class SPSModificationList{project.project_name} {{

        {constructor}

        {fields_text}

        {getters_text}

        {to_odata_method}

        }}
        """
