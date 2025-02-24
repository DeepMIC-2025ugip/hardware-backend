import asyncio
from typing import Union

from src.alg.analyze.format_conversation import format_all_conversation
from alg.analyze.prompt.analyze_character_prompt import SYSTEM_PROMPT, USER_PROMPT
from db.crud import create_character, get_all_conversations
from db.database import get_db
from db.models import Conversation
from db.schemas import CharacterCreate
from schema.character import CharacterModel
from utils.openai_call import llm_response_schema


async def analyze_character() -> Union[CharacterCreate, None]:
    """過去の全会話から性格を分析してDBに追加する"""

    async for db in get_db():
        conversations: list[Conversation] = await get_all_conversations(db)
        break

    if not conversations:
        return None

    conversation_str = format_all_conversation(conversations)

    character_result = llm_response_schema(
        SYSTEM_PROMPT,
        USER_PROMPT.format(all_conversation=conversation_str),
        CharacterModel,
    )
    print(character_result)

    character = CharacterCreate(**character_result.model_dump())

    async for db in get_db():
        created_character = await create_character(db, character)
        break

    return created_character


async def main():
    result = await analyze_character()
    print(f"Created character: {result}")


if __name__ == "__main__":
    asyncio.run(main())
