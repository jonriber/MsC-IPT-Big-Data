import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def open_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == '__main__':
    
    data = open_json_file('extracted_info.json')
    abstracts_text = ' '.join(item['abstract'] for item in data)
    word_cloud = WordCloud(width=800, height=400, background_color='white').generate(abstracts_text)
    
    abstracts_text = ' '.join(item['title'] for item in data)
    word_cloud2 = WordCloud(width=800, height=400, background_color='white').generate(abstracts_text)

    ## Abstract word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(word_cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
    ## Title word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(word_cloud2, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
    # Iterate over the first 5 items
    for item in data[:5]:
        print("ID:", item['id'])
        print("Authors:", item['authors'])
        print("Title:", item['title'])
        print("Abstract:", item['abstract'])
        print()
        
