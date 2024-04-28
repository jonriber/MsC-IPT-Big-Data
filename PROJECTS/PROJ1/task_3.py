
from selenium import webdriver
from selenium.webdriver.common.by import By

TARGET_URL = "https://www.europarl.europa.eu/news/pt"

def quit_driver():
    driver.quit()
    
def get_last_news(id,driver):
    try:
        # Get the last news
        news = driver.find_elements(By.CLASS_NAME, id)
        return news
    except Exception as e:
        print("An error occurred:", e)
        return None

def get_next_events_list(id,driver):
    
    try:
        event_list_element = driver.find_element(By.ID, id)
        list_items = event_list_element.find_elements(By.TAG_NAME, "li")

        return list_items
    except Exception as e:
        print("No list elements found:", e)
        return None
    
def get_event_context(event):
    try:
        date_element = event.find_element(By.CLASS_NAME, "ep_date")
        date = date_element.text.strip()
        
        type_element = event.find_element(By.CLASS_NAME, "ep_type")
        event_type = type_element.text.strip()
        
        # Extract the event title
        title_element = event.find_element(By.CLASS_NAME, "ep_title")
        title = title_element.text.strip()
        
        # Extract the event location
        location_element = event.find_element(By.CLASS_NAME, "ep_location")
        location = location_element.text.strip()
    
     # Print the extracted information for each event
        print("Date:", date)
        print("Type:", event_type)
        print("Title:", title)
        print("Location:", location)
        print()  # Add a line break between events
        return {date, event_type, title, location}
    except Exception as e:
        print("An error occurred:", e)
        return None

def get_news_context(news):
    
    # print("Extracting news context...",news)
    try:
        # Get the news context
        title_element = news.find_element(By.CLASS_NAME, "ep_title")
        title = title_element.text
        
        # date_element = news.find_element(By.CSS_SELECTOR, "time[itemprop='datePublished']")
        # date = date_element.get_attribute("datetime")
        
        content_element = news.find_element(By.CLASS_NAME, "ep-a_text")
        content = content_element.text
        
        if len(title) > 0 and len(content) > 0:
        
            # print("Title:", title)
            # print("Publication Date:", date)  
            # print("Content:", content)
            return {title, content}
        else:
            pass
    except Exception as e:
        print("An error occurred:", e)
        return None
    
def init_driver():
    driver = webdriver.Chrome()
    return driver

if __name__ == "__main__":
    driver = init_driver()
    
    driver.get(TARGET_URL)

    extracted_news = get_last_news("ep_gridcolumn",driver)
    # if len(extracted_news) >5:
    #     extracted_news = extracted_news[:5]
    # print("Extracted news:", extracted_news)
    final_news = []
    for news in extracted_news:
        new = get_news_context(news)
        if new != None:
            final_news.append(new)
            # print("New:", new)
    print("Final news:", final_news)
    
    final_event_list = []
    extracted_next_events = get_next_events_list("event-list",driver)
    
    for event in extracted_next_events:
        event = get_event_context(event)
        if event != None:
            final_event_list.append(event)
            # print("Event:", event)
    print("Final event list:", final_event_list)
    
    quit_driver()