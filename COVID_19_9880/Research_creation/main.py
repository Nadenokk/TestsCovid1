import unittest
from create_Antitel_lGg import CreateAntitel
from create_barcode import CratePcr
from create_Express import CreateExpress
from create_OKI3 import CreateOKI3
from create_OKI4 import CreateOKI4
from create_PCR import CreatePcr


# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateAntitel)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CratePcr)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CreateExpress)
tc4 = unittest.TestLoader().loadTestsFromTestCase(CreateOKI3)
tc5 = unittest.TestLoader().loadTestsFromTestCase(CreateOKI4)
tc6 = unittest.TestLoader().loadTestsFromTestCase(CreatePcr)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
