# Familiarização com a obtenção de dados a partir de packages Python
import wikipedia
import requests
import os

def search_wikipedia(query, results=10):
    return wikipedia.search(query, results=results)


def download_image(article):
    print("Downloading images for article:", article)
    try:
        page = wikipedia.page(article)
        print("Found page:", page.images)
        images = page.images
        for image in images:
            if image.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                print("Found image:", image)
                if image:
                    image_urls.append(image)
    except wikipedia.exceptions.DisambiguationError as e:
        # Skip disambiguation pages
        pass
    except wikipedia.exceptions.PageError as e:
        print(f"Page not found for article: {article}")
        pass
    except KeyError as e:
        print(f"KeyError: {e}")
        pass

  
def try_to_save_image(url, i, save_dir):
    print(f"Downloading image {i}: {url}")
    try:
        response = requests.get(url)
        extension = url.split('.')[-1]
        with open(save_dir + f'image_{i}.{extension}', 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print(f"Error downloading image {i}: {e}")
        pass


if __name__ == "__main__":
    
    print("starting the script")
    
    design_articles = search_wikipedia("Design", results=1000)
    restaurant_articles = search_wikipedia("Restaurant", results=1000)

    articles = design_articles + restaurant_articles
    
    print(articles)

    image_urls = []

    for article in articles:
        download_image(article)
    
    save_dir = 'PROJECTS/PROJ1/image_dataset/'
    
    # Create the directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    for i, url in enumerate(image_urls):

        try_to_save_image(url, i, save_dir)
    
    print("Script finished")