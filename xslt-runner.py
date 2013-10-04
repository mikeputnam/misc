import sys
from lxml import etree
from StringIO import StringIO

if sys.argv[1] == '':
    print "Usage: python xslt-runner.py <xsl file> <xml file>"
    sys.exit()
pathtoxsl = sys.argv[1]
pathtoxml = sys.argv[2]

xslt_input = etree.XML(open(pathtoxsl,'rb').read())
xslt_transform = etree.XSLT(xslt_input)

xml_input = etree.parse(StringIO(open(pathtoxml,'rb').read()))

result_tree = xslt_transform(xml_input)

print result_tree

