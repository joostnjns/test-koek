import pandas as pd
import configparser

def get_download_url() -> str:
    '''
    Read download url as specified in config file
    '''
    config = configparser.ConfigParser()
    config.read('../../config.ini')
    return config['DATA_ACCESS']['url']

def read_raw_data(url: str=None):
    if not url:
        url = get_download_url()
    config = configparser.ConfigParser()
    pdf = pd.read_csv(url)
    return pdf