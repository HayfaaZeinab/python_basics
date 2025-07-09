


"""
#foundation task
fav=["biriyani","mandi","shawarma","shawaya","alfaham"]
print("\nmy favourite foods :\n")
for i in range(len(fav)):
    print(f"{i+1}.{fav[i]}")
"""

"""
#stretch task
l=[]
n=int(input("enter the size of list : "))
for i in range(5):
    l.append(int(input("enter element: ")))
print("original list : ",l)
s= l[::-1]
print(s)
 """


#challnge task

l=[]
while True:
    print("\nShopping List Manager\n")
    print("1.Add item ")
    print("2.Rremove item")
    print("4.Show list")
    print("4.Check item")
    print("5.Exit")
    
    choice=int(input("Enter choice(1-4): "))
    if choice==1:
        l.append(input("\nEnter element : "))
        print("element added")
    elif choice==2:
        l.remove(input("\neleent to be removed : "))
        print("element removed ")

    elif choice==3:
        print("list")
        for i in range(len(l)):
            print(l[i])
    elif choice==4:
        a=input("\nenter element to check : ")
        if a in l:
            print(f"{a} is present in the list")
        else:
            print(f"{a} is not in list")
    elif choice==5:
        print("\nExiting")
        break
    else:
        print("\nwrong choice ")
        break

