import pytest
from radon.raw import analyze
import os
import glob

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
    repo = git.Repo("./")
    count = repo.git.rev_list('--count', 'HEAD')

    # num_comments = at least five times the number of handled assignments
    if (os.path.exists("assignments")):
        assignmentCount = len(next(os.walk('assignments'))[1])
    assert int(count)>=assignmentCount*5

if __name__ == "__main__":
    test_codequality("assignments/assignment*/ass*")
    test_commit_messages()
