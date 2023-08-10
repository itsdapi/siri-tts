import secret
import random
import hashlib
import requests

api = "https://fanyi-api.baidu.com/api/trans/vip/translate"
secrets = secret.secrets
appid = secret.appid


def whatis(_query: str, _source_la: str, _target_la: str):
    salt = str(random.randint(0, 10000))
    sign = signGen(appid, secrets, _query, salt)
    try:
        result = requests.get(f"{api}?q={_query}&from={_source_la}&to={_target_la}&appid={appid}&salt={salt}&sign={sign}")
        if 'trans_result' in result.json():
            print("baidu translator request success")
            dst = result.json()['trans_result'][0]['dst']
        else:
            raise requests.exceptions.RequestException(result.json())
        print(dst)
        return dst
    except requests.exceptions.RequestException as error:
        print(error)
        print("baidu translator fail!, returning source language.")
        return _query


def signGen(_appid, _secrets, _query, salt):
    str1 = _appid + _query + salt + _secrets
    # print(f"str1 = {str1}")
    str1_md5 = hashlib.md5(str1.encode('utf-8')).hexdigest()
    # print(f"signGen success: {str1_md5}")
    return str1_md5


if __name__ == '__main__':
    source_la = input("source_la: ")
    target_la = input("target_la: ")
    query = input("query: ")
    whatis(query, source_la, target_la)
