import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
soup = BeautifulSoup(r.text)


soup = BeautifulSoup(r, "lxml")


# "css-nic7nv ee0hn7b0" "css-eylb5n ee0hn7b0"

for story_heading in soup.find_all(class_="css-eylb5n ee0hn7b0"):
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())