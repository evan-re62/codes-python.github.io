#!/usr/bin/env python3

import requests
import argparse

parser = argparse.ArgumentParser(description="Displays the weather for a city")
parser.add_argument("city", type=str, help="city for which you want the weather")
args = parser.parse_args()
 
url = "https://wttr.in/"+args.city+"?lang=fr"
r = requests.get(url)
r.encoding = "utf-8"
print(r.text)