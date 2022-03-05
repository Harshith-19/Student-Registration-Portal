import itertools,random

def distribute():
    global player,bot1,bot2,bot3
    global deck
    
    # player 1 distribution
    for i in range(13):
        player.append(deck[i])
    #player 2 distribution

    for i in range(13,26):
        bot1.append(deck[i])
    
    #player 3 distribution

    for i in range(26,39):
        bot2.append(deck[i])
    
    #player 4 distribution

    for i in range(39,52):
        bot3.append(deck[i])
def usercard():
    
    
    print(f"Hello player ,your card is-  ",end=" ")
    player.sort(reverse=True)
    for i in range(len(player)):
        print(displaycard(player[i]),end="  ")  
    print()
    print()
def cardchoice1(a,bot):
    flag=0
    for i in bot:
        if(a[1]==i[1] and i[0]>a[0]):

           b=i
           flag=1
           break

        elif(a[1]==i[1]):
            for i in range(len(bot)-1,-1,-1):
                if(a[1]==bot[i][1]):
                   b=bot[i]
                   flag=1
                   break
            if(flag==1):
                break
    if(flag!=1):
        b=bot[-1]
    return b
def cardchoice2(a,b,bot):
    flag=0
    for i in bot:
        if(a[1]==i[1] and i[0]>a[0] and i[0]>b[0]):

           b=i
           flag=1
           break

        elif(a[1]==i[1]):
            for i in range(len(bot)-1,-1,-1):
                if(a[1]==bot[i][1]):
                   b=bot[i]
                   flag=1
                   break
            if(flag==1):
                break
    if(flag!=1):
        b=bot[-1]
    return b
def cardchoice3(a,b,c,bot):
    flag=0
    for i in bot:
        if(a[1]==i[1] and i[0]>a[0] and i[0]>b[0] and i[0]>c[0]):

           b=i
           flag=1
           break

        elif(a[1]==i[1]):
            for i in range(len(bot)-1,-1,-1):
                if(a[1]==bot[i][1]):
                   b=bot[i]
                   flag=1
                   break
            if(flag==1):
                break
    if(flag!=1):
        b=bot[-1]
    return b
def modify(a):
    ls=[0,"A"]
    if(a[1].isdigit()):
        ls[0]=int(a[1:])
        ls[1]=a[0]
        tup=tuple(ls)
        return tup

    else:
        if(a[1]=="A"):
            ls[0]=14
            ls[1]=a[0]
            tup=tuple(ls)
            return tup
        elif(a[1]=="K"):
            ls[0]=13
            ls[1]=a[0]
            tup=tuple(ls)
            return tup
        elif(a[1]=="Q"):
            ls[0]=12
            ls[1]=a[0]
            tup=tuple(ls)
            return tup
        elif(a[1]=="J"):
            ls[0]=11
            ls[1]=a[0]
            tup=tuple(ls)
            return tup
        

def gameplaying(winner,player,bot1,bot2,bot3):

    
    ls=["cheating"]

    if(winner==player):
        usercard()
        
        a=input("player -> ")
        p=modify(a)
        card=p[1]
        if p not in player:
            return ls,0
        b3=cardchoice1(p,bot3)
        b1=cardchoice2(p,b3,bot1)
        b2=cardchoice3(p,b3,b1,bot2)
        print("bot3 -> ",displaycard(b3))
        print("bot1 -> ",displaycard(b1))
        print("bot2 -> ",displaycard(b2))
        
    if(winner==bot1):
        b1=bot1[0]
        card=b1[1]
        b2=cardchoice1(b1,bot2)
        usercard()
        print("bot1 -> ",displaycard(b1))
        print("bot2 -> ",displaycard(b2))
        a=input("player ->")
        p=modify(a)
        if p not in player:
            return ls,0
        b3=cardchoice3(b1,b2,p,bot3)
        print("bot3 -> ",displaycard(b3))
    elif(winner==bot2):
        usercard()
        b2=bot2[0]
        card=b2[1]
        print("bot2 ->",displaycard(b2))
        
        a=input("player -> ")
        
        p=modify(a)
        if p not in player:
            return ls,0
        b3=cardchoice2(b2,p,bot3)
        b1=cardchoice3(b2,p,b3,bot1)
        print("bot3 -> ",displaycard(b3))
        print("bot1 -> ",displaycard(b1))
    elif(winner==bot3):
        usercard()
        b3=bot3[0]
        card=b3[1]
        b1=cardchoice1(b3,bot1)
        b2=cardchoice2(b3,b1,bot2)
        print("bot3 -> ",displaycard(b3))
        print("bot1 -> ",displaycard(b1))
        print("bot2 -> ",displaycard(b2))
        a=input("player -> ")
        p=modify(a)
        if p not in player:
            return ls,0
    
    bot1.remove(b1)
    bot2.remove(b2)
    bot3.remove(b3)
    player.remove(p)
    print()
    winner,w=winner_of_eachturn(b1,b2,b3,p,card)
    print()
    
    return winner,w

