# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained
# in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
# For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5
s = "azcbobobegghakl"
vowels = "aeiou"
count = 0
for char in s:
    if char in vowels:
        count += 1
print("Number of vowels:" + str(count))