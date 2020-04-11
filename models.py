from datetime import datetime
from config import db, ma, base_url


class Image(db.Model):
    __tablename__ = 'image'
    image_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(32))
    tag = db.Column(db.String(64))
    name = db.Column(db.String(64), unique=True, nullable=False)
    image_url = db.Column(db.String(32))
    orientation = db.Column(db.String(32))
    description = db.Column(db.String(100))
    season = db.Column(db.String(32))
    stars = db.Column(db.String(32))
    comments = db.Column(db.String(100))
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ImageSchema(ma.ModelSchema):
    class Meta:
        model = Image
        sqla_session = db.session
