from datetime import datetime,date,timedelta
cart=[]
clean_time=[]  
newspaper_date=[]     
def minutesPassed(arg):
    now= datetime.now()
    current_time=now.strftime("%H:%M:%S")
    min=current_time[3:5]
def get_respone(arg):
    if arg==1:
        print("Hey. How are you?")
        print("Hello, I am doing great.\n")
    elif arg==2:
        print("How's the weather outside")
        print("It's pleasant outside. You should take a walk.\n")
    elif arg==3:
        print("Clean my room")
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        if len(clean_time)==0:
            print("Room is cleaned. It looks tidy now. Job completed at ",current_time,"\n")
            clean_time.append(current_time)
        else:
            start_time=clean_time[0]
            end_time=current_time
            t1= datetime.strptime(start_time, "%H:%M:%S")
            t2 = datetime.strptime(end_time, "%H:%M:%S")
            delta = t2 - t1
            minutes = delta.total_seconds() /60
            if minutes<10:
                print("The room was just cleaned",minutes," minute(s) ago. I hope it's not dirty\n")
            else:
                print("Room is cleaned. It looks tidy now. Job completed at ",current_time,"\n")
                del clean_time[0]
                clean_time.append(current_time)
    elif arg==4:
        print("Add <any-item> to my shopping list")
        item=input("Enter the item  \n")
        if item in cart:
            print("You already have",item,"in your shopping list\n")
        else:
            print(item," added to your shopping list \n")
            cart.append(item)
    elif arg==5:
        print("Fetch the newspaper")
        today=date.today()
        for i in newspaper_date:
            date_today=today.strftime("%d-%m-%y")
            if date_today in newspaper_date:
                print("I think you don't get another newspaper the same day\n")
            else:
                print("Here is your newspaper.\n")
                today=date.today()
                newspaper_date.append(today.strftime("%d-%m-%y"))
        today=date.today()
        if len(newspaper_date)==0:
            print("Here is your newspaper.\n")
            today=date.today()
            newspaper_date.append(today.strftime("%d-%m-%y"))
    elif arg==6:
        print("Read my shopping list")
        if len(cart)==0:
            print("You have no items in your shopping list\n")
        else:
            # print(*a, sep = ", ")
            print("Here is your shopping list. ",*cart,sep =", ")
            # print(*cart,sep =", ")
    else:
        print("Hmm.. I don't know that\n")
try:
    while 1:
        print(" 1. Hey. How are you? \n 2. How's the weather outside? \n 3. Clean my room \n 4. Add <any-item> to my shopping list \n 5. Fetch the newspaper \n 6. Read my shopping list \n")
        inr_instruction =int(input("Give me the instruction..    "))
        print("\n")
        get_respone(inr_instruction)
except KeyboardInterrupt:
    print("Interrupted........!")
   

