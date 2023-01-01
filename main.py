'''
#########$$$$$$$$$$%%%%%%%%%%%
COPY OF MARIO LIKE GAME
BY - PRASHANT RAWAT
DATE OF START - 29/12/2022
%%%%%%%%%%$$$$$$$$$$$##########
'''
import pygame 
import sys 
import random
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((4000,10000))

#function for playing sound
def sond(sn):
    mixer.init()
    coin= pygame.mixer.Sound("coin.wav")
    mdie= pygame.mixer.Sound("mdie2.wav")
    wpn1= pygame.mixer.Sound("wpn1.wav")
    wpn2= pygame.mixer.Sound("wpn2.wav")
    btn= pygame.mixer.Sound("btn.wav")
    pdie= pygame.mixer.Sound("pdie.mp3")
    mlst=[coin,mdie,wpn1,wpn2,btn,pdie]
    pygame.mixer.Sound.play(mlst[sn])
    
    
    
# Function for loading and fixing images
def imag(nam,siz,rot):
    timg=pygame.image.load(nam+".jpg").convert()
    timg=pygame.transform.rotate(timg,rot)
    timg=pygame.transform.scale(timg,siz)
    return timg

#Function for setting up text
def text(txt,col,siz):
    font= pygame.font.SysFont("Script", siz)
    mtxt = font.render(txt, False,col)
    mtxt=pygame.transform.rotate(mtxt,270)
    return mtxt

# Function to display start screen 
def start():
    pygame.init()
    screen=pygame.display.set_mode((4000,10000))
    
    # creating or opening Total score file to check total scare 
    try :
        with open("totalscore.txt","r") as file:
            tscr=int(file.read())
    except :
        with open("totalscore.txt","w") as file:
            file.write("0")
            tscr=0
    
    # images
    mon=imag('mon2',(250,190),270)
    flor=imag('flor',(720,1450),270)
    coin=imag('coin',(90,90),270)
    ext=imag('exit',(110,400),270)
    play=imag('play',(120,400),270)
    crd=imag('cridts',(120,400),270)
    wpn1=imag('wpn1',(50,100),270)
    wpn2=imag('wpn2',(75,75),270)
    pl1=imag('pl1',(240,145),270)
    
    #rectangels
    extr=pygame.Rect(125,520,110,400)
    playrt=pygame.Rect(380,520,120,400)
    crdr=pygame.Rect(250,520,120,400)
    
    # bgm
    mixer.init()
    mixer.music.load('saway.mp3') 
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1)
    
    while True:
        # Bliting or showing images
        screen.blit(flor,(0,0))
        screen.blit(text('Monster Run !',(255,0,5),250),(500,140))
        screen.blit(ext,(125,520))
        screen.blit(play,(380,520))
        screen.blit(crd,(250,520))
        screen.blit(coin,(22,590))
        screen.blit(text(' : '+str(tscr),(255,190,0),120),(22,680))
        screen.blit(mon,(200,1100))
        screen.blit(wpn1,(320,1000))
        screen.blit(wpn2,(400,350))
        screen.blit(pl1,(200,180))
        
        # Cheacking if *person playing clicked on any button
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mous=event.pos
                if extr.collidepoint(mous):
                    sond(4)
                    return False
                elif playrt.collidepoint(mous):
                    sond(4)
                    return True
                elif crdr.collidepoint(mous):
                    sond(4)
                    credits()
        
        pygame.display.update()
    return

