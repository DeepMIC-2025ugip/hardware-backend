import asyncio
from typing import Union

from db.crud.analysis import create_analysis
from db.crud.conversation import get_all_conversations
from db.database import get_db
from db.models import Analysis, Conversation
from db.schemas import AnalysisCreate
from schema.analysis import AnalysisModel
from src.alg.analyze.format_conversation import format_conversation
from src.alg.analyze.prompt.analyze_life_prompt import SYSTEM_PROMPT, USER_PROMPT
from utils.openai_call import llm_response_schema


async def analyze_life() -> Union[Analysis, None]:
    """今日のレポートを作成してDBに追加する"""
    async for db in get_db():
        conversations: list[Conversation] = await get_all_conversations(db)
        break

    if not conversations:
        return None

    conversation_str = format_conversation(conversations)

    analyze_result = llm_response_schema(
        SYSTEM_PROMPT, USER_PROMPT.format(conversation=conversation_str), AnalysisModel
    )
    print(analyze_result)

    analysis = AnalysisCreate(**analyze_result.model_dump())

    async for db in get_db():
        created_analysis = await create_analysis(db, analysis)
        break

    return created_analysis


async def main():
    result = await analyze_life()
    print(f"Created Life: {result}")


if __name__ == "__main__":
    asyncio.run(main())
