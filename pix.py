from PIL import Image

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
filem = open('rr.txt', 'w')


# def gp(image):
#     # Get size
#     width, height = image.size
#
#     # Create new Image and a Pixel Map
#     new = create_image(width, height)
#     pixels = new.load()
#     # Transform to grayscale
#     for i in range(width):
#         for j in range(height):
#             # Get Pixel
#             pixel = get_pixel(image, i, j)
#
#             # Get R, G, B values (This are int from 0 to 255)
#             red = pixel[0]
#             green = pixel[1]
#             blue = pixel[2]
#
#             filem.write(str(i) + ' ' + str(j) + '\n')
#
#             # # Transform to grayscale
#             gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
#
#             # Set Pixel in new image
#             pixels[i, j] = (int(gray), int(gray), int(gray))
#
#         # Return new image
#         return new
rgbArr = [(255,0,0),(0,255,0), (0,0,255), (255,255,255), (255,0,255)]
clrset=set()



img = open_image('000286.png')
w, h = img.size
count = 0
for i in range(w):
    for j in range(h):
        mpixel = get_pixel(img, i , j)
        red = mpixel[0]
        green = mpixel[1]
        blue = mpixel[2]
        filem.write(str(red) + ' ' + str(green)+ ' ' + str(blue)+"\n")
        mcolor = (red,green,blue)
        if mcolor not in rgbArr:
            # print(mcolor)
            clrset.add(mcolor)
            count +=1

print(count)
print(clrset)

filem.close()
