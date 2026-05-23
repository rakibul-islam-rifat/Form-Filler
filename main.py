import logging

from form_filler import FormFiller
from logger_setup import setup_logging

setup_logging("form_filler.log")
logger: logging.Logger = logging.getLogger(__name__)


def get_input(prompt: str) -> str:
    value: str = input(prompt).strip()
    if not value:
        logger.warning("%s cannot be empty", prompt)
        raise ValueError(f"{prompt} cannot be empty")
    return value


def main() -> None:
    print(
        "Please copy the template pdf form into the project and enter the name of the template pdf."
    )
    try:
        template_path: str = get_input("Template Path:- ")
        template_form = FormFiller(template_path)

        print("\nPlease make sure you have these fieldnames in your CSV.\n")
        print(template_form.list_fields())

        print(
            "\nIf you want to continue, add the CSV file in the project and enter the name of the file."
        )
        csv_path: str = get_input("CSV Path :- ")

        print(
            "\nPlease enter the Name Field which will be used to create the form names."
        )
        name_field: str = get_input("Name Field :- ")

        flatten: bool = (
            input("\nDo you want to flatten the PDF form. (y/n):- ").lower() == "y"
        )

        print()

        template_form.fill_from_csv(
            csv_path=csv_path, name_field=name_field, flatten=flatten
        )

    except (FileNotFoundError, ValueError):
        print("\nPlease follow the instruction or contact your developer.")
        return None


if __name__ == "__main__":
    main()
