import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text             # Now inside the variable r_html, you have the HTML of the page as a string.
soup = BeautifulSoup(r_html, "lxml")        # using BeautifulSoup to solve the problem of parsing, adding feature "lxml" as a parser?

# "css-nic7nv ee0hn7b0" "css-eylb5n ee0hn7b0"

for story_heading in soup.find_all(class_='ee0hn7b0'):
    print(story_heading.contents[0])