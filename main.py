from src.DeepLearning import logger
from DeepLearning.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from DeepLearning.pipeline.stage02_base_model import PrepareBaseModelPipeline
from DeepLearning.pipeline.stage_03_training import ModelTrainingPipeline
from DeepLearning.pipeline.stage_04_evaluation import EvaluationPipeline

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

STAGE_NAME="Training Stage"
try:
        logger.info(f"Running {STAGE_NAME}")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed!...")
except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e   


STAGE_NAME="Evaluation Stage"
try:
        logger.info(f"Running {STAGE_NAME}")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed!...")
except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e