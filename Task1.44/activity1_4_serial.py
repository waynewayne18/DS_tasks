'''
To install face_recognition, simply use 'pip install face_recognition' in a terminal
However, often you may meet an error about the 'dlib' library with cmake.
The easy solution is to visit https://github.com/z-mahmud22/Dlib_Windows_Python3.x and download the 
compiled wheels locally with the python version, and install it from local

if you want to show the found image with the known face, you need opencv and also uncomment the related code.

'''
from concurrent.futures import ThreadPoolExecutor
import cv2
import time
import face_recognition
import os
import sys 
import cv2
def show_found_image(unknown_image):
    face_locations = face_recognition.face_locations(unknown_image)

    # Draw rectangles around faces
    for top, right, bottom, left in face_locations:
        cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Found Image", cv2.cvtColor(unknown_image, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

start = time.time()
# Load the known face image and get the features of the face
known_image = face_recognition.load_image_file("known_man.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

folder_path = "imageset/"

# filenames = [file.name for file in os.scandir(folder_path) if file.is_file()]  
#OLD


filepaths = [file.path for file in os.scandir(folder_path) if file.is_file()]
count = 0
found = False
with ThreadPoolExecutor(max_workers=8) as executor: #saving hundreds of milliseconds by creating TPE once 
    for i in range(0, len(filepaths), 32):
        if len(filepaths) - (i + 32) > 32:
            batch = filepaths[i:i + 32] #batch limits memory usage
        else:
            batch = filepaths[i: (len(filepaths))]
        unknown_batch = list(executor.map(cv2.imread, batch)) 
        for unknown in unknown_batch:
            print(filepaths[count])
            unknown_encodings = face_recognition.face_encodings(unknown)  #changed to cv2 for GIL release as its written in
            for unknown_encoding in unknown_encodings:
                matches = face_recognition.compare_faces([known_encoding], unknown_encoding)
                if matches[0]:  
                    print("Match found! in " + filepaths[count])
                    found = True #found flag saves lots of time since task specification says the program only wants to find 1 image 63.5s
                    #show_found_image(unknown_image)
                    break
            if found:
                break
            count += 1
        if found:
            break
    

print(time.time()-start)
#140s completely unoptimized (no found flag)
#59 - 83s unoptimized 3 tests 
#54 - 62 with loading thread pool  4 workers 3 tests
#57-62s  with 16 workers, 3 tests 
#51-57s with 8 workers, 3 tests


