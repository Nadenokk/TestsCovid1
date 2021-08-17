import unittest
from covid_research_by_institution_new import CovidResearchByInstitutionNew
from covid_research_by_institution import CovidResearchByInstitution
from covid_research_by_institution_new_by_sections import CovidResearchByInstitutionNewBySections
from otchet_for_epidemiologists import OtchetForEpidemiologists
from passengers_violators import PassengersViolators



# Get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(CovidResearchByInstitutionNew)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CovidResearchByInstitution)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CovidResearchByInstitutionNewBySections)
tc4 = unittest.TestLoader().loadTestsFromTestCase(OtchetForEpidemiologists)
tc5 = unittest.TestLoader().loadTestsFromTestCase(PassengersViolators)

# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])

unittest.TextTestRunner(verbosity=2).run(smokeTest)