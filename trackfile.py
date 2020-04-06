#!/usr/bin/env python3
#create phonebook.dat file
#open file in wb mode as binary file
with open("phonebook.dat","wb") as f:
    #write data for the file
    n=int(input('How many entries ?'))
    for i in range(n):
          name=input('Enter name')
          phone=input('Enter  phone no')
    name=name.encode()
    phone=phone.encode()
    #write data into the file
    f.write(name+phone)
