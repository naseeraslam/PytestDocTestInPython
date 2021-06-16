import pytest

from Student_Record import *


# Parameterize  Testing Or Data Driven Test
# @pytest.mark.skip
@pytest.mark.parametrize("FName_S,expected_result",
                         [("Naseer", "Found"), ("Farhan", "Found"), ("Bash", "Found"), ("Sohaib", "Found"),
                          ("Munna", "Found"), ("Meesna", "Found"),
                          ("Wahab", "Found"), ("Haji", "Found")])
def test_Record_ManyTestSearchByName(_sd, FName_S, expected_result):
    x = _sd.SearchByFirstName(FName_S)
    assert expected_result == x


def test_Record_Entery(_sd):
    x = _sd.AdressBook("Naseer", "Aslam", "03062403761", "Lahore", "naseeraslam456@gmail.com", "Student")
    assert "Saved" == x


@pytest.mark.slow
def test_Record_SearchByName(_sd):
    x = _sd.SearchByFirstName("Naseer")
    assert "Found" == x


@pytest.mark.search
def test_Record_SearchByMobile(_sd):
    x = _sd.SearchByMobile("03062403761")
    assert "Found" == x


@pytest.mark.skip
def test_Record_SearchByEmail(_sd):
    x = _sd.SearchByEmail("bitf17a039@pucit.edu.pk")
    assert "Found" == x


@pytest.mark.extraslow
def test_Record_SearchByAllName(_sd):
    x = _sd.SpecialSearchByFirstName("Nas")
    assert "Found" == x


# @pytest.mark.skip
def test_Record_UpdateByName(_sd):
    x = _sd.UpdateRecord("Meesna", "MNA", "Aslam", "03062403761", "Lahore", "bitf17a039@pucit.edu.pk", "Student")
    assert "Updated" == x


# Fixtures In Pytest
@pytest.fixture //Alternate Of Setup
def _sd():
    # DocString
    "Creat Object of class Enter 2 enteries and then clear Contact Diary"
    _sd = StudentData()
    _sd.AdressBook("Naseer", "Aslam", "03062403761", "Lahore", "bitf17a039@pucit.edu.pk", "Student")
    _sd.AdressBook("Sohaib", "Salman", "03164141268", "Karachi", "bitf17a040@pucit.edu.pk", "CR")
    _sd.AdressBook("Munna", "Aslam2", "03062453761", "Mumbai", "bitf17a030@pucit.edu.pk", "Police Officer")
    _sd.AdressBook("Bash", "Salmanqe", "03168141068", "Layyah", "bitf17a042@pucit.edu.pk", "Teacher")
    _sd.AdressBook("Farhan", "Aslam", "03069403761", "Kasur", "bitf17a035@pucit.edu.pk", "Farmer")
    _sd.AdressBook("Meesna", "Salman", "03164141008", "Islamabad", "bitf17a020@pucit.edu.pk", "Engineer")
    _sd.AdressBook("Haji", "Aslam2", "03062406761", "Larkana", "bitf17a010@pucit.edu.pk", "Lawyer")
    _sd.AdressBook("Wahab", "Salmanqe", "03168141068", "KingDom", "bitf17a012@pucit.edu.pk", "Professor")
    _sd.AdressBook("Naseer", "Aslam", "03062403761", "Kasur", "bitf17a039@pucit.edu.pk", "Software Engineer")
    yield _sd //Alternate of teardown
    _sd.clear()

# Program run commands
# python -m pytest
# python -m pytest -m "not Veryslow"
# pytest --fixtures -v test_Student_Record.py
# coverage run -m unittest
# pytest --cov-report html: --cov=Student_Record .
#python -m pytest --html=ReportOfPytest.html Generating Pytest report
# python -m pytest --html=Test_Report.html Generating Pytest report
# python -m doctest Student_Record.py
