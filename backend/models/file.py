from database.main import Base
from sqlalchemy import Column, Uuid, String, Integer

class File(Base):
    __tablename__ = 'files'

    id = Column(Uuid, primary_key=True, index=True)
    file_name = Column(String, nullable=False)
    extension = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    path = Column(String, nullable=False)
    content_type = Column(String, nullable=False)