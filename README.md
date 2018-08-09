# OMX_Scripts

Helper scripts for Deltavision OMX

## Generate_Matrix.py
Generates a matrix of N by N new points around a given point.

### Necessary parameters: 

Matrix size: set as variable "matrix_size"
Pixelsize : set as variable "pixelsize"
Field of view: set as variable "FOV"
Spacing  overlap: set as variable "spacing" in µm, negative values will give overlap

Input: a saved pointlist as text file, defined in the variable "input_file". e.g. input_file = "D:/Code/OMX_Scripts/coordinates01.txt""
Output: a new pointlist as text file, defined in the variable "output file", e.g. output_file = "D:/Code/OMX_Scripts/new_coordinates.txt"

Usage: Define points using the OMX software, save the current point list as text file, run the scirpt on the file and load the output file as pointlist into the OMX software.

The output matrix will (hopefully) result in the following format:

1 2 3
4 5 6
7 8 9


Note: Z positions are not interpolated right now but derived from the current z position, we normally do a software autofocus step or run it without
Note2: There is a bug in the autofocus routine of the OMX software - it seems as if it does not perform filter wheel movements between acquiring and software autofocus (occurs only if the autofocus channel is on a light path with a filter wheel) - this is independent of the script function (occurs for all multipoint autofocus events - we need to document this and send a bug report to GE)
