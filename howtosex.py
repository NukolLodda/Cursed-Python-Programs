p21 = "How to Sex\n\nBabies be like: Yo I\ncame out of the\nverjina.\n\nHey this is How to Sex\n2. Tommyinnits novel.\nhow to Sex 1 is so\nvery unavailable."
p22 = "Chapter 1: How to Sex\n\nYou like Sex? Yeah. Me\nneither. But lets read\nthis book so we can\nstop the sinners.\n\nDO NOT HAVE SEX WITH\nTERRORISTS!"
p23 = "Chapter 1: The tutorial\n\nSo. you need to know\nhow to get a fuckin\nkid. You like kids? That\ns very bad if so"
p24 = "Chapter 1: The tutorial\n\nAt first you need a\nfriend. If you have\none: Well done. The\nfriend will, when all\nshriveled, SWITCH UP\nON YO. That's when\nyou're in cho prime.\nThat's when yo make\nyou move"
p25 = "Chapter 2: Speaking\nto Girls and women\n\ngirls and women are\nbeautifl\n\nIf you want to speak\nto one, offer to buy\nthem a handbag. Then\nthey have sex with you"
p26 = "Chapter 3: Having Sex\nDO NOT GO \"MMMMMM\".\nIT PUTS THEM OFF.\n\nsex is really\nscientific and when\nyouve having sex\nmakes notes."
p27 = "Chapter 3: Having Sex\nmake notes on the\nfollowing:\n- what smells you see\n- how hungry you are\n- how angry you are\n- what you do when\nyou're angry\n\nDO NOT HIT GIRLS!"
p28 = "Chapter 3: Having Sex\n\ngirls are not ugly.\ngirls can get hungry\nthough. this is their\none downfall.\nSociety: Women are\nbad. Society is WRONG.\nWomen should be paiyed"
p29 = "Chapter 9\n\nChapter 9 is all about\nBoobs\n\nBOOBS\nBOOBIES\nBOOBS\n\nMen love the boob.\nWomen when they\ncharge they phone\nsthey boob get bigger"
p212 = "Sex with BadBoyHalo;\nDO NOT DO IT"
p218 = "Chapter 128: Permission\n\nCONSENT"
p219 = "Chapter 129\n\nWhat is a dildo?\nSomeone tell me, I\ndon't know\nIs it a sword?\nI know what a\nsword is\nGogy likes dildos\nWhy?"
# How to sex 2 has a total of 24 pages
po31 = "TommyInnits book\nhow 2 sex 3\nTHE MONOPOLY!\n\n\nVirgin Beware!!!!!!"
po32 = "Sex is like God sex is\nlike God but God is"
# How to sex 3 [Original] has a total of 2 pages
pn31 = "How to sex 3:\nChapter 1:\nUnderstanding Men.\n\nWhy are they?"
# How to sex 3 [New] has a total of 1 page
p41 = "How to Sex 4:\nJust pop it in and pray\nDream hot"
# How to sex 4 has a total of 1 page
unavail = "404: Page not found"
pagelist = [p21,p22,p23,p24,p25,p26,p27,p28,p29,p218,p219,po31,po32]
# Indecies   0   1   2   3   4   5   6   7   8   9   10   11   12
lines = "-" * 24
strfor = "\n\n{}\n\n\n----page {} of {}-v {}----"

def bookv(p,v):
    if v == "2":
        if p < 10:
            return strfor.format(pagelist[p-1],p,24,2)
        elif p == 12:
            return strfor.format(p212,p,24,2)
        elif p < 20 and p > 17:
            return strfor.format(pagelist[p-9],p,24,2)
        else:
            return strfor.format(unavail,p,24,2)
    elif v == "4":
        if p == 1:
            return strfor.format(p41,p,1,4)
        else:
            return strfor.format(unavail,"NaN",1,4)

def book3(p,v):
    if v.lower()[0] == "o":
        if p == 1 or p == 2:
            return strfor.format(pagelist[p+10],p,2,v)
        else:
            return strfor.format(unavail,"NaN",2,v)
    else:
        if p == 1:
            return strfor.format(pn31,p,1,"3" + v)
        else:
            return strfor.format(unavail,"NaN",1,"3" + v)

def main():
    book = 0
    while not(book == "2" or book == "3" or book == "4"):
        book = input("Enter which how to sex book you'd like to read: ")
        if book == "1":
            print("This book is currently unavailable at the moment\nPlease check in at a different time\n")
        elif book == "3":
            varient = input("Enter which version you'd like to read (o for original, n for new): ")
            page = int(input("Enter what page of the selected book you'd like tor read: "))
            larg = 1
            if varient.lower()[0] == "o":
                larg = 3
            while page >= 1 and page < larg:
                print(lines + book3(page,varient))
                ting = input()
                ting = ting.lower()[0]
                if ting == "l" or ting == "<":
                    page -= 1
                elif ting == "r" or ting == ">":
                    page += 1
                else:
                    break
        elif book == "2" or book == "4":
            page = int(input("Enter what page of the selected book you'd like tor read: "))
            larg = 2
            if book.lower()[0] == "2":
                larg = 25
            while page >= 1 and page < larg:
                print(lines + bookv(page,book))
                ting = input()
                ting = ting.lower()[0]
                if ting == "l" or ting == "<":
                    page -= 1
                elif ting == "r" or ting == ">":
                    page += 1
                else:
                    break
        elif book.lower()[0] == "x":
            quit()
        else:
            print("The version for the How to Sex book currently\ndoes not exist\nPlease check in at a different time\n")

print("Welcome to the archive of TommyInnit's How to Sex books\nA brilliant archive of wonder and fun and a\nfantastic guide to having intercourse")
print("Currently there are 3 available how to sex books,\nversions 2, 3, and 4.\nIf you're done reading, press x to exit\n")
while __name__ == "__main__": main()
