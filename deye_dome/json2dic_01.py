import json

json_path = "C:/Users/Administrator/Desktop/test-bome/json.json"
json_file = open(json_path,"r",encoding="utf-8")
json_dic = json.load(json_file)
print(json_dic)

output_file = "C:/Users/Administrator/Desktop/test-bome/test.txt"
f = open(output_file, 'w', encoding='utf-8')
for j in list(json_dic.keys()):
    try:
        print(json_dic[j]['type'])
        # *print(j + "\t" + json_dic[j]['type'])
        print(j)
        lines = j + "\t" + json_dic[j]['type'] + "\n"
        f.write(lines)
    except:
        # print(j)
        f.write(j)


f.close()