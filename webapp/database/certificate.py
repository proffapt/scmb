import hashlib
from . import db
from typing import List
from datetime import datetime
from models.error import DB_Error
from models.certificate import Certificate, CertificateType


def get_all_certificates() -> List[Certificate] | DB_Error:
    try:
        certificates: List[Certificate] = Certificate.query.all()
        return certificates
    except Exception as e:
        return {"db_error": str(e)}


def get_all_certificates_by_shipment(shipment: str) -> List[Certificate] | DB_Error:
    try:
        certificates: List[Certificate] = Certificate.query.filter_by(
            shipment=shipment).all()
        return certificates
    except Exception as e:
        return {"db_error": str(e)}


def get_all_certificates_by_issuer(issuer: str) -> List[Certificate] | DB_Error:
    try:
        certificates: List[Certificate] = Certificate.query.filter_by(
            issuer=issuer).all()
        return certificates
    except Exception as e:
        return {"db_error": str(e)}


def get_certificate(id: int) -> Certificate | DB_Error:
    try:
        certificate: Certificate = Certificate.query.get(id)
        if certificate:
            return certificate
        else:
            return {"db_error": "Certificate not found"}
    except Exception as e:
        return {"db_error": str(e)}


def get_certificate_pdf_path(id: int) -> str | DB_Error:
    try:
        certificate: Certificate | DB_Error = get_certificate(id)
        if isinstance(certificate, Certificate):
            return certificate.pdf_path
        else:
            return certificate
    except Exception as e:
        return {"db_error": str(e)}


def create_certificate(certificate_details: CertificateType) -> Certificate | DB_Error:
    try:
        pdf_path = certificate_details.get("pdf_path")
        with open(pdf_path, 'rb') as file:
            pdf_data: bytes = file.read()
        # Calculate hash of stored pdf file
        pdf_hash = hashlib.sha256(pdf_data).hexdigest()

        certificate: Certificate = Certificate(
            timestamp=datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            shipment=certificate_details.get("shipment"),
            issuer=certificate_details.get("issuer"),
            pdf_path=pdf_path,
            pdf_hash=pdf_hash
        )
        db.session.add(certificate)
        db.session.commit()
        return certificate
    except Exception as e:
        return {"db_error": str(e)}


def update_certificate(certificate_details: CertificateType) -> Certificate | DB_Error:
    try:
        pdf_path = certificate_details.get("pdf_path")
        with open(pdf_path, 'rb') as file:
            pdf_data: bytes = file.read()
        # Calculate hash of stored pdf file
        pdf_hash = hashlib.sha256(pdf_data).hexdigest()

        certificate_id = certificate_details.get("id")
        certificate: Certificate | DB_Error = get_certificate(certificate_id)
        if isinstance(certificate, Certificate):
            certificate.timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            certificate.shipment = certificate_details.get("shipment")
            certificate.issuer = certificate_details.get("issuer")
            certificate.pdf_path = pdf_path,
            certificate.pdf_hash = pdf_hash
            db.session.commit()
            return certificate
        else:
            return certificate
    except Exception as e:
        return {"db_error": str(e)}


def delete_certificate(id: int) -> Certificate | DB_Error:
    try:
        certificate: Certificate | DB_Error = get_certificate(id)
        if isinstance(certificate, Certificate):
            db.session.delete(certificate)
            db.session.commit()
            return certificate
        else:
            return certificate
    except Exception as e:
        return {"db_error": str(e)}
