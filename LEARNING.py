
import mysql.connector as ms
from tabulate import tabulate
mycon=ms.connect(host="localhost",user="root",passwd="1234",database="project")
mycursor=mycon.cursor()


mycon.commit()
'''
mycursor.execute("create table Personal_Info (Name varchar(50), Phno int(11) primary key,Location char(100),Restaurant char(100),TotalAmount float,Discount int(11),NetAmount float)")




#creation of table and its python code
mycursor.execute("create table Indian (slno INT ,food_name CHAR(50), price FLOAT)")

mycursor.execute("insert into Indian (slno, food_name, price) values (%s,%s,%s)", (1,"vegetarian thali", 30.00))
mycursor.execute("insert into Indian (slno, food_name, price) values (%s,%s,%s)", (2,"Bread Basket", 10.00))
mycursor.execute("insert into Indian (slno, food_name, price) values (%s,%s,%s)", (3,"butter chicken", 22.00))
mycursor.execute("insert into Indian (slno, food_name, price) values (%s,%s,%s)", (4,"Paneer Kadhai", 18.00))
mycursor.execute("insert into Indian (slno, food_name, price) values (%s,%s,%s)", (5,"Chat Platter (all types of chats", 27.00))

mycon.commit()
mycursor.execute("create table Fast_Food (slno INT ,food_name CHAR(50), price FLOAT)")

mycursor.execute("insert into Fast_Food (slno, food_name, price) values (%s,%s,%s)", (1,"Pizza non veg", 30.00))
mycursor.execute("insert into Fast_Food (slno, food_name, price) values (%s,%s,%s)", (2,"Pizza veg", 25.00))
mycursor.execute("insert into Fast_Food (slno, food_name, price) values (%s,%s,%s)", (3,"Pasta non veg", 20.00))
mycursor.execute("insert into Fast_Food (slno, food_name, price) values (%s,%s,%s)", (4,"Pasta veg", 18.00))
mycursor.execute("insert into Fast_Food (slno, food_name, price) values (%s,%s,%s)", (5,"Shawarma non veg", 10.00))
mycursor.execute("insert into Fast_Food (slno, food_name, price) values (%s,%s,%s)", (6,"French Fries (medium sized)", 18.00))

mycon.commit()
mycursor.execute("create table Arabic (SNO INT ,MENU CHAR(50), PRICE FLOAT)")

mycursor.execute("insert into Arabic (SNO, MENU, PRICE) values (%s,%s,%s)", (1,"Chicken Charcoal", 38.00))
mycursor.execute("insert into Arabic (SNO, MENU, PRICE) values (%s,%s,%s)", (2," Family Platter", 120.00))
mycursor.execute("insert into Arabic (SNO, MENU, PRICE) values (%s,%s,%s)", (3," Mixed Grill", 80.00))
mycursor.execute("insert into Arabic (SNO, MENU, PRICE) values (%s,%s,%s)", (4,"Arabic Shawarma", 5.00))
mycursor.execute("insert into Arabic (SNO, MENU, PRICE) values (%s,%s,%s)", (5,"Kunafa w/ Qahwa", 8.00))

mycon.commit()
mycursor.execute("create table Chinese (SNO INT ,MENU CHAR(50), PRICE FLOAT)")

mycursor.execute("insert into Chinese (SNO, MENU, PRICE) values (%s,%s,%s)", (1,"Vegetable Spring Roll", 12.00))
mycursor.execute("insert into Chinese (SNO, MENU, PRICE) values (%s,%s,%s)", (2,"Mixed Sea Food Soup", 18.00))
mycursor.execute("insert into Chinese (SNO, MENU, PRICE) values (%s,%s,%s)", (3,"Schezwan Chicken", 20.00))
mycursor.execute("insert into Chinese (SNO, MENU, PRICE) values (%s,%s,%s)", (4,"Veg Hakka Noodles", 18.00))
mycursor.execute("insert into Chinese (SNO, MENU, PRICE) values (%s,%s,%s)", (5,"Sweet Red Bean Rice Cake", 20.00))


mycon.commit()
mycursor.execute("create table Restaurants (SNO INT ,Restaurants CHAR(50), Cuisines char(50),location char(50),Phone_number int)")

mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (1,"Dine Out","Indian", "ME-11 Musaffah",25526013))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (2,"Calicut Paragon","Indian","Madinat Zayed",5526013))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (3,"Taste of Punjab","Indian","ME-11 MUSAFFAH",25528213))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (4,"Hot Plate","Indian","ME-10 MUSAFFAH",25527113))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (5," Chappan Bhog","Indian","ME-10 MUSAFFAH",25547862))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (6,"Papa Johns","FAST FOOD","DALMA MALL",25529813))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (7,"Pizza Hut", "FAST FOOD","DALMA MALL",25529814))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (8,"KFC", "FAST FOOD","DALMA MALL",25529815))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (9," McDonalds","FAST FOOD","Mazyad Mall",25529816))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (10,"Burger King","FAST FOOD","Mazyad Mall",25529817))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (12,"Hot Plate","Chinese","ME-10 MUSAFFAH",25529818))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (13,"Al Akkawi","Arabic","ME-10 MUSAFFAH",25529819))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (14,"Layali Al Sham","Arabic","ME-10 MUSAFFAH",25529810))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (15,"Saudi Kitchen","Arabic","Abu Dhabi",25529877))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (16,"Villa Beirut", "Arabic","Dalma Mall",25529844))
mycursor.execute("insert into Restaurants (SNO, Restaurants, Cuisines, location, Phone_number) values (%s,%s,%s,%s,%s)", (11,"Din Tai Fung", "Chinese","Galleria Mall",25529899))

'''

