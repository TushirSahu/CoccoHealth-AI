from src.DeepLearning import logger
from DeepLearning.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from DeepLearning.pipeline.stage02_base_model import PrepareBaseModelPipeline

STAGE_NAME="Data Ingestion Stage"   
try:
        logger.info(f"Running {STAGE_NAME}")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed!...")
except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e

STAGE_NAME="Prepare Base Model Stage"   
try:
        logger.info(f"Running {STAGE_NAME}")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed!...")
except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e

