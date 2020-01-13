from PIL import Image
import os

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image
def get_pixel(image, i, j):
    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
      return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel


# Create a Grayscale version of the image


rgbArr = [(255,0,0),(0,255,0), (0,0,255), (255,255,255), (255,0,255)]
clrset=set()
src = "C:\\Users\\ymgoz\\Desktop\\assigned-to-yunus2\\masksc\\"
dst = "C:\\Users\\ymgoz\\Desktop\\assigned-to-yunus2\\corrected\\"

for filename in os.listdir(src):
    img = open_image(src+filename)
    w, h = img.size
    count = 0
    newImg = create_image(w, h)
    newpix = newImg.load()

    for i in range(w):
        for j in range(h):
            mpixel = get_pixel(img, i, j)
            red = mpixel[0]
            green = mpixel[1]
            blue = mpixel[2]
            mcolor = (red, green, blue)
            if mcolor not in rgbArr:
                # print(mcolor)
                clrset.add(mcolor)
                count += 1
                # r = 0
                # g= 0
                # b = 0
                # mcolor = (r,g,b)
                if mcolor[0] > 125 and mcolor[1] < 125 and mcolor[2] < 125:
                    r = 255
                    g = 0
                    b = 0
                    mcolor = (r, g, b)
                elif mcolor[0] < 125 and mcolor[1] > 125 and mcolor[2] < 125:
                    r = 0
                    g = 255
                    b = 0
                    mcolor = (r, g, b)
                elif mcolor[0] < 125 and mcolor[1] < 125 and mcolor[2] > 125:
                    r = 0
                    g = 0
                    b = 255
                    mcolor = (r, g, b)
                elif mcolor[0] > 125 and mcolor[1] < 125 and mcolor[2] > 125:
                    r = 255
                    g = 0
                    b = 255
                    mcolor = (r, g, b)
                elif mcolor[0] > 200 and mcolor[1] > 200 and mcolor[2] > 200:
                    r = 255
                    g = 255
                    b = 255
                    mcolor = (r, g, b)
                else:
                    r = 255
                    g = 255
                    b = 255
                    mcolor = (r, g, b)

            newpix[i, j] = (int(mcolor[0]), int(mcolor[1]), int(mcolor[2]))

    save_image(newImg, dst+filename)


# print(count)
# print(clrset)

