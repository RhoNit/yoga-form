import datetime as _dt

import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import db.database as _database
# from db.models.payment import TrackPayment


class User(_database.Base):
    __tablename__ = "users"

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name: _sql.Column(_sql.String, nullable=False)
    email: _sql.Column(_sql.String, unique=True, index=True)
    age: _sql.Column(_sql.Integer, nullable=False)
    date_created: _sql.Column(_sql.DateTime, default=_dt.datetime.now().date)

    # leads = _orm.relationship("Lead", back_populates="owner")

    # def verify_password(self, password: str):
    #     return _hash.bcrypt.verify(password, self.hashed_password)