from pip._vendor.distlib.compat import raw_input


def intfunction():
    temp = input('Enter the integer to be iterated ')
    length = len(temp)

    print('you entered ', temp + 'length : ',  length)

    total_sum = 0

    #print('the length of the number entered is ', length)

    for i in range(length):
        total_sum += int(temp[i])
        #given each char and iterating throught the entered input

    print('The sum of the input number digits is ', total_sum)


def hexfunction():
    string_hexnum = raw_input('Enter the Hexadecimal number : ')
    print('you entered : ', string_hexnum)
#for i in string_hexnum :
    #int_hexnum = int(string_hexnum,16)
     # taking an empty list to add the integer values of each hex decimal converted values in the given input
    char = []
    for i in string_hexnum:
        char.append(int(i,16))
        
       #converting the each character in the given input to hex decimal value
       #adding the integer value to the list

    #print('The integer value of the entered Hexadecimal is', int_hexnum)

    #int_hexnum_tostring = str(int_hexnum)
    #print (int_hexnum_tostring)

    length = len(char)
    total_sum = 0;

    for i in range(length):
        #taking the sum of induvudual value
        total_sum += int(char[i])

    print('The sum of the input number digits is ', total_sum)

    print('Converting  to hexadecimal becomes ', hex(total_sum))




type_of = int(input('\n\nSelect the type you want to use : \n 1. Integer Number \n 2. Hexadecimal \n'))

if(type_of == 1):
    intfunction()

elif(type_of == 2):
    hexfunction()
