import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import db.crud as crud
from db.database import get_db
from db.schemas import ConversationCreate, ConversationResponse

conversation_router = APIRouter(prefix="/conversations", tags=["Conversations"])


@conversation_router.post("/", response_model=ConversationResponse)
async def create_conversation(
    conversation: ConversationCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.create_conversation(db, conversation)


@conversation_router.get("/", response_model=list[ConversationResponse])
async def get_conversations(db: AsyncSession = Depends(get_db)):
    return await crud.get_all_conversations(db)


@conversation_router.delete("/{conversation_id}")
async def delete_conversation(
    conversation_id: uuid.UUID, db: AsyncSession = Depends(get_db)
):
    return await crud.delete_conversation(db, conversation_id)
