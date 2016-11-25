lose = False #Losing boolean 
cuaghttext = "Sorry you lost.Press Esc to go back"
#(at start of while loop)
lose = False
finalwintext = False


if st_x == st_x1 and st_y ==st_y1: ## If statements for losing
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True
        if st_x == st_x2 and st_y ==st_y2:
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True
        if st_x == st_x3 and st_y ==st_y3:
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True
        if st_x == st_x4 and st_y ==st_y4:
            losetext = wtext.render(cuaghttext,True,wierdblue)
            st_x_change = 0 
            st_y_change = 0
            st_x1_change = 0
            st_x2_change = 0
            st_x3_change = 0
            st_x4_change = 0
            st_y1_change = 0
            st_y2_change = 0
            st_y3_change = 0
            st_y4_change = 0
            lose = True


#in the end 
if finalwintext == True :# prints strings for "feed pacman mode"
            DISPLAYSURF.blit(winningtext,(60,420))
            DISPLAYSURF.blit(winningtext_2,(60,460))
        if lose == True :
            DISPLAYSURF.blit(losetext,(60,420))
