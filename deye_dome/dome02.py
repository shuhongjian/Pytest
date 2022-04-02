import json

json_pan = "C:/Users/Administrator/Desktop/test-bome/dome.txt"
json_file = open(json_pan,"r",encoding="utf-8")
a = json_file.read()

# 展示消除格式的json字符串
print(a.replace('\n','').replace('\r','').replace(' ',''))


# output_file = "C:/Users/Administrator/Desktop/test-bome/dome01.txt"
# f = open(output_file, 'w', encoding='utf-8')
# f.write(a.replace('\n','').replace('\r','').replace(' ',''))


# a = open("C:/Users/Administrator/Desktop/test-bome/dome.txt")
# a.read()
# print(a)