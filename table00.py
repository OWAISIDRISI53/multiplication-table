import time 
time.sleep(1)
print("""
░█████╗░░██╗░░░░░░░██╗░█████╗░██╗░██████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗██║██╔════╝
██║░░██║░╚██╗████╗██╔╝███████║██║╚█████╗░
██║░░██║░░████╔═████║░██╔══██║██║░╚═══██╗
╚█████╔╝░░╚██╔╝░╚██╔╝░██║░░██║██║██████╔╝
░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚═════╝░""")
time.sleep(0.5)
print ("Multiplication table")
time.sleep(0.5)
num=int(input("Enter number :"))
time.sleep(0.3)
print (f"Table of {num} :")

for i in range(1,11) :
    time.sleep(0.2)
    print (num,"x",i,"=",num*i)