import requests
import xmltodict
import json

class Client:
        def __init__(self, key):
            self.key = key
            self.BASE_URL = 'http://apis.data.go.kr/9760000/PofelcddInfoInqireService/getPoelpcddRegistSttusInfoInqire?serviceKey={0}'.format(key)

        def checkKey(self):
            return self.key

        def searchCandidate(self, id, code, sggname='', sdname='', page='1', number='999'):
            try:
                response = requests.get(f'{self.BASE_URL}&pageNo={page}&numOfRows={number}&sgId={id}&sgTypecode={code}&sggName={sggname}&sdName={sdname}').text
                jsonData = json.loads(json.dumps(xmltodict.parse(response)))
                return jsonData['response']['body']['items']['item']
            except:
                return jsonData['result']

        def serverStatus(self, id, code, sggname='', sdname='', page='1', number='999'):
            response = requests.get(f'{self.BASE_URL}&pageNo={page}&numOfRows={number}&sgId={id}&sgTypecode={code}&sggName={sggname}&sdName={sdname}').text
            jsonData = json.loads(json.dumps(xmltodict.parse(response)))
            jsonData = jsonData['response']['header']
            return jsonData

        def candiCount(self, id, code, sggname='', sdname='', page='1', number='999'):
            response = requests.get(f'{self.BASE_URL}&pageNo={page}&numOfRows={number}&sgId={id}&sgTypecode={code}&sggName={sggname}&sdName={sdname}').text
            jsonData = json.loads(json.dumps(xmltodict.parse(response)))
            jsonData = jsonData['response']['body']['totalCount']
            return jsonData

