import requests
import logging
import json
import schedule
import time

logging.basicConfig(filename='api_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def retrieve_data_from_api():
    try:
        # API data retrieval code here
        
        
        logging.info('Data retrieved successfully from the API')
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')
        
if __name__ == "__main__":
    
    # retrieve_data_from_api()