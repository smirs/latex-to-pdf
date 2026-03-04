from flask import Flask, render_template, request, send_file
from components.lease_generator import generate_lease_pdf
from components.commencement_generator import generate_commencement_pdf
from components.movein_generator import generate_movein_pdf
from components.notice_generator import generate_notice_pdf
from components.keys_generator import generate_keys_pdf
from components.pets_generator import generate_pets_pdf
from components.maintenanance_generator import generate_maintenance_pdf
from components.parking_generator import generate_parking_pdf
from components.utilities_generator import generate_utilities_pdf
from components.proration_generator import generate_proration_pdf
from components.total_payday1_generator import generate_payments_day1_pdf
from components.repair_request_generator import generate_repair_request_pdf


import os

app = Flask(__name__, static_url_path='/')
os.makedirs("output", exist_ok=True)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/generate-repair-request", methods=["POST"])
def repair_request():
    success, result = generate_repair_request_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-notice", methods=["POST"])
def notice():
    success, result = generate_notice_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-payments-day1", methods=["POST"])
def payments_day1():
    success, result = generate_payments_day1_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-proration", methods=["POST"])
def proration():
    success, result = generate_proration_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-utilities", methods=["POST"])
def utilities():
    success, result = generate_utilities_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-parking", methods=["POST"])
def parking():
    success, result = generate_parking_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-maintenance", methods=["POST"])
def maintenance():
    success, result = generate_maintenance_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-pets", methods=["POST"])
def pets():
    success, result = generate_pets_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-keys", methods=["POST"])
def keys():
    success, result = generate_keys_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-lease", methods=["POST"])
def lease():
    success, result = generate_lease_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-commencement", methods=["POST"])
def commencement():
    success, result = generate_commencement_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)

@app.route("/generate-movein", methods=["POST"])
def movein():
    success, result = generate_movein_pdf(request.form)
    if not success:
        return f"<h3>Error:</h3><pre>{result}</pre>"
    return send_file(result, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)