# Function to display credit screen
def credits():
    pygame.init()
    screen=pygame.display.set_mode((4000,10000))
    
    # images and rectangles
    flor=imag('flor',(720,1450),270)
    back=imag('back',(90,90),270)
    backr=pygame.Rect(600,90,90,90)
    
    while True:
        # showing images and rectangels
        screen.blit(flor,(0,0))
        screen.blit(back,(600,90))
        
        # showing text
        screen.blit(text('Made By : Prashant Rawat',(5,0,205),100),(605,250))
        screen.blit(text('Date of complete : 01/01/2023',(5,0,255),100),(516,250))
        screen.blit(text('Made in : 4 Days',(105,0,255),100),(427,250))
        screen.blit(text('Age : 13',(155,0,155),100),(338,250))
        screen.blit(text('Emails : prashantjnv34@gmali.com',(190,0,190),100),(249,250))
        screen.blit(text('                learnehking@gmail.com',(220,0,220),100),(165,250))
        screen.blit(text('Mobile No. : 9817541939',(255,0,255),100),(77,250))
        screen.blit(text('Github : PrashantRawatCoder ',(205,0,205),100),(1,250))
        
        # Cheacking if *person playing clicked on any button
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    mous=event.pos
                    
                    if backr.collidepoint(mous):
                        sond(4)
                        return 
                        
        pygame.display.update()
    return

# function ot display out screen
def out():
    pygame.init()
    screen=pygame.display.set_mode((4000,10000))
    
    # cheackin total score
    with open("totalscore.txt","r") as file:
        tscr=int(file.read())
    
    
    # images
    mon=imag('mon2',(250,190),270)
    flor=imag('flor',(720,1450),270)
    coin=imag('coin',(90,90),270)
    ext=imag('exit',(110,400),270)
    play=imag('play',(120,400),270)
    crd=imag('cridts',(120,400),270)
    wpn1=imag('wpn1',(50,100),270)
    wpn2=imag('wpn2',(75,75),270)
    pl1=imag('pl1',(240,145),270)
    
    #rectangels
    extr=pygame.Rect(125,520,110,400)
    playrt=pygame.Rect(380,520,120,400)
    crdr=pygame.Rect(250,520,120,400)
    
    # bgm
    mixer.init()
    mixer.music.load('saway.mp3') 
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1)
    
    while True:
        #showing text,images and rectangles
        screen.blit(flor,(0,0))
        screen.blit(text('OUT !',(255,0,5),340),(490,450))
        screen.blit(ext,(125,520))
        screen.blit(play,(380,520))
        screen.blit(crd,(250,520))
        screen.blit(coin,(22,590))
        screen.blit(text(' : '+str(tscr),(255,190,0),120),(22,680))
        screen.blit(mon,(200,1100))
        screen.blit(wpn1,(320,1000))
        screen.blit(wpn2,(400,350))
        screen.blit(pl1,(200,180))
        
        # Cheacking if *person playing clicked on any button
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mous=event.pos
                if extr.collidepoint(mous):
                    sond(4)
                    return False
                elif playrt.collidepoint(mous):
                    sond(4)
                    return True
                elif crdr.collidepoint(mous):
                    sond(4)
                    credits()
        
        pygame.display.update()
    return

