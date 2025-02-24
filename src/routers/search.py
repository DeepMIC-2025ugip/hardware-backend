from typing import Union

from fastapi import APIRouter, Body

from alg.ai_search.ai_search_support import hybrid_search

search_router = APIRouter(prefix="/search", tags=["Search"])


@search_router.post("/hybrid_search")
def hybrid_search_api(
    question: str = Body(...), top: int = Body(4)
) -> Union[list[str], list[dict[str, str]]]:
    index_name = "nuigurumi_therapy"
    results = hybrid_search(index_name, question, top=top)

    return results
