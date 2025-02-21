from db.models import Conversation


def conversation_str(conversation: Conversation) -> str:
    speaker = "AI" if conversation.from_system else "Child"
    content = conversation.content
    return f"{speaker}: {content}\n"


def format_conversation(conversations: list[Conversation]) -> str:
    """DBから取得した会話データをLLM入力用の形式に成形する"""
    conversation_str = ""
    for chat in conversations:
        if chat.visible == True:
            conversation_str += conversation_str(chat)
    return conversation_str


def format_all_conversation(conversations: list[Conversation]) -> str:
    """DBから取得した会話データをLLM入力用の形式に成形する"""
    all_conversation_str = ""
    conversation_date = None
    for chat in conversations:
        if chat.timestamp.date() != conversation_date:
            conversation_date = chat.timestamp.date()
            all_conversation_str += f"Date: {conversation_date}\n"

        if chat.visible == True:
            all_conversation_str += conversation_str(chat)

    return all_conversation_str
