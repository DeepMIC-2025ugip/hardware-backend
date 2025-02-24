import asyncio
from datetime import date, datetime
from typing import Union

from alg.analyze.prompt.analyze_day_prompt import SYSTEM_PROMPT, USER_PROMPT
from db.crud import create_analysis, get_conversations_by_timestamp_range
from db.database import get_db
from db.models import Analysis, Conversation
from db.schemas import AnalysisCreate
from schema.analysis import AnalysisModel
from src.alg.analyze.format_conversation import format_conversation
from utils.get_day_timestamp_start_n_end import get_day_timestamp_start_n_end
from utils.openai_call import llm_response_schema


async def analyze_day(day: date = datetime.now().date()) -> Union[Analysis, None]:
    """今日のレポートを作成してDBに追加する"""
    start_timestamp, end_timestamp = get_day_timestamp_start_n_end(day)

    async for db in get_db():
        conversations: list[Conversation] = await get_conversations_by_timestamp_range(
            db, start_timestamp, end_timestamp
        )
        break

    if not conversations:
        return None

    conversation_str = format_conversation(conversations)

    analyze_result = llm_response_schema(
        SYSTEM_PROMPT, USER_PROMPT.format(conversation=conversation_str), AnalysisModel
    )
    print(analyze_result)

    analysis = AnalysisCreate(
        report=analyze_result.report,
        keyword=analyze_result.keywords,
        feelings=analyze_result.feelings.model_dump(),
    )

    async for db in get_db():
        created_analysis = await create_analysis(db, analysis)
        break

    return created_analysis


async def main():
    result = await analyze_day()
    print(f"Created character: {result}")


if __name__ == "__main__":
    asyncio.run(main())
