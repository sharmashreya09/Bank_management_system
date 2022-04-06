#connect sql to python

import mysql.connector as s
mydb = s.connect(host = "localhost", user = "root", password = "abbtpoipiupo", database = "bank")

if mydb.is_connected:
                print("-"*20, "BANK MANAGEMENT SYSTEM", "-"*20)
                print("*"*64)
else:
                print("Not Connected!")

#function for main menu 

def main():
                print("""
                        ----*MAIN MENU*----
                        
                1. Create New Bank Acount
                2. Deposit Money
                3. Withdraw Money
                4. Transfer Money
                5. Display Account Informantion
                6. Show All Records
                7. Update Information
                8. Close An Account

                Press 0 to exit.
                """)

                choice = input("""
                                What would you like to do?
                                Enter your choice: """)

                if choice == "1":
                                createacc()
                if choice == "2":
                                deposit()
                if choice == "3":
                                withdraw()
                if choice == "4":
                                transfer()
                if choice == "5":
                                display()
                if choice == "6":
                                records()
                if choice =="7":
                                modify()
                if choice == "8":
                                close()
                if choice == "0":
                                exit()
                else:
                                print("Invalid Choice")
                                main()

#function for create account

def createacc():
                fname = input("Enter First Name: ")
                lname = input("Enter Last Name: ")
                acno  = int(input("Enter Account Number: "))
                dob   = input("Enter Date Of Birth: ")
                gen   = input("Enter Gender (F/M/T): ")
                add   = input("Enter Address: ")
                phno  = input("Enter Phone Number: ")
                mail  = input("Enter E-mail id: ")
                ob    = int(input("Enter Opening Balance"))
                pin   = input("Enter your Pin: ")

                val1 = (fname, lname, acno, dob, gen, add, phno, mail, ob)
                val2 = (fname, lname, acno, ob)
                val3 = (acno, ob, pin)

                sql1 = 'insert into account values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'           #inserting values in account table
                
                sql2 = 'insert into ammount values(%s,%s,%s,%s)'                          #inserting values in ammount table
                
                sql3 = 'insert into money values(%s,%s,%s)'                               #inserting values in money table

                mycursor = mydb.cursor()                                                  #importing cursor
                
                mycursor.execute(sql1, val1)
                mycursor.execute(sql2, val2)
                mycursor.execute(sql3, val3)

                mydb.commit()                                                             #commiting data

                print("Account Created Successfully!")

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()
                                
                

#function for depostion of money


def deposit():
                acc   = input("Enter Account Noumber: ")
                fname = input("Enter First Name:")
                lname = input("Enter Last Name:")
                amm   = int(input("Deposition Ammount: "))

                sql1 = 'select Balance from ammount where Account_no= %s'                 #selecting the required balance from ammount table    
                val1 = (acc,)

                mycursor = mydb.cursor()                                                  #importing cursor
                
                mycursor.execute(sql1, val1)

                a = mycursor.fetchone()
                total = a[0] + amm                                                        #adding the deposited ammount to initial balance

                sql2 = 'update ammount set Balance= %s where Account_no= %s'              #updating the new balance in ammount table
                val2 = (total,acc)

                mycursor.execute(sql2,val2)
                mydb.commit()                                                             #commiting data

                print("Ammount Deposited Successfully!")

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()

                
                

#function for withdrawal of money


def withdraw():
                acc   = input("Enter Account Noumber: ")
                fname = input("Enter First Name:")
                lname = input("Enter Last Name:")
                amm   = int(input("Withdrawal Ammount: "))
                pin   = input("Enter your Pin: ")

                sql1 = 'select Balance from money where Account_no= %s and Pin_no = %s'         #selecting the required balance from money table
                val1 = (acc, pin)

                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql1, val1)

                a = mycursor.fetchone()
                total = a[0] - amm                                                              #subtracting the withdrawn ammount from initial balance

                sql2 = 'update money set Balance= %s where Account_no= %s and Pin_no = %s'      #updating the new balance in money table
                val2 = (total,acc, pin)

                mycursor.execute(sql2,val2)

                sql3 = 'update ammount set Balance = %s where Account_no= %s'                   #updating the new balance in ammount table
                val3 = (total, acc)

                mycursor.execute(sql3, val3)
                mydb.commit()                                                                   #commiting data

                print("Ammount Withdrawn Successfully!")

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()

#function for transfer money

