import sys
import mysql.connector
mycon=mysql.connector.connect(host='localhost',user='root', password='renn',database='exams')          
mycur = mycon.cursor()
def Student_Profile():
    sql="Insert into student(adm_no,name,class,section)values(%s,%s,%s,%s)"
    print('\nPLEASE PROVIDE THE REQUIRED INFORMATION\n')
    ad=input('\nENTER THE ADMISSION NUMBER TO REGISTER FOR EXAM:')
    nm=input('\nENTER THE STUDENT NAME:')
    cls=int(input('\nENTER THE CLASS(11/12):'))
    sec=input('\nENTER THE SECTION(A-D):')			
    value=(ad,nm,cls,sec)
    try:
        mycur.execute(sql,value)
        print(nm,'ADDED SUCCESSFULLY TO EXAM MODULE')
        mycon.commit()
    except:
        print('UNABLE TO INSERT!!!!!')

def Edit_Profile():
    sql="Update student set section=%s where adm_no=%s";
    ph=input('\nENTER THE ADMISSION NUMBER WHOSE SECTION TO MODIFY:')
    nm=input('\nENTER THE NEW SECTION(A-D):')
    value=(nm,ph)
    try:
        mycur.execute(sql,value)
        mycon.commit()
        print('RECORD UPDATED SUCCESSFULLY')
    except:
        print('UNABLE TO UPDATE SECTION!!!!')

def Remove_Profile():
    ph=input('\nENTER THE ADMISSION NUMBER TO DELETE:')
    sql='Delete from student where Adm_no=%s'
    value=(ph,)
    try:
        mycur.execute(sql,value)
        mycon.commit()
        print('RECORD DELETED SUCCESSFULLY')
    except:
        mycon.rollback()
        print('UNABLE TO DELETE RECORD!!!')

def Record_Entry():
    sql="Insert into result(adm_no,exam_name,sub1,sub2,sub3,sub4,sub5,total,percentage,attendance,grade,remarks)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    print('\nPLEASE PROVIDE THE REQUIRED INFORMATION\n')
    ad=int(input('\nENTER THE ADMISSION NUMBER TO ENTER RECORD:'))
    sec=input("ENTER SECTION :")
    nm=input('\nENTER THE EXAM NAME:')
    if sec=="A":
        print("SECTION : A  SUBJECT1: ENGLISH,SUBJECT2:CHEMISTRY,SUBJECT3:PHYSICS,SUBJECT4:MATHS,SUBJECT5:C.S")
    elif sec=="B":
        print("SECTION : B  SUBJECT1: ENGLISH,SUBJECT2:HISTORY,SUBJECT3:POL. SC,SUBJECT4:ECONOMICS,SUBJECT5:GEOGRAPHY")
    elif sec=="C":
        print("SECTION : C  SUBJECT1: ENGLISH,SUBJECT2:ACCOUNTANCY,SUBJECT3:B. ST,SUBJECT4:ECONOMICS,SUBJECT5:MATHS")
    else:
        print("SECTION : D  SUBJECT1: ENGLISH,SUBJECT2:PHYSICS,SUBJECT3:BIOLOGY,SUBJECT4:CHEMISTRY,SUBJECT5:MATHS")

    sub1=int(input('ENTER MARKS IN SUBJECT 1(MAX:100):'))
    sub2=int(input('ENTER MARKS IN SUBJECT 2(MAX:100):'))
    sub3=int(input('ENTER MARKS IN SUBJECT 3(MAX:100):'))
    sub4=int(input('ENTER MARKS IN SUBJECT 4(MAX:100):'))
    sub5=int(input('ENTER MARKS IN SUBJECT 5(MAX:100):'))
    total=sub1+sub2+sub3+sub4+sub5
    per=total//5
    wrkday=int(input('ENTER TOTAL NUMBER OF WORKING DAYS:'))
    present=int(input('ENTER NO OF DAYS PRESENT:'))
    att=present/wrkday*100
    att=int(att)
    if(per>=90):
        g='A'
        rem='EXCELLENT PERFORMANCE!!'
    elif(per>=75 and per<90):
        g='B'
        rem='VERY GOOD PERFORMANCE!!'
    elif(per>=55 and per<=75):
        g='C'
        rem='SATISFACTORY PERFORMANCE!!'
    elif(per>=35 and per<55):
        g='D'
        rem='AVERAGE PERFORMANCE!!'
    else:
        g='E'
        rem='SCOPE FOR IMPROVEMENT!!'
    value=(ad,nm,sub1,sub2,sub3,sub4,sub5,total,per,att,g,rem)
    print(value)
    try:
        mycur.execute(sql,value)
        print('RECORD ADDED SUCCESSFULLY TO EXAM MODULE')
        mycon.commit()        
    except:
        print('UNABLE TO INSERT!!!!!')


