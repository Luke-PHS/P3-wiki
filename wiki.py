import wikipediaapi
import time

user_agent = "p3_wiki (therealmeltingdiamond@gmail.com)"
wiki = wikipediaapi.Wikipedia(user_agent, "en")

def fetch_links(page):
    links_list = []
    links = page.links

    for title in links.keys():
        links_list.append(title)

    return links_list

def wikipedia_game_solver(start_page, target_page):
    links = fetch_links(start_page)

for
 


start_page = wiki.page("Spider-Man (2018 video game)")
target_page = wiki.page("Star Wars")
wikipedia_game_solver(start_page, target_page)




print(fetch_links (start_page.links))