




# Q1
my_str = "The first one is the easiest!"
res_two= []
my_str_ = my_str.split()
first, second, third = 1, len(my_str_), 2
while first < second:
    res_two.append(my_str_[first])
    first += third

#this code takes a string stored in the var my_str,
#and puts every other word in that str in a list called res.

#this is the oneliner that does the same.
res = [word for index,word in enumerate(my_str.split()) if index % 2 == 1]




##########################
#Q2
n = 42
my_dictionary_m = {}
for x in range(100, 0, -3):
    if x % n == 0:
        my_dictionary_m[x] = f"{x} is divided by {n}.\n"
    else:
        my_dictionary_m[x] = f"the remainder of {x} divided by {n} is: {x % n}.\n"
print(*my_dictionary_m.values(), sep= "")

## this code stores strings in a dict of int keys such that:
# it maps nubers from 100 to 0 to a corrosponding string that either declares that x is divided by n
# and if it cant be divided by n itll declare that re remainder of x by n is <x%n>
# at the end it prints that same dict.

#heres the oneliner for it (ill asumme the print aint part of it):

my_dictionary = { x : f"{x} is divided by {n}.\n" if x % n == 0 else \
    f"the remainder of {x} divided by {n} is: {x % n}.\n" for x in range(100, 0, -3)}

print(*my_dictionary.values(), sep= "")




##Q3

for i in range(0, max(ord('9'), ord('z'), ord('Z'))+1):
    if chr(i).isalpha() or chr(i).isdigit():
        print(f"The ASCII number {i} represent the char '{chr(i)}'")

#this code print every char that is alphanumeric, and says what is its ASCII code.

_ = [print(f"The ASCII number {i} represent the char '{chr(i)}'") \
    for i in range(0, max(ord('9'), ord('z'), ord('Z'))+1) if chr(i).isalpha() or chr(i).isdigit()]


## Q4
list_c = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 102, 117, 110, 33]

tmp = ""
for num in list_c:
    tmp += chr(num)
print(tmp)

# this converts a list of ASCII representaition of chars to a string containing those represnted chars in char form/.


## hererse the oneliner, again i assume the print isnt counted.

tmp_chr = "".join(([chr(ch) for ch in list_c]))
print(tmp_chr)

if __name__ == "__main__":
    print()

