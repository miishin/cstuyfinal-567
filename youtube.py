from apiclient.discovery import build
from apiclient.errors import HttpError
import argparse

API_KEY = "AIzaSyBS4C_zq3U0NoWld0Q42Hv07EXqDHgPaCQ"


def search(args):
    youtube = build("youtube", "v3", developerKey = API_KEY)
    response = youtube.search().list(q = args.query, part = "id, snippet", maxResults = args.numResults).execute()
    vidList = []
    linkList = []
    link = "http://www.youtube.com/watch?v="
    for result in response.get("items",[]):
        if result["id"]["kind"] == "youtube#video":
                  vidList.append(result["snippet"]["title"])
                  linkList.append(link + result["id"]["videoId"])
    return vidList, linkList
    

def youtubeSearch(searchItem):
    x = argparse.ArgumentParser()
    try:
        x.add_argument("--query", help = "Item to search for", default = searchItem)
        x.add_argument("--numResults", help = "number of results", default = 10)
    except ArgumentError:
        x.query = searchItem
    y = x.parse_args()
    try:
        return search(y)
    except HttpError, e:
        print "HTTP error %s:%s" % (e.resp.status, e.content)
        
