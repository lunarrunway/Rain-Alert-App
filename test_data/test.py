import ast
import json

with open("temp_test.json", mode="r") as inpt:
    current = inpt.readline()
    test_json = ast.literal_eval(json.dumps(current))
    print(current)
    print(test_json)

now = json.loads(test_json)
json.dumps(now, indent=1)

# print(json_data)
# file = open("temp_test.json")
# test_data = json.load(file)
# print(test_data)
