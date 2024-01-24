import requests
from bs4 import BeautifulSoup
import datetime

def get_news(api_key):
    """
    Fetches the top headlines for the day.
    """
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',  # You can change this to your preferred country
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        return None

def get_full_article(article_url):
    """
    Attempts to fetch the full content of the news article.
    """
    try:
        response = requests.get(article_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        article_content = ' '.join([p.get_text() for p in paragraphs])
        return article_content
    except Exception as e:
        return "Could not fetch the full article. Error: " + str(e)

def display_news(news):
    """
    Displays the news in a simple text format.
    """
    if news:
        for article in news:
            print(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            full_content = get_full_article(article['url'])
            print(f"Content: {full_content}")
            print("-" * 80)
    else:
        print("No news available or there was an error fetching the news.")

def main():
    api_key = '40b85098d5894da8a0e5e4327bc0675d'
    print(f"Fetching news for {datetime.date.today()}...\n")
    news = get_news(api_key)
    display_news(news)

if __name__ == "__main__":
    main()
