### DAP Renamer script
This is a simple script to rename cover images in the current folder and all subfolders to be the same as the directory name. This is needed for Sony NW-A105 Digital Audio Player to "see" those files (for whatever reason it dislikes "cover.jpg").

Additionally, script changes "Artist" ID3 tag to be either the same as "Album Artist" or, if "Album Artist" is "Various Artists", the same as "Composer" tag. This is done to have easier time searching for particular artist's music on the player. Can be skipped with '-s' or '--skip' command.

'-c' or '--cover' switches to "cover" mode, renaming the images to cover.jpg, in case you need it for another player.

### TODO
- PNG conversion to JPG
- Proper logic for "Artist" tag change, current one is too naïve