import http
import requests
from bs4 import BeautifulSoup

# url = 'http://www.news24.com'

base_url = 'http://www.news24.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
soup1 = BeautifulSoup.prettify(soup)
print(soup1)
for story_heading in soup.find_all(class_="title"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())

# r = requests.get(url)
# soup = BeautifulSoup(r.content)
# soup1 = BeautifulSoup.prettify(soup)
# print(soup1)


# links = soup.find_all('a')
# print(links)
# print(BeautifulSoup(r.content))
# print(soup.prettify())
# print(len(soup))
# print(soup.find_all("a"))

# Finding links "a" and printing then with "href" to see the link
# for link in soup.find_all("a"):
#    print(link.get("href"))

# this is printing the text associated with the link
# for link in links:
#    print("<a href='%s'>%s</a>" %(link.get("href"), link.text))
#    print(link.get("href"))
