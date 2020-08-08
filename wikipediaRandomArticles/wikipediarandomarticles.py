import json
import requests as req

response ='''{"batchcomplete":"haha","continue":{"rncontinue":"0.598107603571|0.598108276726|5325815|0","continue":"-||"},"query":{"random":[{"id":17249989,"ns":0,"title":"Continental O-520"},{"id":24316758,"ns":0,"title":"Stanislaus Joseph Brzana"},{"id":28271825,"ns":0,"title":"Rigid chain actuator"},{"id":29662411,"ns":0,"title":"B. Michael Watson"},{"id":16459655,"ns":0,"title":"Canton of Doullens"}]}}'''
print(response)

cache_response_map = None

def get_random_articles_from_wiki():
    global cache_response_map, response
    # cache_response_map = json.loads(response)
    if cache_response_map == None:
        print("wiki api called")
        base_url = "https://en.wikipedia.org/w/api.php"
        params = {}
        params["action"] = "query"
        params["list"] = "random"
        params["rnnamespace"] = "0"
        params["rnlimit"] = "5"
        params["format"] = "json"
        response = req.get(base_url, params=params)
        cache_response_map = json.loads(response.text)

map_of_titles = {}
list_of_titles =[]
def get_Titles():
    global map_of_titles,list_of_titles
    get_random_articles_from_wiki()
    for link in cache_response_map["query"]["random"]:
        map_of_titles[link["title"]] = link["id"]
        list_of_titles.append(link["title"])

def get_browse_link(id):
    link = "https://en.wikipedia.org/wiki?curid="
    print(link+ str(id))

def start_session():
    global list_of_titles
    get_Titles()
    while True:
        print("Topics: \n")
        print("\n".join([str(count+1)+". "+title for count,title in enumerate(list_of_titles)]))
        selection = input("Please select a topic you would like to browse")
        chosen_title = list_of_titles[int(selection) - 1]
        get_browse_link(map_of_titles[chosen_title])
        choice = input("Would you like to continue - Y/N")
        if choice == "N" or choice == "n":
            break


if __name__ == "__main__":
    start_session()