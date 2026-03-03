import os
import subprocess

OUTPUT_FOLDER = "output"
TEX_DIR = "latex_templates"
LEASE_TEX_FILE = "lease.tex"

def generate_lease_pdf(form_data):
    with open(os.path.join(TEX_DIR, LEASE_TEX_FILE), "r") as f:
        latex_content = f.read()

    placeholders = {
        "{{TENANTNAME}}": form_data.get("tenantname", ""),
        "{{TENANTADDRESS}}": form_data.get("tenantaddress", ""),
        "{{LANDLORDNAME}}": form_data.get("landlordname", ""),
        "{{LANDLORDADDRESS}}": form_data.get("landlordaddress", ""),
        "{{STARTDATE}}": form_data.get("startdate", ""),
        "{{ENDDATE}}": form_data.get("enddate", ""),
        "{{DURATION}}": form_data.get("duration", ""),
        "{{COMMENCEMENT}}": form_data.get("moveindate", ""),
        "{{RENT}}": form_data.get("rent", ""),
        "{{LATEFEE}}": form_data.get("latefee", ""),
        "{{SECURITYDEPOSITE}}": form_data.get("securitydeposit", ""),
        "{{MAXTENANTS}}": form_data.get("maxtenants", ""),
        "{{PROPERTYADDRESS}}": form_data.get("property_address", ""),
        "{{STATE}}": form_data.get("state", ""),
        "{{CITY}}": form_data.get("city", ""),
        "{{COUNTY}}": form_data.get("county", "")
    }

    for k, v in placeholders.items():
        latex_content = latex_content.replace(k, v)

    tex_filename = "output_lease.tex"
    tex_path = os.path.join(TEX_DIR, tex_filename)
    with open(tex_path, "w") as f:
        f.write(latex_content)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_path = os.path.join(OUTPUT_FOLDER, "output_lease.pdf")

    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-output-directory", os.path.abspath(OUTPUT_FOLDER), tex_filename],
        cwd=os.path.abspath(TEX_DIR),
        capture_output=True, text=True
    )

    if result.returncode != 0:
        return False, f"Compilation failed:\n{result.stdout}\n{result.stderr}"

    return True, pdf_path