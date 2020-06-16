import json

numbers = [3,5,61,89,1,23]

filename = "numbers.json"
with open(filename, 'w') as f:
    json.dump(numbers, f)


