import os
import sys

print("""
Salam mamnon hastam ke application man ro entekhab kardid 
baraye inke application be behtarin shekl kar kone bayad chand nokte ro bedonid
1 . behtar ast ke keyfiat dorbin(minimal 360p) va framerate(minimal 24) bala bashe
2 . sharayet norimonaseb bashad baraye mesal posht soje nor nabashad
3 . ta had emkan faghat khod fard controll konande dakhel kadr bashad

Powerd by
    alireza farghadani
    alirezaf999.iran@gmail.com
    09379062915
""")
input("TAB ENTER")
print(""" == config maker == 
khob inja chand ta chizro bayad tanzim konim ta barname 
behtarin karayish ro dashte bash ...

""")
fasele = int(input("-faseley khod ba dorbin ra be metr benevisid (hadeaaghal 1 metr): "))
mirror = input("-dorbin be sorat ayne hast? (y/n): ")=="y"
fix_val = round(20/fasele , 1)

with open("setting/track.txt", "w") as f:
    f.write(f"{mirror}\n{fix_val}")

with open("setting/Ui.txt", "w") as f:
    f.write(f" ")

if not os.path.isfile("setting/btn.txt"):
    with open("setting/btn.txt", "w") as f:
        for i in range(10):
            if i == 9:
                f.write(f'exit')
            elif i == 8:
                f.write(f'hide')
            elif i == 7:
                f.write(f'mouse')   
            else:
                f.write(f'echo "{i+1} (build by alireza farghadani)\n"')


with open("ui/end.txt", "w") as f:
    f.write(f"False")
with open("ui/mouse.txt", "w") as f:
    f.write(f"False")
with open("ui/val.txt", "w") as f:
    f.write(f"False")

if input("barname ro run bokonam? (y/n)") == "y":
    import hands_track