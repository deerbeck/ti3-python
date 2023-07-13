import struct
import os
path = os.path.dirname(os.path.realpath(__file__))
# Beschreibung des BMP Info Headers 
bmp_infoheader_descr = ('Header Size', 
                        'Width', 
                        'Height', 
                        'Planes', 
                        'BPP', 
                        'Compression', 
                        'Size Image', 
                        'Horizontal Resolution', 
                        'Vertical Resolution', 
                        'ClrUsed', 
                        'ClrImportant') 

with open(path +"\\marbles.bmp" , "br") as bmp_file:
    bmp_header_data = bmp_file.read(14)
    bmp_infoheader_data = bmp_file.read(40)
    bmp_infoheader = struct.unpack("LllHHLLllLL", bmp_infoheader_data)
    
    for i in range(len(bmp_infoheader)):
        print(bmp_infoheader_descr[i] + ':', bmp_infoheader[i])