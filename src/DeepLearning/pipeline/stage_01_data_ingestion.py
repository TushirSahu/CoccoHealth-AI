from DeepLearning.config.configuration import ConfigurationManager
from DeepLearning.components.data_ingestion import DataIngestion
from DeepLearning import logger


STAGE_NAME="Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed!...")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e