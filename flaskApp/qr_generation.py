import qrcode
import numpy as np
from PIL import  Image

def gen_qr_code( string_for_qr):
	"""This will generate a QR Code given a specific input string and return an image object
	Currently I will return a png64 string """
	return None




w, h = 600, 800
sq = 15


def use_ogrid(color1, color2):
    coords = np.ogrid[0:w, 0:h]
    idx = (coords[0] // sq + coords[1] // sq) % 2
    vals = np.array([color1, color2], dtype=np.uint8)
    img = vals[idx]
    return img

def use_fromfunction( color1, color2 ):
	img = np.zeros((w, h, 3), dtype=np.uint8)
	c = np.fromfunction(lambda x, y: ((x // sq) + (y // sq)) % 2, (w, h))
		
	img[c == 0] = color1
	img[c == 1] = color2
	return img

def make_checkerboard(color1, color2):
	### CREATE ALIASES FOR ALL THE COLORS AND CONVERT THEM TO HEX
	colorMap = { "red": (0xFF, 0x00, 0x00), "green": (0x00,0xFF,0x00),
				 "blue": (0x00,0x00,0xFF)}
	print ("Received",color1,color2)

	color1 = colorMap[color1]
	color2 = colorMap[color2]


	for f in (use_ogrid, use_fromfunction):
		img = f(color1,color2)
		pilImage = Image.fromarray(img, 'RGB')
		return pilImage