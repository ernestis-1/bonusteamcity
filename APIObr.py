import requests

url_adr = 'https://api.tracker.yandex.net/v2/issues'

headers = {
    'Authorization': 'OAuth y0_AgAAAAA5ozOkAAr5RAAAAAD0hgNx0WF7dIF2QaKhs4lJ4XonLTn8x0U',
    'X-Cloud-Org-ID': 'bpf10vaclnlj4tnvv9ko',
    'Content-Type': 'application/json'
}

data = {
    'queue': 'TEAMCITYBUILDFA',
    'summary': 'BUILD IS REALLY DOWN',
    'assignee': 'e.ivanovernest'
}



result = requests.post(url_adr, headers=headers, json=data)
print(result)

