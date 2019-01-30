import os
rootDirectory = '.'
for directoryName, subdirectoryList, fileList in os.walk(rootDirectory):
    print('Found directory: %s' % directoryName)
    for filename in fileList:
        print('\t%s' % filename)

