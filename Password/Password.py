from ast import arguments
from Password_Manager import pass_func
from Password_Generator import func_generator
import optparse
import subprocess
cls_cmd="cls"
subprocess.call(cls_cmd,shell=True)
def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-m","--manager",dest="manager",help="manager")
    return parse_object.parse_args()

(user_input,arguments) = get_user_input()
if user_input.manager == "m":
    pass_func()   
elif user_input.manager !="m":
    print("Password V1.0 \n")
    userinput_0 = input("What do you want generate or manage(g/m)")
    if userinput_0 =="g":
        func_generator()
    elif userinput_0 =="m":
        pass_func()