def winner_of_eachturn(b1,b2,b3,p,card):
    templst=[b1,b2,b3,p]
    lst=[]
    for i in templst:
        if(i[1]==card):
            lst.append(i)
    lst.sort(reverse=True)
    ans=lst[0]
    
    
    if(ans==b1):
        print("bot1 wins")
        return bot1,1
    elif(ans==b2 ):
        print("bot2 wins")
        return bot2,2
    elif(ans==b3 ):
        print("bot3 wins")
        return bot3,3
    elif(ans==p):
        print("player wins")
        return player,4
def displaycard(a):
    st=a[1]
    if(a[0]==14):
        st=st+"A"
    elif(a[0]==13):
        st=st+"K"
    elif(a[0]==12):
        st=st+"Q"
    elif(a[0]==11):
        st=st+"J"
    else:
        st=st+str(a[0])
    return st
    

def call(a):
    l = []
    for i in range(13):
        l.append(a[i][0])
    count = l.count(14) + l.count(13) + l.count(12) + l.count(11)
    return count 


sp1=[]
sp2=[]
sp3=[]
sp4=[]


wish="Y"
while(wish=="Y"):

    deck=list(itertools.product([2,3,4,5,6,7,8,9,10,11,12,13,14],["S","H","C","D"]))
    print()
    dk=input('Press "f" to play using file or any other alphabet to generate the cards randomly -')

    # distribute in four players 
    player=[]
    bot1=[]
    bot2=[]
    bot3=[]
    ps1=0 
    s1=0
    s2=0
    s3=0
    ts1=0
    ts2=0
    ts3=0
    ts4=0
    random.shuffle(deck)
    distribute()
    if dk=='f':
        # s2=0
        # s3=1
        bot1=[]
        bot2=[]
        bot3=[]
        player=[]
        f=input('Enter filename - ')
        f1=open(f,'r')
        b21=f1.readline()
        b22=f1.readline()
        b23=f1.readline()
        b24=f1.readline()
        # b25=f1.readline()
        b11=b21[6:len(b21)-1].split(',')
        b12=b22[6:len(b22)-1].split(',')
        b13=b23[6:len(b23)-1].split(',')
        b14=b24[8:len(b24)-1].split(',')
        # call1=int(b25[6:len(b25)])
        for i in range(0,len(b11)):
            bot1.append(modify(b11[i]))
            bot2.append(modify(b12[i]))
            bot3.append(modify(b13[i]))
            player.append(modify(b14[i]))
        f1.close()





    
    bot1.sort(reverse=True)

    bot2.sort(reverse=True)
    bot3.sort(reverse=True)
    player.sort(reverse=True)
    

    print()
    winner=random.choice([bot1,bot2,bot3,player])
    if(dk=="f"):
        winner=bot2
    
    usercard()
    call1 = int(input("Enter your call: "))
    print("calls of players")
    call2=call(bot1)
    call3=call(bot2)
    call4=call(bot3)
    print("bot1-> ",call2)
    print("bot2-> ",call3)
    print("bot3-> ",call4)
    print("player-> ",call1)
    print()
    print()

    print("cyclic order bot1->bot2->player->bot3->bot1………")
    print()
    i=1
    if(winner==bot1):
        print("start s from bot1")
    elif(winner==bot2):
        print("start s from bot2")
    elif(winner==bot3):
        print("start s from bot3")
    elif(winner==player):
        print("start s from player")
    
    print()
    while(i<=13):
        ans,w=gameplaying(winner,player,bot1,bot2,bot3)
        if(ans==["cheating"]):
            print("error:  you give the wrong input card,please input a valid card which you have")
        else:
            winner=ans
            if winner==player and w==4:
                ps1+=1
            elif winner==bot1 and w==1:
                s1+=1
            elif winner==bot2 and w==2:
                s2+=1
            elif winner==bot3 and w==3:
                s3+=1
            i+=1
            
        print()
    print('scores:')
    print()
    
    if call2>s1:
        print('bot1 = -10*'+str(call2)+'( y = '+str(s1)+', x = '+str(call2)+')')
        sp2.append(('-10*'+str(call2),-1*(10*call2)))
    else:
        print('bot1 = 10*'+str(call2)+' +('+str(s1)+'-'+str(call2)+') = '+ str((10*call2) + s1-call2)+' ( y = '+str(s1)+', x = '+str(call2)+')')
        sp2.append(('10*'+str(call2)+'+('+str(s1)+'-'+str(call2)+')',(10*call2)+s1-call2))
    if call3>s2:
        print('bot2 = -10*'+str(call3)+'( y = '+str(s2)+', x = '+str(call3)+')')
        sp3.append(('-10*'+str(call3),-1*(10*call3)))
    else:
        print('bot2 = 10*'+str(call3)+' +('+str(s2)+'-'+str(call3)+') = '+ str((10*call3) + s2-call3)+' ( y = '+str(s2)+', x = '+str(call3)+')')
        sp3.append(('10*'+str(call3)+' +('+str(s2)+'-'+str(call3)+')',(10*call3)+s2-call3))
    if call4>s3:
        print('bot3 = -10*'+str(call4)+'( y = '+str(s3)+', x = '+str(call4)+')')
        sp4.append(('-10*'+str(call4),-1*(10*call4)))
    else:
        print('bot3 = 10*'+str(call4)+' +('+str(s3)+'-'+str(call4)+') = '+ str((10*call4) + s3-call4)+' ( y = '+str(s3)+', x = '+str(call4)+')')
        sp4.append(('10*'+str(call4)+' +('+str(s3)+'-'+str(call4)+')',(10*call4)+s3-call4))
    if call1>ps1:
        print('player = -10*'+str(call1)+' ( y = '+str(ps1)+', x = '+str(call1)+')')
        sp1.append(('-10*'+str(call1),-1*(10*call1)))
    else:
        print('player = 10*'+str(call1)+' +('+str(ps1)+'-'+str(call1)+') = '+ str((10*call1) + ps1-call1)+' ( y = '+str(ps1)+', x = '+str(call1)+')')
        sp1.append(('10*'+str(call1)+' +('+str(ps1)+'-'+str(call1)+')',(10*call1)+ps1-call1))
    k=sorted([(sp1[-1][1],'player'),(sp2[-1][1],'bot1'),(sp3[-1][1],'bot2'),(sp4[-1][1],'bot3')],key=lambda x:x[0],reverse=True)
    print()
    print(k[0][1]+' is the winner!!!!!!!')
    print()
    wish=input("Continue (Y/N): ")
    if wish=='N':
        for i in range(0,len(sp1)):
            ts1=ts1+sp1[i][1]
            ts2=ts2+sp2[i][1]
            ts3=ts3+sp3[i][1]
            ts4=ts4+sp4[i][1]
        print()
        print('Total scores:')
        print()
        
        print('bot1 = ',end='')
        k=0
        for i in sp2:
            print('('+str(i[0])+')',end='')
            k+=1
            if k!=len(sp2):
                print('+',end='')
        print('= ',ts2)
        print('bot2 = ',end='')
        k=0
        for i in sp3:
            print('('+str(i[0])+')',end='')
            k+=1
            if k!=len(sp3):
                print('+',end='')
        print('= ',ts3)
        print('bot3 = ',end='')
        k=0
        for i in sp4:
            print('('+str(i[0])+')',end='')
            k+=1
            if k!=len(sp4):
                print('+',end='')
        print('= ',ts4)
        print('player = ',end='')
        k=0
        for i in sp1:
            print('('+str(i[0])+')',end='')
            k+=1
            if k!=len(sp1):
                print('+',end='')
        print('= ',ts1)
        x=[(ts1,'player'),(ts2,'bot1'),(ts3,'bot2'),(ts4,'bot3')]
        x.sort(reverse=True)
        print()
        print(x[0][1]+' wins the series')

print("==============================================================================================================================")










