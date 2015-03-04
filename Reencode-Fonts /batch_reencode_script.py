import os
import shutil

def reencodeFont(path, file):
    print '\n'
    print os.path.join(path, file)
    fontFolder = os.path.basename(os.path.normpath(path))
    files = file.split('.', 1)
    fileName = files[0]
    ttxFile = fileName + '.ttx'
    toTTXCMD = './ttx -q ' + path + '/'+ file
    os.system(toTTXCMD)
    print toTTXCMD
    dstPath = path + '/../../dstFonts/' + fontFolder + '/'
    if not os.path.isdir(dstPath):
        os.makedirs(dstPath)
    backFromTTXCMD = './ttx -q -d ' + dstPath + ' ' + path + '/' + ttxFile
    print backFromTTXCMD
    os.system(backFromTTXCMD)
    os.remove(path + '/'+ ttxFile)

def batchReencodeFonts():
    print('\n************************************************************')
    print('  Reencode all font files to fix invalid idRangeOffset value ')
    print('************************************************************')
    srcPath = './srcFonts'
    dstPath = './dstFonts'
    print('clear dst folder ' + dstPath)
    if os.path.isdir(dstPath):
        shutil.rmtree(dstPath)
    for root, subdirs, files in os.walk(srcPath):
        for name in files:
            if '.ttf' in name or '.otf' in name:
                reencodeFont(root, name)
            if '.ttx' in name:
                os.remove(os.path.join(root, name))
                continue

batchReencodeFonts()
