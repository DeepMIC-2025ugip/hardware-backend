from datetime import date, datetime

from alg.prompt.analyze_day_prompt import SYSTEM_PROMPT, USER_PROMPT
from db.crud import create_analysis, get_conversations_by_timestamp_range
from db.database import get_db
from db.schemas import AnalysisCreate
from schema.analysis import AnalysisModel, Feelings
from utils.get_day_timestamp_start_n_end import get_day_timestamp_start_n_end
from utils.openai_call import llm_response_schema


def format_conversation(conversations: list) -> str:
    conversation_str = ""
    for chat in conversations:
        if chat["visible"] == True:
            speaker = "AI" if chat["from_system"] else "Child"
            content = chat["content"]
            conversation_str += f"{speaker}: {content}\n"
    return conversation_str


def analyze_day(day: date = datetime.now().date()) -> AnalysisModel:
    start_timestamp, end_timestamp = get_day_timestamp_start_n_end(day)
    conversations = get_conversations_by_timestamp_range(
        get_db(), start_timestamp, end_timestamp
    )
    conversation_str = format_conversation(conversations)

    analyze_result = llm_response_schema(
        SYSTEM_PROMPT, USER_PROMPT.format(conversation=conversation_str), AnalysisModel
    )

    analysis = AnalysisCreate(
        report=analyze_result.report,
        keyword=analyze_result.keyword,
        feelings=Feelings(**analyze_result.feelings),
    )

    return create_analysis(get_db(), analysis)
