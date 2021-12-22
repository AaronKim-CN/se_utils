import requests
from math import ceil
import time

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def log(content):
    print(time.strftime('%Y-%m-%d %H:%M:%S -'), content)

def get_results(app_id, id_list):

    log('get result app_id: {}, #number: {}'.format(app_id, len(id_list)))
    if not id_list:
        return {'app_id': app_id, 'result': {}}
    url = "url"
    headers = {
        'Accept': "application/json, text/plain, */*",
    }
    merged_j = {}
    for index, chunk in enumerate(chunks(id_list, 50)):
        log('get result, batch: [{}/{}]'.format(index + 1, ceil(len(id_list) / 50)))
        querystring = {"appId": app_id,
                       "idlist": ','.join(chunk)}
        response = requests.request("GET", url, headers=headers, params=querystring)
        j = response.json()
        to_delete_keys = []
        for k, v in j['result'].items():
            if k.endswith('boxInfo'):
                to_delete_keys.append(k)
        for key in to_delete_keys:
            del j['result'][key]
        merged_j.update(j['result'])
    
    #check if all id got urls
    return_list = []
    for index, id in enumerate(id_list):
        if id in merged_j:
            return_list.append(merged_j[id])
        else:
            return_list.append("nodata")
    
    return return_list