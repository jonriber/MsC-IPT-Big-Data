
from selenium import webdriver
from selenium.webdriver.common.by import By



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

def get_next_events(id,driver):
    # Get the next events
    pass

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
    driver.get("https://www.europarl.europa.eu/news/pt")

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

    quit_driver()