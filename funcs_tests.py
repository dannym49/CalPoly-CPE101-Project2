# Project 2 - Moonlander
# 
# Name: Danny Moreno
# Version: Workman

import unittest
from landerFuncs import *

class TestCases(unittest.TestCase):
   def test_update_acc1(self):
      self.assertAlmostEqual(updateAcceleration(1.62, 0), -1.62)
   def test_update_acc2(self): 
      self.assertAlmostEqual(updateAcceleration(1.62, 10), 1.62)
   def test_update_alt1(self): 
      self.assertAlmostEqual(updateAltitude(100, 5, 3), 106.5)
   def test_update_alt2(self): 
      self.assertAlmostEqual(updateAltitude(400, 5, 3), 406.5)
   def test_update_vel1(self): 
      self.assertAlmostEqual(updateVelocity(20, -1.62), 18.38)
   def test_update_vel2(self): 
      self.assertAlmostEqual(updateVelocity(-5, -1.62), -6.62)
   def test_update_fuel(self): 
      self.assertAlmostEqual(updateFuel(100, 5), 95)
   def test_update_fu2(self): 
      self.assertAlmostEqual(updateFuel(403, 9), 394)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

