village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
school_details = {"address": "Boalia Bazar", "principal": "Sohidullah Kaisar", "founder": "Johir Raihan", "managing_committee": [{"name": "Sohrab Hossain", "age": 55, "occupation": "Retired person", "designation": "Chairman"}, {"name": "Raisul Islam", "age": 49, "occupation": "Businessman", "designation": "General Member"}, {"name": "Altaf Khan", "age": 33, "occupation": "Founder of Toto Company", "designation": "Vice Chairman"}, {"name": "Sohidul Islam", "age": 45, "occupation": "Businessman", "designation": "General Member"}]}

managing_committee_caniddates = [{"name": "Sultan Ahmed", "age": 43, "occupation": "Service Holder", "designation": "General Member"}, {"name": "Jamsed Khan", "age": 45, "occupation": "Doctor", "designation": "Vice Chairman"}, {"name": "Jahangir Talukder", "age": 47, "occupation": "Doctor", "designation": "Chairman"}, {"name": "Josim Uddin", "age": 38, "occupation": "Farmar", "designation": "Vice Chairman"}]
person = {"name": "Rahim", "age": 34, "height": 5.5, "number_of_childs": 2, "childs": [{"name": "Rafiq", "age": 13, "height": 4.5}, {"name": "Sofiq"}]}
#Dictionary

 print(village_school)
 print(village_school["name"])
 village_school["number_of_rooms"]=20
 print(village_school)
 print(village_school["number_of_rooms"])
 village_school["established"]=1962
 print(village_school)
 print(village_school["established"])
village_school.update(school_details)
 print(village_school)
 print(len(village_school))
 village_school["number_of_class_room"] = 25
 print(village_school["number_of_class_room"])
 print(type(village_school))
 for value in village_school.values():
     print(value)
for key in village_school.keys():
    print(key)
print(len(managing_committee_caniddates),"members are there in the managing commitee")





#Set
 students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
 b = {1, 4, 9, 20, 34}
 print(type(students1))
 print(len(students1))
 students1.add('sweety')
 print(students1)
 students1.remove("risat")
 print(students1)
 students1.discard("raihan")
 print(students1)
 students1.update(students2)
 print(students1)
 print(students1.issubset(students2))
 print(students1.issuperset(students2))

  students1.union(students2)
  print(students1)
 print(students1.union(students2))
 students1.intersection_update(students2)
  print(students1)
 print(students1.intersection(students2))
  students1.symmetric_difference_update(students2)
 print(students1)
 print(students1.symmetric_difference(students2))