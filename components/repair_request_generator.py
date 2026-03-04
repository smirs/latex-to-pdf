import os
import subprocess

OUTPUT_FOLDER = "output"
TEX_DIR = "latex_templates"
MAIN_TEX_FILE = "repair_request_form.tex"

def generate_repair_request_pdf(form_data):
    with open(os.path.join(TEX_DIR, MAIN_TEX_FILE), "r") as f:
        latex_content = f.read()

    placeholders = {
        "{{TENANTNAME}}": form_data.get("tenantname", ""),
        "{{PROPERTYADDRESS}}": form_data.get("propertyaddress", ""),
        "{{TENANTPHONE}}": form_data.get("tenantphone", ""),
        "{{TENANTEMAIL}}": form_data.get("tenantemail", "")
    }

    for k, v in placeholders.items():
        latex_content = latex_content.replace(k, v)

    tex_filename = "output_repair_request.tex"
    tex_path = os.path.join(TEX_DIR, tex_filename)
    with open(tex_path, "w") as f:
        f.write(latex_content)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_path = os.path.join(OUTPUT_FOLDER, "output_repair_request.pdf")

    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory", os.path.abspath(OUTPUT_FOLDER), tex_filename],
        cwd=os.path.abspath(TEX_DIR),
        capture_output=True, text=True
    )

    if result.returncode != 0:
        return False, f"Compilation failed:\n{result.stdout}\n{result.stderr}"

    return True, pdf_path