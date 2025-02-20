import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models import Analysis, Conversation
from db.schemas import AnalysisCreate, ConversationCreate


async def create_conversation(db: AsyncSession, conversation: ConversationCreate):
    new_conversation = Conversation(
        id=uuid.uuid4(),
        from_system=conversation.from_system,
        content=conversation.content,
        visible=conversation.visible,
    )
    db.add(new_conversation)
    await db.commit()
    await db.refresh(new_conversation)
    return new_conversation


async def get_all_conversations(db: AsyncSession):
    result = await db.execute(select(Conversation))
    return result.scalars().all()


async def delete_conversation(db: AsyncSession, conversation_id: uuid.UUID):
    conversation = await db.get(Conversation, conversation_id)
    if conversation:
        await db.delete(conversation)
        await db.commit()
    return conversation


async def create_analysis(db: AsyncSession, analysis: AnalysisCreate):
    new_analysis = Analysis(
        id=uuid.uuid4(),
        report=analysis.report,
        keyword=analysis.keyword,
        feelings=analysis.feelings,
    )
    db.add(new_analysis)
    await db.commit()
    await db.refresh(new_analysis)
    return new_analysis


async def get_all_analyses(db: AsyncSession):
    result = await db.execute(select(Analysis))
    return result.scalars().all()


async def delete_analysis(db: AsyncSession, analysis_id: uuid.UUID):
    analysis = await db.get(Analysis, analysis_id)
    if analysis:
        await db.delete(analysis)
        await db.commit()
    return analysis
