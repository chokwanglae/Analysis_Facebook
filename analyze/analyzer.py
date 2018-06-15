import json
import re
# 정규 표현식
# [a-zA-Z1-9] : 모든 문자
# [^\w] : 공백문자로 시작하는 부분
# ex) email 정규표현식 :  var regExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;

def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    jsonfile.close()

    # print(type(json_string), json_string)
    json_data = json.loads(json_string)
    print(type(json_data), json_data)
    data = ''
    for item in json_data:
        value = item.get(key)
        if value is None:
            continue
        data += re.sub(r'[^\w]', '',value)
        # data = ' '.join((data, (re.sub(r'[^\w]', '', value))))

    return data


