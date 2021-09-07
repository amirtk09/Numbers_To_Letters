from os import system


#region DEFINITIONOFLETTERS
alfabet = {
    "یک" : 1,
    "دو": 2,
    "سه" : 3,
    "چهار" : 4,
    "پنچ" : 5,
    "شش" : 6,
    "هفت" : 7,
    "هشت" : 8,
    "نه" : 9,
    "ده" : 10,
    "یازده" : 11,
    "دوازده" : 12,
    "سیزده" : 13,
    "چهارده" : 14,
    "پانزده" : 15,
    "شانزده" : 16,
    "هفده" : 17,
    "هجده" : 18,
    "نوزده" : 19,
    "بیست " : 20,
    "سی" : 30,
    "چهل" : 40,
    "پنچاه": 50,
    "شصت" : 60,
    "هفتاد" : 70,
    "هشتاد" : 80,
    "نود" : 90,
    "صد" : 100,
    "دویست" : 200,
    "سیصد" : 300,
    "چهارصد" : 400,
    "پانصد" : 500,
    "ششصد" : 600,
    "هفت صد" : 700,
    "هشتصد" : 800,
    "نه صد" : 900,
    "هزار" : 1000,
    "میلیون" : 10**6,
    "میلیارد" : 10**9,
    "بیلیون": 10**12,
    "بیلیارد" : 10**15,
    "تریلیون" : 10**18,
    "تریلیارد" : 10**21,
    "کوآدریلیون" : 10**24,
    "کادریلیارد" : 10**27,
    "کوینتیلیون" : 10**30,
    "کوانتینیارد" : 10*33,
    "سکستیلیون" : 10**36,
    "سکستیلیارد" : 10**39,
    "سپتیلیون" : 10**42,
    "سپتیلیارد" : 10**45,
    "اکتیلیون" : 10**48,
    "اکتیلیارد" : 10**51,
    "نانیلیون" : 10**54,
    "نانیلیارد" : 10**57,
    "دسیلیون" : 10**60,
    "دسیلیارد" : 10*63,
    "آندسیلیون" : 10**66,
    "آندسیلیارد" : 10**69,
    "دودسیلیون" : 10**72,
    "دودسیلیارد" : 10**75,
    "تریدسیلیون" : 10**78,
    "تریدسیلیارد" : 10**81,
    "کوادردسیلیون" : 10**84, 
    "کوادردسیلیارد" : 10**87,
    "کویندسیلیون" : 10**90,
    "کویندسیلیارد" : 10**93,
    "سیدسیلیون" : 10**96,
    "سیدسیلیارد" : 10**99,
} 
#endregion

#region GETNUMBER
def get_number(min_val,max_val,message):

    while True:
        number = int(input(message))
        system('cls')

        if number in range(min_val,max_val+1):
            return number

        print('Error!!!, Please try again. ')

