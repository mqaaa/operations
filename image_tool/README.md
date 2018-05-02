# 使用Python归档图片
## Exif的使用
The exiftool script is a command line application.  You run it by typing
commands in a terminal window.  The first step is to determine the name of
the directory where you downloaded the ExifTool distribution package.
Assuming, for example, you downloaded it to a folder called "Desktop" in
your home directory, then you would type the following commands in a
terminal window to extract and run ExifTool:
```
  cd ~/Desktop
  gzip -dc Image-ExifTool-10.94.tar.gz | tar -xf -
  cd Image-ExifTool-10.94
  ./exiftool t/images/ExifTool.jpg
```
Note:  These commands extract meta information from one of the test images. 
To use one of your images instead, enter the full path name of your file in
place of "t/images/ExifTool.jpg".

INSTALLATION

You can install the Image::ExifTool package to make it available for use by
other Perl scripts by typing the following:
```
  perl Makefile.PL
  make
  make test
  make install
```
DownLoad:
* https://sno.phy.queensu.ca/~phil/exiftool/Image-ExifTool-10.94.tar.gz
Website:
* https://sno.phy.queensu.ca/~phil/exiftool/

## 修改图片尺寸
```
#!/usr/bin/python
#_*_ coding: UTF-8 _*_
import glob
import os
from PIL import Image
size = 128,128
for infile in glob.glob("*.jpg"):
    file,ext = os.path.splitext(infile)
    im = Image.open(infile)
    im.thumbnail(size)
    im.save(file + ".thumbnail","JPEG")
``` 
