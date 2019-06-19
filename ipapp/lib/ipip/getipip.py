from __future__ import unicode_literals
import ipdb, sys


def getip(ip):
    db = ipdb.City("./ipipfree.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    print(db.find(ip, "CN"))
    print(db.find_map(ip, "CN"))
    print(db.find_info(ip, "CN").city_name)
    print(db.find_info(ip, 'CN').isp_domain)
    print(db.find_info(ip, 'CN').country_name)


getip('120.27.22.91')

