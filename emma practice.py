print("hello word")
print (5)
print (3>5)

efg="black eye"
abc=efg
print("abc")
print(abc)

formatter = "%r %r %r %r"
print (formatter %(1,2,3,4))
print (formatter %("one","two","three","four"))
print (formatter %(True,False,False,True))
print (formatter % (formatter,formatter,formatter,formatter))
print (formatter % (
    "i had this thing",
    "that  you could type up right",
    "but it didn't sing",
    "so i said goodnight"
))

days=(" Mon Tue Wed Thu Fri Sat Sun")
months=(" \nJan\nFeb\nMar\nApril\nMay\nJune\nJuly\nAug\nSep\nOct\nNov\nDec")

print ("here is the days",days)
print ("here is the months",months)
print ("""
There is some idea,
with the thought,
you can fly to the sky
""")

print ("how old are you?")
age=input()
print ("how tall are you?")
height=input()
print ("how much do you weight?")
weight=input()
print ("so you're",age,"and you're",height,"high","and",weight,"weight")
print ("so you're %r and %r high,and %r weight",(age,height,weight))