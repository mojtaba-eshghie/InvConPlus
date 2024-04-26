import json 
import requests
import time
import traceback
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Accessing the variables
api_path = os.getenv('QUICKNODE_API_PATH')



def fetchAllRuntimeInformation(tx_hash):
    maxTimes = 4
    count = 0
    while count < maxTimes:
        count += 1
        try:
            url = api_path
            myobj = {"method":"trace_replayTransaction","params":[tx_hash,["vmTrace", "trace", "stateDiff"]],"id":1,"jsonrpc":"2.0"}
            x = requests.post(url, json = myobj)
            data = json.loads(x.text)
            return data 
        except:
            traceback.print_exc()
            time.sleep(2)
            
    raise Exception("quicknode data retrieval error!")

def fetchVmTrace(tx_hash):
    maxTimes = 4
    count = 0
    while count < maxTimes:
        count += 1
        try:
            url = api_path
            myobj = {"method":"trace_replayTransaction","params":[tx_hash,["vmTrace"]],"id":1,"jsonrpc":"2.0"}
            x = requests.post(url, json = myobj)
            data = json.loads(x.text)
            result = data["result"]
            vmTrace = result["vmTrace"]
            # output = result["output"]
            return vmTrace
        except:
            traceback.print_exc()
            time.sleep(2)
            
    raise Exception("quicknode data retrieval error!")

def fetchStateDiff(tx_hash):
    maxTimes = 4
    count = 0
    while count < maxTimes:
        count += 1
        try:
            url = api_path
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


if __name__ == "__main__":
    account = "Yearn Finance"
    tx_block = "17222636"
    tx_hash = "0x948b94e827664564401571632d0b2405c09776f1d2bbbdd16f8a068e80e161e1"
    stateDiff = fetchStateDiff(tx_hash=tx_hash)
    vmTrace = fetchVmTrace(tx_hash=tx_hash)
    json.dump(stateDiff, open("stateDiff.json", "w"))
    json.dump(vmTrace, open("vmTrace.json", "w"))