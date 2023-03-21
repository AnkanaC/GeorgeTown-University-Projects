# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 20:45:44 2021

@author: DELL
"""

import time
delay=0.2

print("hello my name is Athena and i am going to help you out with your book shopping today")
time.sleep(delay)
name=input("what is your name ? ")

time.sleep(delay)
print("Wow that's a pretty nice name !")
time.sleep(0.1)
print("so "+name+" what genre of books do you love to read ? ")
genre=input()
time.sleep(delay)
print("great ! so do you want to check out some books of "+genre+" genre ? please enter yes or no")
choice=input()
if(choice=='yes'):
    time.sleep(delay)
    cost=0.00
    print("awesome ! come on lets dive into some amazing book collection !")
    time.sleep(delay)
    #books of detective and crime genre
    if(genre=="detective" or genre=='crime thriller'):
        bookList=["The murder of Roger Ackroyd","The Mysterious Affairs at Styles","The Murder on The Orient Express","And Then There were none","The ABC Murder","The Hound Of The Baskervilles","The complete casebook of Sherlock Holmes","knots and crosses","A is for alibi","The Big Sleep","Gone Girl","The Postman always rings twice","In cold blood","The woman in white"]
        authorList=["Agatha Cristie","Agatha Cristie","Agatha Cristie","Agatha Cristie","Agatha Cristie","Sir Arthur Conan Doyle","Sir Arthur Conan Doyle","Ian Rankin","Sue Grafton","Raymond Chandler","Gillian Flynn","James M. Cain","Truman Capote","Wilkie Collins"]
        price=[350.0,350.0]
        cart=[]
        for i in range (0,14):
            print(bookList[i])
            buy=input("do you want to add this book to your cart ?")
            if(buy=='yes'):
             cost+=price[i]
             cart.append(bookList[i])
            else:
                continue            
        time.sleep(delay)
for book in cart :
     print(book)
print(cost)

    
    
   
        

    
    