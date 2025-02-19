# code6.1.py
#
# Using the smoky_mountains_peaks dictionary, add the necessary code to display
#
# The height of Clingman's Dome is 6643 feet.
# The height of Mount Le Conte is 6593 feet.
#
# The peaks are listed in feet

smoky_mountains_peaks = {
    'Clingmans Dome': 6643, 
    'Mount Guyot': 6621,
    'Mount Le Conte': 6593,
    'Mount Buckley': 6560,
    'Old Black': 6370,
    'Luftee Knob': 6234,
    'Mount Kephart': 6217
}

# Add print statements here
peaks = ['Clingmans Dome', 'Mount Le Conte']

for mountain in smoky_mountains_peaks.keys():
    if mountain in peaks:
        print(f"The height of {mountain.title()} is \
{smoky_mountains_peaks[mountain]} feet.")
