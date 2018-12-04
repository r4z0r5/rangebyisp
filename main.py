#!/usr/bin/python3


import requests
import sys

if len(sys.argv) < 2 or sys.argv[1] == '-h':
    print('''
Usage: rangebyisp.py ISP-NETNAME

    -h is for this help message :)
    ''')

else:
    url = ('https://rest.db.ripe.net/search.json?query-string=%s&flags=no-filtering&source=RIPE' % sys.argv[1])
    try:
        data = requests.get(url).json()['objects']['object']
    except:
        print('[-] No data for this ISP, you could try searching for it\'s proper netname ;)')
        exit(1)

    for object in data:
        try:
            if object['type'] == 'inetnum':
                print(object['attributes']['attribute'][0]['value'])
        except:
            print('[-] No ip range info')
