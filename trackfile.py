#!/usr/bin/env python3
#create phonebook.dat file
#open file in wb mode as binary file
import mmap,sys
def WriteBinary():
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
    return
def ReadBinary():
   with open("phonebook.dat","r+b") as f:
     mm=mmap.mmap(f.fileno(),0)
     print(mm.read().decode())
   return
print("Enter 1 for write 2 for read")
ch=input("Enter the choice")
if(ch=='1'):
   WriteBinary()
if(ch=='2'):
   ReadBinary()
if(ch=='3'):
   sys.exit()
