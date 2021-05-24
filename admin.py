from jsonio import *
from quiz import *


def display_admin_menu():
    print("\t\tADMIN SECTION ")
    print()
    print("\tENTER 1 - NEW QUIZ")
    print("\tENTER 2 - UPDATE QUIZ")
    print("\tENTER 3 - DELETE QUIZ")
    print("\tENTER 4 - LIST OF QUIZ")
    print("\tENTER 5 - RETURN TO MAIN MENU")
    
    ch=input("\tENTER YOUR CHOICE : ")
    print()
    print("="*48)
    return ch

def admin_section():
    choice=''
    while choice != '5':    

        choice = display_admin_menu()

        # Respond to the user's choice.

        if choice == '1':
            new_quiz()
        elif choice == '2':
            update_quiz()
        elif choice == '3':
            del_quiz()
        elif choice == '4':
            show_quiz()
        elif choice == '5':
            return

        else:
            print("\n\tDIDN'T UNDERSTAND THAT CHOICE\n")
            print("="*48)

def new_quiz():
    print()
    sub=input("\tENTER SUBJECT : ")
    d=read_questions()
    if d!=0 and d!={}:
        d.update({sub:{}})
    else:
        d={}
        d[sub]={}
    write_questions(d)
    print("\n\tNEW QUIZ CREATED")
    print("="*48)
    quiz_section(sub)
    
def update_quiz():
    print()
    sub=input("\tENTER SUBJECT : ")
    d=read_questions()
    if d!=0 and d!={}:
        if sub in d.keys():
            quiz_section(sub)
        else:
            print("\n\tENTER VALID SUBJECT")
    else:
        print("\n\tNO QUIZ\n")
        print("="*48)
    
def del_quiz():
    print()
    sub=input("\tENTER SUBJECT : ")
    d=read_questions()
    if sub in d.keys():
        d.pop(sub,None)
        write_questions(d)
    else:
        print("\n\tENTER VALID SUBJECT")
    return
def show_quiz():
    d=read_questions()
    if d!=0 and d!={}:
        print("\n\t\tQUIZ LIST")
        for i in d.keys():
            print("\n\tQUIZ SUBJECT : ",i)
    else:
        print("\n\tNO QUIZ\n")
    print("="*48)
