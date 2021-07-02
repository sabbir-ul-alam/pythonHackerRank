import sys
import xml.etree.ElementTree as etree




def get_attr_number(node):
    # your code goes here
    count=0
    for x in node.iter():
        count=count+len(x.attrib)


    return count

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
