#to print a new list without any duplicates from list1.

def lwdup(list1):
    list2=set(list1)
    print(list2)

list1=eval(input("write any list"))
lwdup(list1)
