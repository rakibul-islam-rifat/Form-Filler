# Form Filler

A Python automation tool for programmatically filling PDF forms — single fill from a dictionary or bulk fill from a CSV file.

---

## Features

- Detect and list all fillable fields in any PDF form
- Fill text fields, checkboxes, and dropdowns programmatically
- Bulk fill from a CSV file — one output PDF per row
- Optional flattening — converts filled fields into static, non-editable content
- Clean logging throughout

---

## Project Structure

```
Form-Filler/
│
├── form_filler.py        # FormFiller class — core logic
├── generate_test_pdf.py  # Generates a sample fillable PDF for testing
├── main.py               # Interactive CLI entry point
├── logger_setup.py       # Rotating file handler logging setup
├── sample_form.pdf       # Sample fillable PDF (generated)
├── sample_data.csv       # Sample bulk data for testing
├── Output/               # Filled PDFs are saved here
└── README.md
```

---

## Installation

```bash
git clone https://github.com/rakibul-islam-rifat/Form-Filler.git
cd Form-Filler
pip install pymupdf pypdf reportlab
```

---

## Usage

### Run the interactive CLI

```bash
python main.py
```

The script will:
1. Ask for the template PDF path
2. Print all available field names
3. Ask for the CSV path and name field
4. Ask whether to flatten the output
5. Generate filled PDFs into the `Output/` folder

---

## CSV Format

CSV headers must match the field names exactly as shown by the tool.

Example for the sample form:

```csv
full_name,email,phone,position,full_time,experience
Rifat Islam,rifat@email.com,01712345678,Python Developer,True,1-3
John Doe,john@email.com,01798765432,Data Analyst,False,3-5
Sarah Ahmed,sarah@email.com,01756781234,ML Engineer,True,5+
```

- **Checkbox fields** accept `True` or `False`
- **Dropdown fields** accept one of the predefined options in the form
- The `name_field` column is used to name each output PDF file

---

## Generate a Test PDF

```bash
python generate_test_pdf.py
```

Creates `sample_form.pdf` with text fields, a checkbox, and a dropdown — ready to test against.

---

## Programmatic Usage

```python
from form_filler import FormFiller

filler = FormFiller("sample_form.pdf")

# List all fields
print(filler.list_fields())

# Fill a single form
filler.fill({
    "full_name": "John Doe",
    "email": "john@email.com",
    "phone": "01798765432",
    "position": "Data Analyst",
    "full_time": "False",
    "experience": "3-5"
}, output_path="john_doe", flatten=True)

# Bulk fill from CSV
filler.fill_from_csv(
    csv_path="sample_data.csv",
    name_field="full_name",
    flatten=True
)
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `pymupdf` | PDF form filling and flattening |
| `pypdf` | Reading form field names |
| `reportlab` | Generating test fillable PDFs |

---

## Author

**MD Rakibul Islam Rifat** — [GitHub](https://github.com/rakibul-islam-rifat) · [Fiverr](https://www.fiverr.com/rifat_automates)