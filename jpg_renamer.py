# JPG Renamer

import time
import os
import sys

print()
print('This program renames all the jpg files in a folder')
print()
folder = input('Please provide the folder name that you want to use: ')

if os.path.isdir(folder):
    print('Looking at directory...')
else:
    print('That was not a valid directory')
    sys.exit()


list_of_files = os.listdir(folder)
# print(list_of_files)
list_of_jpgs = []
for file in list_of_files:
    if file[-4:] == '.jpg':
        list_of_jpgs.append(file)

print('There are ' + str(len(list_of_jpgs)) + ' .jpg files in that folder')



print('Please provide the text string that you want to add to each file')
print()
text = input('Text string to add: ')
print('This program will now add \'' + text + '\' to each file')

start = time.time()

for file in list_of_jpgs:
    old_name = os.path.join(folder, file)
    long_file = file[:-4] + text + file[-4:]
    new_name = os.path.join(folder, long_file)
    os.rename(old_name, new_name)
print('All files have been renamed')

end = time.time()

# Create a unique string name for the time when the program finished
end_string = time.strftime("%Y-%m-%d %H_%M_%S", time.gmtime(end))

# Print the timestamps to the user

print('The program ran for', (end - start),' seconds.')

junk = input('Press Enter to exit the program ')

