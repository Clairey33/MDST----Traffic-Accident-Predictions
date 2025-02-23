# ask for weather condition ("rainy", "sunny", "foggy") and the speed of a car
# if speed > 7 && weather == "rainy" or "foggy" --> print "High change of accident"
# else print "Low chance of accident"

def Ask_for_Weather():
    weather_i = input("Enter the weather condition (rainy, sunny, or foggy): ").strip().lower()
    return weather_i

def Ask_for_Speed():
    speed_i = int(input("Enter the speed: "))
    return speed_i

def Accident_Severity_Predictor():
    weather = Ask_for_Weather()
    speed = Ask_for_Speed()
    if speed > 70 and (weather == "rainy" or weather == "foggy"):
        print("High chance of accident!")
    else:
        print("Low change of accident")

Accident_Severity_Predictor()


## Given a list of vehicle speeds: speeds = [30,45,65,70,85,90]
## count how many vehicles are speeding 
## print the number of speeding vehicles 
speeds = [30,45,65,70,85,90]

def get_num_of_speeding_vehicles(speeds):
    speeding_vehicle = []
    for i in speeds:
        if i > 50:
            speeding_vehicle.append(i) 
    num_of_speeding_veh = len(speeding_vehicle)
    print(num_of_speeding_veh)

get_num_of_speeding_vehicles(speeds)


# create a dictionary with accident prob 
# accident prob = {"morning": 0.1, "afternoon": 0.2, "night": 0.5}
# input time of day 
# print prob of accident
# "Unkown time of day" if invalid input

accident_prob = {"morning": 0.1, "afternoon": 0.2, "night": 0.5}

def get_prob_of_accident():
    time_of_day = input("Input the time of the day: ").strip().lower()
    
    if time_of_day in accident_prob:
        print({accident_prob[time_of_day]})
    else:
        print("Unknown time of day.")

get_prob_of_accident()
