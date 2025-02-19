# code6.2.py
#
# Write code that iterates through the entire dictionary and only displays
# elevations that are greater than 6370
#
# Clingmans Dome: 6643
# Mount Guyot: 6621
# Mount Le Conte: 6593
# Mount Buckley: 6560
#


smoky_mountains_peaks = {
    'Clingmans Dome': 6643, 
    'Mount Guyot': 6621,
    'Mount Le Conte': 6593,
    'Mount Buckley': 6560,
    'Old Black': 6370,
    'Luftee Knob': 6234,
    'Mount Kephart': 6217
}


# Your code here
print("Peaks greater than 6370 feet in elevation:")
for name, height in smoky_mountains_peaks.items():
    if height > 6370:
        print(f"{name}: {height} feet")


