# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 23:30:20 2016

@author: welion
"""
import os
import sys
import pygeoip

DATA_FILE = "GeoLiteCity.dat"



def printGeoInfo(target):
    gi = pygeoip.GeoIP(DATA_FILE)
    rec = gi.record_by_name(target)
    city = rec['city']
    country = rec['country_name']
    longitude = rec['longitude']
    latitude = rec['latitude']
    print '[*] Target: ' + target + ' Geo-located!'
    print '[+] ' + str(city) + ', ' + str(country) 
    print '[+] Longitude: ' + str(longitude) + ', Latitude:' + str(latitude)
    
if __name__ == '__main__':
    target = "210.13.121.74"
    printGeoInfo(target)