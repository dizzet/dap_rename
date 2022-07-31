#TODO: proper logic for Artist tag
#      image conversion - Pillow

import argparse
import mutagen
import os
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument('folder', help='Root directory where to look for music albums', type=str, default='.')
    parser.add_argument('-c', '--cover', help="Rename all images to cover.'ext' instead of 'dirname'.'ext'",
                        action='store_true')
    parser.add_argument('-s', '--skip', help='Skip "Artist" tag population with "Album Artist" value, i.e. leave it intact',
                        action='store_true', default=False)

    args = parser.parse_args()

    regx = re.compile('\.jpg$|\.jpeg$')
    music_regx = re.compile('\.mp3$|\.flac$|\.m4a$')

    for dn, sdl, fl in os.walk(args.folder):
        imgs = list(filter(regx.search, fl))
        if len(imgs) > 1:
            print(f'Directory has more than 1 image: {dn}')
        elif len(imgs) == 0:
            print(f'No images in directory: {dn}')
        else:
            ext = imgs[0][imgs[0].rfind('.'):]
            print(ext)
            if args.cover:
                if imgs[0] == f'cover{ext}':
                    continue
                imgf = os.path.join(dn,imgs[0])
                dst_imgf = os.path.join(dn, f'cover{ext}')
                os.rename(imgf, dst_imgf)
            else:
                if imgs[0] == dn[dn.rfind('\\')+1:]+ext:
                    continue
                imgf = os.path.join(dn,imgs[0])
                dst_imgf = os.path.join(dn, dn[dn.rfind('\\')+1:]+ext)
                os.rename(imgf, dst_imgf)
        
        if not args.skip:
            songs = list(filter(music_regx.search, fl))
            for song in songs:
                song_file = mutagen.File(os.path.join(dn,song))
                new_artist = song_file['composer'] if (str(song_file['albumartist'][0]).lower() == 'various artists' 
                             and str(song_file['composer']) != '') else song_file['albumartist']
                song_file['artist'] = new_artist
                song_file.save()

