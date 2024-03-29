from app import ma
from database import db
from sqlalchemy import Column, Integer, String, Float


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    pw_hash = Column(String)


class Performance(db.Model):
    __tablename__ = 'performance'
    id = Column(Integer, primary_key=True)
    date = Column(String, unique=True)
    memory_usage = Column(Float)
    CPU_usage = Column(Float)
    disk_usage = Column(Float)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'pw_hash')


class PerformanceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'date', 'memory_usage', 'CPU_usage', 'disk_usage')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
performance_schema = PerformanceSchema()
performances_schema = PerformanceSchema(many=True)