print()
print("Welcome to our Food Delivery Service")
print()
print("Please register with us to place an order")

name=input("Enter your Name:")
phoneno=int(input("Enter Your Phone number:"))
location=input("Enter your Location:")
rst='none' 
#shows the cuisines
def show_cuisine():
    mycon.commit()
    mycursor.execute("select distinct cuisines from Restaurants")
    data=mycursor.fetchall()
    print(tabulate(data,headers=["Cuisines"],tablefmt='grid'))

  

#shows the various restaurants under that category
def main(cuisine):

    if cuisine=="I" :
        mycon.commit()
        mycursor.execute("select * from Restaurants where cuisines='Indian'")
        ddata=mycursor.fetchall()
        print(tabulate(ddata,headers=["sn","Restaurants","Cuisine","Location","Phone_number"],tablefmt='grid'))
  
    elif cuisine=="A":
        mycon.commit()
        mycursor.execute("select * from Restaurants where cuisines='Arabic'")
        data=mycursor.fetchall()
        print(tabulate(data,headers=["sn","Restaurants","Cuisine","Location","Phone_number"],tablefmt='grid'))
        
    elif cuisine=="F":
        mycon.commit()
        mycursor.execute("select * from Restaurants where cuisines='FAST FOOD'")
        data=mycursor.fetchall()
        print(tabulate(data,headers=["sn","Restaurants","Cuisine","Location","Phone_number"],tablefmt='grid'))
                       
    elif cuisine=="C" :
        mycon.commit()
        mycursor.execute("select * from Restaurants where cuisines='Chinese'")
        data=mycursor.fetchall()
        print(tabulate(data,headers=["sn","Restaurants","Cuisine","Location","Phone_number"],tablefmt='grid'))
    


