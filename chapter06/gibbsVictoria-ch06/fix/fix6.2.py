# fix6.2.py
#
# What is wrong with this code? It is designed to use a Python dictionary
# instead it uses a list, and generates an error. 
# What can you do to fix the program so it displays all of the peaks?
# The output does not need to display the height.


smoky_mountains_peaks = {
    'Clingmans Dome': 6643, 
    'Mount Guyot': 6621,
    'Mount Le Conte': 6593,
    'Mount Buckley': 6560,
    'Old Black': 6370,
    'Luftee Knob': 6234,
    'Mount Kephart': 6217
}

for smoky_mountins_peak in smoky_mountains_peaks:
    print (smoky_mountins_peak)
