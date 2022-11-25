import string
import subprocess
import random
import time
from Password_Manager import pass_func

print("-------------------------------------------------------")
print(" ")
m = [1,2,3,4,5,6,7,8,9,10,12,11,13,14,15,16,17,18,19,20]
str_m = "".join(str(sm) for sm in m)
d = list(string.ascii_uppercase)
str_d = "".join(str(sd) for sd in d)
s= list(string.ascii_lowercase)
str_s = "".join(str(ss) for ss in s)
fg =["!","_","-","","@"]
den = [str_m,str_d,str_s,fg]
def func_generator():
    cmd_cls = "cls"
    subprocess.call(cmd_cls,shell=True)
    print("PASSWORD GENERATOR \n")
    bnry = [1,0,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0,1,0,0,]
    random.shuffle(bnry)
    str_bnry = "".join(str(sbn) for sbn in bnry)
    print(str_bnry)
    print(" ")
    print("If you want a strong password, you should type numbers more than 3. \n")
    k = int(input("Password lenght(3 x numbers which you type) ? :"))
    a = 1
    passd = []
    while True:
        if a <= k:
            random.shuffle(den)
            frst = random.choices(den[0],k=1)
            str_1 = "".join(str(g) for g in frst)
            secnd = random.choices(den[1],k=1)
            str_2 = "".join(str(h) for h in secnd)
            thrd = random.choices(den[2],k=1)
            str_3 = "".join(str(j) for j in thrd)
            passd.append(str_1)
            passd.append(str_2)
            passd.append(str_3)
            
            a +=1
        else:
            str_4 = "".join(str(l) for l in passd)
            print("Your generated password =>",str_4)
            user_inp = input("Do You Want To Storage Your Password İn Password Manager(yes/no):")
            if user_inp =="yes":
                print(" ")
                print("GOODBYE")
                print("---------------------------------------------------------------------------")

                pass_func()
                break
            elif user_inp =="no":
                print("GOODBYE!!!")
                break