def transfer():
                acc1 = input("Sender's Account Number: ")
                acc2 = input("Reciever's Account Number: ")
                amm  = int(input("Transfer Ammount: "))
                pin  = input("Enter your Pin: ")
 
                sql1 = 'select Balance from money where Account_no= %s and Pin_no = %s'         #selecting the sender's balance from money table
                val1 = (acc1,pin)

                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql1, val1)

                a = mycursor.fetchone()
                total1 = a[0] - amm                                                             #subtracting the tranferred ammount from sender's balance 

                sql2 = 'update money set Balance = %s where Account_no= %s'                     #updating new sender's balance in money table
                val2 = (total1, acc1)

                mycursor.execute(sql2, val2)

                sql3 = 'update ammount set Balance = %s where Account_no = %s'                  #updating new sender's balance in ammount table
                val3 = (total1, acc1)

                mycursor.execute(sql3, val3)
                
                sql4 = 'select Balance from money where Account_no= %s'                         #selecting the reciever's balance from money table
                val4 = (acc2,)

                mycursor.execute(sql4, val4)

                b = mycursor.fetchone()
                total2 = b[0] + amm                                                             #adding the transferred ammount to reciever's balance

                sql5 = 'update money set Balance = %s where Account_no = %s'                    #updating new reciever's balance to money table
                val5 = (total2, acc2)
                
                mycursor.execute(sql5, val5)
                
                sql6 = 'update ammount set Balance = %s where Account_no = %s '                 #updating new reciever's balance to ammount table
                val6 = (total2, acc2)

                mycursor.execute(sql6, val6)
                mydb.commit()                                                                   #commiting data

                print("Ammount Transferred Successfully!")

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()
                

#function to display particular account information

                
def display():
                acc = input("Enter Account Number: ")
                sql = 'select * from account where Account_no = %s'                             #selecting the particular data related to entered account number
                val = (acc,)

                mycursor = mydb.cursor()                                                        #importing cursor                                                      
                
                mycursor.execute(sql, val)
                
                a = mycursor.fetchall()

                for i in a:
                                print(i, end=" ")

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()
                

#function to display all accounts

def records():
                sql = 'select * from account'                                                   #selecting all the data from account table
                
                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql)

                a = mycursor.fetchall()

                for i in a:
                                print(i)

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()
                

#funtion to update last name
                
def lname():
                acc  = input("Enter Account Number: ")
                prev = input("Enter Current Last Name: ")
                new  = input("Enter new Last name: ")
                

                sql = 'update account set Last_Name = %s where Account_no = %s'                 #updating the last name
                val = (new, acc)

                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql, val)
                mydb.commit()                                                                   #commiting data

                print("Last Name updated Successfully!")
                

#function to update address

def address():
                acc  = input("Enter Account Number: ")
                prev = input("Enter Current Address: ")
                new  = input("Enter New Address: ")

                sql = 'update account set Address = %s where Account_no = %s'                   #updating the address
                val = (new, acc)

                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql, val)
                mydb.commit()                                                                   #commiting data

                print("Address updated Successfully!")
                

#function to update phone number

def phone():
                acc  = input("Enter Account Number: ")
                prev = input("Enter Current Phone Number: ")
                new  = input("Enter New Phone Number: ")

                sql = 'update account set Phone_no = %s where Account_no = %s'                  #updating phone number
                val = (new, acc)

                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql, val)
                mydb.commit()                                                                   #commiting data

                print("Phone Number updated Successfully!")
                

#function to update email-id

def email():
                acc  = input("Enter Account Number: ")
                prev = input("Enter Current Email-Id: ")
                new  = input("Enter New Email-Id: ")

                sql = 'update account set Email_id = %s where Account_no = %s'                  #updating email-id
                val = (new, acc)

                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql, val)
                mydb.commit()                                                                   #commiting data

                print("Email-Id  updated Successfully!")
                

#function to update pin number
                
def pin():
                acc  = input("Enter Account Number: ")
                prev = input("Enter Current Pin Number: ")
                new  = input("Enter New Pin Number: ")

                sql = 'update money set Pin_no = %s where Account_no = %s'                      #updating pin number
                val = (new, acc)

                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql, val)
                mydb.commit()                                                                   #commiting data

                print("Pin number updated successfully!")
                

#sub-main function for updation of above information

def modify():
                print("""
                a. Update Last Name
                b. Update Address
                c. Update Phone Number
                d. Update Email-Id
                e. Update Pin Number
                """)

                choice1 = input("What would you like to update? ")

                if choice1 == "a":
                                lname()
                if choice1 == "b":
                                address()
                if choice1 == "c":
                                phone()
                if choice1 == "d":
                                email()
                if choice1 == "e":
                                pin()
                else:
                                print("Invalid Choice!")

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()
                                

#function to delete or close an account
                
def close():
                acc = input("Enter Account Number: ")
                pin = input("Enter Pin Number: ")

                sql1 = 'delete from account where Account_no = %s'                              #deleting data from account table related to entered account number
                
                sql2 = 'delete from ammount where Account_no = %s'                              #deleting data from ammount table related to entered account number
                
                sql3 = 'delete from money where Account_no = %s'                                #deleting data from money table related to entered account number
                
                val = (acc,)
                
                mycursor = mydb.cursor()                                                        #importing cursor
                
                mycursor.execute(sql1, val)
                mycursor.execute(sql2, val)
                mycursor.execute(sql3, val)
                mydb.commit()                                                                   #commiting data

                print("Account Closed Successfully!")

                c = input("Press M to Return to main menu ")
                if c == "M":
                                main()
                
                                                      
main()               
