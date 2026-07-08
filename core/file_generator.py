from pathlib import Path


class FileGenerator:
    """
    Writes generated content to files.
    """

    @staticmethod
    def write(file_path: Path, content: str):
        """
        Writes content to the specified file.
        Creates parent folders if they don't exist.
        """

        file_path.parent.mkdir(parents=True, exist_ok=True)

        file_path.write_text(content, encoding="utf-8")
