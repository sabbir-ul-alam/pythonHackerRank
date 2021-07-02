import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
    global maxdepth

    if len(elem)==0:
        return level +1
    for i in elem:
        #print(i.tag,"---",elem.tag)
        x=(depth(i,level+1))
        if x:
            if x >maxdepth:
                 maxdepth=x
         #   print(maxdepth)








if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

    """
6
< feed
xml: lang = 'en' >
< title > HackerRank < / title >
< subtitle
lang = 'en' > Programming
challenges < / subtitle >
< link
rel = 'alternate'
type = 'text/html'
href = 'http://hackerrank.com/' / >
< updated > 2013 - 12 - 25
T12: 00:00 < / updated >
< / feed >
    
    """