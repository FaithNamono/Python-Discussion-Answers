# Question 1(ii)
# The volume of a sphere with radius r is (4/3)*pie*r**2. What is the volume of the sphere with radius 5. 
# Use a function and make sure the radius is entered from the keyboard and provide the answer in 2 decimal place
import math

# Function to calculate the volume of a sphere
def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius**2)
    return round(volume, 3)
radius = float(input("Enter the radius of the sphere: "))
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is {volume}")


# Question 1
# Temperature Classifier: Using a function, write a Python script that takes a temperature as input and classifies
#  it into the 
# following categories: 
# Below 0°C: Freezing
# 0 to 10°C: Cold 
# 11 to 20°C; Moderate 
# 21 to 30°C: Warm 
# Above 30°C: Hot 

# Function to classify temperature
def classify_temperature(temp):
    if temp < 0:
        return "Freezing"
    elif 0 <= temp <= 10:
        return "Cold"
    elif 11 <= temp <= 20:
        return "Moderate"
    elif 21 <= temp <= 30:
        return "Warm"
    else:
        return "Hot"

temperature = float(input("Enter the temperature: "))
classification = classify_temperature(temperature)

print(f"The temperature is classified as: {classification}")



