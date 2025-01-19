animal = "    happY pIg   "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())
print(animal.rstrip())
print(animal.lstrip())
print(animal.find("pI"))  ##return index of specific character or string
print(animal.replace("pI", "no"))
print("pI" in animal)  ## cehcek if exist or not the specified character or string
print("pI" not in animal)
