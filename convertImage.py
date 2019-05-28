from PIL import Image
import numpy

#https://stackoverflow.com/questions/18777873/convert-rgb-to-black-or-white/18778280

colorImage = Image.open("orion.jpg")
grayImage = colorImage.convert('L')
blackWhiteImage = grayImage.point(lambda x: 0 if x<128 else 255, '1')
blackWhiteImage.save("orion-bw.jpg")
size = 128,128
blackWhiteImage = blackWhiteImage.resize(size, 0)
blackWhiteImage.save("orion-bw-resized.jpg")

arr = numpy.ndarray.tolist(numpy.array(blackWhiteImage.getdata(),numpy.uint8).reshape(blackWhiteImage.size[1], blackWhiteImage.size[0]))