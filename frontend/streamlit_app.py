
import asyncio
import sys
from pathlib import Path

import streamlit as st


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# APPLICATION IMPORTS
# ============================================================

from app.workflow import run_research


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="ResearchMate",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# HEADER
# ============================================================

st.title("🔎 ResearchMate")

st.markdown(
    """
    ### Multi-Agent AI Research Assistant

    Research any topic using **AutoGen**, **Gemini 2.5 Flash**,
    and **Tavily Web Search**.
    """
)

st.caption(
    "ResearchMate uses multiple AI agents to search, analyze, "
    "and synthesize information from the web."
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("🤖 Agent Architecture")

    st.markdown(
        """
        **1. Researcher Agent**

        - Searches the web using Tavily
        - Collects relevant sources
        - Extracts useful information

        **2. Writer Agent**

        - Receives research findings
        - Synthesizes the information
        - Creates a structured report
        - Preserves source references
        """
    )

    st.divider()

    st.header("🛠️ Technology")

    st.markdown(
        """
        - **AutoGen 0.7.5**
        - **Gemini 2.5 Flash**
        - **Tavily Web Search**
        - **Python**
        - **Streamlit**
        """
    )

    st.divider()

    st.caption(
        "Built with AutoGen + Gemini + Tavily"
    )


# ============================================================
# RESEARCH INPUT
# ============================================================

st.subheader("🔍 Research Topic")

question = st.text_area(
    "What would you like to research?",
    placeholder=(
        "Example: What are the latest developments "
        "in Retrieval-Augmented Generation?"
    ),
    height=120,
    help="Enter a question or topic that requires web research.",
)


# ============================================================
# RESEARCH BUTTON
# ============================================================

if st.button(
    "🔍 Start Research",
    type="primary",
    use_container_width=True,
):

    if not question.strip():

        st.warning(
            "Please enter a research question."
        )

    else:

        st.session_state.pop("report", None)

        with st.spinner(
            "🔎 Researcher and Writer agents are working..."
        ):

            try:

                report = asyncio.run(
                    run_research(
                        question.strip()
                    )
                )

                st.session_state["report"] = report
                st.session_state["question"] = question.strip()

                st.success(
                    "Research completed successfully!"
                )

            except Exception as error:

                st.error(
                    "❌ Research failed."
                )

                st.exception(error)


# ============================================================
# DISPLAY REPORT
# ============================================================

if "report" in st.session_state:

    st.divider()

    st.subheader("📄 Research Report")

    st.markdown(
        st.session_state["report"]
    )

    st.divider()

    # ========================================================
    # DOWNLOAD REPORT
    # ========================================================

    st.download_button(
        label="⬇️ Download Report",
        data=st.session_state["report"],
        file_name="research_report.md",
        mime="text/markdown",
        use_container_width=True,
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "ResearchMate • Multi-Agent Research Assistant • "
    "AutoGen + Gemini + Tavily"
)

