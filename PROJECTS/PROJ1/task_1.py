from selenium import webdriver
import shutil
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

if __name__ == "__main__":
    
    driver = webdriver.Chrome()

    driver.get("https://openresearch.ceu.edu/browse?type=dateissued")

    article_url_count = 0
    href_links = []
    while article_url_count < 100:
        # Scraping articles here using XPath or CSS selectors
        articles = driver.find_elements("css selector", ".description-content a")

        # Process each article
        for article in articles:
            # Scrape the article content
            # Your scraping logic here
            href_links.append(article.get_attribute("href"))
            article_url_count += 1
            if article_url_count == 100:
                break

        # Click the next page button
        try:
             # Check if there is a "Next" button
            next_button = driver.find_element(By.CLASS_NAME, 'next-page-link')
            
            if next_button:
                # Click the "Next" button to navigate to the next page
                next_button.click()
            else:
                # Exit the loop if there is no "Next" button
                break
        except:
            break

    # Close the WebDriver
    
    print("href_links:",href_links)
    
    # Create the destination folder if it doesn't exist
    destination_folder = "pdf_source"
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for url in href_links:
        driver.get(url)
        
        download_button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'file-download-button')))
    
        # Get the download link
        download_link = download_button.get_attribute('href')
        
        # Download the file

        try:
            driver.get(download_link)

            file_name = download_link.split('/')[-1].split('?')[0]
            # Wait for the file to be downloaded
            time.sleep(20)  # Adjust the sleep time as needed

            # Create the destination folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            time.sleep(20)  # Adjust the sleep time as needed

            # Move the file to the destination folder
            shutil.move(file_name, f"{destination_folder}/{file_name}")
        except Exception as e:
            print("An error occurred:", e)
            pass

        
        

        
    driver.quit()

