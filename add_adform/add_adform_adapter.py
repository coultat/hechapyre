import requests
import time
import urllib
import json
import collections
from store.login import login
from store.stroeer_placements_ids import placements
#import mysql.connector
#from adform_placement_ids import best_placements_b as placements



def get_process_id(auth, placement):
    data = {'placement_name': json.dumps(placement)}
    result = requests.post(u'http://ec2-35-156-226-95.eu-central-1.compute.amazonaws.com/api/execute/HeaderBidding/get_prebid_placement_config',
                           data=urllib.parse.urlencode(data),
                           headers={'Content-Type': 'application/x-www-form-urlencoded'},
                           auth=auth,
                           stream=True)
    process_id = result.json()
    return process_id


def get_placement_json(process_id):
    while True:
        placement_info = requests.get(
            'http://ec2-35-156-226-95.eu-central-1.compute.amazonaws.com/api/get_yieldbot_process/' + str(process_id),
            auth = auth,
            stream = True)
        if placement_info.json()['status'] == 2:
            return placement_info.json()
        elif placement_info.json()['status'] == -1 or placement_info.json()['status'] == -2:
            return "NOT PREBID"
        else:
            time.sleep(1)


def declaring_placement_json(placement_data, placement):
    placement_json =collections.OrderedDict()
    placement_json['placement_name'] = json.dumps(placement)
    placement_json['code'] = json.dumps(placement_data['result']['data']['code'])
    placement_json['bids'] = json.dumps(json.dumps(placement_data['result']['data']['bids']))
    auxiliar = [[str(size) for size in sizes] for sizes in placement_data['result']['data']['sizes']]
    auxiliar = ','.join(["x".join(sizes) for sizes in auxiliar])
    placement_json['sizes'] = json.dumps(auxiliar)
    placement_json['breakpointMin'] = json.dumps(str(placement_data['result']['data']['breakpointMin']))
    placement_json['breakpointMax'] = json.dumps(str(placement_data['result']['data']['breakpointMax']))
    placement_json['device'] = json.dumps(placement_data['result']['data']['device'])
    placement_json['minPrice'] = json.dumps(placement_data['result']['data']['minPrice'])
    placement_json['countries'] = json.dumps([])
    placement_json['aliases'] = json.dumps(','.join(placement_data['result']['data']['aliases']))
    placement_json['invalidate_cdn'] = json.dumps(True)
    placement_json['refreshInterval'] = json.dumps(placement_data['result']['data']['refreshInterval'])
    placement_json['refreshMinScreenTime'] = json.dumps(placement_data['result']['data']['refreshMinScreenTime'])
    placement_json['refreshMinVisibility'] = json.dumps(placement_data['result']['data']['refreshMinVisibility'])
    placement_json['refreshPlacementId'] = json.dumps(placement_data['result']['data']['refreshPlacementId'])
    placement_json['refreshScreenIdleTime'] = json.dumps(placement_data['result']['data']['refreshScreenIdleTime'])
    placement_json['refreshMaxImpressions'] = json.dumps(placement_data['result']['data']['refreshMaxImpressions'])
    placement_json['sticky_enabled'] = json.dumps(placement_data['result']['data']['sticky_enabled'])
    placement_json['platform'] = json.dumps(placement_data['result']['data']['platform'])
    return placement_json


def send_the_json(auth, placement_json):
    result = requests.post(
        u'http://ec2-35-156-226-95.eu-central-1.compute.amazonaws.com/api/execute/HeaderBidding/set_prebid_placement_config',
        data=urllib.parse.urlencode(placement_json),
        auth=auth,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        stream=True)
    print(result.json())


def adapting_adform_adapter(adapter, adform_id):
    adapter['params']['mid'] = adform_id
    return adapter


def adapting_stroeer_adapter(adapter, ss_id):
    adapter['params']['sid'] = ss_id
    return adapter


def deleting_adform_redundancy(adapters):
    final_adapter = []
    i = 0
    for adapter in adapters:
        if i == 0 and adapter['bidder'] == 'adform':
            i += 1
            final_adapter.append(adapter)
        elif adapter['bidder'] != 'adform':
            final_adapter.append(adapter)
        if i == 1 and adapter['bidder'] == 'adform':
            print(f"melón aquí!")
    return final_adapter


def check_if_adform_is_inside(placement, adapters):
    helper = 0
    helper = [1 for adapter in adapters if adapter['bidder'] == 'adform']
    if helper == []:
        print(f"check the following placement: {placement}")

adform_adapter = {'bidder': 'adform', 'params': {'mid': 'xxxxxxx'}}
stroeer_adapter = {'params': {'ssat': 1, 'sid': 'xxxxxxxxxxxxx'}, 'bidder': 'stroeerCore'}
auth= login.auth
placements =
for placement in placements:
    print(placement[0])
    process_id = get_process_id(auth, placement[0])
    placement_info  = get_placement_json(process_id)
    #check_if_adform_is_inside(placement[0], placement_info['result']['data']['bids'])
    #adform_adapter = adapting_adform_adapter(adform_adapter, placement[2])
    stroeer_adapter = adapting_stroeer_adapter(stroeer_adapter, placement[1])
    #placement_info['result']['data']['bids'].append(adform_adapter)
    try:
        placement_info['result']['data']['bids'].append(stroeer_adapter)
        placement_formatted = declaring_placement_json(placement_info, placement[0])
        send_the_json(auth, placement_formatted)
        print(placement[0])
    except TypeError:
        print(f"{placement[0]} is not prebid")
    #placement_info['result']['data']['bids'] = deleting_adform_redundancy(placement_info['result']['data']['bids'])
