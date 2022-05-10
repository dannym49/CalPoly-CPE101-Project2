# Project 2 - Moonlander
# 
# Name: Danny Moreno
# Version: Workman

def showWelcome():
   print("\nWelcome aboard the Lunar Module Flight Simulator\n")
   print("   To begin you must specify the LM's initial altitude") 
   print("   and fuel level.  To simulate the actual LM use") 
   print("   values of 1300 meters and 500 liters, respectively.\n")
   print("   Good luck and may the force be with you!\n")

def getFuel():
   fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))

   while fuel < 0:
      print("ERROR: Amount of fuel must be positive, please try again")
      fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))

   return fuel

def getAltitude():
   altitude =int(input("Enter the initial altitude of the LM (in meters): "))
  
   while altitude < 1 or altitude > 9999:
      print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
      altitude =int(input("Enter the initial altitude of the LM (in meters): "))
 
   return altitude


def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   time = elapsedTime
   altitude = altitude
   fuel = fuelAmount
   vel = velocity
   rate = fuelRate
   print("Elapsed Time:", "%4d" % time, "s" )
   print("        Fuel:", "%4d" % fuel, "l"  )
   print("        Rate:", "%4d" % rate , "l/s")
   print("    Altitude: %7.2f" % altitude, "m")
   print("    Velocity: %7.2f" % velocity, "m/s")

def displayLMState1(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   time = elapsedTime
   altitude = altitude
   fuel = fuelAmount
   vel = velocity
   rate = fuelRate
   print("Elapsed Time:", "%4d" % time, "s" )
   print("        Fuel:", "%4d" % fuel, "l"  )
   print("        Rate:", "%4d" % rate , "l/s")
   print("    Altitude: %7.2f" % altitude, "m")
   print("    Velocity: %7.2f" % velocity, "m/s\n")

def getFuelRate(currentFuel):
   fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   
   while fuelRate < 0 or fuelRate > 9:
      print("ERROR: Fuel rate must be between 0 and 9, inclusive")
      fuelRate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
   if fuelRate > currentFuel:
      return currentFuel
   else:
      return fuelRate
   
def updateAcceleration(gravity, fuelRate):
   return gravity*((fuelRate/5)-1)
    

def updateAltitude(altitude, velocity, acceleration):
   return altitude + velocity + (acceleration/2)


def updateVelocity(velocity, acceleration):
   return velocity + acceleration
   

def updateFuel(fuel, fuelRate):
   return fuel - fuelRate
   

def displayLMLandingStatus(velocity):
   if 0 >= velocity >= -1:
      print("Status at landing - The eagle has landed!")
   elif -2 >= velocity > -10:
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif velocity <=-10:
      print("Status at landing - Ouch - that hurt!")
