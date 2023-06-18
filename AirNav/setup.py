import os
import sys

print("""
Salam mamnon hastam ke application man ro entekhab kardid 
baraye inke application be behtarin shekl kar kone bayad chand nokte ro bedonid
1 . behtar ast ke keyfiat dorbin(minimal 360p) va framerate(minimal 24) bala bashe
2 . sharayet norimonaseb bashad baraye mesal posht soje nor nabashad
3 . ta had emkan faghat khod fard controll konande dakhel kadr bashad
""")
input("TAB ENTER")
print(""" == config maker == 
khob inja chand ta chizro bayad tanzim konim ta barname 
behtarin karayish ro dashte bash ...

""")
fasele = int(input("-faseley khod ba dorbin ra be metr benevisid (hadeaaghal 1 metr): "))
mirror = input("-dorbin be sorat ayne hast? (y/n): ")=="y"
fix_val = round(20/fasele , 1)
print(fix_val,mirror)

