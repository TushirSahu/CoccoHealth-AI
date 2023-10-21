from DeepLearning.config.configuration import ConfigurationManager
from DeepLearning.components.prepare_model import PrepareBaseModel
from DeepLearning import logger


STAGE_NAME="Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        prepare_base_model_config=config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f"Running {STAGE_NAME}")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"{STAGE_NAME} completed!...")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e