def reverse(str):
    
    if str != '':
        print(str)
        return str[-1]+ reverse(str[:-1])
    else:
        return str

print(reverse('hello'))