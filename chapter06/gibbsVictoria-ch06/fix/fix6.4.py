#fix6.4.py
# What's wrong with this code? The dictionary lists the peaks by order
# of the mountain's height, and now there is a change order from your
# client to list the mountains alphabetically. What can you do to fix the code?

smoky_mountains_peaks = {
    'Clingmans Dome': 6643, 
    'Mount Guyot': 6621,
    'Mount Le Conte': 6593,
    'Mount Buckley': 6560,
    'Old Black': 6370,
    'Luftee Knob': 6234,
    'Mount Kephart': 6217
}

for name in sorted(smoky_mountains_peaks.items()):
    print (name)