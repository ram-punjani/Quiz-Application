from jsonio import *
from classes.StudentClass import *





def display_student_section():
    print("\t\tSTUDENT SECTION ")
    print()
    print("\tENTER 1 - TAKE QUIZ")
    print("\tENTER 2 - RETURN TO MAIN MENU")
    
    ch=input("\tENTER YOUR CHOICE : ")
    print()
    print("="*48)
    return ch

def student_section():
    choice=''
    score=0
    while choice!=2:
        choice=display_student_section()
              
        if choice == '1':
            d=read_questions()
            if d==0 or d=={}:
                print("\n\t NO QUIZ\n")
                print("="*48)
                choice=3
            else:
                take_quiz()
        elif choice == '2':
            return

        else:
            print("\n\tDIDN'T UNDERSTAND THAT CHOICE\n")
            print("="*48)

            
            
def take_quiz():
    print()
    sub=input("\tENTER SUBJECT :")
    d=read_questions()
    if sub not in d.keys():
        print("\n\t ENTER VALID SUBJECT")
        print("="*48)
        return
    else:
        student_menu(sub)

def student_menu(sub):
    print("\t\tSTUDENT DETAILS ")
    print()
    name=input("\tENTER NAME : ")
    gender=input("\tENTER GENDER : ")
    print()
    print("="*48)
    score=0
    id=1
    student=Student(name,gender,score)
    d=read_students()
    if d!=0 and d!={}:
        
        if sub in d.keys():
            data=d[sub]
            m=int(max(data))
            data[m+1]=student.__dict__
            id=m+1
        else:
            data={}
            data[1]=student.__dict__
        d[sub]=data
    else:
        data={}
        d={}
        data[1]=student.__dict__
        d[sub]=data
    id=str(id)
    write_students(d)
    quiz(sub,id)
    return

def quiz(sub,id):
    d=read_questions()
    data=d[sub]
    q=0
    score=0
    if data:
        print("\n\t QUESTION LIST\n")
        for i,j in data.items():

            print()
            print("\tQ :",j['prompt'])
            print("\tA :",j['option1'])
            print("\tB :",j['option2'])
            print("\tC :",j['option3'])
            print("\tD :",j['option4'])
            print()
            ans=input('''\tENTER ANSWER (A:B:C:D) : ''')
            q=q+1
            if ans==j['answer'] :
                print()
                print("\n\tCORRECT\n")
                print("="*48)
                score=score+1
            else:
                print()
                print("\n\tINCORRECT\n")
                print("\tCORRECT OPTION IS :",j['answer'])
                print("="*48)

        score=(score/q)*100
        d=read_students()
        data2=d[sub]
        data2[id]['score']=score
        d.update({sub:data2})
        write_students(d)
        return
    else:
        print("\n\t\tNO QUESTIONS ADDED\n")
        print("="*48)
