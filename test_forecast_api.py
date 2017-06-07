#encoding:utf-8
import urllib2, sys
import json

# refference url http://qiita.com/shizuma/items/ad04e08ab31ba436d34e
try: citycode = sys.argv[1]
except: citycode = '130010' #東京
resp = urllib2.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()

# 読み込んだJSONデータをディクショナリ型に変換
resp = json.loads(resp)
print '**************************'
print resp['title']
print '**************************'
print resp['description']['text']

for forecast in resp['forecasts']:
    print '**************************'
    print forecast['dateLabel']+'('+forecast['date']+')'
    print forecast['telop']
print '**************************'
