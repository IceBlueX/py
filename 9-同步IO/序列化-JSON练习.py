import json

obj = dict(name = '小明', age = 20)
s = json.dumps(obj, ensure_ascii = False)#True 显示ascii码 FALSE显示汉字 默认为真

print(s)
