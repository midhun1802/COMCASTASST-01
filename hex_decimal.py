from pip._vendor.distlib.compat import raw_input


def intfunction():
    temp = input('Enter the integer to be iterated ')
    length = len(temp)

    print('you entered ', temp + 'length : ', length)

    total_sum = 0

    print('the length of the number entered is ', length)

    for i in range(length):
        total_sum += int(temp[i])

    print('The sum of the input number digits is ', total_sum)


def hexfunction():
    string_hexnum = raw_input('Enter the Hexadecimal number : ')
    print('you entered : ', string_hexnum)

    int_hexnum = int(string_hexnum,16)

    print('The integer value of the entered Hexadecimal is', int_hexnum)

    int_hexnum_tostring = str(int_hexnum)

    length = len(int_hexnum_tostring)
    total_sum = 0;

    for i in range(length):
        total_sum += int(int_hexnum_tostring[i])

    print('The sum of the input number digits is ', total_sum)

    print('Converting  to hexadecimal becomes ', hex(total_sum))




type_of = int(input('\n\nSelect the type you want to use : \n 1. Integer Number \n 2. Hexadecimal \n'))

if(type_of == 1):
    intfunction()

elif(type_of == 2):
    hexfunction()

