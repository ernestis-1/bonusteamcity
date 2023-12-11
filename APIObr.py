import requests

url_adr = 'https://api.tracker.yandex.net/v2/issues'

headers = {
    'Authorization': 'OAuth y0_AgAAAAA5ozOkAAr5RAAAAAD0hryjLDTbl6_eTX2W63pfrtAH6L2bz34',
    'X-Cloud-Org-ID': 'bpf10vaclnlj4tnvv9ko',
    'Content-Type': 'application/json'
}

data = {
    'queue': 'TEAMCITYBUILDFA',
    'summary': 'BUILD REALLY FAIL BRO',
    'assignee': 'e.ivanovernest'
}

response = requests.post(url_adr, headers=headers, json=data)
print(response)