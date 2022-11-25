from ast import Break
import subprocess
import re
import string
import os
import sys

                     
def pass_func():
       cmd_cls = "cls"
       subprocess.call(cmd_cls,shell=True)     
       print("Password Manager")              
       while True:
              passd_check = input("Do you have root password(yes/no):")
              if passd_check=="no":
                     crt_passd = input("Enter Your New Password:")
                     cmd ="echo "+crt_passd+":root > Passd_root.txt"
                     subprocess.Popen(cmd,shell=True)        
              elif passd_check =="yes":
                     auth_passd = input("Please Type Your Password:")
                     with open("Passd_root.txt") as pa_ro:
                            au_pa = str(pa_ro.readline())
                     re_au = re.findall(auth_passd+":.*t $",au_pa)
                     str_reau = "".join(str(au) for au in re_au)

                     if auth_passd+":root " == str_reau:
                            user_choice = input("What Do You Want Add New A Password Or Learn A Password That What You Want(a/l):")
                            if user_choice == "a":
                                   name = input("Give A Name Or Number For Your New Password:")
                                   passd_add = input("Type Your New Password Which Do You Want To Add:")
                                   add_cmd ="echo "+name+":["+passd_add+"]"+" >> password_database.txt"
                                   subprocess.Popen(add_cmd,shell=True)
                                   print("Password Added. Good Bye")
                                   k = input("press to exit")
                                   break
                            elif user_choice == "l":
                                   us_in = input("Which Password Do You Want:")
                                   if us_in == "":
                                          print("Password Doesn't Exist!!!")
                                          k = input("press to exit")
                                          break
                                   with open("password_database.txt") as read_db:
                                          re_pa = read_db.read()
                                          
                                   re_da = re.findall(us_in+":.*] $",re_pa,re.M)
                                   str_2 = "".join(str(dgf) for dgf in re_da)
                                   
                                   
                                   print(str_2)
                                   k = input("press to exit")
                                   break                  
                     
              else:
                     print("Please Enter Just yes or no")             