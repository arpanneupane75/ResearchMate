from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.messages import TextMessage

from app.agents.researcher import researcher_agent
from app.agents.writer import writer_agent


def create_research_team():
    """Create the two-agent research team."""

    termination = TextMentionTermination(
        text="RESEARCH_COMPLETE"
    )

    return RoundRobinGroupChat(
        participants=[
            researcher_agent,
            writer_agent,
        ],
        termination_condition=termination,
    )


async def run_research(question: str) -> str:
    """
    Run the complete research workflow.

    Args:
        question: User's research question.

    Returns:
        Final research report.
    """

    team = create_research_team()

    result = await team.run(
        task=question
    )

    # Find the writer's final text response.
    for message in reversed(result.messages):

        if (
            isinstance(message, TextMessage)
            and message.source == "writer"
        ):
            report = message.content

            # Remove the internal termination marker.
            report = report.replace(
                "RESEARCH_COMPLETE",
                ""
            ).strip()

            return report

    return "No research report was generated."