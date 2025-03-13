import asyncio
import logging
from loguru import logger
import httpx
from pydantic import BaseModel
from serpapi import GoogleSearch

class SearchResult(BaseModel):
    title: str
    link: str
    snippet: str
    displayed_link: str
    content: str | None = None

class SearchService:
    pass