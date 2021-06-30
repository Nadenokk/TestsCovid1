import unittest
from Research_creation.create_Antitel import CreateAntitel
#from Research_creation.create_barcode import CratePcr
from Research_creation.create_Express import CreateExpress
from Research_creation.create_OKI3 import CreateOKI3
from Research_creation.create_OKI4 import CreateOKI4
from Research_creation.create_PCR import CreatePCR
from Barcode_Verification.Barcode import Barcode1
from Barcode_Verification.Barcodev2 import Barcode2
from Check_module_express_testing_for_command_execution.Express_test_status import ExpressTestStatus
from Create_analyses.Create_analyzes import CreateAnalyzes
from Create_Passengers.Create_passanger import CreatePassanger
from Filling_Lab_Tablets.lab_planshet_1 import LabPlanshet1
from Filling_Lab_Tablets.lab_planshet_2 import LabPlanshet2
from Filling_Lab_Tablets.lab_planshet_3 import LabPlanshet3
from Research_creation.create_public import CreatePublic
# Get all tests
tc1 = unittest.TestLoader().loadTestsFromTestCase(CreateAntitel)
#tc2 = unittest.TestLoader().loadTestsFromTestCase(CratePcr)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CreateExpress)
tc4 = unittest.TestLoader().loadTestsFromTestCase(CreateOKI3)
tc5 = unittest.TestLoader().loadTestsFromTestCase(CreateOKI4)
tc6 = unittest.TestLoader().loadTestsFromTestCase(CreatePCR)
tc7=unittest.TestLoader().loadTestsFromTestCase(Barcode1)
tc8=unittest.TestLoader().loadTestsFromTestCase(Barcode2)
tc9=unittest.TestLoader().loadTestsFromTestCase(ExpressTestStatus)
tc10=unittest.TestLoader().loadTestsFromTestCase(CreateAnalyzes)
tc11=unittest.TestLoader().loadTestsFromTestCase(CreatePassanger)
tc12 = unittest.TestLoader().loadTestsFromTestCase(LabPlanshet1)
tc13 = unittest.TestLoader().loadTestsFromTestCase(LabPlanshet2)
tc14 = unittest.TestLoader().loadTestsFromTestCase(LabPlanshet3)
#tc15 = unittest.TestLoader().loadTestsFromTestCase(CreatePublic)

# Create a test suite combining
smokeTest = unittest.TestSuite([ tc1, tc3, tc4, tc5, tc5, tc7, tc8, tc9, tc10, tc11, tc12, tc13, tc14])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
