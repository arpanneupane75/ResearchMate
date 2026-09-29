import asyncio

from app.workflow import run_research


async def main():

    print()
    print("=" * 60)
    print("🔎 RESEARCHMATE")
    print("Multi-Agent AI Research Assistant")
    print("=" * 60)
    print()
    print("Enter a research question.")
    print("Type 'exit' or 'quit' to stop.")
    print()

    while True:

        question = input("Research topic: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("\n👋 Goodbye!")
            break

        if not question:
            print("⚠️ Please enter a research question.")
            continue

        print("\n🤖 Researching...\n")

        try:

            report = await run_research(question)

            print("\n" + "=" * 60)
            print("📄 RESEARCH REPORT")
            print("=" * 60)
            print()
            print(report)

        except Exception as error:

            print("\n❌ Research failed.")
            print(
                f"{type(error).__name__}: {error}"
            )

        print("\n" + "-" * 60)


if __name__ == "__main__":
    asyncio.run(main())