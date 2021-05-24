from jsonio import *
from classes.QuestionClass import *

def display_quiz_menu():
    print("\t\tQUIZ SECTION ")
    print()
    print("\tENTER 1 - SHOW ALL QUESTIONS")
    print("\tENTER 2 - ADD QUESTION")
    print("\tENTER 3 - DELETE QUESTION")
    print("\tENTER 4 - RETURN TO QUIZ MENU")
    
    ch=input("\tENTER YOUR CHOICE : ")
    print()
    print("="*48)
    return ch

def quiz_section(sub):
    choice=''
    while choice != '4':    

        choice = display_quiz_menu()

        if choice == '1':
            show_all_questions(sub)
        elif choice == '2':
            add_question(sub)
        elif choice == '3':
            delete_question(sub)
        elif choice == '4':
            return

        else:
            print("\n\tDIDN'T UNDERSTAND THAT CHOICE\n")
            print("="*48)

def add_question(sub):
    print()
    prompt=input("\tENTER QUESTION :")
    option1=input("\tENTER OPTION A : ")
    option2=input("\tENTER OPTION B : ")
    option3=input("\tENTER OPTION C : ")
    option4=input("\tENTER OPTION D : ")
    answer=input('''\tENTER ANSWER (A:B:C:D) : ''')
    difficulty=input("\tENTER DIFFICULTY : ")
    print()
    print("="*48)
    
    d=read_questions()
    data=d[sub]
    question=Question(prompt,option1,option2,option3,option4,answer,difficulty)
    if data!=0 and data!={}:
        m=int(max(data))
        data[m+1]=question.__dict__
    else:
        data={}
        data[1]=question.__dict__
    d.update({sub:data})
    write_questions(d)
        
    return 

def delete_question(sub):
    show_all_questions(sub)
    print()
    id=input("\tENTER ID :")
    d=read_questions()
    data=d[sub]
    data.pop(id,None)
    print("\t\tQUESTION DELETED")
    print()
    print('='*48)
    d.update({sub:data})
    write_questions(d)
    return

def show_all_questions(sub):
    d=read_questions()
    data=d[sub]
    if data:
        print()
        print("\t\tQUESTION LIST")
        print()
        for i,j in data.items():
            print()
            print("\tID : ",i)
            print("\tQUE :",j['prompt'])
            print("\tOPTION A :",j['option1'])
            print("\tOPTION B :",j['option2'])
            print("\tOPTION C :",j['option3'])
            print("\tOPTION D :",j['option4'])
            print("\tANSWER : ",j['answer'])
            print("\tDIFFICULTY : ",j['difficulty'])
            print()
            print("="*48)
    else:
        print()
        print("\t\tNO QUESTIONS ADDED")
        print()
        print("="*48)
    return
