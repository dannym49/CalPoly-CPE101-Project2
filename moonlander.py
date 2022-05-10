from landerFuncs import *

def main():
   showWelcome()
   altitude = getAltitude()
   fuel = getFuel()
   gravity = 1.62
   time = 0
   rate = 0
   velocity = 0
   print("\nLM state at retrorocket cutoff")
   while (fuel > 0) and (altitude > 0) : 

      displayLMState1(time, altitude, velocity, fuel, rate)
      rate = getFuelRate(fuel)
      time+=1
      acceleration = updateAcceleration(gravity, rate)
      altitude = updateAltitude(altitude, velocity, acceleration)
      velocity = updateVelocity(velocity, acceleration)
      fuel = updateFuel(fuel, rate)

   if fuel == 0:
      while altitude > 0:
         print("OUT OF FUEL - Elapsed Time: %3d Altitude: %7.2f Velocity: %7.2f" % (time, altitude, velocity))
         rate = 0
         fuel = 0
         time +=1
         fuel = updateFuel(fuel, rate)
         acceleration = updateAcceleration(gravity, rate)
         altitude = updateAltitude(altitude, velocity, acceleration)
         velocity = updateVelocity(velocity, acceleration)
         
   print("\nLM state at landing/impact")
   altitude = 0
   displayLMState1(time, altitude, velocity , fuel, rate)

   displayLMLandingStatus(velocity)

if __name__ == '__main__':
   main()
   
   