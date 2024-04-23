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
        
def job():
    retrieve_data_from_api()


        
if __name__ == "__main__":
    
    # retrieve_data_from_api()
    # Schedule the job every hour
    schedule.every().hour.do(job)

    # Run the schedule for 5 days
    for _ in range(24 * 5):
        schedule.run_pending()
        time.sleep(3600)  # Sleep for 1 hour