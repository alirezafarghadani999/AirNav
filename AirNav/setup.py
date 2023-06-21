import os

if not os.path.isdir("setting"):
    os.makedirs("setting")


if not os.path.isdir("Ui"):
    os.makedirs("Ui")
    

print("""
Salam mamnon hastam ke application man ro entekhab kardid 
baraye inke application be behtarin shekl kar kone bayad chand nokte ro bedonid
1. behtar ast ke keyfiat dorbin (minimal 360p) va framerate (minimal 24) bala bashe
2. sharayet norimonaseb bashad baraye mesal posht soje nor nabashad
3. ta had emkan faghat khod fard controll konande dakhel kadr bashad

Powerd by
    alireza farghadani
    alirezaf999.iran@gmail.com
    09379062915
""")
input("TAB ENTER")

print("""== config maker == 
khob inja chand ta chizro bayad tanzim konim ta barname 
behtarin karayish ro dashte bash ...
""")

fasele = int(input("-faseley khod ba dorbin ra be metr benevisid (hadeaaghal 1 metr): "))
mirror = input("-dorbin be sorat ayne hast? (y/n): ") == "y"
fix_val = round(20 / fasele, 1)

with open("setting/track.txt", "w") as f:
    f.write(f"{mirror}\n{fix_val}")

if not os.path.isfile("setting/btn.txt"):
    with open("setting/btn.txt", "w") as f:
        btn_options = ['echo "{} (build by alireza farghadani)"'.format(i + 1) for i in range(10)]
        btn_options[7] = 'mouse'
        btn_options[8] = 'hide'
        btn_options[9] = 'exit'
        f.write('\n'.join(btn_options))

with open("setting/Ui.txt", "w") as f:
    f.write(" ")

with open("Ui/end.txt", "w") as f:
    f.write("False")
with open("Ui/mouse.txt", "w") as f:
    f.write("False")
with open("Ui/val.txt", "w") as f:
    f.write("False")

if input("barname ro run bokonam? (y/n) ") == "y":
    import hands_track
