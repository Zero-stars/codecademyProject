weight = 41.5       #weight in lbs
#dollar
ground_cost = 0    
premium_cost = 125.00
drone_cost = 0

#Ground Shipping
if weight<=2:
  ground_cost = 20.00 + 1.50*weight
elif weight<=6:
  ground_cost = 20.00 + 3.00*weight
elif weight<=10:
  ground_cost = 20.00 + 4.00*weight
elif weight>10:
  ground_cost = 20.00 + 4.75*weight

print ("Ground shipping: $" + str(ground_cost))

#Ground Shipping Premium
print("Ground Shipping Premium: $" + str(premium_cost))

#Drone Shipping
if weight<=2:
  drone_cost = 0.00 + 4.50*weight
elif weight<=6:
  drone_cost = 0.00 + 9.00*weight
elif weight<=10:
  drone_cost = 0.00 + 12.00*weight
elif weight>10:
  drone_cost = 0.00 + 14.25*weight

print("Drone shipping: $" + str(drone_cost))

