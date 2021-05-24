from admin import *
from student import *
from results import *




def display_title_bar():
    print()
    print("="*48)
    print("\t\tQUIZ APPLICATION ")
    print('='*48)
    return

def main_menu():
    print("\n\t\tMAIN MENU \n")
    print("\tENTER 1 - ADMIN SECTION")
    print("\tENTER 2 - STUDENT SECTION")
    print("\tENTER 3 - STUDENTS RESULTS")
    print("\tENTER 4 - EXIT")
    ch=input("\tENTER YOUR CHOICE : ")
    print("="*48)
    return ch

def main():
    display_title_bar()

    choice = ''

    while choice!='4':    

        choice = main_menu()

        if choice == '1':
            admin_section()
        elif choice == '2':
            student_section()
        elif choice == '3':
            student_result()
        elif choice == '4':
            pass
        else:
            print("\n\tDIDN'T UNDERSTAND THAT CHOICE\n")
            print("="*48)

    print('\t\tThanks')
    
if __name__=='__main__':
    main()

