import json

stra = "{'name': '冯振振', 'age': '23', 'job': 'Python engineer', 'motto': 'I like coding'}, {'name': '康康', 'age': '23', 'job': 'web engineer', 'motto': '专业前端，不至于前端'}"
json_load = eval(stra)
print(json_load)