num_input=int(input("Enter a numerical input value:"))
print(num_input)
num_input+=10
print(num_input)
list_inp=[]
n=int(input("Enter number of elements:"))
for i in range(0,n):
    list_ele=int(input(f"Enter the numerical input_{i+1}:"))
    list_inp.append(list_ele)
print(list_inp)
#using map()
def multiplication(num1,num2):
    return num1*num2
