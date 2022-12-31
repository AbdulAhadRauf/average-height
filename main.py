height=input("Enter heights of the students\n").split()
total=0
total_students=0
for tall in range(0,len(height)):
  height[tall]=int(height[tall])
#   total = total + height[tall]
# print("The average is",round(total/len(height)))
for i in height:
  total+=i
for a in height:
  total_students+=1
print("The average is",round(total/total_students))