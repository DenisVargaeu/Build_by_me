import math
import json
import time
import sys
import os
from rich.console import Console
from rich.table import Table
from rich import box
hun = (0)
fif = (0)
twen = (0)
ten = (0)

fiv = (0)
tw = (0)
on = (0)
work = (0)

print("--------------------------------------------------------------")
print("| Program na rozdelenie peňazí na bankové penazie            |")
print("| Autor: Denis Varga | denisvarga.eu                         |")
print("--------------------------------------------------------------")

number = int(input ("Zadajte hodnotu prosim: "))



console = Console()


def debug():
    print(f"hun = {hun}")
    print(f"fif = {fif}")
    print(f"twen = {twen}")
    print(f"ten = {ten}")
    print(f"work = {work}")
def output():
    os.system("cls" if os.name == "nt" else "clear")
    print("Pocitajte prosim...")
    time.sleep(2)

    os.system("cls" if os.name == "nt" else "clear")
    table = Table(title="Vysledok rozdelenia peňazí", box=box.ROUNDED, style="green", show_lines=True)
    table.add_column("Hodnota", justify="center", style="cyan", no_wrap=True)
    table.add_column("Počet bankoviek", justify="center", style="magenta")

    table.add_row("100", str(hun))
    table.add_row("50", str(fif))
    table.add_row("20", str(twen))
    table.add_row("10", str(ten))
    table.add_row("5", str(fiv))
    table.add_row("2", str(tw))
    table.add_row("1", str(on))
    console.print(table)
    data = {
        "hodnota": number,
        "Stovky": hun,
        "Padesiatky": fif,
        "Dvaciatky": twen,
        "Desiatky": ten,
        "Patky": fiv,
        "Dvojky": tw,
        "Jednoky": on
    }
    with open("export.json", "w") as file:
        json.dump(data, file, indent=4)
        

def hundret():
    global hun
    global number
    work = (number/100)
    hun = (math.floor(work))
    work1 = (100*hun)
    number = (number-work1)
    #print (work1)

def fifty():
    global fif
    global number
    work = (number/50)
    fif = (math.floor(work))
    work1 = (50*fif)
    number = (number-work1)
    #print (work1)

def twenty():
    global twen
    global number
    work = (number/20)
    twen = (math.floor(work))
    work1 = (20*twen)
    number = (number-work1)
    #print (work1)

def tenf():
    global ten
    global number
    work = (number/10)
    ten = (math.floor(work))
    work1 = (10*ten)
    number = (number-work1)
    #print (work1) debug

def five():
    global fiv
    global number
    work = (number/5)
    fiv = (math.floor(work))
    work1 = (5*fiv)
    number = (number-work1)
    #print (work1) debug

def two():
    global tw
    global number
    work = (number/2)
    tw = (math.floor(work))
    work1 = (2*tw)
    number = (number-work1)
    #print (work1) debug

def one():
    global on
    global number
    work = (number/1)
    on = (math.floor(work))
    work1 = (1)
    number = (number-work1)
    #print (work1) debug


def main():
    hundret()
    fifty()
    twenty()   
    tenf()
    five()
    two()
    one()
    output()




main()