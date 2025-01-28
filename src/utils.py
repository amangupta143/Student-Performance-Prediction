import os
import sys

import numpy as np 
import pandas as pd
import dill

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        logging.info(f"Saving object to {file_path}")
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved to {file_path}")

    except Exception as e:
        raise CustomException(e, sys)