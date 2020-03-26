from store.sample import placements
import json
import random

def transforming_placements_json(placements):
    mother_placement = []
    for placement in placements:
        son = json.dumps({'name': placement[0], 'sizes':placement[1], 'created': 'no'})
        son = json.loads(son)
        mother_placement.append(son)
    return mother_placement


def transforming_websites_json(placements):
    websites = []
    mother_website = []
    [websites.append(placement[0][:placement[0].find('_')]) for placement in placements
     if placement[0][:placement[0].find('_')] not in websites]
    for website in websites:
        web_json = json.dumps({'website': website, 'desktop': [],'mobile': [], 'tablet': [], 'desk_created': 'no', 'mob_created': 'no', 'tab_created': 'no'})
        web_json = json.loads(web_json)
        mother_website.append(web_json)
    return mother_website


def merging_placements_websites(websites, placements):
    for website in websites:
        [website['desktop'].append(placement) for placement in placements
        if website['website'] in placement['name'] and '_d_' in placement['name']]
        [website['mobile'].append(placement) for placement in placements
         if website['website'] in placement['name'] and '_m_' in placement['name']]
        [website['tablet'].append(placement) for placement in placements
         if website['website'] in placement['name'] and '_t_' in placement['name']]
    return websites

websites_json = []
placements_json = []
final_json = []
placements_json = transforming_placements_json(placements)
websites_json = transforming_websites_json(placements)
websites_json = merging_placements_websites(websites_json, placements_json)


