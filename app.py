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
    name = request.form["name"]
    address = request.form["address"]
    moveindate = request.form["moveindate"]
    # Read the main LaTeX template
    main_tex_path = os.path.join(TEX_DIR, LEASE_TEX_FILE)
    with open(main_tex_path, "r") as file:
        latex_content = file.read()

    # Replace placeholders
    latex_content = latex_content.replace("{{NAME}}", name)
    latex_content = latex_content.replace("{{ADDRESS}}", address)
    latex_content = latex_content.replace("{{MOVEINDATE}}", moveindate)


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


@app.route("/generate-pdf", methods=["POST"])
def generate_pdf():
    template_type = request.form["template_type"]
    landlord_name = request.form["landlord_name"]
    tenant_name = request.form["tenant_name"]
    start_date = request.form["start_date"]
    rent = request.form["rent"]

    # 1️⃣ Inject variables into LaTeX template
    with open("templates/lease_template.tex") as f:
        latex_content = f.read()

    latex_content = latex_content.replace("{{landlord_name}}", landlord_name)
    latex_content = latex_content.replace("{{tenant_name}}", tenant_name)
    latex_content = latex_content.replace("{{start_date}}", start_date)
    latex_content = latex_content.replace("{{rent}}", rent)

    output_tex = "output.tex"
    with open(output_tex, "w") as f:
        f.write(latex_content)

    # 2️⃣ Compile LaTeX
    subprocess.run(["pdflatex", output_tex])

    return send_file("output.pdf", as_attachment=True)