def Report_Card():
    ad=int(input('\nENTER THE ADMISSION NUMBER TO SEARCH:'))
    sql1='Select * from student where adm_no=%s'
    value=(ad,)
    mycur.execute(sql1,value)
    rec1=mycur.fetchone()
    if(rec1!=None):
          adm=rec1[0]
          name=rec1[1]
          cls=rec1[2]
          sec=rec1[3]
    sql2='Select * from result where adm_no=%s'
    value=(ad,)
    mycur.execute(sql2,value)
    rec2=mycur.fetchone()
    if(rec2!=None):
        adm=rec2[0]
        exname=rec2[1]
        sub1=rec2[2]
        sub2=rec2[3]
        sub3=rec2[4]
        sub4=rec2[5]
        sub5=rec2[6]
        total=rec2[7]
        per=rec2[8]
        att=rec2[9]
        g=rec2[10]
        rem=rec2[11]
        if(rec1==None and rec2==None):
            print('WRONG ADMISSION NUMBER GIVEN!!!!!!')
        else:
            print("===========================================")
            print('*******REPORT CARD OF ',exname,'*******')
            print("===========================================")
            print('Name : ',name,'  ' ,'CLASS -',cls,' SECTION-',sec)
            print('------------------------------------------')

            if(sec=='A'):
                print("     SUBJECT       MARKS")
                print("------------------------------------------")
                print('     ENGLISH    : ',sub1)
                print('     CHEMISTRY  : ',sub2)
                print('     PHYSICS    : ',sub3)
                print('     MATHS      : ',sub4)
                print('     C. S       : ',sub5)
                print("------------------------------------------")
                print('TOTAL      : ',total,'  PERCENTAGE : ',per)
                print("------------------------------------------")
                print('ATTENDANCE : ',att,'%','  GRADE      : ',g)
                print('REMAKS     : ',rem)
                print("------------------------------------------")
            elif(sec=='B'):
                print("     SUBJECT       MARKS")
                print("------------------------------------------")
                print('ENGLISH    : ',sub1)
                print('HISTORY : ',sub2)
                print('POL. SC.  : ',sub3)
                print('ECONOMICS  : ',sub4)
                print('GEOGRAPHY  : ',sub5)
                print("------------------------------------------")
                print('TOTAL      : ',total,'  PERCENTAGE : ',per)
                print("------------------------------------------")
                print('ATTENDANCE : ',att,'%','  GRADE      : ',g)
                print('REMAKS     : ',rem)
                print("----------------------------------------")
            elif(sec=='C'):
                print("     SUBJECT       MARKS")
                print("------------------------------------------")
                print('\n ENGLISH    : ',sub1)
                print('\n ACCOUNTANCY    : ',sub2)
                print('\n B. SC    : ',sub3)
                print('\n ECONOMICS  : ',sub4)
                print('\n MATHEMATICS: ',sub5)
                print("------------------------------------------")
                print('TOTAL      : ',total,'  PERCENTAGE : ',per)
                print("------------------------------------------")
                print('ATTENDANCE : ',att,'%','  GRADE      : ',g)
                print('REMAKS     : ',rem)
                print("----------------------------------------")


            elif(sec=='D'):
                print("------------------------------------------")
                print('\n ENGLISH    : ',sub1)
                print('\n PHYSICS    : ',sub2)
                print('\n BIO    : ',sub3)
                print('\n CHEMISTRY  : ',sub4)
                print('\n MATHEMATICS: ',sub5)
                print("------------------------------------------")
                print('TOTAL      : ',total,'  PERCENTAGE : ',per)
                print("------------------------------------------")
                print('ATTENDANCE : ',att,'%','  GRADE      : ',g)
                print('REMAKS     : ',rem)
                print("----------------------------------------")

def Remove_Record():

    n=int(input('Enter STUDENT number to delete:'))
    mycur.execute('SELECT * FROM RESULT WHERE adm_NO=%s'%(n,))
    d=mycur.fetchone()
    if d!=None:
        query='DELETE FROM RESULT WHERE ADM_NO=%s'%(n,)
        mycur.execute(query)
        mycon.commit()
        print('RECORDED DELETED!')
    else:
        print('NO SUCH STUDENT IS FOUND!')



def Close():
    print('\nTHANK YOU FOR USING THE APPLICATION')
    sys.exit()             



print("-------------------------------------------------------------------------")
print('**********RANGAPAHAR EXAMINATION SYSTEM FOR CLASS-XI & XII***************')
print("-------------------------------------------------------------------------")
while(True):
    print()
    print('1. TO CREATE A STUDENT PROFILE')
    print('2. TO EDIT A STUDENT PROFILE')
    print('3. TO DELETE A STUDENT PROFILE')
    print('4. FOR MARKS AND ATTENDANCE ENTRY')
    print('5. TO GENERATE REPORT CARD')
    print('6. TO DELETE MARKS DETAILS')
    print('7. TO CLOSE THE APPLICATION')
    print("-------------------------------------------------------------------------")
    choice=int(input('ENTER YOUR CHOICE : '))
    if(choice==1):
        Student_Profile()
    elif(choice==2):
        Edit_Profile()
    elif(choice==3):
        Remove_Profile()
    elif(choice==4):
        Record_Entry()
    elif(choice==5):
        Report_Card()
    elif(choice==6):
        Remove_Record()
    elif(choice==7):
        Close()
