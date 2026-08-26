import streamlit as st
from config.windchill_objects import OBJECTS
from core.project_builder import ProjectBuilder
from core.project_generator import ProjectGenerator
from core.retrieval.registry import STRATEGIES

st.set_page_config(page_title="Windchill REST Studio", page_icon="🚀", layout="wide")

st.title("🚀 Windchill REST Studio")

st.markdown("---")

project_name = st.text_input("Project Name", placeholder="Example : IA4AE")

root_object = st.selectbox("Root Object", list(OBJECTS.keys()))

retrieval_strategy = st.selectbox(
    "Retrieval Strategy",
    options=list(STRATEGIES.keys()),
    format_func=lambda key: STRATEGIES[key].display_name,
)

st.markdown("---")

st.subheader("Output Attributes")

selected_attributes = []

windchill_object = OBJECTS[root_object]

for attribute in windchill_object.attributes:

    if st.checkbox(attribute.display_name):

        selected_attributes.append(attribute)

if st.button("🚀 Generate Project", type="primary"):

    if not project_name.strip():
        st.error("Please enter a Project Name.")
        st.stop()

    builder = ProjectBuilder()

    project = builder.build(
        project_name=project_name,
        root_object=root_object,
        retrieval_strategy=retrieval_strategy,
        output_attributes=selected_attributes,
    )

    ProjectGenerator.generate(project)

    st.success("✅ Project generated successfully!")
