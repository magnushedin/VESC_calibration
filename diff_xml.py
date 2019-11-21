# exec(open('diff_xml.py').read())

import xml.etree.ElementTree as ET
import sys

if len(sys.argv) == 3:

    file1_name = sys.argv[2]
    file2_name = sys.argv[1] # Inverse order for diff to be displayed in correct order

    tree1 = ET.parse(file1_name)
    tree2 = ET.parse(file2_name)
    root1 = tree1.getroot()
    root2 = tree2.getroot()

    root1_dict = {}
    for child in root1:
        root1_dict[child.tag] = child.text

    for child in root2:
        if len(child.text) < 2000 and child.text != root1_dict[child.tag]:
            print("{tag:30} {num:11} : {num2}".format(tag=child.tag, num=child.text, num2=root1_dict[child.tag]))

else:
    print('No files to parse')
