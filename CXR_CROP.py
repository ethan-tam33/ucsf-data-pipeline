# lungs_finder package documentation: https://github.com/dirtmaxim/lungs-finder

import lungs_finder as lf # ML algorithm automatically finding and cropping everything but the lungs in an image
import glob # finds all image file paths on computer
import cv2 # loads in and saves images
import os # changes initial set directory to another directory
import numpy as np #check if numpy array is empty

# set list to contain names of images that fail to run through the get_lungs package
bugged_CXR = []
# set a variable to the folder containing the uncropped images
uncropped_directory = "/Users/ethantam/Desktop/UCSF/CXRs/*"
# set a variable to the folder where we want the cropped images to be stored
directory = "/Users/ethantam/Desktop/UCSF/Other Cropped"
# iterate through all paths in our folder containing the uncropped images
for name in glob.glob(uncropped_directory):
    # print the path so that if the code errors, we know which path caused it
    print(name)
    # load in the image
    image = cv2.imread(name)
    # use the lungs_finder package to create a new image that contains just the lungs
    found_lungs = lf.get_lungs(image)
    # print(os.getcwd()) to check directory
    # set a variable to what we want the name of the cropped image to be
    filename = name[43:54] + " CROPPED.jpg"
    # check if found_lungs array is empty and if the shape of the image is irregular
    # only save file if array is not empty and if the image shape is normal (in this case, above 100 units of width)
    if np.any(found_lungs) and found_lungs.shape[1] > 100:
        # save the cropped image to the folder
        cv2.imwrite(os.path.join(directory, filename), found_lungs)
    else:
        # append name of bugged image to list
        bugged_CXR.append(name[43:54])

print("Bugged CXRs:", bugged_CXR)