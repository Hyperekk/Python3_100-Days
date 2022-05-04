from bs4 import BeautifulSoup
import requests

URL = "http://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text,"html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movie_list = [item.getText() for item in movie_tags]
movie_list.reverse()

with open("movies.txt","w") as f:
    for movie in movie_list:
        f.write(f"{movie} \n")





# print(article_scores[max_index])
# print(article_links[max_index])
# print(article_names[max_index])


# article_text = article_tags.getText()
# article_link = article_tags["href"]
# print(articles)



















# with open("website.html") as f:
#     content = f.read()

# soup = BeautifulSoup(content, 'html.parser')

# section_heading = soup.find(name="h3",class_ ="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url)