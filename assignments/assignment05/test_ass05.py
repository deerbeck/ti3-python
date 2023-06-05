import pytest

import glob
from radon.raw import analyze
import sys, os
import subprocess

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def get_commit_count_exclude_user(folder_path, username):

    cmd = ["git", "log", "--format='%H %an'", "--", folder_path]
    
    output = subprocess.check_output(cmd).decode('utf-8')
    commits = output.split('\n')
    flohr_commits = [username in el for el in commits]
    return len(commits) - sum(flohr_commits) -1

def test_codequality():
    ncomments = 0
    nloc = 0
    files_grabbed = glob.glob("./*.py")
    for filename in files_grabbed:
        with open(filename) as fobj:
            source = fobj.read()
            report =  analyze(source)
            ncomments+=report.comments
            nloc+=report.loc
    assert nloc != 0
    print("#comments:",ncomments,"#loc:",nloc, "#comments/#loc:", ncomments / nloc)
    assert ncomments / nloc >= 0.25


def test_commit_messages():
    count = get_commit_count_exclude_user("./", "Fabian Flohr")
    assert int(count)>=5




if __name__ == "__main__":
    test_codequality()
    test_commit_messages()