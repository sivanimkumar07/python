def create_record(city, comment, visit_date):
    return {
        "city": city,
        "comment": comment,
        "visit_date": visit_date
    }
from tracker import create_record
from datetime import datetime
import json


records = [
    create_record("Paris", "Visited the Eiffel Tower", "05-06-2022"),
    create_record("London", "Enjoyed the city tour", "15-08-2023"),
    create_record("Tokyo", "Tried delicious sushi", "20-12-2024")
]


for record in records:
    date_obj = datetime.strptime(record["visit_date"], "%d-%m-%Y")
    record["visit_date"] = date_obj.strftime("%B %d, %Y")

json_data = json.dumps(records, indent=4)

print("JSON String:")
print(json_data)


parsed_records = json.loads(json_data)

print("\nParsed Records:")
for record in parsed_records:
    print(
        f"City: {record['city']}, "
        f"Comment: {record['comment']}, "
        f"Date: {record['visit_date']}"
    )