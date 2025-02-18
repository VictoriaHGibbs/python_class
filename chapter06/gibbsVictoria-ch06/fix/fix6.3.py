# fix6.3.py
#
# What is wrong with this code? It should display both the name of the peak
# and its height but it generates an error instead. What can you 
# change so the program displays both the name and the height?


smoky_mountains_peaks = {
    'Clingmans Dome': 6643, 
    'Mount Guyot': 6621,
    'Mount Le Conte': 6593,
    'Mount Buckley': 6560,
    'Old Black': 6370,
    'Luftee Knob': 6234,
    'Mount Kephart': 6217
}

for peak, height in smoky_mountains_peaks:
    print (f"{peak}:{height}")
