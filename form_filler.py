import csv
import logging
from pathlib import Path
from typing import cast

import pymupdf
import pypdf

logger: logging.Logger = logging.getLogger(__name__)


class FormFiller:
    output_folder: Path = Path(__file__).parent / "Output"

    def __init__(self, template_path: str) -> None:
        self.output_folder.mkdir(exist_ok=True, parents=True)
        self.template_path: Path = Path(template_path)

        if not self.template_path.is_file():
            logger.warning("File not found, %s", self.template_path)
            raise FileNotFoundError(f"Template PDF not found: {self.template_path}")
        if self.template_path.suffix != ".pdf":
            logger.warning("Expected a .pdf file, got: %s", self.template_path.suffix)
            raise ValueError(f"Expected a .pdf file, got: {self.template_path.suffix}")

        logger.info(f"FormFiller initialized with: {self.template_path.name}")

    def list_fields(self) -> list[str]:
        reader = pypdf.PdfReader(self.template_path)

        if (fields := reader.get_fields()) is None:
            logger.warning("No fillable fields found in: %s", self.template_path.name)
            return []

        data_fields: list[str] = list(fields.keys())

        logger.debug("Found %d fields: %s", len(data_fields), data_fields)
        return data_fields

    def fill(
        self,
        data_dict: dict,
        output_path: str = "filled",
        flatten: bool = False,
    ) -> None:

        output: Path = self.output_folder / f"{output_path}.pdf"
        with pymupdf.open(self.template_path) as doc:
            for page in doc:
                for field in page.widgets():
                    widget: pymupdf.Widget = cast(pymupdf.Widget, field)

                    fieldname = widget.field_name
                    if fieldname is None:
                        logger.warning("Found a field with no name, skipping")
                        continue

                    value = data_dict.get(fieldname)
                    if value is None:
                        logger.warning(
                            "No value provided for field: %s, skipping", fieldname
                        )
                        continue

                    if widget.field_type == pymupdf.PDF_WIDGET_TYPE_CHECKBOX:  # type: ignore
                        widget.field_value = value.strip().lower() == "true"
                    else:
                        widget.field_value = value

                    widget.update()

            if flatten:
                doc.bake(widgets=True)  # type: ignore

            doc.save(output)

    def fill_from_csv(
        self,
        csv_path: str,
        name_field: str,
        field_mapping: dict | None = None,
        flatten: bool = False,
    ) -> None:
        form_num = 0
        with open(csv_path, "r", encoding="utf-8", newline="") as rf:
            reader = csv.DictReader(rf)
            if field_mapping and reader.fieldnames:
                reader.fieldnames = [
                    field_mapping.get(col, col)
                    for col in reader.fieldnames  # type: ignore
                ]

            for row in reader:
                output_path: str | None = row.get(name_field)
                if not output_path:
                    logger.error("Missing Field Name. Skipping Form for %s", row)
                    continue

                self.fill(
                    row,
                    output_path=output_path.replace(" ", "_").lower(),
                    flatten=flatten,
                )
                form_num += 1

        logger.info(
            "Filled %d Forms. Please see the Output Folder for more details.\n",
            form_num,
        )
