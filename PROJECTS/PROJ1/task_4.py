import requests
import logging
import json
import schedule
import time

logging.basicConfig(filename='api_data.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def retrieve_data_from_api():
    try:
        # API data retrieval code here
        url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

        headers = {
            "accept": "application/json",
            "X-RapidAPI-Key": "aa24d1a197msh7c322f1111480c2p16c025jsn35b22e6582d6",
            "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        print(response.json())
        
        
        response = requests.get(url, headers=headers)

        logging.info(f'Data retrieved successfully from the API: {response.json()}')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
        logging.error(f'An error occurred: {str(e)}')
        
def job():
    print("Job started")
    retrieve_data_from_api()


        
# if __name__ == "__main__":
    
# retrieve_data_from_api()
# Schedule the job every hour
# schedule.every().hour.do(job)

# Run the schedule for 5 days
for _ in range(24 * 5):
    print("Running the schedule",_)
    job()
    # schedule.run_pending()
    time.sleep(60)  # Sleep for 1 hour