import pytest
import glob
from radon.raw import analyze
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


@pytest.mark.order(1)
def test_codequality(search_str):
    ncomments = 0
    nloc = 0
    for filename in glob.glob(search_str):
        with open(filename) as fobj:
            source = fobj.read()
            report =  analyze(source)
            ncomments+=report.comments
            nloc+=report.loc
    print("#comments:",ncomments,"#loc:",nloc, "#comments/#loc:", ncomments / nloc)
    assert nloc != 0
    assert ncomments / nloc >= 0.25

@pytest.mark.order(2)
def test_commit_messages():
    import git
    repo = git.Repo("./../../")
    count = repo.git.rev_list('--count', 'HEAD')

    # num_comments = at least five times the number of handled assignments
    assignmentCount=1
    if (os.path.exists("../assignments")):
        assignmentCount = len(next(os.walk('../assignments'))[1])
    assert int(count)>=assignmentCount*5

@pytest.mark.order(3)
def testTask1():
    import ass01_1 as p01
    if p01.text[0][:4]=='FEST':
        print("\nSchiller-Test zu Aufgabe 1")
        assert p01.temp_code == "NRNEHEUDAS"
        assert p01.codeword == "REEDS"
    else:
        print("\nTest zu Aufgabe 1")
        assert p01.temp_code == "DASPOFTERL"
        assert p01.codeword == "APFEL"

@pytest.mark.order(4)
def testTask2():
    import ass01_2 as p01
    print("\nTest zu Aufgabe 2")
    assert p01.message1 == "RTFVQXSSE"
    assert p01.code1 == "X"
    assert p01.message1_val == [17, 19, 5, 21, 16, 23, 18, 18, 4]
    assert p01.result1_val == [6, 4, 18, 2, 7, 0, 5, 5, 19]
    assert p01.result1 == "GESCHAFFT"

@pytest.mark.order(5)
def testTask3():
    import ass01_3 as p01
    if p01.text[0][:4]=='FEST':
        print("\nSchiller-Test zu Aufgabe 3")
        assert p01.message == "SEW^Y[ELMBPEQBV"
        assert p01.codeword == "REEDS"
        assert p01.message_val == [18, 4, 22, 29, 24, 26, 4, 11, 12, 1, 15, 4, 16, 1, 21]
        assert p01.result_val == [3, 0, 18, 30, 10, 11, 0, 15, 15, 19, 30, 0, 20, 2, 7]
        assert p01.result == "DAS_KLAPPT_AUCH"
    else:
        print("\nTest zu Aufgabe 3")
        assert p01.message == "SLCVZCILAG"
        assert p01.codeword == "APFEL"
        assert p01.message_val == [18, 11, 2, 21, 25, 2, 8, 11, 0, 6]
        assert p01.result_val == [18, 4, 7, 17, 18, 2, 7, 14, 4, 13]
        assert p01.result == "SEHRSCHOEN"

if __name__ == "__main__":
    test_codequality("ass*")
    test_commit_messages()
    testTask1()
    testTask2()
    testTask3()
