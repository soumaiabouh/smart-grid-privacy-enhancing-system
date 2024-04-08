import pymongo

from pymongo import MongoClient

import csv
from datetime import datetime

cluster = MongoClient("mongodb+srv://User1:TestPassword9028_@cluster0.boy2x7w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = cluster["SmartMeters"]
collection = db["dataInfo"]

multipleApartmentcollection = db["multipleApartments"]


#send data from DC to database

'''
can use collection.insert_one(post) or collection.insert_many(post)
'''




#calculate the sum of power used during the whole year

attribute_name = "power"

pipelineYear = [
    {"$group": {"_id": None, "total": {"$sum": f"${attribute_name}"}}}]

resultYear = list(collection.aggregate(pipelineYear))

print(f"Total sum of {attribute_name} per Year: {resultYear[0] ['total']}")


#sum of power used during  month
date_string_template  = "1/{day}/2016"
total_power = 0

for day in range(1, 32):
    date_to_search = date_string_template.format(day=day)

    
    pipelineMonth = [
        {
            "$match":{
                "time": {"$regex": f"^{date_to_search}"}
            }
        },
        {"$group": {"_id": None, "total": {"$sum": f"${attribute_name}"}}}
        
        ]
        
    resultMonth = list(collection.aggregate(pipelineMonth))
    if resultMonth:
        total_power += resultMonth[0]["total"]
             
print(f"Total sum of {attribute_name} per Month: {total_power}")



array = []
for index in range(10):
    array.append([0,0,0,0,0])



for index in range(101, 111):    

    for hour in range(24):
        pipelineMonth = [
                {
                    "$match":{
                        "apartment": index,
                        "time": {"$regex": f"2016 {hour}:"}
                        
                    }
                },
                {"$group": {"_id": None, "total": {"$sum": f"${attribute_name}"}}}
                
                ]
        result = list(multipleApartmentcollection.aggregate(pipelineMonth))
                
        if 0<= hour < 6:                       
            array[index-101][0] += result[0]["total"]       

        elif 6 <= hour < 12:
            array[index-101][1] += result[0]["total"]

        elif 12 <= hour < 18:
            array[index-101][2] += result[0]["total"]

        elif 18 <= hour < 21:
            array[index-101][3] += result[0]["total"]

        elif 21 <= hour < 24:
            array[index-101][4] += result[0]["total"]
        
    



#print(resultMonth)

#print(f"Total sum of {attribute_name} per Month: {total_power}")

#checkTotal= 0;


            
consumptionArray=[]
for x in range(5):
    consumptionArray.append(0)

for apt in range(10):

    maxConsumption =0
    partOfDay=-1
    for x in range(5):
        if(array[apt][x] > maxConsumption):
            maxConsumption = array[apt][x]
            partOfDay = x
    consumptionArray[partOfDay] += 1

print(consumptionArray)
        
#print(array)



'''
    if(array[x] > maxConsumption):
        maxConsumption = array[x]
        partOfDay = x
    
    #checkTotal+=array[x]

#print(checkTotal)
        
if partOfDay ==0:
    print("early morning")
elif partOfDay == 1:
    print("morning")
elif partOfDay == 2:
    print("afternoon")
elif partOfDay == 3:
    print("evening")
elif partOfDay == 4:
    print("night")

'''


    
'''
collection.segment.drop()

header = ["time", "power"]
filename = open('Apt100_2016.csv', 'r')
reader = csv.DictReader(filename)

for each in reader:
    rows = {}
    for field in header:
        rows[field] = each[field]
        
    
    collection.insert_one(rows)
    
#collection.segment.insert(rows)




#insert a single entry/post

post = {"_id": 0, "name": "v", "score": 5}

collection.insert_one(post)


#insert many entries/posts

post1 = {"_id": 10, "name": "joe"}
post2 = {"_id": 7, "name": "bill"}

collection.insert_many([post1, post2])

#search for an attribute

results = collection.find({"name": "bill"})


for result in results:
    print(result)
    print(result["_id"])

results1 = collection.find_one({"_id": 0})
print(results1)


#delete an entry/post

collection.delete_one({"_id": 0})


#to delete many use .delete_many

#to update can do collection.update_one({"_id": 5},{"$set": {"name": "tim"})
#can also use this to add a field
'''
