def get_trip(city,visit_date,comment):
    return{
        "city":city,
        "visit_date":visit_date,
        "comment":comment
    }
from tripdata import get_trip
from datetime import datetime
import json
trips = [
    get_trip("Paris", "15-05-2023", "Visited the Eiffel Tower"),
    get_trip("Thailand", "10-08-2024", "Enjoyed local food"),
    get_trip("Dubai", "22-12-2022", "Amazing desert safari")
]
for trip in trips:
     date_obj = datetime.strptime(trip["visit_date"], "%d-%m-%Y").date()
     trip["visit_date"] = date_obj.strftime("%B %d, %Y")
json_data=json.dumps(trips,indent=4)
print(json_data)