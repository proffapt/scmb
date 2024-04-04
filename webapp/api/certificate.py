import os
from models.certificate import *
from database.certificate import *
from models.error import API_Error, DB_Error
from middleware.auth import login_authorisation
from flask import Response, request, jsonify, send_file


@login_authorisation
def get(id: int | str) -> tuple[Response, int] | tuple[API_Error, int]:
    if isinstance(id, str) and id.casefold() == "all":
        try:
            db_resps: List[Certificate] | DB_Error = get_all_certificates()
            if not isinstance(db_resps, Certificate):
                certificates: List[CertificateType] = [
                    serialize(certificate) for certificate in db_resps]
                return jsonify(certificates), 200
            else:
                return jsonify(db_resps), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500
    else:
        try:
            db_resp: Certificate | DB_Error = get_certificate(int(id))
            if isinstance(db_resp, Certificate):
                certificate: CertificateType = serialize(db_resp)
                return jsonify(certificate), 200
            else:
                return jsonify(db_resp), 400
        except Exception as e:
            return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_shipment(code: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[Certificate] | DB_Error = get_all_certificates_by_shipment(
            code)
        if not isinstance(db_resps, Certificate):
            certificates: List[CertificateType] = [
                serialize(certificate) for certificate in db_resps]
            return jsonify(certificates), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def get_all_by_issuer(username: str) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        db_resps: List[Certificate] | DB_Error = get_all_certificates_by_issuer(
            username)
        if not isinstance(db_resps, Certificate):
            certificates: List[CertificateType] = [
                serialize(certificate) for certificate in db_resps]
            return jsonify(certificates), 200
        else:
            return jsonify(db_resps), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def create_or_update() -> tuple[Response, int] | tuple[API_Error, int]:
    if 'pdf_file' not in request.files:
        return jsonify({"api_error": "A pdf certificate was not provided"}), 400

    pdf = request.files['pdf_file']
    if not pdf:
        return jsonify({"api_error": "Invalid file format"}), 400
    elif pdf.filename == '':
        return jsonify({"api_error": "No selected file"}), 400

    pdf_name: str = request.form.get("pdf_name")
    pdf_name_list: List[str] = pdf_name.split(".")
    if len(pdf_name_list) != 2 or pdf_name_list[1] != "pdf":
        return jsonify({"api_error": "Only pdf format is supported"}), 400

    current_dir: str = os.getcwd()
    shipment_code: str = request.form.get("shipment")
    issuer_username: str = request.form.get("issuer")
    pdf_dir = os.path.join(current_dir, "certificates",
                           shipment_code, issuer_username)
    os.makedirs(pdf_dir, exist_ok=True)

    pdf_path = os.path.join(pdf_dir, pdf_name)
    pdf.save(pdf_path)

    certificate: CertificateType = CertificateType(
        shipment=shipment_code,
        issuer=issuer_username,
        pdf_path=pdf_path,
    )
    if not certificate:
        return jsonify({"api_error": "Certificate details not provided"}), 400

    try:
        if request.method == "PUT":
            db_resp: Certificate | DB_Error = update_certificate(
                certificate)
        else:
            db_resp: Certificate | DB_Error = create_certificate(
                certificate)

        if isinstance(db_resp, Certificate):
            certificate: CertificateType = serialize(db_resp)
            return jsonify(certificate), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def delete(id: int) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        pdf_path: str | DB_Error = get_certificate_pdf_path(id)
        db_resp: Certificate | DB_Error = delete_certificate(id)
        if isinstance(db_resp, Certificate):
            if isinstance(pdf_path, str):
                os.remove(pdf_path)
            certificate: CertificateType = serialize(db_resp)
            return jsonify(certificate), 200
        else:
            return jsonify(db_resp), 400
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500


@login_authorisation
def download(id: int) -> tuple[Response, int] | tuple[API_Error, int]:
    try:
        pdf_path: str | DB_Error = get_certificate_pdf_path(id)
        return send_file(pdf_path, as_attachment=True), 200
    except Exception as e:
        return jsonify({"api_error": str(e)}), 500
