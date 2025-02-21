import asyncio
from datetime import date, datetime

from alg.prompt.analyze_day_prompt import SYSTEM_PROMPT, USER_PROMPT
from db.crud import create_analysis, get_conversations_by_timestamp_range
from db.database import get_db
from db.schemas import AnalysisCreate, ConversationCreate
from schema.analysis import AnalysisModel, Feelings
from utils.get_day_timestamp_start_n_end import get_day_timestamp_start_n_end
from utils.openai_call import llm_response_schema


def format_conversation(conversations: list[ConversationCreate]) -> str:
    """会話データをLLM入力用の形式に成形する"""
    conversation_str = ""
    for chat in conversations:
        if chat.visible == True:
            speaker = "AI" if chat.from_system else "Child"
            content = chat.content
            conversation_str += f"{speaker}: {content}\n"
    return conversation_str


async def analyze_day(day: date = datetime.now().date()) -> AnalysisModel:
    """今日のレポートを作成してDBに追加する"""
    start_timestamp, end_timestamp = get_day_timestamp_start_n_end(day)

    async for db in get_db():
        conversations: list[ConversationCreate] = (
            await get_conversations_by_timestamp_range(
                db, start_timestamp, end_timestamp
            )
        )
        break

    conversation_str = format_conversation(conversations)

    analyze_result = llm_response_schema(
        SYSTEM_PROMPT, USER_PROMPT.format(conversation=conversation_str), AnalysisModel
    )
    print(analysis_result)

    analysis = AnalysisCreate(
        report=analyze_result.report,
        keyword=analyze_result.keywords,
        feelings=analyze_result.feelings.dict(),
    )

    return create_analysis(get_db(), analysis)


if __name__ == "__main__":
    asyncio.run(analyze_day(date(2025, 2, 20)))
