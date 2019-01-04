import os
import xml.dom.minidom
import xml.sax
path = '//10.75.10.81/Share/Dynamo2/CTS/V0.500/CTS/results'
dirs = os.listdir(path)
#for dir in dirs:
print(dirs[0])
subPath = path +'/'+ dirs[0]
dom = xml.dom.minidom.parse(subPath + '/test_result.xml')
#subDirs = os.listdir(subPath)
#for subDir in subDirs:
#    print(subDir)
root = dom.documentElement
summary = root.getElementsByTagName('Summary')

print('nodeName='+ summary[0].nodeName )
passCount = summary[0].getAttribute('pass')
print(passCount)
