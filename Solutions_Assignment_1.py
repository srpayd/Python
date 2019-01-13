# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 16:48:24 2018

@author: serap aydogdu
"""

def problem1(input):
    if input>=0 and input < 10:
        output= input*12
    elif input >=10 and input <100:
        output=input*10
    elif input >=100:
        output=input*7
    else:
        output=0
    print(input,' times items bought and total cost of items is ', output)
    
problem1(5)


#%% 
def problem2():
    import random
    my_randoms=[]
    evenCount=0
    
    for i in range(20):
        my_randoms.append(random.randrange(1,101,1))
    
    for i in range(20):
        if my_randoms[i]%2==0:
            evenCount=evenCount+1
                  
    print('\r\n a. The random list is : \r\n','*'*22,'\r\n', my_randoms)
    print('\r\n b. The average of the list is: \r\n','*'*30,'\r\n', sum((my_randoms))/(len(my_randoms))) 
    print('\r\n c. The largest and smallest values on the list are: \r\n','*'*30,'\r\n', max(my_randoms),'and', min(my_randoms))
    my_randoms.sort()
    print('\r\n d. The second largest and the second smallest entries are : \r\n','*'*30,'\r\n', my_randoms[-2],'and', my_randoms[1] )
    print ('\r\n e. How many times even number are in the list is : \r\n','*'*30,'\r\n', evenCount )
    
problem2()


#%%
def problem3():
    n=eval(input("How many Fibonacci numbers you would like to print:"))
    
    if n==1:
        l=1
    elif n==2:
        l=[1,1]
    else: 
        l=[1,1]
        for i in range(2,n):
            l.append(l[i-1]+l[i-2])
    
    print(l)
    
problem3()
#%%
def problem4():
    import re
    lines=open('C:/Users/orhan aydogdu/Desktop/Advances in Data Science/homeworks/homework1-data/blood_pressure.csv').readlines()   
    # firstly, delete the title
    del lines[0]    
 
#a  ###########################################################################
    
    #In order to take out the blood pressure numbers split based on "," and append L list
    L=[]
    for line in lines:
       mean_x=line.split(",")[1][3:].strip()   # For each row; 1.column from third line to the end is needed to be seperated
       L.append(mean_x)  #then add this low and high blood pressure numbers into to L list.
    #Then sort the L list and show  
    L.sort()
    # In order to get rid of any blanks and punctuations
    L=[re.findall("\d+",line) for line in L ]
    
    
    #First column is low pressure line so we need to get min of it.
    print("*"*80,"\na. Lowest blood pressure is : ",min(L[0]))
    #Second column is high presure line so we need to swap the list items and get the max of the first column.
    L=[(i[1], i[0]) for i in L]
    L.sort(reverse=True)
    
    # lowest and highest blood pressures
    print("   Highest blood pressure is: ",max(L[0]))
    
    
    
#b  ###########################################################################
    # Create a new list
    meanList=[]  
    for line in lines:
        mean_x=line.split(",")[1][:3]   # her satırın 1. sutunun ilk 3 hanesi alınıt
        meanList.append(mean_x)                #listemize eklenir.
    
    meanList=[int(i) for i in meanList]               # L listesindeki degerleri int cev irdik                         #listeyi yazdır.
    print("b. Average of the mean values is:",sum(meanList)/len(meanList))
    
problem4()

#%%
def problem5():
    lines=open('C:/Users/orhan aydogdu/Desktop/Advances in Data Science/homeworks/homework1-data/gdp_per_capita.csv').readlines()
    #Take out of the title.
    del lines[0]
    
#a  ###########################################################################
    #Find the Turkey inside of lines and get rid of any blanks & punctuations
    listofTurkey=[]
    for x in lines:
        if "Turkey" in x:
            listofTurkey=x.strip().split(";")
    #Get rid of subtitle
    del listofTurkey[0]
    
    #Generate years between 1960-2017 for dictionary 
    years=[1960]
    for i in range(1,58):
        sum=years[0]+i
        years.append(sum)

    #Create a dictionary, put years as keys and rates as values.
    my_ratio_dic={}
    for i in range(0,len(listofTurkey)):
        my_ratio_dic[years[i]]=(((float(listofTurkey[i])-float(listofTurkey[i-1]))/float(listofTurkey[i]))*100)
        
    #So we should assign a default value for the first year.Due to there is no interaction year for it.
    my_ratio_dic[1960]=0
    #sort the dictionary based on values then find the year of max value.    
    inverse = [(value, key) for key, value in my_ratio_dic.items()]
    inverse
    
    # see the finalized dictionary and the year of highest percentage
    print("*"*80,"\na. The yearly percentage increase compared to previous year :\n")
    print("Years  "+"Percentage Increase\n"+"-----  "+"-------------------")
    for key,value in my_ratio_dic.items():
        print (key," ", value)
    print ("\na. The year of the highest increase in terms of percentage is:",max(inverse)[1])
#b  ###########################################################################
    #Sorted based on the first columns
    inverse.sort(reverse=True)
    
    print ("*"*80,"\nb. The years that GDP per capita decreased :")
    # Take the decreased GDPs compared to the previous years
    for num in range(1,58):                    # We have 58 years
        if inverse[num][0]< 0:                 # if ratio is decrease
            print(inverse[num][1],end=' ')     # then show up its year 
            
problem5()