import requests
from PySide6.QtWidgets import *

from hdr import headers, BASE_URL

table_name = "food_entry"
URL = f"{BASE_URL}/{table_name}"

response = requests.get(URL, headers=headers)
data = response.json()

# print first row
# print(data[0])
# print(data[0]["food_name"])

# item = QTableWidgetItem(str())


# {'id': 3, 'created_at': '2026-11-17T03:48:04.10944+00:00', 'food_name': 'sfda', 'qty': 10110.0, 'cal': None, 'protein': None, 'carb': None, 'fat': None}
# for row, item in enumerate(data):
#     print(data[row]["id"])
#     print(data[row]["food_name"])
#     print()



for row , item in enumerate(data):
    for col, key in enumerate(["id", "food_name", "qty", "cal", "protein", "carb", "fat"]):
        item = QTableWidgetItem(str(data[row][key] or "") )
        print(data[row][key] or "-")
    print()
