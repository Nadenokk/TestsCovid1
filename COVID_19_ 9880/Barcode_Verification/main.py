import unittest
from Barcode import Barcode1
from Barcodev2 import Barcode2



# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(Barcode1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Barcode2)


# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
