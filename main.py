import lotteri
import os

lotteriet = lotteri.lotteri

looping = True

while looping:


    os.system("cls" if os.name == "nt" else "clear")
    antal_lotter=input("\n\t\thur många lotter vill du ha max 3 får du!")


    try:
        int_antal_lotter = int(antal_lotter)
        i=0

        if (int_antal_lotter < 4):
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\t\tGRATTIS DU VANN DET HÄR!!")

            while i < int_antal_lotter:
                vinst=lotteriet.get_vinst()
                print("\t\t" + vinst)
                i+=1

        elif(int_antal_lotter > 3):
            print("\n\t\tdu har valt för många lotter")

        


    except ValueError:
        print("\n\t\terror")

    print("---------------------------------------------------------")
    spela_igen = input("\n\t\tvill du spela igen? j/n")
    if (spela_igen=="n"):
        break