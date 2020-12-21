# -*- coding: utf-8 -*-
"""Python Simulations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UNLWxxKWFJDNo_e1nqINedoov7s9AJGS
"""

total_population=50
growth_factor=1.00005
day_count=0  #Every 2 months the population is reported

while total_population < 1000000:
  total_population *= growth_factor
  #Every 56th day population is reported
  day_count +=1
  if day_count==56:
    day_count=0
    print(total_population)

#Creating the Variables.
import random
starting_population=50
infant_mortality=25
agriculture=5
disaster_chance=10
food=0
fertilityx=18
fertilityy=35

#Store the all these pepole into list
people_dictionary=[]

class person:
  def __init__(self,age):
    self.gender=random.randint(0,1)
    self.age=age

#Creating Harvest function
def harvest(food,agriculture):
  ablepeople=0
  for person in people_dictionary:
    if person.age > 8:
      ablepeople +=1

  food +=ablepeople * agriculture

  if food < len(people_dictionary):
    del people_dictionary[0: int(len(people_dictionary)-food)]
    food=0
  else:
    food-=len(people_dictionary)

#To grow our population, we need a reproduce function
def reproduce(fertilityx,fertilityy):
  for person in people_dictionary:
    if person.gender==1:
      if person.age > fertilityx:
        if person.age > fertilityy:
          if random.randint(0,5)==1:
            people_dictionary.append(person(0))

#Bedining simulation
def beginsim():
  for x in range(starting_population):
    people_dictionary.append(person(random.randint(18,50)))

beginsim()

def run_year(food, agriculture, fertilityx , fertilityy):
  harvest(food, agriculture)
  reproduce(fertilityx, fertilityy)
  for person in people_dictionary:
    if person.age > 80:
      people_dictionary.remove(person)
    else:
      person.age +=1

  
  reproduce(fertilityx, fertilityy, infant_mortality)
  if random.randint(0,100)<disasterChance:
    del people_dictionary[0:int(random.uniform(0.05,0.2)*len(people_dictionary))]
    print(len(people_dictionary))
    infant_mortality *= 0.985
  
  return infant_mortality

while len(people_dictionary)<100000 and len(pepole_dictionary)> 1:
  infant_mortality=run_year(food, agriculture, fertilityx , fertilityy)






