import os

from dotenv import load_dotenv

from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.knowledge.chunking.recursive import RecursiveChunking
from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.knowledge.reader.pdf_reader import PDFReader
from agno.models.google import Gemini
from agno.vectordb.lancedb import LanceDb
from agno.vectordb.search import SearchType

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "Iqra_University_Fees_Structure.pdf")
LANCEDB_URI = os.path.join(BASE_DIR, "data", "lancedb")
CONTENTS_DB_FILE = os.path.join(BASE_DIR, "knowledge_contents.db")

MODEL_ID = "gemini-3.5-flash-lite"
QUESTION = "Fees Structure of BS (CS) complete fees with numbers "


def build_knowledge() -> Knowledge:
    vector_db = LanceDb(
        table_name="pdf_docs",
        uri=LANCEDB_URI,
        search_type=SearchType.keyword,
        embedder=OllamaEmbedder(id="nomic-embed-text", dimensions=768),
    )

    return Knowledge(
        vector_db=vector_db,
        contents_db=SqliteDb(db_file=CONTENTS_DB_FILE),
    )


def build_agent(knowledge: Knowledge) -> Agent:
    return Agent(
        model=Gemini(
            id=MODEL_ID,
            temperature=0.0,
            api_key=os.getenv("GEMINI_API_KEY"),
        ),
        knowledge=knowledge,
        search_knowledge=True,
        instructions=[
            "Always search the knowledge base before answering recipe questions.",
            "Answer only from the retrieved recipe information.",
            "If the recipe is not in the knowledge base, say so.",
        ],
        markdown=True,
        debug_mode=True,
    )


def main():
    knowledge = build_knowledge()

    contents, _ = knowledge.get_content()
    for content in contents:
        print(content.id, content.name, content.status)
        if content.name == os.path.basename(PDF_PATH):
            knowledge.remove_content_by_id(content.id)

    reader = PDFReader(
        chunking_strategy=RecursiveChunking(
            chunk_size=200,
            overlap=40,
        ),
        split_on_pages=True,
    )

    print("Loading the PDF into the knowledge base...")
    knowledge.insert(
        path=PDF_PATH,
        reader=reader,
        skip_if_exists=False,
    )
    print("PDF is ready.\n")

    agent = build_agent(knowledge)
    agent.print_response(QUESTION, stream=True)


if __name__ == "__main__":
    main()