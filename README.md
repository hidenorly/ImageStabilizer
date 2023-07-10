# ImageStabilizer

```
usage: ImageStabilizer.py [-h] [-k KERNELSIZE] [-s SIGMA] imageFiles [imageFiles ...]

ImageStabilizer

positional arguments:
  imageFiles            Image files

options:
  -h, --help            show this help message and exit
  -k KERNELSIZE, --kernelSize KERNELSIZE
                        Specify kernel size
  -s SIGMA, --sigma SIGMA
                        Specify sigma
```

```
$ python3 imageStabilizer.py IMG_3546.jpg -k 500 -s 2 
$ python3 imageStabilizer.py IMG_3546.jpg -k 1000 -s 4
```