social_data = {'gender':[{'code':'male','weight':19},{'code':'female','weight':18}],'gender_per_age':[{'code':'1','male':2.4,'female':2.9},{'code':'2','male':2.1,'female':4},{'code':'3','male':2.9,'female':8},{'code':'4','male':2.2,'female':2}]}
dic1 = social_data['gender_per_age']
val = dic1[0]
print(val)
dic2 = dic1.keys()

for value in dic1:
    value2 = list(value.keys()) 
    print(value2[1] + " - " + value2[2])

for value in social_data['gender_per_age']:
    value2 = list(value.keys()) 
    print(value2[1] + " - " + value2[2])