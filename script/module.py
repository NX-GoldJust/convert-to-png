def install_package(packages: list):
    from os import system
    for p in packages:
        system(f"pip install {p}")
    
    system("cls")
    print("Installation des modules terminé / Installation of modules completed")
    
        
def remove_accent(text: str):
    text = list(text)
    
    new = []

    
    
    for l in text:
        maj = False
        if l == l.upper():
            maj = True

        l = l.lower()
        
        if l in ["é", "è", "ê", "ë"]:
            l = "e"
            
        elif l in ["à", "á", "â", "ä", "å", "ã"]:
            l = "a"

        elif l in ["î", "ï", "í", "ì"]:
            l = "i"
            
        elif l == "ñ":
            l = "n"
        elif l in ["ó", "ò", "ô", "ö", "õ"]:
            l = "o"
            
        elif l == "š":
            l == "s"
        elif l in ["ú", "ù", "ü", "û"]:
            l == "u"

        elif l in ["ý", "ÿ"]:
            l == "y"
            
            
        elif l == "ž":
            l == "z"

        if maj:
            l = l.upper()
        new.append(l)
        
        
    return "".join(new)






