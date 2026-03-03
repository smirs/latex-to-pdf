import os
import subprocess

OUTPUT_FOLDER = "output"
TEX_DIR = "latex_templates"
NOTICE_TEX_FILE = "notice.tex"

def generate_notice_pdf(form_data):
    with open(os.path.join(TEX_DIR, NOTICE_TEX_FILE), "r") as f:
        latex_content = f.read()

    placeholders = {
        "{{TENANTNAME}}": form_data.get("tenantname", ""),
        "{{PROPERTYADDRESS}}": form_data.get("propertyaddress", ""),
        "{{NOTICEDATE}}": form_data.get("noticedate", ""),
        "{{NOTICETYPE}}": form_data.get("noticetype", "")
    }

    for k, v in placeholders.items():
        latex_content = latex_content.replace(k, v)

    tex_filename = "output_notice.tex"
    tex_path = os.path.join(TEX_DIR, tex_filename)
    with open(tex_path, "w") as f:
        f.write(latex_content)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_path = os.path.join(OUTPUT_FOLDER, "output_notice.pdf")

    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory", os.path.abspath(OUTPUT_FOLDER), tex_filename],
        cwd=os.path.abspath(TEX_DIR),
        capture_output=True, text=True
    )

    if result.returncode != 0:
        return False, f"Compilation failed:\n{result.stdout}\n{result.stderr}"

    return True, pdf_path