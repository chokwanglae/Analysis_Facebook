# def html_request

import sys
import json
from urllib.request import Request, urlopen
from datetime import datetime

def print_html(html):
    print(html)

def print_error(e): # insert to the param error code
    print('%s %s' % (e, datetime.now()), file=sys.stdout) # == print('%s %s' % (e, datetime.now())) (생략가능)

def error_my(e):
    pass

def html_request(
        url='',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stdout)
        ):
    try:
        request = Request(url)
        resp = urlopen(request)
        html = resp.read().decode(encoding) #.decode(encoding)
        # print(type(html), html)

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return html

        success(html)

    except Exception as e:
        if callable(error) is False:
            error(e)


# html_request(url='http://www.naver.com')
# html_request(url='http://www.naver.com', success=print_html) # function to parameter >> print_html(html)
# html_request(url='http://www.naver.com', success=print_html, error=error_my)


def json_request(
        url='',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s %s' % (e, datetime.now()), file=sys.stdout)
        ):
    try:
        request = Request(url)
        resp = urlopen(request)
        resp_body = resp.read().decode(encoding) # usally data's type is byte
        json_result = json.loads(resp_body) # json loader ( str --> dict )

        print('%s : success for request[%s]' % (datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)

    except Exception as e:
        print('%s %s' % (e, datetime.now()), file=sys.stdout)
