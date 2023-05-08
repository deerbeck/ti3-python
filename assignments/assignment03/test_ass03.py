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
    for filename in glob.glob("./ass03*"):
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


@pytest.mark.order(11)
def testTask1():
    import ass03 as p03
    print("Test zu Aufgabe 1")
    table_no2 = p03.read_data('München/Lothstraße', 'NO2')
    assert type(table_no2) == dict
    keys_no2 = list(table_no2.keys())
    assert len(keys_no2) == 3
    assert "date" in keys_no2
    assert "time" in keys_no2
    assert 'NO2' in keys_no2
    assert type(table_no2["date"]) == list
    assert type(table_no2["time"]) == list
    assert type(table_no2['NO2']) == list
    assert len(table_no2["date"]) == 35064
    assert len(table_no2["time"]) == 35064
    assert len(table_no2['NO2']) == 35064
    assert table_no2["date"].count("02.11.2021") == 24
    assert table_no2["date"].count("03.11.2021") == 24
    assert table_no2["date"].count("04.11.2021") == 24
    assert table_no2["date"].count("05.11.2021") == 24
    assert table_no2["time"][0] == '01:00'
    assert table_no2["time"][-1] == '00:00'
    assert table_no2["time"][26] == '03:00'
    assert table_no2['NO2'][0] == 48.0
    assert table_no2['NO2'][-1] == 12.0
    assert table_no2['NO2'][26] == 6.0
    
    table_fs = p03.read_data('München/Lothstraße', 'PM10')
    assert type(table_fs) == dict
    keys_fs = list(table_fs.keys())
    assert len(keys_fs) == 3
    assert "date" in keys_fs
    assert "time" in keys_fs
    assert 'PM10' in keys_fs
    assert type(table_fs["date"]) == list
    assert type(table_fs["time"]) == list
    assert type(table_fs['PM10']) == list
    assert len(table_fs["date"]) == 35064
    assert len(table_fs["time"]) == 35064
    assert len(table_fs['PM10']) == 35064
    assert table_fs["date"].count("02.11.2021") == 24
    assert table_fs["date"].count("03.11.2021") == 24
    assert table_fs["date"].count("04.11.2021") == 24
    assert table_fs["date"].count("05.11.2021") == 24
    assert table_fs["date"].count("06.11.2021") == 24
    assert table_fs["date"].count("07.11.2021") == 24
    assert table_fs["time"][0] == '01:00'
    assert table_fs["time"][-1] == '00:00'
    assert table_fs["time"][65] == '18:00'
    assert table_fs['PM10'][0] == 561.0
    assert table_fs['PM10'][-1] == 6.0
    assert table_fs['PM10'][65] == 3.0

@pytest.mark.order(12)
def testTask2():
    import ass03 as p03
    print("Test zu Aufgabe 2")
    table_no2 = p03.read_data('München/Lothstraße', 'NO2')
    (laenge, mini, maxi, mittel) = p03.stats(table_no2, 'NO2')
    assert laenge == 34986
    assert mini == 3.0
    assert maxi == 148.0
    assert pytest.approx(mittel) == 24.591636654661865

    table_fs = p03.read_data('München/Lothstraße', 'PM10')
    (laenge, mini, maxi, mittel) = p03.stats(table_fs, "PM10")
    assert laenge == 34932
    assert mini == 0.0
    assert maxi == 777.0
    assert pytest.approx(mittel) == 15.007299896942632

@pytest.mark.order(13)
def testTask3():
    import ass03 as p03
    print("Test zu Aufgabe 3")
    table = {"date": [], "time": [], "no2": [], "fs": []}
    p03.add_entry(table, "11.11.18", "10:15", "no2", "fs", 13, 14)
    p03.add_entry(table, "11.11.18", "10:16", "no2", "fs", 15, 16)
    p03.add_entry(table, "11.11.18", "10:17", "no2", "fs", 17, 18)
    assert table["date"] == ["11.11.18"]*3
    assert table["time"] == ["10:15", "10:16", "10:17"]
    assert table["no2"] == [13, 15, 17]
    assert table["fs"] == [14, 16, 18]

