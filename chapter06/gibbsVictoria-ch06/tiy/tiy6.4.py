glossary = {
    'variable': 'a named storage locations that hold values or data.',
    'list': 'a mutable, ordered sequence of elements.',
    'tuple': 'a collection which is ordered and unchangeable.',
    'method': 'a block of code which only runs when it is called.',
    'dictionary': 'used to store data values in key:value pairs.',
}

for key, value in glossary.items():
    print(f"A {key} is {value}.")
print("")
print("Adding 5 more terms")
print("")

glossary['comment'] = 'a line or lines in a program that the program ignores.'
glossary['spec'] = 'a list of requirements for a what a program needs to do.'
glossary['standard library'] = 'the set of tools included in a language\'s standard installation.'
glossary['bug'] = 'a problem in the way a program runs.'
glossary['test'] = 'code outside your program that runs some of your program code to check whether it works correctly.'

print("Printing all 10 terms in the loop")
print("")
for key, value in glossary.items():
    print(f"A {key} is {value}.")
