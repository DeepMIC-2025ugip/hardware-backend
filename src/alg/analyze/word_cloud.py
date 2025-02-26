import asyncio
from typing import Union

from db.crud.conversation import get_all_conversations
from db.crud.word_cloud import create_word_cloud
from db.database import get_db
from db.models import Conversation
from db.schemas import WordCloudCreate
from schema.word_cloud import WordCloud
from src.alg.analyze.format_conversation import format_conversation
from src.alg.analyze.prompt.analyze_word_cloud_prompt import SYSTEM_PROMPT, USER_PROMPT
from utils.openai_call import llm_response_schema


async def analyze_word_cloud() -> Union[WordCloud, None]:
    """今日のレポートを作成してDBに追加する"""
    async for db in get_db():
        conversations: list[Conversation] = await get_all_conversations(db)
        break

    if not conversations:
        return None

    conversation_str = format_conversation(conversations)

    word_cloud_result = llm_response_schema(
        SYSTEM_PROMPT, USER_PROMPT.format(conversation=conversation_str), WordCloud
    )
    print(word_cloud_result)

    analysis = WordCloudCreate(**word_cloud_result.model_dump())

    async for db in get_db():
        created_analysis = await create_word_cloud(db, analysis)
        break

    return created_analysis


async def main():
    result = await analyze_word_cloud()
    print(f"Created Life: {result}")


if __name__ == "__main__":
    asyncio.run(main())
