steps_data={
   "Saturday": 1000,
   "Sunday": 3500,
   "Monday": 1100,
   "Tuesday": 6850,
   "Wednesday": 5200,
   "Thursday": 2750,
   "Friday": 15400,
}

total_steps=0
count=0
max_steps=None
min_steps=None
goal=5000
goal_days=0

for day , steps in steps_data.items():
    count+=1
    total_steps+=steps
    
    if max_steps is None or max_steps < steps:
        max_steps = steps
        
    if min_steps is None or min_steps > steps:
        min_steps = steps
        
    if goal <= steps :
        goal_days+=1
        
if count>0:
    average = total_steps/count
    goal_percentage= (goal_days/count)*100
    
    print("Total Steps is " ,total_steps)
    print("Average Steps is " ,f"{average:.2f}")
    print(" Max Steps is " ,max_steps)
    print("Min Steps is " ,min_steps)
    print("Goal Days is " ,goal_days , "which is" , f"{goal_percentage:.2f}%")
    print("Total Days is " ,count)

else:
    print("No steps Available")
    
    
        

        
        
    
 
    

    
    

