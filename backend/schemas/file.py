from pydantic import BaseModel
from pydantic import UUID4

class File(BaseModel):
    id: UUID4
    file_name: str
    path: str
    extension: str
    size: int
    content_type: str

    class Config:
        orm_mode = True


class StoredFile(BaseModel):
    id: UUID4
    file_name: str
    path: str
    extension: str
    size: int
    content_type: str

class CreatedFile(BaseModel):
    id: UUID4


class InformationAboutFile(BaseModel):
    id: UUID4
    file_name: str
    extension: str
    size: int
    content_type: str