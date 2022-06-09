# Aidan Zarski
# String methods excersize

import os
os.system('cls')

# escersize 1A

str1_a = "James"

first = 0
middle = int(len(str1_a)/2)
last = len(str1_a) - 1

output = str1_a[first] + str1_a[middle] + str1_a[last] # new string
print(output)

# excersize 1B

str1_b = "JhonDipPeta"
str2_b = "JaSonAy"

middle1 = int(len(str1_b)/2)
middle2 = int(len(str2_b)/2)

output1b = str1_b[(middle1-1):(middle1+2)]
print(output1b)

output2b = str2_b[(middle2-1):(middle2+2)]
print(output2b)

# Excersize 2

s1_e2 = "Ault"
s2_e2 = "kelly"

s1_middle = int(len(s1_e2)/2)
s1_firsthalf = s1_e2[0:s1_middle]
s1_seccondhalf = s1_e2[s1_middle:]

print(s1_firsthalf + s2_e2 + s1_seccondhalf)

# Excersize 3

s1 = "America"
s2 = "Japan"



middle1 = int(len(s1)/2)
middle2 = int(len(s2)/2)

last1 = len(s1) -1
last2 = len(s2) -1

output = s1[0] + s2[0] +s1[middle1] +s2[middle2] + s1[last1] + s2[last2]
print(output)


# Excersize 4

str1 = "PyNaTive"
strlowercase = ""
struppercase = ""

for x in str1:
    if x.isupper():
        struppercase += x
    else:
        strlowercase += x   

print(strlowercase + struppercase)









