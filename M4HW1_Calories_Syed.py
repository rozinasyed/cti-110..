# Calories Burned  
# CTI-110M4HW1 - Calories Burned
# 6/20/17
#Syed


caloriesBurnedPerMinute = 4.2

for numberOfMinutes in range(10, 31, 5 ):
    numberOfCaloriesBurned = ( numberOfMinutes / 1) * caloriesBurnedPerMinute
    print(" You will burn", numberOfCaloriesBurned, "calories in", \
       numberOfMinutes, "minutes")
