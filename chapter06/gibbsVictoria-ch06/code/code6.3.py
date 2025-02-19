# code6.3.py
# Use the following list of dictionaries to solve the following exercises.
#
# Here are the dictionaries for the Canadian provinces
provinces = []

province_00 = {'province_name': 'Alberta', 'capital': 'Edmonton', 'population': 4_400_000}
province_01 = {'province_name': 'British Columbia', 'capital': 'Victoria', 'population': 5_100_000}
province_02 = {'province_name': 'Manitoba', 'capital': 'Winnipeg', 'population': 1_400_000}
province_03 = {'province_name': 'New Brunswick', 'capital': 'Fredericton', 'population': 780_000}
province_04 = {'province_name': 'Newfoundland and Labrador', 'capital': "St. John's", 'population': 520_000}
province_05 = {'province_name': 'Nova Scotia', 'capital': 'Halifax', 'population': 970_000}
province_06 = {'province_name': 'Ontario', 'capital': 'Toronto', 'population': 14_700_000}
province_07 = {'province_name': 'Prince Edward Island', 'capital': 'Charlottetown', 'population': 160_000}
province_08 = {'province_name': 'Quebec', 'capital': 'Quebec City', 'population': 8_400_000}
province_09 = {'province_name': 'Saskatchewan', 'capital': 'Regina', 'population': 1_200_000}
province_10 = {'province_name': 'Northwest Territories', 'capital': 'Yellowknife', 'population': 45_000}
province_11 = {'province_name': 'Nunavut', 'capital': 'Iqaluit', 'population': 40_000}
province_12 = {'province_name': 'Yukon', 'capital': 'Whitehorse', 'population': 42_000}

# This is a list of the dictionaries

provinces = [ 
    province_00,
    province_01,
    province_02,
    province_03,
    province_04,
    province_05,
    province_06,
    province_07,
    province_08,
    province_09,
    province_10,
    province_11,
    province_12,
]

# Print the information for Alberta
# Your output should look like
# {'province_name': 'Alberta', 'capital': 'Edmonton', 'population': 4400000}
#
# your code here
for place in provinces:
    for key, value in place.items():
        if value == 'Alberta':
            print(place)

# Print the information for Alberta line by line. 
# Your output should look like
#
# Province: Alberta
# Capital: Edmonton
# Population: 4400000
#
# your code here
print("")
for place in provinces:
    for key, value in place.items():
        if value == 'Alberta':
            print(f"Province: {place['province_name']}\nCapital: {place['capital']}\nPopulation: {place['population']}")

# Display all of the province information from the first 4 provinces
# Your output should look like
#
# {'province_name': 'Alberta', 'capital': 'Edmonton', 'population': 4400000}
# {'province_name': 'British Columbia', 'capital': 'Victoria', 'population': 5100000}
# {'province_name': 'Manitoba', 'capital': 'Winnipeg', 'population': 1400000}
# {'province_name': 'New Brunswick', 'capital': 'Fredericton', 'population': 780000}
#
# your code here
for place in provinces[:4]:
    print(place)

        