#TODO: ID3 - https://mutagen.readthedocs.io/en/latest/index.html
#      image conversion - https://python-pillow.org/ or OpenCV ck2

import os, re

regx = re.compile('\.jpg$|\.jpeg$')
png_regx = re.compile('\.png$')

for dn, sdl, fl in os.walk('.'):
    imgs = list(filter(regx.search, fl))
    if len(imgs) > 1:
        for img in imgs:
            print('Directory has more than 1 image: ' + dn)
    elif len(imgs) == 0:
        pngs = list(filter(png_regx.search, fl))
        if len(pngs) > 0:
            print('Directory has only png images: ' + dn)
        continue
    else:
        ext = imgs[0][imgs[0].rfind('.'):]
        if imgs[0] == dn[dn.rfind('\\')+1:]+ext:
            continue
        imgf = os.path.join(dn,imgs[0])
        dst_imgf = os.path.join(dn, dn[dn.rfind('\\')+1:]+ext)
        os.rename(imgf, dst_imgf)