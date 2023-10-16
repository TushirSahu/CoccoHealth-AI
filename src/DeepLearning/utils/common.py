import os
from box.exceptions import BoxValueError
from src.DeepLearning import logger
import json
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml:Path)-> ConfigBox:
    try:
        with open(path_to_yaml, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            config = ConfigBox(config)
            logger.info(f"yaml file loaded from {path_to_yaml}")
            return ConfigBox(config)

    except BoxValueError as e:
        logger.error(f"error in reading yaml file {e}")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path)
            if verbose:
                logger.info(f"created directory at {path}")
        else:
            if verbose:
                logger.info(f"directory already exists at {path}")

@ensure_annotations
def load_json(path:Path)->dict:
    with open(path,"r") as f:
        data=json.load(f)
    logger.info(f"json file loaded from {path}")
    return ConfigBox(data)

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at {path}")

# @ensure_annotations
# def 


    
