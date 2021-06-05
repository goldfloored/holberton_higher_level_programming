#!/usr/bin/python3
""" add to json file module """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

l = []
open("add_item.json", "a")
try:
    l = load_from_json_file("add_item.json")
except Exception:
    l = []
save_to_json_file(l + sys.argv[1:], "add_item.json")
