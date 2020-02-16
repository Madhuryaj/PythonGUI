options = {
  "one":{
    "value":"something ",
    "selected":False
  },
  "two":{
    "value":"something ",
    "selected":False
  },
  "three":{
    "value":"something ",
    "selected":False
  },
  "four":{
    "value":"something ",
    "selected":False
  }
}

def getUnselectedOptions():
  unselectedOptions = []
  for o in options:
    if options[o]["selected"] == False:
      unselectedOptions.append(o)
  return unselectedOptions


def selectOption(optionKey):
  options[optionKey]["selected"] = True

def changeOption(previousOption, newOption):
  options[previousOption]["selected"] = False
  options[newOption]["selected"] = True

# available options for combo 1
print(getUnselectedOptions())

# combo 1 - select option 3
print("select three")
selectOption("three")

# see available options for combo 2
print(getUnselectedOptions())

# combo 2 - select option 4
print("select four")
selectOption("four")

# see available options for combo 3
print(getUnselectedOptions())

# combo 3 - select option 1
print("select one")
selectOption("one")

# see options left
print(getUnselectedOptions())

# Change combo 1 option to two
print("select two instead of three in combo 1")
changeOption("three", "two")

# see options left
print(getUnselectedOptions())