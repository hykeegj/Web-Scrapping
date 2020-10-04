import requests
from bs4 import BeautifulSoup


indeed_result = requests.get(
    'https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=C%23&l=')

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

pages = pagination.find_all("a")

spans = []

for page in pages:
    spans.append(page.find("span").string)

for span in spans[:-1]:
    print(span)