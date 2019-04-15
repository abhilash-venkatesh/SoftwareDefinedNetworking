import urllib.parse
import requests
import json
from tabulate import *
from get_ticket import *
import time

requests.packages.urllib3.disable_warnings()

def path_trace(srcip,dstip):
    ticket = get_ticket()
    headers = {
     "content-type": "application/json",
     "X-Auth-Token": ticket
    }

    api_url = "https://sandboxapicem.cisco.com/api/v1/flow-analysis"
    body_json = {
      "destIP": dstip,
      "sourceIP": srcip
    }

    resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    response_json = resp.json()
    flowAnalysisId = response_json["response"]["flowAnalysisId"] 
    print("The flowAnalysisId is :", flowAnalysisId)

    api_url = "https://sandboxapicem.cisco.com/api/v1/flow-analysis/"+flowAnalysisId
    status="INPROGRESS"
    while status == "INPROGRESS":
        resp=requests.get(api_url, headers=headers, verify=False)
        response_json = resp.json()
        status = response_json["response"]["request"]["status"]
        print("Path Trace Status : ",status)
        time.sleep(1)

    trace_list = []
    i = 0
    for item in response_json["response"]["networkElementsInfo"]:
         i+=1
         node = [
                 i,
                 item["type"],
                 item["ip"],
                ]
         trace_list.append( node )
    table_header = ["Number", "Type", "IP Address"]
    print( tabulate(trace_list, table_header) )
