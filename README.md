# 🔎 ResearchMate

### Multi-Agent AI Research Assistant

ResearchMate is a multi-agent web research assistant built with **AutoGen**, **Gemini 2.5 Flash**, **Tavily Web Search**, and **Streamlit**.

It uses two specialized AI agents:

* **Researcher Agent** — searches the web and collects relevant evidence.
* **Writer Agent** — analyzes the research findings and produces a structured report.

The application can be used from both the command line and a Streamlit web interface.

---

## 🏗️ Architecture

```text
                         User
                           │
                           ▼
                    ResearchMate UI
                       Streamlit
                           │
                           ▼
                  ┌─────────────────┐
                  │ Researcher Agent│
                  │    AutoGen      │
                  └────────┬────────┘
                           │
                           ▼
                    Web Search Tool
                           │
                           ▼
                    Tavily Search API
                           │
                           ▼
                    Search Results
                           │
                           ▼
                  ┌─────────────────┐
                  │   Writer Agent  │
                  │    AutoGen      │
                  └────────┬────────┘
                           │
                           ▼
                  Structured Research
                       Report
                           │
                           ▼
                  Markdown Download
```

---

## ✨ Features

* Multi-agent workflow using AutoGen
* Gemini 2.5 Flash integration
* Tavily web search tool
* Evidence collection from multiple web sources
* Source titles and URLs preserved in reports
* Handling of conflicting information
* Structured research reports
* Streamlit web interface
* Markdown report download
* Command-line interface
* Basic input validation
* Basic automated tests
* Docker support

---

## 🧠 Agents

### Researcher Agent

The Researcher Agent is responsible for:

1. Understanding the research question
2. Calling the Tavily web-search tool
3. Collecting relevant sources
4. Comparing information from multiple sources
5. Identifying conflicting information
6. Preserving source titles and URLs
7. Passing the findings to the Writer Agent

### Writer Agent

The Writer Agent receives the research findings and creates a structured report containing:

* Executive Summary
* Key Findings
* Detailed Analysis
* Sources
* Limitations

The Writer is instructed not to invent information and to preserve source attribution.

---

## 🛠️ Tech Stack

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| Python           | Application development   |
| AutoGen 0.7.5    | Multi-agent orchestration |
| Gemini 2.5 Flash | LLM                       |
| Tavily           | Web search                |
| Streamlit        | Web interface             |
| pytest           | Testing                   |
| Docker           | Containerization          |

---

## 📁 Project Structure

```text
researchmate/
│
├── app/
│   ├── agents/
│   │   ├── researcher.py
│   │   └── writer.py
│   │
│   ├── tools/
│   │   └── web_search.py
│   │
│   └── config.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│   └── test_search.py
│
├── reports/
│
├── main.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env.example
├── .gitignore
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd researchmate
```

### 2. Create a virtual environment

Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Do not commit `.env` to Git.

An example configuration is provided in:

```text
.env.example
```

---

## 🖥️ Run the Streamlit Application

```bash
streamlit run frontend/streamlit_app.py
```

The application will be available at:

```text
http://localhost:8501
```

Enter a research question and click:

**🔍 Start Research**

The Researcher Agent searches the web, and the Writer Agent produces the final report.

---

## 💻 Run from the Command Line

The project also provides a CLI interface:

```bash
python main.py
```

Enter a research topic when prompted.

Type:

```text
exit
```

or:

```text
quit
```

to stop the application.

---

## 🧪 Testing

Run the automated tests:

```bash
pytest
```

The current tests cover basic web-search input validation.

---

## 🐳 Docker

### Build the image

```bash
docker build -t researchmate .
```

### Run the container

```bash
docker run --env-file .env -p 8501:8501 researchmate
```

Then open:

```text
http://localhost:8501
```

If port `8501` is already being used, map another host port:

```bash
docker run --env-file .env -p 8502:8501 researchmate
```

Then open:

```text
http://localhost:8502
```

---

## 🔄 Research Workflow

A typical research request follows this process:

```text
1. User enters a research question
              ↓
2. Researcher Agent receives the question
              ↓
3. Researcher calls Tavily
              ↓
4. Tavily returns web sources
              ↓
5. Researcher analyzes the evidence
              ↓
6. Findings are passed to Writer Agent
              ↓
7. Writer synthesizes the findings
              ↓
8. Structured report is generated
              ↓
9. Report displayed in Streamlit
              ↓
10. User can download Markdown report
```

---

## ⚠️ Limitations

ResearchMate depends on the information returned by the web-search service and the quality of the available sources.

Potential limitations include:

* Conflicting information between sources
* Incomplete search results
* Outdated web pages
* Preliminary statistics
* Differences in reporting dates or geographic scope
* Dependence on third-party APIs
* LLM-generated synthesis requiring user verification

ResearchMate should therefore be treated as a research-assistance tool rather than an authoritative source of truth.

---

## 🔮 Future Improvements

Possible future improvements include:

* Streaming agent activity in the UI
* Improved source ranking
* Source credibility classification
* PDF report export
* Research history
* Additional research tools
* More comprehensive automated evaluation

These features are intentionally outside the current minimal two-agent architecture.

---

## 👨‍💻 Author

**Arpan Neupane**

Computer Engineering | AI/ML

GitHub:
https://github.com/arpanneupane75

---

## 📄 License

Add your preferred open-source license here.
For example:

```text
MIT License
```
