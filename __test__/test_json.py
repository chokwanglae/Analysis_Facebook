# http test

import sys
import json
from urllib.request import Request, urlopen
from datetime import datetime

try:
    url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'
    request = Request(url)
    resp = urlopen(request)
    resp_body = resp.read().decode('utf-8') # usally data's type is byte
    print(type(resp_body), resp_body)
    # error
    # print(resp_body["data"])

    # json loader ( str --> dict )
    json_result = json.loads(resp_body)
    print(type(json_result), json_result) # this program is browser. but, dont have image, script, etc... rendering function.0
    # non-error, ( list )
    print(type(json_result['data']), json_result['data'])

except Exception as e:
    print('%s %s' % (e, datetime.now()), file = sys.stdout )

