from src.pipeline import ContentPilotPipeline


def test_pipeline_instantiation():
    pipeline = ContentPilotPipeline()
    assert pipeline.agent_manager is not None
    assert pipeline.rag_manager is not None
    assert pipeline.generator is not None