while True:

    num = get_number(
                        min_val = 1,
                        max_val = ((9*(10**99))+1),
                        message= "Please enter a number between 1 and up to 100 digit: "
                    )
    count = len(str(num))
    num2 = num - (num//(10**(3*(count//3)))*(10**(3*(count//3))))
    num3 = num2//(10**(3*(count//3)-3))
    break
#endregion 

#region CONVERTER
print(num, ": ")
for key , value in alfabet.items():
    if num <= 20:
        if num == value:
            print(key)  
    elif 20 < num <= 99:
        if ((num//10)*10) == value:
            print(key,end="")
            for key , value in alfabet.items():
                if (num%10) == value:
                    print(" و ",key)
    elif 100 <= num <= 999:
        if (num // 100)*100 == value:
            print(key,end="")
            for key , value in alfabet.items():
                if num%100 < 20:
                    if num%100 == value:
                        print(" و ",key)
                else:
                    if ((num % 100)//10)*10 == value:
                        print(" و ",key,end="")
                        for key , value in alfabet.items():
                            if num % 10 == value:
                                print(" و ",key)
    elif num >= 1000:
        if num//(10**(3*(count//3))) <= 20:
            for key , value in alfabet.items():
                if (num//(10**(3*(count//3)))) == value:
                    print(key,end="")
                    for key , value in alfabet.items():
                        if 10**(3*(count//3)) == value != 1:
                            print(" ",key,end=" ")     

            while (3*(count//3)) > 0:
                num2 = num - (num//(10**(3*(count//3)))*(10**(3*(count//3))))
                num3 = ((num2//(10**(3*(count//3)-3))))
                num6 = num3
                num7 = 10**(3*(count//3))
                
                if 100 <= num6 <= 999:
                    for key , value in alfabet.items():
                        if (num6 // 100)*100 == value:
                            print(key,end="")
                            for key , value in alfabet.items():
                                if num6%100 < 20:
                                    if num6%100 == value:
                                        print(" و ",key,end="")
                                else:
                                    if ((num6 % 100)//10)*10 == value:
                                        print(" و ",key,end="")
                                        for key , value in alfabet.items():
                                            if num6 % 10 == value:
                                                print(" و ",key,end="")
                elif num6 <= 20:  
                    for key , value in alfabet.items():
                        if num6 == value:
                            print(key,end=" ")  
                elif 20 < num6 <= 99:
                    for key , value in alfabet.items():
                        if ((num6//10)*10) == value:
                            print(key,end="")
                            for key , value in alfabet.items():
                                if (num6%10) == value:
                                    print(" و ",key,end="")
                
                if str(num3) != "0":
                    for key , value in alfabet.items():
                        if 10**(3*(count//3)-3) == value != 1:
                            print(" ",key,end=" ")
                            
                elif str(num3) == "0":
                    print("",end="")

                count -= 3
                    
        elif 20 < (num//(10**(3*(count//3)))) <= 99:
            for key , value in alfabet.items():
                if (((num//(10**(3*(count//3))))//10)*10) == value:
                    print(key,end="")
                    for key , value in alfabet.items():
                        if ((num//(10**(3*(count//3))))%10) == value:
                            print(" و ",key,end=" ")
                            for key , value in alfabet.items():
                                if 10**(3*(count//3)) == value != 1:
                                    print(" ",key,end=" ")  
                            while (3*(count//3)) > 0:
                                num2 = num - (num//(10**(3*(count//3)))*(10**(3*(count//3))))
                                num3 = ((num2//(10**(3*(count//3)-3))))
                                num6 = num3

                                if 100 <= num6 <= 999:
                                    for key , value in alfabet.items():
                                        if (num6 // 100)*100 == value:
                                            print(key,end="")
                                            for key , value in alfabet.items():
                                                if num6%100 < 20:
                                                    if num6%100 == value:
                                                        print(" و ",key,end="")
                                                else:
                                                    if ((num6 % 100)//10)*10 == value:
                                                        print(" و ",key,end="")
                                                        for key , value in alfabet.items():
                                                            if num6 % 10 == value:
                                                                print(" و ",key,end="")
                                elif num6 <= 20:  
                                    for key , value in alfabet.items():
                                        if num6 == value:
                                            print(key,end=" ")  
                                
                                elif 20 < num6 <= 99:
                                    for key , value in alfabet.items():
                                        if ((num6//10)*10) == value:
                                            print(key,end="")
                                            for key , value in alfabet.items():
                                                if (num6%10) == value:
                                                    print(" و ",key,end="")
                                
                                if str(num3) != "0":
                                    for key , value in alfabet.items():
                                        if 10**(3*(count//3)-3) == value != 1:
                                            print(" ",key,end=" ")
                                            
                                elif str(num3) == "0":
                                    print("",end="")

                                                        
                                count -= 3
        
        if 100 <=  (num//(10**(3*(count//3)-3))) <= 999:
            while (3*(count//3)) > 0:
                num2 = num - (num//(10**(3*(count//3)))*(10**(3*(count//3))))
                num3 = ((num2//(10**(3*(count//3)-3))))
                num6 = num3
                if 100 <= num6 <= 999:
                    for key , value in alfabet.items():
                        if (num6 // 100)*100 == value:
                            print(key,end="")
                            for key , value in alfabet.items():
                                if num6%100 < 20:
                                    if num6%100 == value:
                                        print(" و ",key,end="")
                                else:
                                    if ((num6 % 100)//10)*10 == value:
                                        print(" و ",key,end="")
                                        for key , value in alfabet.items():
                                            if num6 % 10 == value:
                                                print(" و ",key,end="")
                elif num6 <= 20:  
                    for key , value in alfabet.items():
                        if num6 == value:
                            print(key,end=" ")  
                elif 20 < num6 <= 99:
                    for key , value in alfabet.items():
                        if ((num6//10)*10) == value:
                            print(key,end="")
                            for key , value in alfabet.items():
                                if (num6%10) == value:
                                    print(" و ",key,end="")
                if str(num3) != "0":
                    for key , value in alfabet.items():
                        if 10**(3*(count//3)-3) == value != 1:
                            print(" ",key,end=" ")
                            
                elif str(num3) == "0":
                    print("",end="")
            
                count -= 3
#endregion