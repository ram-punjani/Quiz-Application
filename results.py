from jsonio import *

def student_result():
    print()
    sub=input("\tENTER SUBJECT :")
    d=read_students()
    if sub not in d.keys():
        print("\n\t\t NO DATA\n")
        print("="*48)
        return
    else:
        data=d[sub]
        if data:
            print()
            print("\t\tSTUDENT LIST")
            print()
            for i,j in data.items():
                print()
                print("\tID : ",i)
                print("\tNAME :",j['name'])
                print("\tSCORE :",j['score'])
                print()
                print("="*48)
        else:
            print("\n\t NO DATA\n")
            print("="*48)
