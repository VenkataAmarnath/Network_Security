import os
import sys
import json

from dotenv import load_dotenv # to interacr with .env file
 
import certifi  # to define security protocol whenever we are goi ng to interact with the cloud from local(expecially with mongodb), using this we can define ssl certificate for secure connection
import pandas as pd
import numpy as np
import pymongo

#customised class in exception folder under networksecurity folder
from networksecurity.exception import NetworkSecurityException

#customised class in logger folder under networksecurity folder
from networksecurity.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def pushing_data_to_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    if __name__=='__main__':
        pass
        



