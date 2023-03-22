from junitparser import JUnitXml
import glob

xml = JUnitXml()
print("merging files")
for junit in glob.glob("./junit_*.xml"):
    print(junit)
    xml += JUnitXml.fromfile(junit)

xml.write("./junit_assignment_report_merged.xml")