from sqlalchemy import Column, Integer, Text
from database import Base


class TestcaseHistory(Base):
    __tablename__ = "testcase_history"

    id = Column(Integer, primary_key=True, index=True)
    requirement = Column(Text)
    response = Column(Text)