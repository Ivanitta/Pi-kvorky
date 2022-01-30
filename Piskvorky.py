from random import randrange

def vyhodnot(pole):
    if 'xxx' in pole:
        vyhodnoceni = "x"
        print("Vyhrál jsi!")
        return vyhodnoceni
    elif 'ooo' in pole:
        vyhodnoceni = "o"
        print("Prohrál jsi! Vyhrál počítač!")
        return vyhodnoceni
    elif '-' not in pole: 
        vyhodnoceni = "!" # remíza
        print("Remíza.")
        return vyhodnoceni
    else:
        vyhodnoceni = ''
        print("Pokračuj ve hře.")
        return vyhodnoceni


def tah(pole, pozice, symbol):
    if symbol not in ('x','o'):
        raise Warning ("Zadej jen 'x' nebo 'o'.")

    if pozice<0 or pozice >19:
        raise Warning ("Číslo pozice zadej v rozmezí 0-19.")
    
    if pole[pozice] != '-':
        raise Warning("Pozice je již obsazená. Zadej jiné číslo pozice.")
        

    else:      
        zacatek_pole = (pole[:pozice])
        konec_pole = (pole[pozice + 1:])
        pole = zacatek_pole + symbol + konec_pole   
        return pole

def tah_hrace(pole, symbol):
    
    while True:
                 
        try: 
            pozice = int(input("Zadej číslo pozice, kde chceš dát křížek. Číslo zadej v rozmezí 0-19.: "))   
            pole=tah(pole, pozice, symbol)
            break
        except ValueError:
            print("Zadávej jen čísla!")
        
    return pole

def tah_pocitace(pole, symbol):
    while True:
        try:
            pozice=randrange(20)
            pole=tah(pole, pozice, symbol)
            print(pozice)
            break
        except Warning as message:
            print(message)  
            continue 
    return pole

def piskvorky1d():
    pole = "--------------------"
    print(pole)
   
    while True:
        
        pole = tah_hrace(pole, "x")
        pole = tah_pocitace(pole, "o")
        print(pole)
        
        vyhodnoceni=vyhodnot(pole)
        
        if vyhodnoceni == "":
            continue  
        else:
            print(vyhodnot(pole))
            break

           
print(piskvorky1d())