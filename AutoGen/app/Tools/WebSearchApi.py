from typing import Optional, List, Dict
from ddgs import DDGS
import ddgs


async def duckduckgo_search(
        query: str,
        num_results: int = 3,
        include_snippets: bool = True,
        include_content: bool = True,
        content_max_length: Optional[int] = 10000,
        language: str = "en",
        country: Optional[str] = None,
        safe_search: bool = True,
):
    return ddgs.DDGS().text(query, max_results=5)
