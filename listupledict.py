#1 inputting elements to an empty list
list=[]
n=int(input("enter number of elements of the list"))
for i in range(0,n):
    a=int(input("enter the element"))
    list.append(a)
    list1=list
print(list1)
# addind an element in existing list,let the number be 67
list1.append(67)
print(list1)
# adding more than one element to a list,let the numbers be 34,43
list1.extend([34,43])
print(list1)

 #2 accessing elements from a tupple
 tuple=("orange","candy","apple","guava","mango","melon")
 print(tuple)
 # access using index of the element
 print(tuple[1])
 #access more than one element
 print(tuple[1:])
 print(tuple[:-1])
 print(tuple[2:4])
 
 #deleting different dictionary elements
 dictionary={"a":1,"b":2,"c":3,"d":4}
 print(dictionary)
 del dictionary["b"]
 print(dictionary)
