# http test

import sys
from urllib.request import Request, urlopen
from datetime import datetime

try:
    url = 'http://www.naver.com'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode('utf-8') # usally data's type is byte
    print(resp_body) # this program is browser. but, dont have image, script, etc... rendering function.
except Exception as e:
    print('%s %s' % (e, datetime.now()), file = sys.stdout )

