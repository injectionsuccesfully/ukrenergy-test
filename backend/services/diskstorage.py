from fastapi import UploadFile
from .storage import Storage
from schemas.file import StoredFile
from uuid import uuid4
from configs.config import get_settings
import os 
import shutil

class DiskStorage(Storage):
    def save(inputFile: UploadFile) -> StoredFile:
        id = uuid4()

        file_name, file_extension = os.path.splitext(inputFile.filename)
        file_extension = file_extension.replace('.','')

        file_location = f"{get_settings().upload_files_path}/{id}.{file_extension}"

        with open(file_location,'wb+') as file_object:
            shutil.copyfileobj(inputFile.file, file_object)

        return StoredFile(
            id=id,
            file_name=file_name,
            path=file_location,
            extension=file_extension,
            size=inputFile.size,
            content_type=inputFile.content_type
        )
    
    def check_if_file_exist(path: str) -> bool:
        return os.path.exists(path)