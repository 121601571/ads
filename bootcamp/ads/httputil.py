import urllib
from urllib import request
import json
import io
from rest_framework.parsers import JSONParser

def getres(name):
    url = "http://127.0.0.1:8000/api/v1/averageRatings/%s/?format=json"%(name)
    print(url)
    with request.urlopen(url) as f:
        data = f.read()
        str1 = data.decode('utf-8')
        stream = io.BytesIO(data)
        data2 = JSONParser().parse(stream)

        #data_obj = json.loads(str1)
    return data2

if __name__ == '__main__':
    pass
    res = getres('aa')
    print(res)
