from random import randint

#Some random comments that teachers always use for school reports 
Comments = ['is an enthusiastic learner who seems to enjoy school.','exhibits a positive outlook and attitude in the classroom.',"appears well rested and ready for each day's activities."
"shows enthusiasm for classroom activities.","shows initiative and looks for new ways to get involved.","uses instincts to deal with matters independently and in a positive way.","strives to reach their full potential.","is committed to doing their best.","seeks new challenges.","takes responsibility for their learning.","cooperates consistently with the teacher and other students.","transitions easily between classroom activities without distraction.","is courteous and shows good manners in the classroom.","follows classroom rules.","conducts themselves with maturity.","responds appropriately when corrected.","remains focused on the activity at hand.","resists the urge to be distracted by other students.","is kind and helpful to everyone in the classroom.","sets an example of excellence in behavior and cooperation."]

number = int(input("Number of students: "))
NameList = []
for i in range(number):
  name = input("Name: ")
  NameList.append(name)

for i in range(number):
  print(NameList[i],Comments[randint(0,19)])

  #alternatively can do random.choice(Comments) as well.
