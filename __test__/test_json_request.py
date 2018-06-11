###



from analysis_fb.collect.api import web_request as a

url = 'http://kickscar.cafe24.com:8080/myapp-api/api/user/list'


def print_json(json_result):
    print(type(json_result), json_result) # this program is browser. but, dont have image, script, etc... rendering function.0
    # non-error, ( list )
    print(type(json_result['data']), json_result['data'])

def json_request(
        url='',
        encoding='utf-8',
        success=None,
        error=lambda e: print('%s %s' % (e, a.datetime.now()), file=a.sys.stdout)
        ):
    try:
        request = a.Request(url)
        resp = a.urlopen(request)
        resp_body = resp.read().decode(encoding) # usally data's type is byte
        json_result = a.json.loads(resp_body) # json loader ( str --> dict )

        print('%s : success for request[%s]' % (a.datetime.now(), url))

        if callable(success) is False:
            return json_result

        success(json_result)

    except Exception as e:
        print('%s %s' % (e, a.datetime.now()), file=a.sys.stdout)

json_request(url=url, success=print_json, error=a.error_my)
