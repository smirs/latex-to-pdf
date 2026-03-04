import os
import subprocess

OUTPUT_FOLDER = "output"
TEX_DIR = "latex_templates"
MAIN_TEX_FILE = "payments_day1.tex"

def generate_payments_day1_pdf(form_data):
    with open(os.path.join(TEX_DIR, MAIN_TEX_FILE), "r") as f:
        latex_content = f.read()

    placeholders = {
        "{{TENANTNAME}}": form_data.get("tenantname", ""),
        "{{PROPERTYADDRESS}}": form_data.get("propertyaddress", ""),
        "{{COMMENCEMENT}}": form_data.get("commencement", ""),
        "{{LEASESTART}}": form_data.get("leasestart", ""),
        "{{RENT}}": form_data.get("rent", ""),
        "{{SECURITYDEPOSIT}}": form_data.get("securitydeposit", ""),
        "{{PETDEPOSIT}}": form_data.get("petdeposit", ""),
        "{{NUMPETS}}": form_data.get("numpets", ""),
        "{{OTHERFEES}}": form_data.get("otherfees", ""),
    }

    for k, v in placeholders.items():
        latex_content = latex_content.replace(k, v)

    tex_filename = "output_payments_day1.tex"
    tex_path = os.path.join(TEX_DIR, tex_filename)
    with open(tex_path, "w") as f:
        f.write(latex_content)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_path = os.path.join(OUTPUT_FOLDER, "output_payments_day1.pdf")

    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory", os.path.abspath(OUTPUT_FOLDER), tex_filename],
        cwd=os.path.abspath(TEX_DIR),
        capture_output=True, text=True
    )

    if result.returncode != 0:
        return False, f"Compilation failed:\n{result.stdout}\n{result.stderr}"

    return True, pdf_path