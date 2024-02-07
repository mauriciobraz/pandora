from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile

from ...helpers.database import User
from ...helpers.users import current_super_user

document_router = APIRouter(
    prefix="/documents",
)


@document_router.post("/documents", status_code=status.HTTP_201_CREATED)
async def upload_document(
    files: List[UploadFile] = File(...),
    user: User = Depends(current_super_user),
):
    # for file in files:
    #     try:
    #         contents = await file.read()
    #     except Exception:
    #         raise HTTPException(
    #             status_code=status.HTTP_400_BAD_REQUEST,
    #             detail="File could not be read",
    #         )

    raise HTTPException(status_code=501, detail="Not implemented yet")


@document_router.put("/documents/{id}", status_code=status.HTTP_200_OK)
async def update_document(
    id: int, file: UploadFile = File(...), user: User = Depends(current_super_user)
):
    # try:
    #     contents = await file.read()
    # except Exception:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="File could not be read",
    #     )

    raise HTTPException(status_code=501, detail="Not implemented yet")


@document_router.get("/documents", status_code=status.HTTP_200_OK)
async def list_documents(user: User = Depends(current_super_user)):
    raise HTTPException(status_code=501, detail="Not implemented yet")


@document_router.get("/documents/{id}", status_code=status.HTTP_200_OK)
async def retrieve_document(id: int, user: User = Depends(current_super_user)):
    raise HTTPException(status_code=501, detail="Not implemented yet")


@document_router.delete("/documents/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_document(id: int, user: User = Depends(current_super_user)):
    raise HTTPException(status_code=501, detail="Not implemented yet")
