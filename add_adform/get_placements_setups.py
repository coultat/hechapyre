import mysql.connector
import re
from store.login import login
#from duplicated_placements import best_placements as placements
from store.stroeer_placements_ids import placements


def post_bid(raw_setup, new_network = ''):
    final_setup_beg = []
    network_setup = []
    possible_networks = ['adf', 'adt', 'nxs', 'nxs2', 'rbhb', 'cthb', 'pp2hb', 'pphb', 'pp3hb', 'ss', 'tl', 'pbhb',
                         'ox2', 'ox', 'sahb', 'ot', 'svhb', 'dm', 'iehb']
    final_setup_beg.extend([result + '>' for result in raw_setup if 'adx1' == result.lower()])
    final_setup_beg.extend([result + '>' for result in raw_setup if 'adx1a' == result.lower()])
    final_setup_beg.extend([result + ',' for result in raw_setup if 'ct' == result.lower()])
    final_setup_beg.extend([result + ',' for result in raw_setup if 'rb' == result.lower()])
    helper = [1 for result in raw_setup if result.lower() in possible_networks]
    if helper != []:
        final_setup_beg.extend('[')
        network_setup = ",".join([result for result in raw_setup if result.lower() in possible_networks])
        final_setup_beg.extend([new_network, network_setup, ']', '>'])
    final_setup_beg.extend([result + '>' for result in raw_setup if 'adx1b' == result.lower()])
    final_setup_beg.extend([result for result in raw_setup if 'dc1' == result.lower() or 'pb' == result.lower()])
    final_setup_beg = "".join(final_setup_beg)
    return final_setup_beg


connection = mysql.connector.connect(
    host=login.db_host,
    port="3306",
    user= login.db_user,
    password=login.db_password)


cursor = connection.cursor()
cursor.execute("""USE db00055768""")
final = []
#change this to add some new network to the setup
new_network = ''
for placement in placements:
    query = "SELECT n.short FROM netzwerke n WHERE netzwerke_id in (SELECT pn.netzwerke_id FROM platzierung_netzwerke pn JOIN platzierung ON platzierung.platzierung_id =  pn.platzierung_id WHERE platzierung.name = (%s) AND fill<> 99);"
    cursor.execute(query, (placement[0],))
    rows = cursor.fetchall()
    raw_setup = []
    raw_setup.extend(result for row in rows for result in row)
    final_setup_beg = []
    network_setup = []
    end_setup = []
    dc = ''


    if 'ADX1' in raw_setup:
        final.append([placement[0],placement[1],post_bid(raw_setup, new_network)])
    else:
        final_setup_beg.extend([result for result in raw_setup if result.find('prime')>0])
        final_setup_beg.extend([result for result in raw_setup if result.find('prebid')>0])
        final_setup_beg.extend('[')
        network_setup.extend([result for result in raw_setup if result.lower().find('adx')<0 and len(re.findall('dc[0-9]', result.lower())) < 1 and result.lower().find('a9') < 0 and result.lower().find('nbf') < 0 and result.lower().find('pb') < 0])
        network_setup.extend([new_network])
        network_setup = ','.join(network_setup)
        final_setup_beg = '-'.join(final_setup_beg)
        if 'a9' in raw_setup or 'A9' in raw_setup:
            final_setup_beg += network_setup + '] - [A9]/'
        else:
            final_setup_beg += network_setup + '] /'
        end_setup.extend([result for result in raw_setup if result.lower().find('[A9]') > 0])
        end_setup.extend([result for result in raw_setup if result.lower().find('nobid') > 0])
        end_setup.extend([result for result in raw_setup if len(re.findall('adx[0-9][a-z]', result.lower())) > 0 and (result.lower().find('nobid') < 0 and result.lower().find('prebid') <0 and result.lower().find('prime') <0 )])
        if len(end_setup) > 1:
            end_setup = '>'.join(end_setup)
        else:
            end_setup = ' '.join(end_setup)
        dc = '>'.join([result for result in raw_setup if len(re.findall('dc[0-9]', result.lower())) > 0 or result.lower().find('nbf') > -1 or result.lower().find('pb') > -1 or result.lower().find('tw') > -1])

        if dc != '':
            if dc.lower() == 'pb':
                end_setup = end_setup + '>' + dc
            elif final_setup_beg[3] == dc[2]:
                end_setup = end_setup + '>' + dc
            else:
                end_setup = end_setup + '>>' + dc
        final_setup_beg += end_setup
        try:
            final.append([placement[0],placement[1],final_setup_beg])
        except AttributeError:
            print(f"ERROR {placement[0]}")


for data in final:
    print(f"{data},")