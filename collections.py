# myFruitList = ['apple', 'banana', 'cherry']

# print(type(myFruitList))

# edades = {
#     "samuel" : 22,
#     100 : 125
# }

# for key, value in edades.items():
#     if type(key) == int:
#         key = str(key)
        
#     print (key, value)
    

myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))