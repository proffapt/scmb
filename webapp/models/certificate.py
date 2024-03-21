from database import db
from typing import TypedDict


class Certificate(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    shipment = db.Column(db.String(50), db.ForeignKey(
        'shipment.code'), nullable=False)
    issuer = db.Column(db.String(50), db.ForeignKey(
        'person.username'), nullable=False)
    pdf_path = db.Column(db.String(50), nullable=False)
    pdf_hash = db.Column(db.String(200), nullable=False)


class CertificateType(TypedDict):
    id: int
    timestamp: str
    shipment: str
    issuer: str
    pdf_path: str
    pdf_hash: str


def serialize(certificate: Certificate) -> CertificateType:
    return {
        "id": certificate.id,
        "timestamp": certificate.timestamp.isoformat(),
        "shipment": certificate.shipment,
        "issuer": certificate.issuer,
        "pdf_path": certificate.pdf_path,
        "pdf_hash": certificate.pdf_hash
    }
