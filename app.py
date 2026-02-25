import os
import subprocess
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

LATEX_TEMPLATE_PATH = "latex_templates/template.tex"
OUTPUT_FOLDER = "output"

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    score = request.form["score"]

    # Read LaTeX template
    with open(LATEX_TEMPLATE_PATH, "r") as file:
        latex_content = file.read()

    # Replace placeholders
    latex_content = latex_content.replace("{{NAME}}", name)
    latex_content = latex_content.replace("{{SCORE}}", score)

    # Create output tex file
    tex_path = os.path.join(OUTPUT_FOLDER, "output.tex")
    with open(tex_path, "w") as file:
        file.write(latex_content)

    # Compile LaTeX to PDF
    subprocess.run([
        "pdflatex",
        "-output-directory", OUTPUT_FOLDER,
        tex_path
    ])

    pdf_path = os.path.join(OUTPUT_FOLDER, "output.pdf")

    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    app.run(debug=True)
