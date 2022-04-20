from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from os import getcwd


router = APIRouter()

Path_File = getcwd() + "/documents/" 

@router.post('/upload')
async def upload_document(file:UploadFile = File(...)):
    with open(Path_File + file.filename, "wb") as  myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return JSONResponse(content={"message": "success"},status_code=200)

@router.get('/file/{name_document}')
def get_document(name_document:str):
    return FileResponse( Path_File + name_document)

@router.get("/download/{name_document}")
def download_file(name_document: str):
    return FileResponse(Path_File + name_document, media_type="application/octet-stream", filename=name_document)
