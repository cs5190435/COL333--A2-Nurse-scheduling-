import json
import re
import sys

data = []
try:
    with open('solution.json') as f:
        for line in f:
            data.append(json.loads(line))
except Exception as e:
    print(f"FAILED | Not able to read file as a list of jsons (key value are string), make sure every assignment is in different line | Error : {e}")
    sys.exit()

assert type(data)==type([]),"FAILED | Not able to read file as a list of solutions, make sure every assignment is in different line"

for line,sol in enumerate(data):
    assert type(sol)==type({}), f"FAILED | Every solution line should be json | Error in line | {line+1}"
    for key,value in sol.items():
        assert type(key)==type(""),f"FAILED | Key should be of string form | Error in line {line+1} | key : {key}"
        assert type(key) == type(""), f"FAILED | Value should be of string form | Error in line {line+1} | value : {value}"
        k = re.compile(r"[0-9]+").sub("##",key)
        assert k=="N##_##", f"FAILED | Key should be of N#_# where # is number (0,1...) form | Error in line {line} | key : {key}"
        assert value in ["R","M","A","E"], f"FAILED | Value should be one of the following - A,E,M,R | Error in line {line} | value : {value}"

print("PASSED")