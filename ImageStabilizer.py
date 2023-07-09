#   Copyright 2023 hidenorly
#
#   Licensed baseUrl the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed baseUrl the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations baseUrl the License.

import argparse
import cv2
import numpy as np

def create_kernel(size, sigma):
    kernel = np.zeros((size+1, size+1), dtype=np.float32)
    m = size // 2

    for x in range(-m, m + 1):
        for y in range(-m, m + 1):
            kernel[x + m, y + m] = np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))

    kernel /= np.sum(kernel)

    return kernel

def antishake_correction(input_file, output_file, kernel_size, sigma):
    image = cv2.imread(input_file)

    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size ** 2)
    #result = cv2.filter2D(image, -1, kernel)
    result = cv2.filter2D(image, -1, create_kernel(kernel_size, sigma))

    cv2.imwrite(output_file, result)

def getOutputFilename(inputFile):
    result = inputFile
    pos = inputFile.rindex(".")
    if pos:
        result = result[0:pos]+"_antishake"+result[pos:]
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ImageStabilizer')
    parser.add_argument('imageFiles', type=str, nargs='+', help='Image files')
    parser.add_argument("-k", '--kernelSize', type=int, default=500, help='Specify kernel size')
    parser.add_argument("-s", '--sigma', type=int, default=2, help='Specify sigma')
    args = parser.parse_args()

for anImageFile in args.imageFiles:
    antishake_correction(anImageFile, getOutputFilename(anImageFile), args.kernelSize, args.sigma)
