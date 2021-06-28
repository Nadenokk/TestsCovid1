import unittest
from lab_planshet_1 import LabPlanshet1
from lab_planshet_2 import LabPlanshet2
from lab_planshet_3 import LabPlanshet3



# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(LabPlanshet1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LabPlanshet2)
tc3 = unittest.TestLoader().loadTestsFromTestCase(LabPlanshet3)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
