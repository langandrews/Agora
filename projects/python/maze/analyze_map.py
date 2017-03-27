''' This file can analyze a map image (on windows) and convert it to a text file.
Specific rules for map making are included in the folder in a file titled "map_rules.txt"
Created Fall 2014
analyze_map.py
@author: Jonathan Manni (jdm42)
'''

from PIL import Image

while True: # run a while loop to ask for an image until a good file is reached
    try:
        img = Image.open(input('Enter map image file location and name: ')) # set the image variable
        break
    except Exception as err: # if an exception is thrown
        print("Couldn't open file, try again:", err) # tell the user

def getFill(pix): # see sources line 2
    '''This function will get the color of a pixel in hex instead of rgb.'''
    im = img.convert('RGB') # change img mode to RGB, in case it isn't
    color_inst = '#%02x%02x%02x' % im.getpixel(pix)  # convert color to hex - see sources line 2
    return color_inst  # send hex color

img_size_y = img.size[1] # set a variable to the width of the image
img_size_x = img.size[0] # set a variable to the height of the image
print('Image size is:', img_size_x, 'x', img_size_y) # print the image size
print('Image type is:', img.format) # print the image type

cols = [] # create an empty columns list
rows = [] # create an empty rows list

count_x = 0 # set a count x variable to 0
count_y = 0 # set a count y variable to 0 

pixel = (count_x, count_y) # create pixel tuple

while count_y < img_size_y: # while the amount of rows is less than the total rows
    while count_x < img_size_x: # while the amount of columns is less than the total columns
        cols.append(getFill(pixel)) # append the hex color of the pixel to the cols list
        count_x += 1 # add one to the column count
        pixel = (count_x, count_y) # update the pixel
    rows.append(cols) # append the columns list
    cols = [] # reset the columns list
    count_x = 0 # reset the columns counter
    count_y += 1 # add one to the row counter
    pixel = (count_x, count_y) # reset the pixel
    
# write the map data to file
file = open('hey_lava.txt', 'w') # open a file to write to 
for row in rows: # for each row in the rows list
    for item in row: # for each item in the row
        file.write(item) # write the item
        file.write(' ') # add a space
    file.write('\n') # write a new line
file.close() # close the file