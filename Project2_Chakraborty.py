# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:35:22 2021
@author: DELL
"""
import time
delay=0.2

print("hello my name is Athena and i am going to help you out with your book shopping today")
time.sleep(delay)
name=input("what is your name ? ")

time.sleep(delay)
print("Wow that's a pretty nice name !")
time.sleep(delay)
print("so "+name+" what genre of books do you love to read ? ")
genre=input()
time.sleep(delay)
print("great ! so do you want to check out some books of "+genre+" genre ? please enter yes or no")
choice=input()
if(choice=='yes'):
    time.sleep(delay)
    cost=0.00
    cart=[]
    time.sleep(delay)
    while (True):
    #books of detective and crime genre
            if(genre=='crime thriller'):
                print("awesome ! come on lets dive into some amazing book collection !")
                bookList=["The murder of Roger Ackroyd","The Mysterious Affairs at Styles","The Murder on The Orient Express","And Then There were none","The ABC Murder","The Hound Of The Baskervilles","The complete casebook of Sherlock Holmes","knots and crosses","A is for alibi","The Big Sleep","Gone Girl","The Postman always rings twice","In cold blood","The woman in white"]
                authorList=["Agatha Cristie","Agatha Cristie","Agatha Cristie","Agatha Cristie","Agatha Cristie","Sir Arthur Conan Doyle","Sir Arthur Conan Doyle","Ian Rankin","Sue Grafton","Raymond Chandler","Gillian Flynn","James M. Cain","Truman Capote","Wilkie Collins"]
                l=len(bookList)
                price=[350.0,350.0,399.0,399.0,350.0,350.0,499.0,450.0,399.0,499.0,450.0,350.0,399.0,450.0,499.0]
                for i in range(l) :
                    print("Book name : "+str(bookList[i])+" , Author name : "+str(authorList[i])+" and Price : "+str(price[i]))
                    time.sleep(delay)
                    buy=input("do you want to add this book to your cart ? ")
                    print()
                    if(buy=='yes'):
                        cost+=price[i]
                        cart.append(bookList[i])
                    else:
                        continue            
                time.sleep(delay)
                print("do you want to check out any other genre of books ? ")
                selection=input()
                print()
                if(selection=='no'):
                    break
                else:
                    time.sleep(delay)          
                    genre=input("enter the genre that you want to visit")
                    print()
    #books of fantasy genre
            if(genre=="fantasy"):
                    print("awesome ! come on lets dive into some amazing book collection !")
                    bookList=["Percy Jackson and the Olympians","The Mortal Instruments","The Never tilting World","Cindrella is dead","Legendborn","Fallen","Teardrop","The Hobbit","Shatter me","The Lord of the Rings","Eragon","The Hunger Games","Legend","The Maze Runner"]
                    authorList=["Rick Riordan","Cassandra Clare","Rin Chupeco","Kalynn Bayron","Tracy Deonn","Lauren Kate","Lauren Kate","J.R.R. Tolkien","Tahereh Mafi","J.R.R Tolkien","Christopher Paolini","Suzanne Collins","Marie Lu","James Dashner"]
                    price=[599.0,350.0,350.0,399.0,399.0,350.0,350.0,499.0,450.0,399.0,499.0,450.0,350.0,399.0,450.0]
                    for i in range(0,14) :
                        print("Book name : "+str(bookList[i])+" , Author name : "+str(authorList[i])+" and Price : "+str(price[i]))
                        time.sleep(delay)
                        buy=input("do you want to add this book to your cart ? ")
                        print()
                        if(buy=='yes'):
                         cost+=price[i]
                         cart.append(bookList[i])
                        else:
                            continue
                    time.sleep(delay)
                    print("do you want to check out any other genre of books ? ")
                    selection=input()
                    if(selection=='no'):
                        break
                    else:
                        time.sleep(delay)      
                        genre=input("enter the genre that you want to visit")
                        print()
    #science fiction books
                        time.sleep(delay)
            if(genre=="science fiction"):
                    print("awesome ! come on lets dive into some amazing book collection !")
                    bookList=["Red Rising","A Wrinkle in Time","Ready Player Two","The Road","The Stand","The Time Machine","The Three Body Problem","The Martian Chronicles","The War of the Worlds","The Martian","Snow Crash","Farenheit 451","Dragonflight","The Forever World"]
                    authorList=["Pierce Brown","Madeleine L'Engle","Ernest Cline","Cormac McCarthy","Stephen King","H.G.Wells","Cixin Lu","Ray Bradbury","H.G.Wells","Andy Weir","Neal Stephenson","Ray Bradbury","Anne McCafferey","Wilkie Collins"]
                    price=[350.0,350.0,399.0,399.0,350.0,350.0,499.0,450.0,399.0,499.0,450.0,350.0,399.0,450.0,299.0]
                    l=len(bookList)
                    for i in range(0,l):
                        print("Book name : "+str(bookList[i])+" , Author name : "+str(authorList[i])+" and Price : "+str(price[i]))
                        buy=input("do you want to add this book to your cart ? ")
                        print()
                        if(buy=='yes'):
                         cost+=price[i]
                         cart.append(bookList[i])
                        else:
                            continue
                    time.sleep(delay)
                    print("do you want to check out any other genre of books ? ")
                    selection=input()
                    if(selection=='no'):
                        break
                    else:
                        time.sleep(delay)     
                        genre=input("enter the genre that you want to visit")
                        print()
            #contemporary books
                    time.sleep(delay)
            if(genre=="contemporary"):
                    print("awesome ! come on lets dive into some amazing book collection !")
                    bookList=["The Hating Game","It ends with Us","Cloud Atlas","A thousand splendid sun","Fangirl","A man called Ove","The midnight Library","The Hate U give","The Fault in our Stars","The Sense of ending","Red,White and Royal Blue","Me Before You","The Book Thief","To kill a Mockingbird","Girl Online"]
                    authorList=["Sally Thorne","Colleen Hoover","David Mitchell","Khaled Hosseini","Rainbow Rowell","Fredrick Backman","Matt Haig","Angie Thomas","John Green","Julian Barnes","Casey McQuiston","Jojo Meyes","Markus Zusak","Harper Lee","Zoella Sugg"]
                    price=[350.0,350.0,399.0,399.0,350.0,350.0,499.0,450.0,399.0,499.0,450.0,350.0,399.0,450.0,500.0]
                    l=len(bookList)
                    for i in range(l) :
                        print("Book name : "+str(bookList[i])+" , Author name : "+str(authorList[i])+" and Price : "+str(price[i]))
                        buy=input("do you want to add this book to your cart ? ")
                        print()
                        if(buy=='yes'):
                         cost+=price[i]
                         cart.append(bookList[i])
                        else:
                            continue
            time.sleep(delay)
            print("do you want to check out any other genre of books ? ")
            selection=input()
            if(selection=='no'):
                break
            else:
                time.sleep(delay)
                genre=input("enter the genre that you want to visit")
                print()
        #horror
            time.sleep(delay)
            if(genre=="horror"):
                    print("awesome ! come on lets dive into some amazing book collection !")
                    bookList=["It","The Shining","Let the Right One in","The Exorcist","Bird Box","The Hunger","The Stand","Carrie","The Woman in Black","The Silence of Lambs","Salem's Lot","The Turn of the Screw","Pet Sematary","The Terror"]
                    authorList=["Stephen King","Stephen King","John Ajvide Lindqvist","William Peter Blatty","Josh Malerman","Alma Katsu","Stephen King","Stephen King","Susan Hill","Thomas Harris","Stephen King","Henry James","Stephen King","Dan Simmons"]
                    price=[350.0,350.0,399.0,399.0,350.0,350.0,499.0,450.0,399.0,499.0,450.0,350.0,399.0,450.0,399.0]
                    for i in range(0,14) :
                        print("Book name : "+str(bookList[i])+" , Author name : "+str(authorList[i])+" and Price : "+str(price[i]))
                        buy=input("do you want to add this book to your cart ? ")
                        if(buy=='yes'):
                         cost+=price[i]
                         cart.append(bookList[i])
                        else:
                            continue
            time.sleep(delay)
            print("do you want to check out any other genre of books ? ")
            print()
            selection=input()
            if(selection=='no'):
                break
            else:
                time.sleep(delay)
                genre=input("enter the genre that you want to visit")
                print()
                    
    print("The books that you have bought today are :")
    for book in cart:
        print(book)
    print("your total price is : "+str(cost))
    print("Thank you for book shopping with us today ! Have a good day !")
else:
    if(choice=='no'):
        print("sorry i cannot help you out today !")
    
           
    
