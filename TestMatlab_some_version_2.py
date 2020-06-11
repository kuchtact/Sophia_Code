import scipy.io
import os
import numpy as np
from pylab import plot, xlabel, ylabel, show, title, imshow, colorbar, savefig, close, pcolor, gca, axis

# Change the file directory variable depending on where the data is currently stored.
folder_dir = '/media/sophianowak/My Passport/AsymmetricScan400/'
fileList = ['uix', 'uiy', 'uiz', 'bx', 'by', 'bz', 'ex', 'ey', 'ez', 'jx', 'jy', 'jz', 'ne', 'ni']
folderList = ['d10-gf0']  # , 'd10.5-gf0', 'd11-gf0', 'd12-gf0', 'd74-gf4'
folders_in_dir = []
time = 62

for folder in folderList:
    # intitalize a 3-D array, to the size of the data stored in each file
    # x, y, number of var
    data = np.zeros((1680, 3360, 13))
    counter = 0

    # Get the correct address to the folder.
    dir = folder_dir + folder
    print(dir)

    # Loop for finding the files.
    # for time in range(0,102,1):
    for item in fileList:
        current_dir = dir + '/' + item + '_' + str(time) + '.mat'
        # print(current_dir)
        # print(time)
        # Check if the file exists, if it does append the data at that file to the data list.
        for counter in range(0,14):
            if os.path.isfile(current_dir):
                rawData = scipy.io.loadmat(current_dir)
                # print(type(rawData[item]))
                for j in range(3360):
                    for i in range(1680):
                        #data[i][j][counter].append(rawData[item][i][j])
                        print(rawData[i][j][counter])







