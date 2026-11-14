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

- response.status_code
```python
print(response.status_code)
```
HTTP Status code is three digit number returned by the server to tell the client whether its request was successful or failed.

```txt
Code	    Name	        Meaning
200	        OK	            Request successful
201	        Created	        New record created
204	        No Content	    Successful request, no response body
400	        Bad Request	    Invalid request
401	        Unauthorized	Authentication failed
403	        Forbidden	    Access denied
404	        Not Found	    Resource not found
409	        Conflict	    Data conflict
500	        Internal Server Error	Server-side error
```
