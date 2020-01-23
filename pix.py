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
def nearest_colour(subjects, query):
    return min(subjects, key=lambda subject: sum((s - q) ** 2 for s, q in zip(subject, query)))


colours = ((255, 255, 255, "white"),
           (255, 0, 0, "red"),
           (0, 0, 255, "blue"),
           (0, 255, 0, "green"),
           (255, 0, 255, "fuchsia"))

rgbArr = [(255, 0, 0),
          (0, 255, 0),
          (0, 0, 255),
          (255, 255, 255),
          (255, 0, 255)]
clrset = set()
src = "SOURCE PATH FOR IMAGES"
dst = "DESTINATION PATH TO SAVE PIXEL CORRECTED IMAGES"
allcount = 0
for filename in os.listdir(src):
    img = open_image(src + filename)
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
                allcount += 1
                corrected_color = nearest_colour(colours, mcolor)
                mcolor = (corrected_color[0], corrected_color[1], corrected_color[2])

            newpix[i, j] = (int(mcolor[0]), int(mcolor[1]), int(mcolor[2]))

    save_image(newImg, dst + filename)

# print(allcount) #TO COUNT ALL CORRECTED PIXELS
# print(clrset) #A SET FOR DIFFERENT COLORS FROM OUR COLOR MAP
