from analysis_fb.collect.api import api

# 전처리
def preprocess_post(post):
    pass

def crawling(pagename, since, until):
    print("crawling " + pagename)
    for posts in api.fb_fetch_posts(pagename, since, until):
        print(posts)
        print(len(posts))


