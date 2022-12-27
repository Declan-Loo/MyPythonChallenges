"""
A264	100	
ROCKET LAUNCH	
Create an instance of a planet class, and if I enter a planet's mass and radius, the program should output the escape velocity required for the rocket	
"""

#Import math module
import math

#Initalise class called Planet
class Planet:
    #Initlaise mass/radius arguments
    def __init__(self, massP, radiusP):
        self.mass = massP
        self.radius = massP
    
    #Get the escape velocity
    def get_escape_velocity(self):
        #Calculate escape velocity (formula: square root of 2GM/r where G is gravitational constant or 6.67 x 10^-11) and M is mass and r is radius of planet)
        x = "Escape velocity required for the rocket:" + str(math.sqrt((2*6.67 * 10**-11 * self.mass)/self.radius)) + 'm/s'
        return x

#Get input for planet mass and radius
planetMass = float(input("Mass of the planet: "))
planetRadius = float(input("Radius of the planet: "))

#Create an instance of Planet class
myPlanet = Planet(planetMass,planetRadius)

#Get the escape velocity by using one of the methods defined in the class.
print(myPlanet.get_escape_velocity())
