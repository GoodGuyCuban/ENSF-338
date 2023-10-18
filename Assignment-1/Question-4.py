import json
from uuid import uuid4


with open("/home/marcos/dev/ENSF-338/Assignment-1/documents.json", "r") as f:
    data = json.load(f)


for i, record in enumerate(data):
    record["id"] = str(uuid4())


with open("/home/marcos/dev/ENSF-338/Assignment-1/documents_unique.json", "w") as f:
    json.dump(data, f)

with open("/home/marcos/dev/ENSF-338/Assignment-1/documents_unique.json", "r") as f:
    data = json.load(f)


sum_values = 0
count = 0
for record in data:
    if record["pages"] > 5:
        sum_values += record["pages"]
        count += 1
average = sum_values / count

print(average)