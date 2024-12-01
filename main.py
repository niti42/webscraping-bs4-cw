import requests
from bs4 import BeautifulSoup


url = "https://news.ycombinator.com/news"

response = requests.get(url=url)
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all("span", class_="titleline")


article_texts = []  # title
article_links = []  # link
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.find("a").get("href")
    article_links.append(link)

# upvotes
article_upvote = [int(score.get_text().split()[0]) for score in soup.find_all(
    name="span", class_="score")]

highest_upvote = max(article_upvote)
highest_upvote_idx = article_upvote.index(highest_upvote)

max_upvote_article_link = article_links[highest_upvote_idx]
max_upvote_article = article_texts[highest_upvote_idx]

# print(article_texts)
# print(article_links)
print(max_upvote_article_link)
print(max_upvote_article)
