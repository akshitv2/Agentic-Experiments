from typing import Optional, List, Dict

import requests
from ddgs import DDGS


async def google_search(
        query: str,
        num_results: int = 3,
        include_snippets: bool = True,
        include_content: bool = True,
        content_max_length: Optional[int] = 10000,
        language: str = "en",
        country: Optional[str] = None,
        safe_search: bool = True,
):
    return DDGS().text(query, max_results=5)