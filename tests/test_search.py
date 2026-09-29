import asyncio

from app.tools.web_search import search_web


def test_empty_query():
    result = asyncio.run(search_web(""))
    assert "Please provide a valid query" in result


def test_whitespace_query():
    result = asyncio.run(search_web("   "))
    assert "Please provide a valid query" in result