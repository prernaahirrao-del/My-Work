def ride(base_fare,distance_km,traffic_delay_mins):
    #standard rates
    cost_per_km = 12.0
    cost_per_minute = 2.0

    #Single variable arithmetic
    distance_cost = distance_km * cost_per_km
    time_cost = traffic_delay_mins * cost_per_minute

    total_fare = base_fare + distance_cost + time_cost

    if traffic_delay_mins > 20:
        total_fare = total_fare * 1.20 # Apply 20% surge multiplier

    return total_fare

    #customer requests a trip estimates

ride_1 = ride(30 , 5.5 , 5)#Normal Traffic
ride_2 = ride(30 , 5.5 , 25) #heavy traffice surge

print("Cloud Ride Hailing Calculation")
print("Normal trip :",round(ride_1,2))
print("Surger trip : ",round(ride_2,2))