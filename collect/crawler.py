import os
import json
from datetime import datetime, timedelta
from .api import api

RESULT_DIRECTORY = '__results__/crawling'


# 전처리   # 이 함수는 외부로 보여지고 싶지 않은데? --> init과 main 부분 변경
def preprocess_post(post):
    if 'shares' not in post:
        post['count_shares'] = 0
    else:                                              # shares라는 컬럼이 안에 있다면,
        post['count_shares'] = post['shares']['count'] # count_shares로 새로 넣듬

    # 전체 코멘트 수
    if 'comments' not in post:
        post['count_comments'] = 0
    else:
        post['count_comments'] = post['comments']['summary']['total_count']
    # 데이터를 불러올 depth를 줄이는 단순한 전처리를 배워보았다.

    # KST = UTC + 9
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst + timedelta(hours=9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')

def crawling(pagename, since, until, fetch=True):
    results = []
    for posts in api.fb_fetch_posts(pagename, since, until):
        for post in posts:
            preprocess_post(post)
        results += posts
    # save results to file(저장, 적재)
    filename = '%s/%s_%s_%s.json' % (RESULT_DIRECTORY, pagename, since, until)
    with open(filename, 'w', encoding='utf-8') as outfile:
        json_string = json.dumps(results, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(json_string)

    return filename

# 경로가 없으면 만들자
if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)

