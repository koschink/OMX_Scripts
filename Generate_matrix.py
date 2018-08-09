"""
this script takes OMX pointlists and gennerates several additional points (a matrix of 3x3, 5x5... fields)
this allows to use the OMX (or deltavision) to acquire a matrix of points and serve as high throughput system
use either Fiji Jython or a standard python interpreter.

"""
from __future__ import division
from __future__ import print_function
import sys

#  These values should be adjusted for your experiment

input_file = "D:/Code/OMX_Scripts/coordinates01.txt" # path to saved pointlist file

output_file = "D:/Code/OMX_Scripts/coordinates_new.txt" # path to new pointlist, load this into the pointlist window in the OMX control software

matrix_size = 3 ## currently only works for odd numbers, i.e. 3,5,7,....will be 3x3, 5x5 etc
pixelsize = 0.08
 ## should be 0.08 for current OMX, adjust as needed
FOV=1024            # field of view in pixel, normally 1024 or 512
spacing = 10        # spacing between fields of view in µm, if no spacing is given, the field of view should be directly overlapping, negative numbers give overlap.


### Do not change anything below here

shift = (FOV*pixelsize)+spacing
print(shift)
def generate_matrix(coordinates, matsize):
    print(matsize)
    if matsize %2 ==0:
        mat_size=int((matsize/2))
    else:
        mat_size = int((matsize-1)/2)

    coordinate_list = []
    for i in range(-mat_size, mat_size+1):
        for j in range(-mat_size, mat_size+1):
            coordinate = [round(coordinates[0]+j*shift,1), round(coordinates[1]-i*shift,1), coordinates[2]]
            coordinate_list.append(coordinate)
    return coordinate_list



with open(input_file) as pointlist_file:
    lines = pointlist_file.read().split("\n")

coordinate_matrix = []

for i in lines:
    if len(i)>0:
        string1 = i
        splits = string1.split(': ')
        split2 = splits[1].split(", ")
        split2 = [float(i) for i in split2]
        matrix1 =  generate_matrix(split2,matrix_size)
        for j in matrix1:
            coordinate_matrix.append(j)
    
    #print(len(generate_matrix(split2,3)))

output_matrix = []
for k in range(0, len(coordinate_matrix)):
    print(k)
    output_string = str(k+1)+": "+ str(coordinate_matrix[k][0])+", "+str(coordinate_matrix[k][1])+", "+str(coordinate_matrix[k][2])
    output_matrix.append(output_string)

output_matrix.append("")
with open(output_file, "w") as output:
    output.write("\n".join(map(lambda x: str(x), output_matrix)))
