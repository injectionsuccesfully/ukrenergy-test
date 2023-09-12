from models.file import File
from .main import Service
from sqlalchemy import desc
from fastapi import UploadFile
from .diskstorage import DiskStorage
from schemas.file import StoredFile, InformationAboutFile
from pydantic import UUID4

class FileService(Service):
    def create(self, file : UploadFile) -> File:
        file : StoredFile = DiskStorage.save(file)

        file = File(
            id=file.id,
            file_name=file.file_name,
            extension=file.extension,
            size=file.size,
            path=file.path,
            content_type=file.content_type
        )

        self.db.add(file)
        self.db.commit()
        self.db.refresh(file)

        return file

    def get_information_about_file(self, id: UUID4) -> InformationAboutFile:
        file = self.db.query(File).filter(File.id == id).first()
        
        if file is not None:
            return InformationAboutFile(
                id=file.id,
                file_name=file.file_name,
                extension=file.extension,
                size=file.size,
                content_type=file.content_type
            )
        
        return file
    
    def get_by_id(self, id: UUID4) -> File:
        return self.db.query(File).filter(File.id == id).first()

    
    def get_top_ten_files(self) -> list[File]:
        return self.db.query(File).order_by(desc(File.size)).limit(10).all()
    
    def check_if_file_exist_by_path(self, path: str) -> bool:
        return DiskStorage.check_if_file_exist(path)