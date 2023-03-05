from script.module import install_package
from sys import argv

    #Installation module 
try:
    import PIL
    import colorama
    
except:
    install_package(["Pillow", "colorama"])
    import PIL, colorama
    
    
import colorama
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)    
    

    
def convert(file):
    from PIL import Image
    import os
    new = os.path.basename(file).split(".")[0]+".png"
    Image.open(file).save(new, format="png")
    

    

if len(argv)==2:
    file = argv[1]

    
else:
    file = input("Glissez le fichier ici .\n")

print(Fore.GREEN+"Conversion en cours ...")
convert(file)
print(Fore.RED+"Conversion terminé !!")
import time
time.sleep(5)
exit()