import random

def bar():
    print("-" * 83)
    return

def dick_float(num):
    if num // 1 == num:
        print(int(num),end="")
    else:
        print(num,end="")

def true_dick(num):
    print("your penis really is",end=" ")
    dick_float(num)
    print("in' long",end="")
    return

def smol_msg():
    inthing = random.randint(0,2)
    if inthing == 0:
        print("I'd never fuck you even if it meant the end of humanity.")
    elif inthing == 1:
        print("you're balls don't make testoterone you childish ass.")
    else:
        print("clearly, you're plain unfuckable.")
    return

def smol_penis(num,option):
    if num == 0:
        print("So basically you don't have a penis huh?\n Then nothing here ever applies so goodbye!")
    else:
        if option == "1":
            num = int(num // 1)
            for _ in range(num):
                    print("Your dick is small, like",end=" ")
                    smol_msg()
        elif option == "2":
            if num <= 2:
                div_12 = 12 / num
                print("Looks like I was right all along,")
                true_dick(num)
                print("\nwhich is like",end=" ")
                dick_float(div_12)
                print(" times shorter than average")
            else:
                print("There's no possible way")
                true_dick(num)
                print(" that's like impossible you know? You liar")
    bar()
    print("\n")
    return


num = float(input('Type the length of your penis in inches: '))
option =  input("Press \"1\" for belittlement,\nPress \"2\" for insincerity\n")
while not(option == "1" or option == "2"):
    option =  input("Press \"1\" for belittlement,\nPress \"2\" for insincerity\n")
bar()
smol_penis(num,option)
input()
