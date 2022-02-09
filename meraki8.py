import json
a={"name":"neelam","Designation":"programer","age":24,"salary":2400}
b={"name":"komal","Designation":"trainer","age":24,"salary":20000}
c={"name":"anuradha","Designation":"HR","age":25,"salary":40000}
d={"name":"Abhishek","Designation":"manager","age":29,"salary":63000}
m=[]
m.append(a)
m.append(b)
m.append(c)
m.append(d)
with open("meraki8.json","w")as dict1:
    json.dump(m,dict1,indent=4)
