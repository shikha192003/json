import json
dic={"Name":"Abhishek","Designation":"CEO of navgurukul","Gender":"male","Age":29}
with open("meraki7.json","w")as dict1:
    json.dump(dic,dict1,indent=4)