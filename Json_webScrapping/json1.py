import json
d={"101":"ram","102":"arjun","103":"ravi"}
jsonStr=json.dumps(d)
# jsonStr is the serialized form of the dictionary
print(jsonStr)
dic_Json=json.loads(jsonStr)
print(dic_Json)
