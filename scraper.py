import requests
from bs4 import BeautifulSoup
import pprint


def sort_articles_by_votes(hn):
    return reversed(sorted(hn, key=lambda k: k['votes']))


def create_custom_hn(links, votes, sub, hn):
    for idx, item in enumerate(links):
        if sub[idx]:
            if idx < len(votes):
                points = votes[idx].getText()
            else:
                points = "0 votes"  # Default value for articles without votes
            clear_points = int(points.partition(' ')[0])
            if clear_points >= 100:
                title = links[idx].getText()
                href = links[idx].get('href', None)
                hn.append({'title': title, 'link': href, 'votes': points})
    return hn

if __name__ == '__main__':
    pages = int(input('Please enter the number of pages you want to scrape: '))
    hn = []

    for page in range(1, pages + 1):
        url = f'https://news.ycombinator.com/news?p={page}'
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.titleline > a')
        sub = soup.select('.subtext')
        votes = soup.select('.score')
        best_articles = create_custom_hn(links, votes, sub, hn)
        print(f'Done Scraping Page: {page} \u2713')

    sorted_best_articles = sort_articles_by_votes(best_articles)
    for article in sorted_best_articles:
        pprint.pprint(article)
