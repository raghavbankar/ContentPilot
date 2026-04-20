from src.agents import AgentManager
from src.rag_manager import RAGManager
from src.content_generator import ContentGenerator


class ContentPilotPipeline:
    def __init__(self):
        self.agent_manager = AgentManager()
        self.rag_manager = RAGManager()
        self.generator = ContentGenerator()

    def run(self):
        print("Starting ContentPilot pipeline...")
        trend_data = self.agent_manager.discover_trends()
        enriched_data = self.rag_manager.enrich_trends(trend_data)
        self.generator.generate_content(enriched_data)
        print("Pipeline complete.")
