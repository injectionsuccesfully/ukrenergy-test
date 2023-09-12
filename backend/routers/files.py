from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse, JSONResponse, Response
from schemas.file import File, CreatedFile, InformationAboutFile
from fastapi import UploadFile
from services.file.file import FileService
from sqlalchemy.orm import Session
from database.main import get_db_session
from pydantic import UUID4

router = APIRouter(prefix='/files', tags=['files'])

@router.get('/top', response_model=list[File])
async def get_top_files(db: Session = Depends(get_db_session)):
    return FileService(db).get_top_ten_files_by_size()

@router.get('/{file_id}')
async def get_file(file_id : UUID4, db: Session = Depends(get_db_session)):
    file: File = FileService(db).get_by_id(file_id)

    if file is None:
        return JSONResponse(content={'message':'File not found!'}, status_code=404)

    if FileService(db).check_if_file_exist_by_path(file.path) is False:
        return JSONResponse(content={'message':'File not found!'}, status_code=404)

    return FileResponse(path=file.path, filename=f"{file.file_name}.{file.extension}")

@router.head('/{file_id}', response_class=Response)
async def get_information_about_file(file_id : UUID4, db: Session = Depends(get_db_session)):
    file : InformationAboutFile = FileService(db).get_information_about_file(file_id)

    if file is None:
        return Response(status_code=404)

    return Response(headers={
        'Content-Length' : str(file.size),
        'Content-Type': file.content_type
    },status_code=200)

@router.post('', response_model=CreatedFile)
async def upload_file(file: UploadFile, db : Session = Depends(get_db_session)) -> CreatedFile:
    file : File = FileService(db).create(file)

    return CreatedFile(
        id=file.id
    )
