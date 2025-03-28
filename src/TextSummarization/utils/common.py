import os
from box.exceptions import BoxValueError
import yaml
from src.TextSummarization.logging import logger
from box import ConfigBox
from pathlib import Path 
from typing import Any 


##Read Yaml 
def read_yaml(path_to_yaml:Path) -> ConfigBox: 
    """
    Read Yaml files and return value 
    """
    try: 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"load {content} succesfully")
            return ConfigBox(content)
    except BoxValueError : 
        raise ValueError("Yaml file is empty")
    except Exception as e : 
        raise e 

def create_directories(path_to_dir: list,verbose = True): 
    """
    Create a path to directories
    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"Created the directory {path}")
