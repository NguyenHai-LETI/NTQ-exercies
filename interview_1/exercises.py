#ex1
str = 'abcdjdkabarueh'
print(str[::-1])


#ex2
ds = [5, 6, 1, 8, 0, -1]
n = 3
if (n < len(ds)):
    ds.sort(reverse=True)
    print(ds[n - 1])

#ex3
# str2 = "aaabbbcdreeeff"
# str2 = "abceeeefff"
str2 = 'baaabbbefgaaaagfh'
first_flag = False
for i in range(len(str2)):
    if (first_flag):
        break
    if ( (i == 0 and str2[i] != str2[i + 1])
        or (str2[i] != str2[i - 1] and str2[i] != str2[i + 1])):
        print(str2[i], end='')
        if (i < len(str2) - 2 and str2[i + 1] == str2[i + 2]):
            first_flag = True
    elif (i == len(str2) - 1 and str2[i] != str2[i - 1]):
        print(str2[i])
        break





