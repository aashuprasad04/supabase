```python
# Common Setup (same for all operation)
import requests

# BASE_URL = 'https://mofxjzremvuivjaisnyc.supabase.co'
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
```
