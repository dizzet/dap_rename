import os, re

regx = re.compile('\.jpg$|\.jpeg$')

for dn, sdl, fl in os.walk('.'):
    imgs = list(filter(regx.search, fl))
    if len(imgs) > 1:
        for img in imgs:
            print(os.path.join(dn,img))
    elif len(imgs) == 0:
        continue
    else:
        ext = imgs[0][imgs[0].rfind('.'):]
        if imgs[0] == dn[dn.rfind('\\')+1:]+ext:
            continue
        imgf = os.path.join(dn,imgs[0])
        dst_imgf = os.path.join(dn, dn[dn.rfind('\\')+1:]+ext)
        os.rename(imgf, dst_imgf)