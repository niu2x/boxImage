import sys
import os
import argparse
from PIL import Image
def box(filename, size, gray):
	try:
		img = Image.open(filename)
	except IOError, e:
		print "can't open file"
		return
	filename, ext = os.path.splitext(filename)
	outfilename = filename + '-box-' + str(size) + ext
	for i in range(img.size[0]):
		for j in range(img.size[1]):
			if i % size == 0 or j % size == 0:
				img.putpixel((i, j), (0, 0, 0))
	print gray
	if gray == 'true':
		img = img.convert(mode='L')
	img.save(outfilename)
if __name__ == "__main__":
	parse = argparse.ArgumentParser(prog="BoxImage", description="None")
	parse.add_argument("filename", help="None")
	parse.add_argument("size", help="", type=int)
	parse.add_argument("gray", help="", type=str)
	args = parse.parse_args()
	box(args.filename, args.size, args.gray)
