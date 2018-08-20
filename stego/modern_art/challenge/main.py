from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import binascii

st = "flag{pyr4mid_0f_4scii}"
binary = ''.join(format(ord(x), 'b').zfill(8) for x in st)

source_img = Image.new('RGB', (len(binary) * 2,len(binary) * 2))

draw = ImageDraw.Draw(source_img)

for i, bit in enumerate(binary):
    print i
    if bit=="1":
        print "1"
        draw.rectangle(((i, i), (len(binary) * 2 - i, len(binary) * 2 - i)), fill="white")
    else:
        print "0"
        draw.rectangle(((i, i), (len(binary) * 2 - i, len(binary) * 2 - i)), fill="black")

source_img.save('art.png')