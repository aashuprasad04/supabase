```python
import requests

BASE_URL = "https://mofxjzremvuivjaisnyc.supabase.co/rest/v1"
API_KEY = "sb_publishable_A-iGwxUMWBgVZlPXICsSlw_0DBwpIfp"

table_name = "User"
URL = f"{BASE_URL}/{table_name}"

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation",
}

data = {"name": "Rahul", "age": 22}

response = requests.post(URL, headers=headers, json=data)

print(response.status_code)
print(response.json())
```
