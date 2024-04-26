import requests
import traceback
import json
import time


def fetchStateDiff(tx_hash):
    maxTimes = 4
    count = 0
    while count < maxTimes:
        count += 1
        try:
            url = 'https://white-flashy-research.quiknode.pro/661a68de75cca81104455a0cb1b244812d574fef/'
            myobj = {"method":"trace_replayTransaction","params":[tx_hash,["stateDiff"]],"id":1,"jsonrpc":"2.0"}
            x = requests.post(url, json = myobj)
            data = json.loads(x.text)
            result = data["result"]
            stateDiff = result["stateDiff"]
            return stateDiff
        except:
            traceback.print_exc()
            time.sleep(2)
            
    raise Exception("quicknode data retrieval error!")
