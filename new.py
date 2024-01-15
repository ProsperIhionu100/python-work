# import json
# import requests
# from pprint import pprint

# data ='''
# [
#     {"id":"001",
#      "x"   : "7",
#      "name" : "brent"
#     },    
    
#     {"id":"007",
#      "x"   : "6",
#      "name" : "chuks"
#     },    
    
#    {"id":"019",
#     "x"   : "8",
#     "name" : "benice",
#     "skills" :["A","B","C"]   
    
         
    
# ]'''

# #info = json.loads(data)
# #for p in info:
#  #   print(p)
#   #  print(p["sills"][0])if "sills" in p else...
  
# BASE_ENDPOINT = "http://fakestoreapi.com/"
# url = "products/" 
# CART_ENDPOINT = "carts/"
# post_data ={
#         "title" :"benice",
#         "price" : 1.5,
#         "categories" :'electronic'
#     }
# response = requests.post(url, json=post_data)
# data = response.json()
# pprint(data, indent=4)


# import json 
# user = {
#     "name" : "Miracle",
#     "age"  : "38",
#     "state": "oopiata",
#     "city" : "johnwickCity"
#  }

# food = '{food1":"eba","food2":amala","food3:"rice"}'
# print(food)
# add = {"food4":"beans" + food}
# print(add) 

import json 
# food = '{"food1":"eba","food2":"amala","food3":"rice"}'
# adding = json.loads(food)
# # adding["food4"] = "beans"
# # print(adding)

# print(adding['food1']) 


# user = '{"name":"John","age":"60",}'
# checkingkey = json.loads(user)
# if 'nameff' in checkingkey:
#     print('Name exists in json object')
# else:
#     print('Name does not exists in json')
    
user1 = '{"name":"John", "age":30}'
user2 = '{"city":"New york", "country":"USA"}'
user3 = '{"Occupation":"Engineer"}'
data1 = json.loads(user1)
data2 = json.loads(user2)
data3 = json.loads(user3)
merge_data = {}
merge_data.update(data1)
merge_data.update(data2)
merge_data.update(data3)

merged_json =json.dumps(merge_data)

print(merged_json)

