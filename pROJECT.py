''import mysql.connector as sql
conob = sql.connect(host="localhost",user = "root",passwd = "root",database="dtvs")
if sql:
    print("SUCCESSFULLY CONNECTED TO MySQL DATABASE")
else:
    print("COULD NOT CONNECT TO MySQL DATABASE....TRY AGAIN")
    exit
cur=conob.cursor()
ch = 1
c=3
while ch>=1 and ch<=5:
    print("\n"*2)
    print("<"*40,'SELECTION TABLE',">"*40)
    print("[1] ADD A NEW RECORD")
    print("[2] VIEW A RECORD")
    print("[3] UPDATE A RECORD")
    print("[4] DELETE A RECORD")
    print("[5] EXIT")
    print("<"*40,'SELECTION TABLE',">"*40)
    ch = int(input("ENTER CHOICE HERE: "))
    if ch==1:
        # TO ADD A RECORD WE MUST FIRST ASK WHERE DOES THE USER WANT TO ADD RECORD AND CHECK IF A RECORD ALREADY EXISTS
        comm = "select * from tdtvs"
        data = cur.execute(comm)
        r_no = []
        for i in data:
            r_no.append(i[0])
        choice = 1
        d = 3
        print("\n"*2)
        print("<"*40,'SELECTION TABLE',">"*40)
        print("[1] TO ADD PERSONAL DETAILS OF THE STUDENT")
        print('[2] TO ADD VACCINATION DETAILS OF THE STUDENT')
        print("[3] TO EXIT TO MAIN MENU")
        print("<"*40,'SELECTION TABLE',">"*40)
        while choice:
            choice = int(input("ENTER YOUR CHOICE :"))
            if choice == 1:
                admno = int(input("ENTER THE ADMISSION NUMBER(4 DIGITS): "))
                clas= input("ENTER THE CURRENT CLASS OF THE STUDENT:- ")
                name = input("ENTER THE NAME OF THE STUDENT(WITHIN 20 CHARACTERS) : ")
                gender = input(" ENTER THE GENDER (M/F/O): ")
                mobile_no = input("ENTER THE MOBILE NUMBER : ")
                guardian_name = input("ENTER THE GUARDIAN NAME(WITHIN 30 CHARACTERS) : ")
                if admno in admno:
                    print("ANOTHER RECORD WITH SAME SCHOLAR NUMBER EXIST")
                    break
                else:
                    st = "insert into tdtvs(admno,clas,name,gender,mobile_no,guardian_name) values({},'{}','{}','{}','{}')",format(admno,clas,name,gender,mobile_no,guardian_name)
                    cur.execute(st)
                    conob.commit()
                    more = input('DO YOU WANT TO ADD MORE RECORDS[Y/N]: ')
                    if more =="y" or "Y":
                        choice = 1
                    else :
                        break               
            elif choice == 2:
                admno = int(input("ENTER THE ADMISSION NUMBER(4 DIGITS): "))
                first_dose= input("ENTER [Y/N] FOR FIRST DOSE: ")
                first_dose_date = input("ENTER THE DATE OF FIRST DOSE(YYYY-MM-DD): ")
                second_dose = input("ENTER [Y/N] FOR SECOND DOSE: "))
                second_dose_date = int(input(": "))
                additional_dose = int(input("ENTER THE ROLLNUMBER(4 DIGITS): "))
                if r_no2 in r_no:
                    print("ANOTHER RECORD WITH SAME SCHOLAR NUMBER EXIST")
                    break
                else:
                    st = "insert into acad(sch,test,subject,marks,max_marks) values({},'{}',{},{})",format(r_no2,term,subject,marks,max_marks)
                    cur.execute(st)
                    conob.commit()
                    more = input('DO YOU WANT TO ADD MORE RECORDS[Y/N]: ')
                    if more =="y" or "Y":
                        choice = 1
                    else :
                        break
            elif choice ==3:
                break
            else:
                d-=1
                if d>0:
                    print("ENTER A VALID CHOICE...[",d,"]TRIE(S) LEFT")
                    continue
                else:
                    print("SORRY YOU DID NOT INPUT A VALID CHOICE")
                    
    elif ch==2:
        rec = 1
        r = 3
        while rec>=1 and rec<=5:
            print("\n"*5)
            print("<"*40,'SELECTION TABLE',">"*40)
            print("[1] VIEW RECORDS IN INCREASING ORDER OF ADMISSION NUMBERS")
            print("[2] VIEW RECORDS IN ORDER OF MARKS")
            print("[3] VIEW RECORDS IN ALPHABETICAL ORDER OF NAME")
            print("[4] VIEW A PARTICULAR RECORD OF ANY STUDENT")
            print("[5] EXIT TO MAIN MENU")
            print("<"*40,'SELECTION TABLE',">"*40)
            rec = int(input("ENTER CHOICE HERE: "))
            if rec == 1:
                st = "select * from sturec group by sch"
                cur.execute(st)
            elif rec == 2:
                test = input("ENTER THE TEST TERM[PT-1]/[PT-2]: ")
                subj = input("ENTER THE SUBJECT[ENG/PHY/CHEM/MATH/BIO/PHE/CSC/PHE]: ")
                if test not in ["PT-1", "PT-2"]:
                    exit
                if subj.lowercase() not in ["eng","phy","che","math","bio","csc","phe"]:
                    exit
                st = "select sch,name,marks from ultimate where subject='{}' and test='{}' order by marks desc",format(subject,test)
                cur.execute(st)
            elif rec == 3:
                st = "select * from sturec order by name asc"
                cur.execute(st)
            elif rec == 4:
                print("\n"*2)
                print("<"*40,'SELECTION TABLE',">"*40)
                print("[1] TO SEE PERSONAL DETAILS OF A STUDENT")
                print('[2] TO SEE ACADEMIC DETAILS OF A STUDENT')
                print("[3] TO EXIT TO MAIN MENU")
                print("<"*40,'SELECTION TABLE',">"*40)
                selection = input("ENTER CHOICE HERE: ")
                if selection == 1:
                    sch1 = int(input("ENTER THE SCH NUMBER(4 DIGITS): "))
                    field = input("ENTER THE FIELD NAME VARCHAR(10): ")
                    st = "select '{}' from sturec where sch1 = {}",format(field,sch1)
                    cur.execute(st)
                elif selection == 2:
                    sch1 = int(input("ENTER THE SCH NUMBER(4 DIGITS): "))
                    test = input("ENTER THE TEST TERM[PT-1]/[PT-2]: ")
                    subj = input("ENTER THE SUBJECT[ENG/PHY/CHEM/MATH/BIO/PHE/CSC/PHE]: ")
                    st = " select sch,name,marks from ultimate where sch={}and test='{}'and subject='{}'",format(sch1,test,subj)
                    cur.execute(st)
                if test not in ["PT-1", "PT-2"]:
                    exit
                if subj.lowercase() not in ["eng","phy","che","math","bio","csc","phe"]:
                    exit
            elif rec == 5:
                break
            else :
                r-=1
                if r>0:
                    print("ENTER A VALID NUMBER...[",r,"]TRIE(S) LEFT")
                    rec=1
                else:
                    print("SORRY YOU DID NOT INPUT A VALID NUMBER")
    elif ch==3:
        print("\n"*2)
        print("<"*40,'SELECTION TABLE',">"*40)
        print("[1] TO UPDATE PERSONAL DETAILS OF A STUDENT")
        print('[2] TO UPATE ACADEMIC DETAILS OF A STUDENT')
        print("[3] TO EXIT TO MAIN MENU")
        choice = 1
        d = 3
        while choice:
            choice = int(input("ENTER YOUR CHOICE :"))
            if choice == 1:
                sch1 = int(input("ENTER THE SCH NUMBER(4 DIGITS): "))
                field = input("ENTER WHAT DO YOU WANT TO UPDATE:[NAME/GEN/DOB{YYYY/MM/DD}/RESIDENCE] ")
                new = input("ENTER THE NEW DATA: ") # SHOULD I CREATE IF /ELSE IF THE DTATATYPE IS NUMERICAL BECAUSE INPUT IS RECEIVED IN STRING
                if sch1 not in r_no:
                    print("THE SCHOLAR NUMBER DOES NOT EXIST")
                    break
                if field not in ["NAME","GEN","DOB","RESIDENCE","name","gen","dob","resdience"]:
                    print("THE FIELD DOES NOT EXIST")
                    break   
                at = "UPDATE sturec set {} = {} where sch = {}",format(field,new,sch1)
                cur.execute(at)
                conob.commit()
                more = input('DO YOU WANT TO UPDATE MORE RECORDS[Y/N]: ')
                if more =="y" or "Y":
                    continue
                else :
                    break
            elif choice == 2:
                sch1 = int(input("ENTER THE SCH NUMBER(4 DIGITS): "))
                test = input("ENTER THE TEST TERM[PT-1]/[PT-2]: ")
                subj = input("ENTER THE SUBJECT[ENG/PHY/CHEM/MATH/BIO/PHE/CSC/PHE]: ")
                marks = input("ENTER NEW MARKS HERE: ")
                if sch1 not in r_no :
                    print("RECORD DOESN'T EXIST...TRY AGAIN")
                    break
                if test not in ["PT-1", "PT-2"]:
                    print("INVALID TEST INPUTTED...TRY AGAIN")
                    break
                if subj.lowercase() not in ["eng","phy","che","math","bio","csc","phe"]:
                    print("INPUTTED SUBJECT DOES NOT EXIST...TRY AGAIN")
                    break 
                at = " update acad set marks = {} where sch = {} and test ='{}' and subject = '{}'",format(marks,sch1,test,subj)
                cur.execute(at)
                conob.commit()
                more = input('DO YOU WANT TO UPDATE MORE RECORDS[Y/N]: ')
                if more =="y" or "Y":
                    continue
                else :
                    break
            elif choice ==3:
                break
            else:
                d-=1
                if d>0:
                    print("ENTER A VALID CHOICE...[",d,"]TRIE(S) LEFT")
                    continue
                else:
                    print("SORRY YOU DID NOT INPUT A VALID CHOICE")
    elif ch == 4:
        print("\n"*2)
        print("<"*40,'SELECTION TABLE',">"*40)
        print("[1] TO VIEW PERSONAL DETAILS OF A STUDENT")
        print('[2] TO VIEW ACADEMIC DETAILS OF A STUDENT')
        print("[3] TO EXIT TO MAIN MENU")
        print("<"*40,'SELECTION TABLE',">"*40)
        choice = 1
        d = 3
        while choice:
            choice = int(input("ENTER YOUR CHOICE :"))
            if choice == 1:
                sch1 = int(input("ENTER THE SCH NUMBER(4 DIGITS): "))
                field = input("ENTER WHAT DO YOU WANT TO DISPLAY[NAME/GEN/DOB{YYYY/MM/DD}/RESIDENCE]: ")
                at = "select {} from sturec where sch = {}",format(field,sch1)# A POSSIBLE ERROR MAY BE GENERATED BECAUSE OF DIFFERENT DATATYPES
                cur.execute(at)
                more = input('DO YOU WANT TO UPDATE MORE RECORDS[Y/N]: ')
                if more =="y" or "Y":
                    continue
                else :
                    break
            elif choice == 2:
                sch1 = int(input("ENTER THE SCH NUMBER(4 DIGITS): "))
                test = input("ENTER THE TEST TERM[PT-1]/[PT-2]: ")
                subj = input("ENTER THE SUBJECT[ENG/PHY/CHEM/MATH/BIO/PHE/CSC/PHE]: ")
                marks = input("ENTER NEW MARKS HERE: ")
                if sch1 not in r_no :
                    print("RECORD DOESN'T EXIST...")
                    break
                if test not in ["PT-1", "PT-2"]:
                    print("INVALID TEST INPUTTED...TRY AGAIN")
                    break
                if subj.lowercase() not in ["eng","phy","che","math","bio","csc","phe"]:
                    print("INPUTTED SUBJECT DOES NOT EXIST...TRY AGAIN")
                    break  
                at = " SELECT marks from acad where sch={} and test='{}' and subject = '{}'",format(sch1,test,subj)
                cur.execute(at)
                more = input('DO YOU WANT TO UPDATE MORE RECORDS[Y/N]: ')
                if more =="y" or "Y":
                    continue
                else :
                    break
            elif choice ==3:
                break
            else:
                d-=1
                if d>0:
                    print("ENTER A VALID CHOICE...[",d,"]TRIE(S) LEFT")
                    continue
                else:
                    print("SORRY YOU DID NOT INPUT A VALID CHOICE") 
    elif ch== 5:
        exit
    else :
        c -=1
        if c>0:
            print("PLEASE ENTER A VALID NUMBER....[",c,"]TRIES LEFT")
            ch = 1
        else:
            print("SORRY YOU DID NOT INPUT A VALID CHOICE")
