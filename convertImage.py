from PIL import Image
import numpy
import os

size = (128,128)
#https://stackoverflow.com/questions/18777873/convert-rgb-to-black-or-white/18778280

for file_name in os.listdir("new-images/Ursa_Major/"):
    colorImage = Image.open("new-images/Ursa_Major/" + file_name)
    grayImage = colorImage.convert('L')
    blackWhiteImage = grayImage.point(lambda x: 0 if x<128 else 255, '1')
    blackWhiteImage = blackWhiteImage.resize(size, 0)
    blackWhiteImage.save("new-images/Ursa_Major/" + file_name[0:-4] + "-resized.jpg")


arr = numpy.ndarray.tolist(numpy.array(blackWhiteImage.getdata(),numpy.uint8).reshape(blackWhiteImage.size[1], blackWhiteImage.size[0]))