from pathlib import Path


class Settings:
    """
    Global application settings.
    """

    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    TEMPLATE_FOLDER = PROJECT_ROOT / "templates"

    OUTPUT_FOLDER = Path(r"C:\share\WindchillRestServices")

    # Windchill folder names
    CODEBASE_FOLDER = "codebase"

    SRC_FOLDER = "src"

    REST_FOLDER = "rest"

    CUSTOM_FOLDER = "custom"

    DOC_FOLDER = "doc"

    DOMAIN_FOLDER = "domain"

    VERSION_FOLDER = "v1"

    COMPLEXTYPE_FOLDER = "complexType"

    EXT_FOLDER = "ext"

    GEODE_FOLDER = "geode"

    SPSQUERY_FOLDER = "spsquery"
