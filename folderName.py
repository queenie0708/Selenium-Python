import os
import xml.dom.minidom
import xml.sax
path = r'D:\test\BTS\KaiOS\advanced_stability'
dirs = os.listdir(path)
for dir in dirs:
    print(dir)
#subPath = path +'/'+ dirs[0]
#dom = xml.dom.minidom.parse(subPath + '/test_result.xml')
#subDirs = os.listdir(subPath)
#for subDir in subDirs:
#    print(subDir)
#root = dom.documentElement
#summary = root.getElementsByTagName('Summary')

#print('nodeName='+ summary[0].nodeName )
#passCount = summary[0].getAttribute('pass')
#print(passCount)
