import asyncio
from typing import AsyncGenerator

from alg.ai_search.ai_search_support import hybrid_search
from alg.analyze.prompt.rag_prompt import SYSTEM_PROMPT, USER_PROMPT
from db.crud.analysis import get_latest_analysis
from db.crud.character import get_latest_character
from db.crud.conversation import get_all_conversations
from db.crud.mental import get_latest_mental
from db.database import get_db
from utils.openai_call import llm_response_stream


async def get_analyses() -> tuple:
    async for db in get_db():
        conversations = await get_all_conversations(db)

        character = await get_latest_character(db)
        character = character.to_dict() if character else None

        analysis = await get_latest_analysis(db)
        analysis = analysis.to_dict() if analysis else None

        mental = await get_latest_mental(db)
        mental = mental.to_dict() if mental else None
        break
    return conversations, character, analysis, mental


async def get_user_prompt(
    question: str, related_docs: list[dict], callback: callable
) -> str:
    conversations, character, analysis, mental = await callback()
    user_prompt = USER_PROMPT.format(
        related_docs=related_docs,
        character=character,
        analysis=analysis,
        mental=mental,
        question=question,
    )
    return user_prompt


async def analysis_qa(question: str, top: int) -> AsyncGenerator[str, None]:
    index_name = "nuigurumi_therapy"
    related_docs = hybrid_search(index_name, question, top=top)

    user_prompt = await get_user_prompt(question, related_docs, get_analyses)
    for chunk in llm_response_stream(SYSTEM_PROMPT, user_prompt, print_response=True):
        yield chunk
        await asyncio.sleep(0)
