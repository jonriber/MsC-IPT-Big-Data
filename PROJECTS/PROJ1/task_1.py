from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://ejpr.onlinelibrary.wiley.com/action/doSearch?SeriesKey=14756765&sortBy=Earliest&startPage=&ConceptID=15941")

article_count = 0

while article_count < 100:
    # Scraping articles here using XPath or CSS selectors
    articles = driver.find_elements(By.XPATH, "YOUR_ARTICLE_XPATH_HERE")

    # Process each article
    for article in articles:
        # Scrape the article content
        # Your scraping logic here

        article_count += 1
        if article_count == 100:
            break

    # Click the next page button
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "YOUR_NEXT_BUTTON_XPATH_HERE"))
        )
        next_button.click()
    except:
        break

# Close the WebDriver
driver.quit()