@pytest.mark.order(14)
def testTask4():
    import ass03 as p03
    print("Test zu Aufgabe 4")
    table_no2 = p03.read_data('München/Lothstraße', 'NO2')
    table_fs = p03.read_data('München/Lothstraße', 'PM10')
    assert p03.check_time(table_no2, table_fs, 0, 1000) == -1
    assert p03.check_time(table_no2, table_fs, 1000, 1) == 1
    assert p03.check_time(table_no2, table_fs, 0, 0) == 0
    assert p03.check_time(table_no2, table_fs, 42, 128) == -1
    assert p03.check_time(table_no2, table_fs, 47, 126) == -1

@pytest.mark.order(15)
def testTask5():
    import ass03 as p03
    print("Test zu Aufgabe 5")
    table_no2 = p03.read_data('München/Lothstraße', 'NO2')
    table_fs = p03.read_data('München/Lothstraße', 'PM10')
    table_new = p03.merge(table_no2, table_fs)
    assert type(table_new) == dict
    keys_new = list(table_new.keys())
    assert len(keys_new) == 4
    assert "date" in keys_new
    assert "time" in keys_new
    assert "NO2" in keys_new
    assert "PM10" in keys_new
    assert type(table_new["date"]) == list
    assert type(table_new["time"]) == list
    assert type(table_new["NO2"]) == list
    assert type(table_new["PM10"]) == list
    assert len(table_new["date"]) == 35064
    assert len(table_new["time"]) == 35064
    assert len(table_new["NO2"]) == 35064
    assert len(table_new["PM10"]) == 35064
    assert table_new["date"].count("03.11.2021") == 24
    assert table_new["date"].count("04.11.2021") == 24
    assert table_new["date"].count("05.11.2021") == 24
    assert table_new["date"].count("06.11.2021") == 24
    assert table_new["date"].count("07.11.2021") == 24
    assert table_new["date"].count("08.11.2021") == 24
    assert table_new["date"].count("09.11.2021") == 24
    assert table_new["time"][0] == '01:00'
    assert table_new["time"][-1] == '00:00'
    assert table_new["time"][67] == '20:00'
    assert table_new["NO2"].count(None) == 78
    assert table_new["NO2"][0] == 48.0
    assert table_new["NO2"][78] == 20.0
    assert table_new["NO2"][-6] == 30.0
    assert table_new["NO2"][-5] == 19.0
    assert table_new["NO2"][79] == 24.0
    assert table_new["NO2"][-1] == 12.0
    assert table_new["PM10"].count(None) == 132
    assert table_new["PM10"][0] == 561.0
    assert table_new["PM10"][-1] == 6.0
    assert table_new["PM10"][-2] == 5.0
    assert table_new["PM10"][-3] == 5.0
    assert table_new["PM10"][-4] == 5.0
    assert table_new["PM10"][-5] == 6.0

@pytest.mark.order(16)
def testTask6():
    import ass03 as p03
    print("Test zu Aufgabe 6")
    table_no2 = p03.read_data('München/Lothstraße', 'NO2')
    table_fs = p03.read_data('München/Lothstraße', 'PM10')
    table_new = p03.merge(table_no2, table_fs)
    (laenge, mini, maxi, mittel) = p03.stats(table_new, 'NO2')
    assert laenge == 34986
    assert mini == 3.0
    assert maxi == 148.0
    assert pytest.approx(mittel) == 24.591636654661865
    (laenge, mini, maxi, mittel) = p03.stats(table_new, 'PM10')
    assert laenge == 34932
    assert mini == 0.0
    assert maxi == 777.0
    assert pytest.approx(mittel) == 15.007299896942632


if __name__ == "__main__":
    test_codequality()
    test_commit_messages()
    testTask1()
    testTask2()
    testTask3()
    testTask4()
    testTask5()
    testTask6()

