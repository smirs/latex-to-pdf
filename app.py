import os
import subprocess
from flask import Flask, render_template, request, send_file

app = Flask(__name__, static_url_path='/')

# Folder where all LaTeX templates and dependencies live
TEX_DIR = "latex_templates"
MAIN_TEX_FILE = "template.tex"  # main LaTeX file inside TEX_DIR
LEASE_TEX_FILE = "lease.tex"  # main LaTeX file inside TEX_DIR

OUTPUT_FOLDER = "output"

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/generate-commencement", methods=["POST"])
def generate_commencement():
    name = request.form["name"]
    address = request.form["address"]
    moveindate = request.form["moveindate"]
    # Read the main LaTeX template
    main_tex_path = os.path.join(TEX_DIR, MAIN_TEX_FILE)
    with open(main_tex_path, "r") as file:
        latex_content = file.read()

    # Replace placeholders
    latex_content = latex_content.replace("{{NAME}}", name)
    latex_content = latex_content.replace("{{ADDRESS}}", address)
    latex_content = latex_content.replace("{{MOVEINDATE}}", moveindate)


    # Create output tex file inside TEX_DIR
    tex_filename = "output.tex"
    tex_path = os.path.join(TEX_DIR, tex_filename)
    with open(tex_path, "w") as file:
        file.write(latex_content)

    # Ensure output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_path = os.path.join(OUTPUT_FOLDER, "output.pdf")

    # Compile LaTeX to PDF **from TEX_DIR** so \input works
    result = subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory", os.path.abspath(OUTPUT_FOLDER),
            tex_filename
        ],
        cwd=os.path.abspath(TEX_DIR),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"<h3>LaTeX compilation failed:</h3><pre>{result.stdout}\n{result.stderr}</pre>"

    return send_file(pdf_path, as_attachment=True)

@app.route("/generate-lease", methods=["POST"])

def generate_lease():

    tenantname = request.form["tenantname"]
    tenantaddress = request.form["tenantaddress"]
    tenantemail = request.form["tenantemail"]
    tenantphone = request.form["tenantphone"]

    startdate = request.form["startdate"]
    enddate = request.form["enddate"]
    duration = request.form["duration"]
    moveindate = request.form["moveindate"]
    rent = request.form["rent"]
    securitydeposit = request.form["securitydeposit"]
    maxtenants = request.form["maxtenants"]

    property_address = request.form.get("property_address")
    state = request.form.get("state")
    city = request.form.get("city")
    county = request.form.get("county")
    
    # Read the main LaTeX template
    main_tex_path = os.path.join(TEX_DIR, LEASE_TEX_FILE)
    with open(main_tex_path, "r") as file:
        latex_content = file.read()

    # Replace placeholders
    latex_content = latex_content.replace("{{TENANTNAME}}", tenantname)
    latex_content = latex_content.replace("{{TENANTADDRESS}}", tenantaddress)
    latex_content = latex_content.replace("{{TENANTEMAIL}}", tenantemail)
    latex_content = latex_content.replace("{{TTENANTPHONES}}", tenantphone)

    latex_content = latex_content.replace("{{STARTDATE}}", startdate)
    latex_content = latex_content.replace("{{ENDDATE}}", enddate)
    latex_content = latex_content.replace("{{DURATION}}", duration)
    latex_content = latex_content.replace("{{COMMENCEMENT}}", moveindate)
    latex_content = latex_content.replace("{{RENT}}", rent)
    latex_content = latex_content.replace("{{SECURITYDEPOSITE}}", securitydeposit)
    latex_content = latex_content.replace("{{RMAXTENANTST}}", maxtenants)

    latex_content = latex_content.replace("{{PROPERTYADDRESS}}", property_address)
    latex_content = latex_content.replace("{{STATE}}", state)
    latex_content = latex_content.replace("{{CITY}}", city)
    latex_content = latex_content.replace("{{COUNTY}}", county)

    # Create output tex file inside TEX_DIR
    tex_filename = "output_lease.tex"
    tex_path = os.path.join(TEX_DIR, tex_filename)
    with open(tex_path, "w") as file:
        file.write(latex_content)

    # Ensure output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_path = os.path.join(OUTPUT_FOLDER, "output_lease.pdf")

    # Compile LaTeX to PDF **from TEX_DIR** so \input works
    result = subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",
            "-output-directory", os.path.abspath(OUTPUT_FOLDER),
            tex_filename
        ],
        cwd=os.path.abspath(TEX_DIR),
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return f"<h3>LaTeX compilation failed:</h3><pre>{result.stdout}\n{result.stderr}</pre>"

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True, host="0.0.0.0", port=5000)

