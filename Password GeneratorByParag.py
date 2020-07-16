def main():
    import string
    import random
    if __name__ == '__main__':
        print("Welcome to secret your life\n This code is developed by Sameer\Parag Jain:\n")

        s1=string.ascii_lowercase
        s2=string.ascii_uppercase
        s3=string.digits
        s4=string.punctuation
        plen=int(input("Enter your Password length:\n"))
        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        # print(s)
        random.shuffle(s)
        print("Your Secret Strong Password is:\n",end="")
        print("".join(s[0:plen]))

        print("\nDo you want to generate again your Password:\n Press y for Yes and Press n for Quit")
        restart=""

        while restart!="y" and restart!="no":
            restart=input()
            if restart=="y":
                main()

            elif restart=="n":
                print("Thank you for using password generator\n Have a great day")
                exit()
main()
