print("hello world")
print(8 * "\n")
print("welcome to", end=" ")
print("pycharm")
print("python")
# ----------------------------------------------------(Variables)------------------------------------------------------
a=3
print(a)
a="hasnaa"
print(a)
# -------Concatenation--------
b="hasnaa" #String
c=25       #Integer
d = (b+str(c))
print(d)
# -------Global & Local Variables---------
x = 2 #Global
def one() :
    x=3 #Local
    print (x)
print(x)
one()
# -------------------
def two() :
    # x=4 #Local
    print (x) #calling from global

two()
# -------------------
def three() :
    global x
    x=5
    print(x)
three()
print(x)
def four() :
    print (x)
four()
# ------------------
x=5
def one () :
    x =2
    print (x)
print (x)
one()

def two() :
    global x
    x=10
    print(x)

def three() :
    print (x)
one()
print(x)
two()
three()
# -------------------------------------------------Escape characters ---------------------------------------------------
# \  >> escape new line +\
print ("hello \
world")
# \b >> back space
print("hello\bpython")
# \t >> tab
print("hasnaa\tsalah")
print("hasnaa   salah")
# \n >> new line
print("hello\nworld")
# \" >> escape double quotes
print("i love \"python\" ")
print('i love "python"')
# \' >> escape single quote
# \\ >> escape back slash
# \r >> carriage return
print("abcd\r12345")
# ---------------------------------------------Python Version-----------------------------------------------------------
import sys
print(sys.version)

from platform import python_version
print("python version is " , python_version())


import sys
print(sys.version_info)
print(type(sys.version_info))
