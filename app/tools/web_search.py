import asyncio

from tavily import TavilyClient

from app.config import TAVILY_API_KEY


tavily_client = TavilyClient(
    api_key=TAVILY_API_KEY
)


async def search_web(query: str) -> str:
    """
    Search the web using Tavily.

    Returns relevant sources with titles,
    URLs, relevance scores, and content.
    """

    if not query or not query.strip():
        return "Search failed: Please provide a valid query."

    query = query.strip()

    try:
        response = await asyncio.to_thread(
            tavily_client.search,
            query=query,
            search_depth="advanced",
            max_results=5,
            include_answer=True,
            include_raw_content=False,
        )

    except Exception as error:
        return (
            "Web search failed.\n"
            f"Error type: {type(error).__name__}\n"
            f"Details: {error}"
        )

    results = response.get("results", [])

    if not results:
        return f"No useful results found for: {query}"

    formatted_results = []

    for index, result in enumerate(results, start=1):

        title = result.get(
            "title",
            "Untitled"
        )

        url = result.get(
            "url",
            "No URL"
        )

        content = result.get(
            "content",
            "No content available."
        )

        score = result.get(
            "score",
            "N/A"
        )

        formatted_results.append(
            f"""
SOURCE {index}

Title:
{title}

URL:
{url}

Relevance Score:
{score}

Content:
{content}
"""
        )

    answer = response.get("answer")

    answer_section = ""

    if answer:
        answer_section = f"""
TAVILY SEARCH SUMMARY:

{answer}

"""

    return (
        f"Search results for: {query}\n\n"
        + answer_section
        + "\n".join(formatted_results)
    )