import asyncio
from typing import Union

from db.crud.conversation import get_all_conversations
from db.crud.mental import create_mental
from db.database import get_db
from db.models import Conversation, Mental
from db.schemas import MentalCreate
from schema.mental import MentalModel
from src.alg.analyze.format_conversation import format_conversation
from src.alg.analyze.prompt.analyze_mental_prompt import SYSTEM_PROMPT, USER_PROMPT
from utils.openai_call import llm_response_schema


async def analyze_mental() -> Union[Mental, None]:
    """今日のレポートを作成してDBに追加する"""
    async for db in get_db():
        conversations: list[Conversation] = await get_all_conversations(db)
        break

    if not conversations:
        return None

    conversation_str = format_conversation(conversations)

    mental_result = llm_response_schema(
        SYSTEM_PROMPT, USER_PROMPT.format(conversation=conversation_str), MentalModel
    )
    print(mental_result)

    analysis = MentalCreate(**mental_result.model_dump())

    async for db in get_db():
        created_analysis = await create_mental(db, analysis)
        break

    return created_analysis


async def main():
    result = await analyze_mental()
    print(f"Created Mental: {result}")


if __name__ == "__main__":
    asyncio.run(main())
