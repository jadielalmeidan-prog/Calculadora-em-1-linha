dec1 = input("Vc deseja fazer uma conta?").lower()
if dec1 in ("sim","s"):

    while True:
        num = float(eval(input(">>>")))
        print(num)
        dec2 = input("Vc deseja fazer outra conta?").lower()
        if dec2 in("sim","s"):
            continue
        else:
            print("Ok,então!!!")
            break
else:
    print("Ok então...")