
# Chapter 2 – Supabase Setup & Dashboard

| No. | Topic |
|---:|---|
| 11 | Create Supabase Account |
| 12 | Create New Project |
| 13 | Organization |
| 14 | Project Settings |
| 15 | Dashboard Overview |
| 16 | Table Editor |
| 17 | SQL Editor |
| 18 | Database Settings |
| 19 | API Settings |
| 20 | Project URL & API Keys |



## Organization
Create a new organization
Organizations are a way to group your projects. Each organization can be configured with different team members and billing settings.


- project Name -  MyFirstProject 
- pass         -  1197284582L*

### API (Application Programming Interface)
API is way for two diff soft application to communicate with each other 
<br> In simple term API WORKS LIKE A MESSENGER BETWEEN TWO APPLICATION 

## Project Security
- Enable Data API
- Automatically expose new tables
- Enable automatic RLS

#### Enable Data API 
It automatically creates REST API for your databse.

<img width="551" height="453" alt="image" src="https://github.com/user-attachments/assets/6ec8c7ed-ce71-4bea-8377-b867e752e4d4" />

#### Automatically expose new tables 
#### Enable automatic RLS
RLS stands for Row Level Security.
- It controls which rows a user can read, insert, update, or delete.

## DashBoard
<img width="1920" height="1080" alt="db_" src="https://github.com/user-attachments/assets/9cf130ba-6903-4a92-bd73-5722a21810f1" />

# suabase url And api key
<img width="916" height="656" alt="image" src="https://github.com/user-attachments/assets/b8d9e2b3-a93b-4359-b461-6c1ed6bb1b77" />

- REST API URL    :   "https://mofxjzremvuivjaisnyc.supabase.co/rest/v1/"
- PROJECT URL     :   "https://mofxjzremvuivjaisnyc.supabase.co"

<img width="941" height="846" alt="image" src="https://github.com/user-attachments/assets/aa79ae79-e9b3-49ca-8d7b-112264069a5d" />

- API KEY        :    "sb_publishable_A-iGwxUMWBgVZlPXICsSlw_0DBwpIfp"


### Example

```python
# pip install supabase
# pip show supabase


# from supabase import create_client
# 
# url = "YOUR_PROJECT_URL"
# key = "YOUR_PUBLISHABLE_KEY"
# 
# supabase = create_client(url, key)
# 
# print("Supabase client initialized!")




# from PySide6.QtWidgets import *
# 
# from supabase_db import supabase
# 
# 
# class Employee(QWidget):
# 
    # def loadEmployees(self):
# 
        # response = supabase.table("employee").select("*").execute()
# 
        # employees = response.data
# 
        # print(employees)
        

```

- database.py
```python
from supabase import create_client

url = "https://mofxjzremvuivjaisnyc.supabase.co"
key = "sb_publishable_A-iGwxUMWBgVZlPXICsSlw_0DBwpIfp"

supabase = create_client(url,key)
print("Supabase client initialized!")
```
- test.py
```python
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

# ┌──(.venv)─(kali㉿localhost)-[~/Desktop/project/subase/s_connectivity]
# └─$ python test.py 
# Supabase client initialized!
# Loading Use....
# [{'id': 1, 'created_at': '2026-11-10T17:58:34.033728+00:00', 'name': 'Aashu', 'age': 21}]
                                                                                        #     
# ┌──(.ven
```
