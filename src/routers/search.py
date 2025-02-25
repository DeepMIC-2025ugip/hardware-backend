from fastapi import APIRouter, Body
from starlette.responses import StreamingResponse

from alg.ai_search.ai_search_support import hybrid_search
from alg.analyze.rag import analysis_qa

search_router = APIRouter(prefix="/search", tags=["Search"])


@search_router.post("/hybrid_search")
def hybrid_search_api(
    question: str = Body(...), top: int = Body(4)
) -> list[dict[str, str]]:
    index_name = "nuigurumi_therapy"
    results = hybrid_search(index_name, question, top=top)

    return results


@search_router.post("/rag")
async def rag_api(question: str = Body(...), top: int = Body(2)) -> StreamingResponse:
    return StreamingResponse(analysis_qa(question, top=top), media_type="text/event-stream")