# shows the food menu
def select_menu(x):
    if cuisine=="I":
        mycon.commit()
        mycursor.execute("select * from Indian")
        d=mycursor.fetchall()
        print(tabulate(d,headers=["sn","Menu","Price"],tablefmt='grid'))
    elif cuisine=="A":
        mycon.commit()
        mycursor.execute("select * from Arabic")
        d=mycursor.fetchall()
        print(tabulate(d,headers=["sn","Menu","Price"],tablefmt='grid'))
    elif cuisine=="F":
        mycon.commit()
        mycursor.execute("select * from fast_food")
        d=mycursor.fetchall()
        print(tabulate(d,headers=["sn","Menu","Price"],tablefmt='grid'))
    elif cuisine=="C":
        mycon.commit()
        mycursor.execute("select * from Chinese")
        d=mycursor.fetchall()
        print(tabulate(d,headers=["sn","Menu","Price"],tablefmt='grid'))
        


#calculates the price
totalprice=0
def calc_food_price(food):
    
    global totalprice
    
    if cuisine=='I':
        mycon.commit()
        mycursor.execute("select * from Indian")
        data=mycursor.fetchall()
        q="select Price from Indian where food_name='{}'".format(food)
        mycursor.execute(q)
        p=mycursor.fetchone()
        price=p[0]
        print("price: ",price)
        totalprice+=price
        
    if cuisine=='A':
        mycon.commit()
        mycursor.execute("select * from Arabic")
        data=mycursor.fetchall()
        q="select PRICE from Arabic where MENU='{}'".format(food)
        mycursor.execute(q)
        p=mycursor.fetchone()
        price=p[0]
        print("price: ",price)
        totalprice+=price

        
    if cuisine=='F':
        mycon.commit()
        mycursor.execute("select * from fast_food")
        data=mycursor.fetchall()
        q="select Price from Fast_Food where food_name='{}'".format(food)
        mycursor.execute(q)
        p=mycursor.fetchone()
        price=p[0]
        print("price: ",price)
        totalprice+=price
        
    if cuisine=='C':
        mycon.commit()
        mycursor.execute("select * from Chinese")
        data=mycursor.fetchall()
        q="select PRICE from Chinese where MENU='{}'".format(food)
        mycursor.execute(q)
        p=mycursor.fetchone()
        price=p[0]
        print("price: ",price)
        totalprice+=price



#calculates the discount
netamount=0
discount=0
def discount_calc():
    global discount
    global netamount
    if totalprice<50:
        discount=0
        netamount=totalprice-discount
        print()
    elif totalprice>50:
        discount=(10/100)*totalprice
        netamount=totalprice-discount
        print("Your bill after discount",netamount)
    elif 50<totalprice<70:
        discount=(15/100)*totalprice
        netamount=totalprice-discount
        print("Your bill after discount",netamount)
    elif 70<totalprice<100:
        discount=(20/100)*totalprice
        netamount=totalprice-discount
        print("Your bill after discount",netamount)
    elif totalprice>100:
        discount=(25/100)*totalprice
        netamount=totalprice-discount
        print("Your bill after discount",netamount)
    elif totalprice<50:
        print("your bill is below aed 50")
        
          
#inserting the information into the table 
def insert_info():
    ins="insert into personal_info(Name,Phno,Location,Restaurant,TotalAmount,Discount,NetAmount) values('{}',{},'{}','{}','{}','{}','{}')".format(name,phoneno,location,rst,totalprice,discount,netamount)
    mycursor=mycon.cursor()
    mycursor.execute(ins)
    mycon.commit()

ch=" "

while ch:
    ch=input("do you want to place an order(yes/no): ")
    if ch=='yes':
        show_cuisine()
        cuisine=input("enter the cuisine you want (I=Indian,A=Arabic,C=Chinese,F=Fast Food):  ")           
        main(cuisine)
        rst=input("Enter the Restaurant You wan to order from: ")        
        select_menu(rst)
        food=input("Enter the food item: ")   
        calc_food_price(food)
    
        
    else:
        print(totalprice,"is your total bill")
        discount_calc()
        insert_info()
        print("Thankyou visit us again")
        ch=""
        

  
