from pathlib import Path


class TemplateEngine:
    """
    Reads template files from disk.
    """

    @staticmethod
    def read(template_path: Path) -> str:
        """
        Reads a template file and returns its contents.
        """

        if not template_path.exists():
            raise FileNotFoundError(f"Template not found: {template_path}")

        return template_path.read_text(encoding="utf-8")
