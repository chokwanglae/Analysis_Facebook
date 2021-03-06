# FaceBook API Wrapper Functions

from urllib.parse import urlencode
from .web_request import json_request

# https://graph.facebook.com/v3.0/jtbcnews/?token=ca31dsqw3&since=20170101&until=20171231&limit=50
BASE_URL_FB_API = 'https://graph.facebook.com/v3.0'
ACCESS_TOKEN = 'EAACEdEose0cBAHzG9gybYOlhspewi6l5ZB45urTwZBnddzi8suAyPAHQDJ33ryPYbZCZCjdfLGmZAvT4eq6y7qM7uhAHySZB1eyXyOSMm3ZAU7VquaV0x47ZC0HUEdzLNpBMHZCyMtbWZCZAPHRRo1EUBfOoyzX7Ujgmd6dTNiodh7DWfks5TzYaw9OQNllTKvsuZAWMTRO981yMfgabB1iXyh1C'

def fb_gen_url(
        base=BASE_URL_FB_API,
        node='', #node
        **params #parameters # params = {'since':20170101, 'until':20171231, 'limit':50}
):
    # https://graph.facebook.com/v2.8/[Node, Edge]/?parameters
    url = '%s/%s/?%s' % (base, node, urlencode(params))
    return url

def fb_name_to_id(pagename):
    url = fb_gen_url(node=pagename, access_token=ACCESS_TOKEN)
    json_result = json_request(url=url)
    print(json_result)
    return json_result.get("id")

def fb_fetch_posts(pagename, since, until):
    url = fb_gen_url(
        node=fb_name_to_id(pagename)+"/posts",
        fields='id,message,link,name,type,shares,reactions,created_time,comments.limit(0).summary(true).limit(0).summary(true)',
        since=since,
        until=until,
        limit=50,
        access_token=ACCESS_TOKEN
    )
    results = []
    isnext = True
    while isnext is True:
        json_result = json_request(url=url)
        posts = None if json_result is None else json_result.get('data')
        paging = None if json_result is None else json_result.get('paging')
        # paging = None
        # if json_result is None:
        #     paging = None
        # else:
        #     paging = json_result.get('paging')
        url = None if paging is None else paging.get("next") #next url
        isnext = url is not None
        # if url is not None:
        #     isnext = True
        # else:
        #     isnext = False
        yield posts
