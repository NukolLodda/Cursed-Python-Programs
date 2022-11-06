import dick

num = float(input('Type the length of your penis in inches: '))
option =  input("Press \"1\" for belittlement,\nPress \"2\" for insincerity\n")
while not(option == "1" or option == "2"):
    option =  input("Press \"1\" for belittlement,\nPress \"2\" for insincerity\n")
dick.bar()
dick.smol_penis(num,option)
input()
