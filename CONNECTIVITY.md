
# Connection
```zsh
python -m venv .venv
source .venv/bin/activate
```

1. Install python library
```zsh
pip install supabase
pip show supabase
```

2. database.py
```sql
from supabase import create_client

url = "https://mofxjzremvuivjaisnyc.supabase.co"
key = "sb_publishable_A-iGwxUMWBgVZlPXICsSlw_0DBwpIfp"

supabase = create_client(url,key)
print("Supabase client initialized!")
```
3. test.py
```sql
# import sys
# from PySide6.QtWidgets import *
from database import supabase

# class MWindow(QWidget):
        
def loadUser():
        print("Loading Use....")
        response = supabase.table("User").select("*").execute()
        user = response.data
        print(user)

loadUser()

```
- output
```zsh
┌──(.venv)─(kali㉿localhost)-[~/Desktop/project/subase/s_connectivity]
└─$ python test.py 
Supabase client initialized!
Loading Use....
[{'id': 1, 'created_at': '2026-11-10T17:58:34.033728+00:00', 'name': 'Aashu', 'age': 21}]
                                                                                            
┌──(.venv)─(kali㉿localhost)-[~/Desktop/project/subase/s_connectivity]
```
