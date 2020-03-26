from store.stroeer_placements_ids import placements
import urllib
import requests
import json
from store.login import login
i = 0

for placement in placements:
    if 'prebid' in placement[2]:
        i += 1
        print(placement[0], i)
        data = {u'new_setup': json.dumps(placement[2]), u'placement_name': json.dumps(placement[0])}
        result = requests.post(login.change_setup, data=urllib.parse.urlencode(data),
        auth= login.auth,
        headers={'Content-Type': 'application/x-www-form-urlencoded'})