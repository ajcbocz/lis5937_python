import math
def main():
    print("This program finds the real solutions to a quadratic")
    print()
a, b, c = eval(input("Please enter the coefficients(a,b,c):"))
discRoot = math.sqrt(b * b - 4 * a * c)
root1=(-b + discRoot) / (2 * a)
root2=(-b - discRoot) / (2 * a)
print()
print("The solutions are:", root1, root2)
main()

# Problem 2
for i in [1/2,1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10]:
    print(i)