import enum

from flask_login import UserMixin
from sqlalchemy import Column, String, Boolean, Enum, DATETIME, Double, ForeignKey,INTEGER
from sqlalchemy.orm import relationship

from app import db, app


# User
class UserRoleEnum(enum.Enum):
    khach_hang = 1
    le_tan = 2
    quan_ly = 3


class User(db.Model, UserMixin):
    id = Column(String(45), primary_key=True, nullable=False)
    username = Column(String(45), unique=True, nullable=True)
    password = Column(String(45), nullable=True)
    ten = Column(String(45), nullable=False)
    ho = Column(String(22), nullable=False)
    gioi_tinh = Column(Boolean, nullable=False, default=False)
    ngay_sinh = Column(DATETIME, nullable=True)
    cccd = Column(String(45), nullable=False, unique=True)
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.quan_ly)


# nhan vien

class nhanvien(db.Model):
    id = Column(String(45), ForeignKey(User.id), primary_key=True, nullable=False)
    luong = Column(Double, nullable=False, default=0)


# ca lam viec

class calamviec(db.Model):
    id = Column(String(45), primary_key=True, nullable=False)
    thoi_gian_bat_dau = Column(DATETIME, nullable=False)
    thoi_gian_ket_thuc = Column(DATETIME, nullable=False)


# BAN PHAN CONG
class bangphancong(db.Model):
    id_calamviec = Column(String(45), ForeignKey(calamviec.id), primary_key=True, nullable=False)
    id_nhanvien = Column(String(45), ForeignKey(nhanvien.id), primary_key=True, nullable=False)


# tiennghi
class tiennghi(db.Model):
    id = Column(String(45), primary_key=True, nullable=False)
    ten = Column(String(45), nullable=False)
    tinh_trang = Column(Boolean, nullable=False, default=True)
    gia_tien = Column(Double, nullable=False, default=0)


# loai phong
class loaiphong(db.Model):
    id = Column(String(45), primary_key=True, nullable=False)
    loai_phong = Column(String(45), nullable=False)
    mo_ta = Column(String(255), default="")
    cacphong = relationship("phong", backref="loaiphong", lazy=True)


# loaiphong -- tiennghi
class loaiphong_tiennghi(db.Model):
    id_loaiphong = Column(String(45), ForeignKey(loaiphong.id), primary_key=True, nullable=False)
    id_tiennghi = Column(String(45), ForeignKey(tiennghi.id), primary_key=True, nullable=False)


# dich vu
class dichvu(db.Model):
    id = Column(String(45), primary_key=True, nullable=False)
    ten = Column(String(45), nullable=False)
    tinh_trang = Column(Boolean, nullable=False, default=True)
    gia_tien = Column(Double, nullable=False, default=0)


# loaiphong -- dichvu
class loaiphong_dichvu(db.Model):
    id_loaiphong = Column(String(45), ForeignKey(loaiphong.id), primary_key=True, nullable=False)
    id_dichvu = Column(String(45), ForeignKey(dichvu.id), primary_key=True, nullable=False)


# PHONG
class phong(db.Model):
    id = Column(String(45), primary_key=True, nullable=False)
    tinh_trang = Column(Boolean, nullable=False, default=True)
    gia_tien = Column(Double, nullable=False, default=0)
    id_loaiphong = Column(String(45), ForeignKey(loaiphong.id), primary_key=True, nullable=False)


# letan
class letan(db.Model):
    id = Column(String(45), ForeignKey(nhanvien.id), primary_key=True, nullable=False)


# letan-phong
class letan_phong(db.Model):
    id_letan = Column(String(45), ForeignKey(letan.id), primary_key=True, nullable=False)
    id_phong = Column(String(45), ForeignKey(phong.id), primary_key=True, nullable=False)


# khachhang
class khachhang(db.Model):
    id = Column(String(45), ForeignKey(User.id), primary_key=True, nullable=False)
    nguoi_o= Column(INTEGER, default=1)


# khach hang - phong
class thoigianthuetraphong(db.Model):
    id_khachhang = Column(String(45), ForeignKey(khachhang.id), nullable=False)
    id_phong = Column(String(45), ForeignKey(phong.id), primary_key=True, nullable=False)
    thoi_gian_thue = Column(DATETIME, primary_key=True, nullable=False)
    thoi_gian_tra = Column(DATETIME, nullable=False)


# hinhanh
class hoadon(db.Model):
    id = Column(String(45), primary_key=True)
    ngay_thanh_toan = Column(DATETIME, nullable=False)
    tien_tong = Column(Double, nullable=False)
    id_phong = Column(String(45), ForeignKey(phong.id), nullable=False)


# hinhanh
class hinhanh(db.Model):
    id = Column(INTEGER, primary_key=True, autoincrement=True)
    duong_dan = Column(String(255), nullable=False)
    ghi_chu = Column(String(255), default="")


# hinhanh-dichvu
class hinhanh_dichvu(db.Model):
    id_dichvu = Column(String(45), ForeignKey(dichvu.id), nullable=False)
    id_hinhanh = Column(INTEGER, ForeignKey(hinhanh.id), primary_key=True, nullable=False)

# hinhanh - loaiphong
class hinhanh_loaiphong(db.Model):
    id_loaiphong = Column(String(45), ForeignKey(loaiphong.id), nullable=False)
    id_hinhanh = Column(INTEGER, ForeignKey(hinhanh.id), primary_key=True, nullable=False)
if __name__ == "__main__":
    with app.app_context():
        db.session.commit()
        # db.create_all()
