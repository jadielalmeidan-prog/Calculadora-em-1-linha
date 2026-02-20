def decisão():

    dec1 = input("Vc deseja fazer uma conta?\n").lower()
    if dec1 in ("sim","s"):

        while True:
            num = float(eval(input(">>>")))
            print(f"{num:.2f}")
            dec2 = input("Vc deseja fazer outra conta?\n").lower()
            if dec2 in("sim","s"):
                continue
            else:
                print("Ok,então!!!")
                break
    else:
        print("Ok então...")

decisão()
