import mysql.connector as ct
from datetime import date
cnt=ct.connect(host="localhost",user="root",password="root",database="hotel")
if ct:
    print("Connected to mysql")
else:
    print("Not Able to connect.Retry")
    exit
r=cnt.cursor()

while True:
    print("*"*20,"Welcome of Hotel Menu","*"*20)
    print("[1] Customer Details")
    print("[2] Room Info")
    print("[3] Refreshment")
    print("[4] Bill")
    print("[5] Exit")


    cho=int(input("Enter your choice:"))
    if cho==1:
        while True:
            print("*"*20,"Booking","*"*20)
            print("[1] To Register new Customer record:")
            print("[2] To Remove existed Customer record:")
            print("[3]Exit to main menu:")
    

            y=int(input("Enter your choice:"))
            if y==1:
                name = input('Enter Customer Name:')
                address = input('Enter Customer Address:')
                phone = input('Enter Customer Phone NO:')
                id_proof = input('Enter Customer ID(Aadhar/Passport/DL/VoterID):')
                id_proof_no = input('Enter Customer ID proof NO:')
                total_customer=input('Enter number of Customers:')
                
                
                sql = 'insert into customer(name,address,phone,id_proof,id_proof_no,total_customer) values("'+name+'","' + address.upper()+'","'+phone+'","'+id_proof.upper()+'","'+id_proof_no.upper()+'",'+total_customer+');'
                r.execute(sql)
                cnt.commit()
                sql1='select * from customer where name="'+name+'";'
                r.execute(sql1)
                record=r.fetchall()
                result=record[0][0]
                print("Your ID is:",result)
                print('Customer Added successfully ...............')
                print("For room booking go to Room Info")

                
            if y==2:
                def customer_exist(room_no):
                    import mysql.connector
                    cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
                    r = cnt.cursor()
                    sql ="select * from customer where id ="+id+";"
                    r.execute(sql)
                    record = r.fetchone()
                    return record
                import mysql.connector
                cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
                r=cnt.cursor()
                id=input("Enter customer id:")
                room_no=input("Enter customer room no:")
                sql="delete from customer where id="+id+";"
                sql1="delete from booking where id="+id+";"
                sql2="update room set status='Free' where room_no="+room_no+";"
                result=customer_exist(id)
                if result is None:
                    r.execute(sql)
                    r.execute(sql1)
                    r.execute(sql2)
                    print("Customer does not exist in our database")
                    cnt.commit()
                if result is not None:
                    r.execute(sql)
                    r.execute(sql1)
                    r.execute(sql2)
                    cnt.commit()
                    print("Customer successfully removed from database")
            if y==3:
                break
    
        
        
    if cho==2:
        while True:
            print("[1] Room Preview:")
            print("[2] Room Booking:")
            print("[3] Cancel Booking:")
            print("[4] Exit to main menu:")
            z=int(input("Enter your choice:"))
            if z==1:
                sql ="select * from room"
                r.execute(sql)
                record = r.fetchall()
                for x in record:
                    print(x)
            if z==2:
        
                def customer_exist(id):
                    import mysql.connector
                    cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
                    r = cnt.cursor()
                    sql = "select * from customer where id ="+id+";"
                    r.execute(sql)
                    record = r.fetchone()
                    return record
                def room_exist(room_no):
                    import mysql.connector
                    cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
                    r = cnt.cursor()
                    sql ="select * from room where room_no ="+room_no+";"
                    r.execute(sql)
                    record = r.fetchone()
                    return record
    
                room_no =input('Enter room no to book :')
                id = input('Enter customer ID :')
                check_in_date = input('Enter date of occupancy (yyyy-mm-dd):')
                check_out_date = input('Enter date of leaving (yyyy-mm-dd):')
                sql1 = 'update room set status = "occupied" where room_no ='+room_no +';'
                sql2 = 'insert into booking(room_no,id,check_in_date,check_out_date) values ('+room_no+','+id+',"'+check_in_date+'","'+check_out_date+'");'
                result = room_exist(room_no)
                result1 = customer_exist(id)

                if result[4]=='Free' and result1 is not None: 
                    r.execute(sql1)
                    r.execute(sql2)
                    print('Room no', room_no, 'booked for', id)
                    cnt.commit()
                if result[4]!='Free':
                    print('Room is not available for booking. Right now it is booked:')
                    cnt.commit()
                if result1 is None:
                    print('Customer does not exist....Please add customer first in our database')
                    cnt.commit()
            if z==3:
                def Booking_exist(room_no):
                    import mysql.connector
                    cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
                    r = cnt.cursor()
                    sql ="select * from booking where room_no ="+room_no+";"
                    r.execute(sql)
                    record = r.fetchone()
                    return record
            
                import mysql.connector
                cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
                r=cnt.cursor()
                room_no=input("Enter your room number:")
                sql="delete from booking where room_no="+room_no+";"
                sql1="update room set status='Free' where room_no="+room_no+";"
                result=Booking_exist(room_no)
                if result is None:
                    r.execute(sql)
                    r.execute(sql1)
                    print("You have not booked your room")
                    cnt.commit()
                if result is not None:
                    r.execute(sql)
                    r.execute(sql1)
                    cnt.commit()
                    print("Your Booking Cancelled Successfully")
            if z==4:
                break

    if cho==3:
        while True:
            print("Welcome to Refreshment menu")
            print("[1] Refreshment Menu")
            print("[2] Exit to main menu")
            o=int(input("Enter your choice:"))
            if o==1:
                while True:
                    print("*"*20,"Available Food","*"*20)
                    print("[1] Tea ---> 10")
                    print("[2] Coffee ---> 15")
                    print("[3] Samosa --->10")
                    print("[4] Sandwich ---> 30")
                    print("[5] Colddrink ---> 20")
                    print("[6] Pasta ----> 40")
                    h=int(input("Enter your choice:"))
                    if h==1:
                        print("You have ordered Tea:")
                        b=int(input("Enter Quantity:"))
                        sum1=10*b
                        print("Your amountfor Tea:",sum1)
                    elif h==2:
                        print("You have ordered Coffee:")
                        b=int(input("Enter Quantity:"))
                        sum1=15*b
                        print("Your amountfor Coffee:",sum1)
                    elif h==3:
                        print("You have ordered Samosa:")
                        b=int(input("Enter Quantity:"))
                        sum1=10*b
                        print("Your amountfor Samosa:",sum1)
                    elif h==4:
                        print("You have ordered Sandwich:")
                        b=int(input("Enter Quantity:"))
                        sum1=30*b
                        print("Your amountfor Sandwich:",sum1)
                    elif h==5:
                        print("You have ordered Colddrink:")
                        b=int(input("Enter Quantity:"))
                        sum1=20*b
                        print("Your amountfor Colddrink:",sum1)
                    elif h==6:
                        print("You have ordered Pasta:")
                        b=int(input("Enter Quantity:"))
                        sum1=40*b
                        print("Your amountfor Pasta:",sum1)
                    else:
                        print("please enter your choice from the menu")
                    u=input("Do you want to order more?[Y/N]:")
                    if u=='n':
                        break
            
            if o==2:
                break
            
    if cho==4:
        print("[1]Room bill:")
        print("[2]Exit to main menu:")
        n=int(input("Enter your choice"))
        if n==1:
            def room_exist(room_no):
                import mysql.connector
                cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
                r = cnt.cursor()
                sql ="select * from room where room_no ="+room_no+";"
                r.execute(sql)
                record = r.fetchone()
                return record
            import mysql.connector
            cnt = mysql.connector.connect(host='localhost', database='hotel', user='root', password='root')
            r = cnt.cursor()
            room_no = input('Enter your room :')
            id = input('Enter customer ID :')
            bill_no=input("Enter Customer Bill No.")
            sql = "select * from booking where id="+id+" and room_no = "+room_no+";"
            r.execute(sql)
            record = r.fetchone()
            print('Bill Generation ')
            print('-'*100)
            check_in_date = record[2]
            check_out_date = record[3]
            total_days = (check_out_date-check_in_date).days
            result = room_exist(room_no)
            rent = result[3]
            amount = total_days*rent
            print('Date of Occupancy :',check_in_date, '\nDate of Leaving :',check_out_date)
            print('Total Payable Days : ', total_days)
            print('Room Rent Per Day : ', rent)
            print('Total Amount  :',amount)
            sql1 = 'update room set status ="free" where room_no ='+room_no+';'
            sql2 = 'insert into bill(bill_no,id,total_amount) values('+str(bill_no)+','+str(id)+','+str(amount)+');'
            r.execute(sql1)
            r.execute(sql2)
            cnt.commit()
        if n==2:
            print("******************************Thanks For Visiting Please Visit Again******************************")
            break
    if cho==5:
        break
              
