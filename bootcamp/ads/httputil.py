import urllib
from urllib import request
import json
import io

import os
import asyncio
import aiohttp
from . import redisutil
import redis

def sendSign(name):
    con1 = redisutil.getCon()
    ps = con1.pubsub()
    con1.publish('review-channel', name)
    return


def getres(name):
    from rest_framework.parsers import JSONParser
    host = os.environ.get('REVIEW_HOST', '')
    url = host + "/api/v1/averageRatings/%s/?format=json" % (name)

    with request.urlopen(url) as f:
        data = f.read()
        str1 = data.decode('utf-8')
        stream = io.BytesIO(data)
        data2 = JSONParser().parse(stream)

        # data_obj = json.loads(str1)
    return data2


async def getaysncres(session, url):
    async  with session.get(url) as resp:
        res1 = await  resp.json()
        return res1


async def getresMain(name):
    res = redisutil.getRankingStatus(name)
    if res !=  {}:
        return res

    sendSign(name)


    # async with aiohttp.ClientSession() as session:
    #     host = os.environ.get('REVIEW_HOST', 'http://127.0.0.1:9998/')
    #     url = host + "/api/v1/averageRatings/%s/?/" % (name)
    #     tasks = []
    #     tasks.append(asyncio.ensure_future(getaysncres(session, url)))
    #     reslist = await  asyncio.gather(*tasks)
    #     # for i in reslist:
    #     #     print(i)
    #     # return 'abc'
    #     # [i for i in reslist]
    #     redisutil.setLocalCache(name, reslist )
    #     return reslist

if __name__ == '__main__':
    pass
    # res = getres('aa')
    # print(res)
    # a =  getresMain('aa')
    res  = asyncio.run(getresMain('liyi2'))
    print(res)