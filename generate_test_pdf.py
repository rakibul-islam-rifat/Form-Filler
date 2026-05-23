from reportlab.lib.colors import black
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def generate_test_form(output_path="sample_form.pdf"):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Job Application Form")

    c.setFont("Helvetica", 12)

    # Full Name
    c.drawString(50, height - 100, "Full Name:")
    c.acroForm.textfield(
        name="full_name",
        tooltip="Full Name",
        x=180,
        y=height - 110,
        width=300,
        height=20,
        borderColor=black,
        fillColor=None,
        textColor=black,
        forceBorder=True,
    )

    # Email
    c.drawString(50, height - 140, "Email:")
    c.acroForm.textfield(
        name="email",
        tooltip="Email",
        x=180,
        y=height - 150,
        width=300,
        height=20,
        borderColor=black,
        fillColor=None,
        textColor=black,
        forceBorder=True,
    )

    # Phone
    c.drawString(50, height - 180, "Phone:")
    c.acroForm.textfield(
        name="phone",
        tooltip="Phone",
        x=180,
        y=height - 190,
        width=300,
        height=20,
        borderColor=black,
        fillColor=None,
        textColor=black,
        forceBorder=True,
    )

    # Position
    c.drawString(50, height - 220, "Position Applied For:")
    c.acroForm.textfield(
        name="position",
        tooltip="Position Applied For",
        x=220,
        y=height - 230,
        width=260,
        height=20,
        borderColor=black,
        fillColor=None,
        textColor=black,
        forceBorder=True,
    )

    # Full Time checkbox
    c.drawString(50, height - 270, "Available Full Time:")
    c.acroForm.checkbox(
        name="full_time",
        tooltip="Available Full Time",
        x=220,
        y=height - 278,
        size=15,
        borderColor=black,
        fillColor=None,
        forceBorder=True,
    )

    # Experience dropdown
    c.drawString(50, height - 310, "Years of Experience:")
    c.acroForm.choice(
        name="experience",
        tooltip="Years of Experience",
        x=220,
        y=height - 320,
        width=200,
        height=20,
        options=["0-1", "1-3", "3-5", "5+"],
        value="0-1",
        borderColor=black,
        fillColor=None,
        forceBorder=True,
    )

    c.save()
    print(f"Test form generated: {output_path}")


if __name__ == "__main__":
    generate_test_form()
