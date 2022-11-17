import time
# Here is the links I used for the strings below
# p21 - p219 https://dreamteam.fandom.com/wiki/Dream_SMP_books/Non-lore_books/How_to_sex_2
# the rest of the strings - https://dreamteam.fandom.com/wiki/Dream_SMP_books/Non-lore_books

p21 = "How to Sex\n\nBabies be like: Yo I\ncame out of the\nverjina.\n\nHey this is How to Sex\n2. Tommyinnits novel.\nhow to Sex 1 is so\nvery unavailable.\n\n\n"
p22 = "Chapter 1: How to Sex\n\nYou like Sex? Yeah. Me\nneither. But lets read\nthis book so we can\nstop the sinners.\n\nDO NOT HAVE SEX WITH\nTERRORISTS!\n\n\n\n"
p23 = "Chapter 1: The tutorial\n\nSo. you need to know\nhow to get a fuckin\nkid. You like kids?\nThat is very bad\nif so\n\n\n\n\n\n"
p24 = "Chapter 1: The tutorial\n\nAt first you need a\nfriend. If you have\none: Well done. The\nfriend will, when all\nshriveled, SWITCH UP\nON YO. That's when\nyou're in cho prime.\nThat's when yo make\nyou move\n\n"
p25 = "Chapter 2: Speaking\nto Girls and women\n\ngirls and women are\nbeautifl\n\nIf you want to speak\nto one, offer to buy\nthem a handbag. Then\nthey have sex with you\n\n\n"
p26 = "Chapter 3: Having Sex\nDO NOT GO \"MMMMMM\".\nIT PUTS THEM OFF.\n\nsex is really\nscientific and when\nyouve having sex\nmakes notes.\n\n\n\n\n"
p27 = "Chapter 3: Having Sex\nmake notes on the\nfollowing:\n- what smells you see\n- how hungry you are\n- how angry you are\n- what you do when\nyou're angry\n\nDO NOT HIT GIRLS!\n\n\n"
p28 = "Chapter 3: Having Sex\n\ngirls are not ugly.\ngirls can get hungry\nthough. this is their\none downfall.\nSociety: Women are\nbad. Society is WRONG.\nWomen should be paiyed\n\n\n\n"
p29 = "Chapter 9\n\nChapter 9 is all about\nBoobs\n\nBOOBS\nBOOBIES\nBOOBS\n\nMen love the boob.\nWomen when they\ncharge they phone\nthey boob get bigger"
p212 = "Sex with BadBoyHalo;\nDO NOT DO IT\n\n\n\n\n\n\n\n\n\n\n"
p218 = "Chapter 128: Permission\n\nCONSENT\n\n\n\n\n\n\n\n\n\n"
p219 = "Chapter 129\n\nWhat is a dildo?\nSomeone tell me, I\ndon't know\nIs it a sword?\nI know what a\nsword is\nGogy likes dildos\nWhy?\n\n\n"
# How to sex 2 has a total of 24 pages
po31 = "TommyInnits book\nhow 2 sex 3\nTHE MONOPOLY!\n\n\nVirgin Beware!!!!!!\n\n\n\n\n\n\n"
po32 = "Sex is like God sex is\nlike God but God is\n\n\n\n\n\n\n\n\n\n\n"
# How to sex 3 [Original] has a total of 2 pages
pn31 = "How to sex 3:\nChapter 1:\nUnderstanding Men.\n\nWhy are they?\n\n\n\n\n\n\n\n"
# How to sex 3 [New] has a total of 1 page
p41 = "How to Sex 4:\nJust pop it in and pray\nDream hot\n\n\n\n\n\n\n\n\n\n"
# How to sex 4 has a total of 1 page
unavail = "404: Page not found\n\n\n\n\n\n\n\n\n\n\n\n"
pagelist = [p21,p22,p23,p24,p25,p26,p27,p28,p29,p218,p219,po31,po32]
# Indecies   0   1   2   3   4   5   6   7   8   9   10   11   12
lines = "-" * 24
strfor = "{}\n----page {} of {}-b{}--"
PREV_LINE = "\u001b[1F"
LINE_CLEAR = '\x1b[2K'

def bookv(p,v):
    page = str(p)
    if len(page) == 1:
        page += " "
    if v == "2":
        if p < 10:
            return strfor.format(pagelist[p-1],page,24,"2-")
        elif p == 12:
            return strfor.format(p212,page,24,"2-")
        elif p < 20 and p > 17:
            return strfor.format(pagelist[p-9],p,24,"2-")
        else:
            return strfor.format(unavail,page,24,"2-")
    elif v == "4":
        return strfor.format(p41,p,1,"4-")

def book3(p,v):
    if v.lower()[0] == "o":
        return strfor.format(pagelist[p+10],p,2,"3" + v)
    else:
        return strfor.format(pn31,p,1,"3" + v)

def pgd(p,ting):
    nting = ting.lower()[0]
    x = 0
    if len(ting) >= 2:
        x = 1
    if nting == "l" or nting == "<":
        p -= 1
    elif nting == "r" or nting == ">":
        p += 1
    elif (ord(ting[0]) > 47 and ord(ting[0]) < 58):
        if len(ting) <= 2:
            p = int(ting[0:])
        elif (ord(ting[x]) > 47 and ord(ting[x]) < 58) and x == 2:
            p = int(ting[0:2])
    return p

def main():
    book = input("Enter which How to Sex book you'd like to read: ")
    b = book.lower()
    if b == "two": book = "2"
    elif b == "three": book = "3"
    elif b == "four": book = "4"
    if book[0] == "3":
        varient = input("Enter which version you'd like to read (o for original, n for new): ")
        page = 1
        larg = 2
        num = 1
        if varient.lower()[0] == "o":
            page = int(input("Enter what page of the selected book you'd like tor read: "))
            larg = 3
            num += 1
        print("\n" + lines)
        while page > 0 and page < larg:
            print(book3(page,varient))
            ting = input()
            page = pgd(page,ting)
            print((PREV_LINE + LINE_CLEAR) * 15,end=LINE_CLEAR)
            if ting.lower()[0] == "x":
                break
    elif book[0] == "2" or book[0] == "4":
        page = 1
        larg = 2
        num = 0
        if book.lower()[0] == "2":
            page = int(input("Enter what page of the selected book you'd like tor read: "))
            larg = 25
            num += 1
        print("\n" + lines)
        while page > 0 and page < larg:
            print(bookv(page,book))
            ting = input()
            page = pgd(page,ting)
            print((PREV_LINE + LINE_CLEAR) * 15,end=LINE_CLEAR)
            if ting.lower()[0] == "x":
                break
    elif book.lower()[0] == "x":
        quit()
    else:
        print("This book is currently unavailabe/does not exist\nThe program will be updated as soon as the data is out\n")
        num = 1
        time.sleep(3)
    print((PREV_LINE + LINE_CLEAR) * (3 + num),end=LINE_CLEAR)

print("Welcome to the archive of TommyInnit's How to Sex books.                        |")
print("A brilliant place of wonder and fun and a fantastic guide to having intercourse.|")
print("Currently, there are 3 available How to Sex books: books 2, 3, and 4.           |")
print("data for the books are obtained from the link below:                            |")
print("\u001b[36;1mhttps://dreamteam.fandom.com/wiki/Dream_SMP_books/Non-lore_books \u001b[0m               |")
print("If you're done reading, press x to exit.                                        |")
print("_" * 80,end="|\n\n")
while __name__ == "__main__": main()
