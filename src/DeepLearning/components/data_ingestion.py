import urllib.request as request
import zipfile
import os
from pathlib import Path
from DeepLearning.entity.config_entity import DataIngestionConfig
from DeepLearning import logger
from DeepLearning.utils.common import get_size


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers = request.urlretrieve(url=self.config.source_url,filename=self.config.local_data_file)
            logger.info(f"{filename} downloaded successfully with info {headers}")
        else : logger.info(f"File already exits with size: {get_size(Path(self.config.local_data_file))}")
            # os.makedirs(self.config.root_dir)
    def extract_zip_file(self):
        unzip_path= (self.config.unzip_dir)
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)