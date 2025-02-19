favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}   

recommended = ['victoria', 'sarah', 'phil', 'bobbert']

for name in recommended:
    if name in favorite_languages.keys():
        print(f"{name.title()} thank you for taking the poll!")
    else:
        print(f"{name.title()} you should come take the poll!")
