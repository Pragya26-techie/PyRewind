"""Store the word "Python" in a variable, then print every second letter."""
# a = "Python"
# print(a[0:6:2])
# print(a[::])
# print(a[::-2])

# b = "code yug"
# print(b[4:3:-2])
# # print(b[:-4:-1])
# # print(b[-1:-5:-3])
# # print(b[0:0])

# s = "Python"
# print(s[1] + s[4])
# print(s[:])
# print(s[::])
# print(s[::2])

## Negative steps and reverse slicing
# print(s[::-1])
# print(s[5:1:-1])
# print(s[4:3:-2])
# print(s[3:0:-1])
# print(s[-1:-4:-1])
# print(s[-2::-1])
# print(s[0:6:-1])
# print(s[5:0:1])/

a = "code yug"
b = "Data Science"
c = "programming"

# print(a[7:4:-1])
# print(a[7:3:-2])
# print(a[4:3:-2])
# print(a[::-1])
# print(a[::2])
# print(b[0:4])
# print(b[-7:])
# print(c[1:10:3])
# print(c[-1:-8:-2])
# print(c[:: -1])

"""Print the first and last characters of a string."""
print(a[0],a[-1])
"""Reverse a string using slicing only."""
print(a[::-1])

"""44.Print a string without its first and last characters."""
print(c[1:-1])

"""Extract the middle two characters from the string 'Python'."""
s = "python"
print(s[2:4])

"""46. Print every second character, starting from index 1."""
print(s[1::2])

"""47. Given 'Hello World', extract only 'World' using slicing."""
p = "Hello World"
print(p[6::])

"""48.Given 'programming', print the characters at odd indices."""
print(c[1:12:2])

