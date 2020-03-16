from PIL import Image
import glob

mode_to_bpp = {"1": 1, "L": 8, "P": 8, "RGB": 24, "RGBA": 32, "CMYK": 32, "YCbCr": 24, "LAB": 24, "HSV": 24, "I": 32, "F": 32}
image_list = map(Image.open, glob.glob('tests/*'))
for image in image_list:
    print("filename = " + image.filename)
    width, height = image.size
    print("width = " + str(width) + ", height = " + str(height))
    print("dpi =", image.info.get("dpi") if image.info.get("dpi", "") != 0 else "not provided")
    print("depth =", mode_to_bpp[image.mode])
    print("compression =", image.info.get('compression') if image.info.get("compression") != 0 else "not provided")
    print("******************")
    print()