# Main function to run the game
def main():
	clock = pygame.time.Clock()
	
	#Images 
	flor=imag('flor',(720,1450),270)
	pl1=imag('pl1',(240,145),270)
	pl2=imag('pl2',(240,145),270)
	pl3=imag('pl3',(240,145),270)
	mon1=imag('mon1',(140,120),270)
	mon2=imag('mon2',(140,120),270)
	mon3=imag('boss',(140,120),270)
	mon4=imag('coin',(140,120),270)
	wpn1=imag('wpn1',(50,100),270)
	wpn2=imag('wpn2',(75,75),270)
	btnr=imag('btnr',(90,90),0)
	btnl=imag('btnl',(90,90),0)
	sht1=imag('wpn1',(80,170),270)
	ext=imag('exit',(80,130),270)
	
	#rectangels
	wall=pygame.Rect(0,1450,720,1)
	blr=pygame.Rect(80,410,90,90)
	brr=pygame.Rect(80,130,90,90)
	sht1r=pygame.Rect(85,230,80,170)
	sht2r=pygame.Rect(85,580,75,75)
	extr=pygame.Rect(600,1230,80,130)
	
	#important variables
	pco1=200 #player cordinate 1
	pco2=300 #player cordinate 2
	mco=1500 #monster cordinate 1
	mco2=200 #monster cordinate 2
	wco1=260 #weapon cordinate 1
	wco2=450 #weapon cordinate 1
	jno=0
	msp=15 #monster speed
	mstr=50 #monster strength
	plst=[pl1,pl2,pl3,pl2] #list to make player animation
	mon=[mon1,mon2,mon3,mon4]  #list of monsters
	pnum=0 #number to help in animation of player
	hasm=True # has monster
	wpn=False #has weapon
	wpnj=False #player jumping while throwing weapon
	wpns=False #player scrolling while throwing weapon
	jump=False #player jumping
	scrol=False #player scrolling
	cmon=mon1 #which monmster is currently on screen
	scor=0 #score
	wpntry=3 # second weapon number
	
	#background music
	mixer.init()
	mixer.music.load('bgm.mp3')
	mixer.music.set_volume(0.7) 
	mixer.music.play(-1)
    
	while True:
		
		screen.blit(flor,(0,0))
		
		# Cheacking if *person playing clicked on any button
		for event in pygame.event.get():  
			if event.type == pygame.KEYDOWN:
			    if event.key == pygame.K_ESCAPE:
			       #storing total score
			       with open("totalscore.txt","r") as file:
			          tscr=int(file.read())
			       with open("totalscore.txt","w") as file:
			           file.write(str(tscr+scor))
			           sond(4)
			       return
			    elif event.key == pygame.K_UP and not scrol:
			        jump=True
			        sond(4)
			    elif event.key == pygame.K_DOWN and not jump:
			        scrol=True
			        sond(4)
			    elif event.key == pygame.K_RETURN:
			        wpn=True
			        cwpn=wpn1
			        sond(4)
			    elif event.key == pygame.K_END:
			        sond(4)
			        wpn=True
			        cwpn=wpn2
			        
			elif event.type == pygame.MOUSEBUTTONDOWN:
			    mous=event.pos
			    #storing total score
			    if extr.collidepoint(mous):
			       sond(4)
			       with open("totalscore.txt","r") as file:
			           tscr=int(file.read())
			       with open("totalscore.txt","w") as file:
			           file.write(str(tscr+scor))
			       return
			    elif blr.collidepoint(mous):
			        sond(4)
			        jump=True
			    elif brr.collidepoint(mous):
			        sond(4)
			        scrol=True
			    elif sht1r.collidepoint(mous):
			        sond(4)
			        wpn=True
			        cwpn=wpn1
			    elif sht2r.collidepoint(mous):
			        sond(4)
			        wpn=True
			        cwpn=wpn2
			        
			
        		        
        		
			
			    
			
			
		#player part	
		#player jumping
		if jump:
		    if not wpns and wpn:
		        wpnj=True
		        wco1=440
		    if jno<4:
		        
		        pco1+=35
		        plr=pygame.Rect(pco1,pco2, 240, 145)
		        screen.blit(plst[pnum%4],(pco1,pco2))
		        jno+=1
		    elif jno<8:
		        pco1-=35
		        plr=pygame.Rect(pco1,pco2, 240, 145)
		        screen.blit(plst[pnum%4],(pco1,pco2))
		        jno+=1
		    else:
		        wpnj=False
		        jump=False
		        jno=0
		        pco1=200
		        plr=pygame.Rect(pco1,pco2, 240, 145)
		        screen.blit(plst[pnum%4],(pco1,pco2))
		#player scrolling
		elif scrol:
		    if not wpnj and wpn:
		        wpns=True
		        wco1=100
		    if jno<4:
		        pco1-=35
		        plr=pygame.Rect(pco1,pco2, 240, 145)
		        screen.blit(plst[pnum%4],(pco1,pco2))
		        jno+=1
		    elif jno<8:
		        pco1+=35
		        plr=pygame.Rect(pco1,pco2, 240, 145)
		        screen.blit(plst[pnum%4],(pco1,pco2))
		        jno+=1
		    else :
		        wpns=False
		        scrol=False
		        jno=0
		        pco1=200
		        plr=pygame.Rect(pco1,pco2, 240, 145)
		        screen.blit(plst[pnum%4],(pco1,pco2))
		#player normal , not jumping and not scrolling
		else :
		    plr= pygame.Rect(pco1,pco2, 240, 145)
		    screen.blit(plst[pnum%4],(pco1,pco2))
		
		#monster part
		
		# cheacking if monster died
		if mstr<1:
		    
		    mstr=50
		    wpn=False
		    hasm=False
		    mco=1600
		    mco2=random.choice([200,400,62,100,350])
		    
		#fastning the speed of monster
		if cmon !=mon4 :
		     msp=10
		if cmon==mon4:
		    msp=60
		elif scor > 30:
		    msp+=10
		elif scor > 60:
		    msp+=20
		    
		
		#creating random monster
		if not hasm:
		    rann=random.choice([0,0,0,1,1,1,2,2,3,3,3,3,3])
		    cmon=mon[rann]
		    hasm=True
		
		#displaying monster
		monr= pygame.Rect(mco2,mco, 140,120)
		screen.blit(cmon,(mco2,mco))
		mco-=msp
		
		#displaying and working of weapon
		if wpn:
		    if cwpn==wpn1 :
		        wpnr=pygame.Rect(wco1,wco2,50,100)
		        screen.blit(wpn1,(wco1,wco2))
		        wco2+=100
		        if pygame.Rect.colliderect(wall,wpnr):
		            wpn=False
		            wpns=False
		            wpnj=False
		            wco1=260
		            wco2=450
		        elif pygame.Rect.colliderect(monr,wpnr):
		            sond(2)
		            sond(1)
		            if cmon==mon1:
		                mstr-=25
		                scor+=1
		            elif cmon==mon2:
		                mstr-=12.5
		                scor+=1
		            elif cmon == mon3:
		                mstr-=10
		                scor+=1
		            wpn=False
		            wpns=False
		            wpnj=False
		            wco1=260
		            wco2=450
		    elif cwpn==wpn2 and wpntry>0 :
		        wpnr=pygame.Rect(wco1,wco2,75,75)
		        screen.blit(wpn2,(wco1,wco2))
		        wco2+=100
		        if pygame.Rect.colliderect(wall,wpnr):
		            wpn=False
		            wpns=False
		            wpnj=False
		            wco1=260
		            wco2=450
		            if wpntry>0:
			            wpntry-=1
		        elif pygame.Rect.colliderect(monr,wpnr):
		            sond(3)
		            sond(1)
		            if cmon==mon1:
		                mstr-=50
		                scor+=1
		            elif cmon==mon2:
		                mstr-=50
		                scor+=1
		            elif cmon == mon3:
		                mstr-=25
		                scor+=3
		            wpn=False
		            wpns=False
		            wpnj=False
		            wco1=260
		            wco2=450
		            if wpntry>0:
		                wpntry-=1
		
		
		# Die part
		if pygame.Rect.colliderect(plr,monr) and cmon !=mon4:
		    #writing total score
		    sond(5)
		    mixer.music.stop()
		    with open("totalscore.txt","r") as file:
		        tscr=int(file.read())
		    with open("totalscore.txt","w") as file:
			    file.write(str(tscr+scor))
		    return
		elif pygame.Rect.colliderect(plr,monr) and cmon ==mon4:
		    #coin
		    sond(0)
		    mstr=0
		    scor+=1
		    wpntry+=1

		# More graphic details 
		#score
		screen.blit(imag('coin',(70,70),270),(640,170))
		screen.blit(text(': '+str(scor),(60,60,255),80),(645,250))
		
		#buttons
		screen.blit(btnr,(80,410))
		screen.blit(btnl,(80,130))
		screen.blit(sht1,(85,230))
		screen.blit(wpn2,(85,580))
		screen.blit(ext,(600,1250))
		screen.blit(text(str(wpntry),(255,0,5),80),(30,605))
		
		pnum+=1
		pygame.display.update()
		clock.tick(8)


if __name__=='__main__':
    
    canrun=start()
    while canrun:
        main()
        canrun = out()