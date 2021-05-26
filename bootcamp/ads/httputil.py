import urllib
from urllib import request
import json
import io
from rest_framework.parsers import JSONParser
import os
def getres(name):
    host = os.environ.get('REVIEW_HOST', '')
    #url = "http://127.0.0.1:9998/api/v1/averageRatings/%s/?format=json"%(name)
    url = host+"/api/v1/averageRatings/%s/?format=json"%(name)


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
