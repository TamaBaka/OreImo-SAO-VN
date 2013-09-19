# http://direct-lemmasoft.renai.us/forums/viewtopic.php?f=8&t=20081&view=next
init python:

    # Todo: Reduce the framerate to 0
    # Todo: When health = 0, empty out the square

    import math
    
    class HealthBar(renpy.Displayable):

        def __init__(self, hp, width, height, barcount, barheight, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(HealthBar, self).__init__(**kwargs)
          
            # The width and height of us, and our child.
            self.width = width
            self.height = height
            
            self.health = hp
            self.barcount = barcount
            
            self.barheight = barheight
            
            self.max_health = 100
            
            self.new_health_flag = False
            
            self.start_health = 0
            self.current_health = 0
            self.lastevent = 0
            self.lastdraw = 0
            self.bar_animstart = 0
            self.framerate = 10
            self.targetcolor = 0
            self.currentcolor = 0
            self.barcolor_animstart = 0
                        
            self.anim_bar_time = 0.1
            self.anim_color_time = 0.2
#            self.record_flag = False
                        
            
        def render(self, width, height, st, at):

            # settings
            limit = 0
            
            resolution = 30  
            
            offset = self.barheight * 1.50
            
            barheight = self.barheight
            curvewidth = self.width - 1
            curveheight = barheight / 2
            startx1 = curvewidth
            starty1 = 0 + curveheight
            startx2 = curvewidth
            starty2 = 0 + curveheight + barheight
            
            
            backalpha = 200
            outline_color = (240, 240, 240, backalpha)
            green_color = (0, 190, 0, backalpha)
            yellow_color = (190, 190, 0, backalpha)
            red_color = (190, 0, 0, backalpha)

            # Create a transform, that can adjust the alpha channel of the
            # child.
            #t = Transform(child=self.child, alpha=self.alpha)

            # Create a render from the child.
            #child_render = renpy.render(t, width, height, st, at)

            # Get the size of the child.
            # self.width, self.height = child_render.get_size()
            
            if (self.new_health_flag == True):
                self.bar_animstart = st
                self.anim_bar_time = 0.1
                self.start_health = self.current_health
                self.new_health_flag = False
            
            # Interpolate the health
            if (self.current_health != self.health or self.bar_animstart != 0):
                self.framerate = 60
                
                #f = open('out.txt', 'a')
                        
                #if self.bar_animstart == 0:
                #    self.bar_animstart = st
                    
                if (self.anim_bar_time == 0.1):
                    timespan = float(self.start_health - self.health) / self.max_health
                    if timespan < 0:
                        timespan = -timespan
                    if timespan < 0.1:
                        self.anim_bar_time = 0.25
                    elif timespan < 0.4:
                        self.anim_bar_time = 0.30 * self.barcount
                    else:
                        self.anim_bar_time = 0.20 * self.barcount

                        
                timeelapsed = st - self.bar_animstart
                    
                if (timeelapsed > self.anim_bar_time):
                    
                    #self.current_health = float(self.health)
                    self.start_health = 0
                    
                    self.framerate = 10
                    self.bar_animstart = 0
                    self.anim_bar_time = 0.1
                    #if (self.record_flag == True):
#                        f = open('out.txt', 'a')
#                        f.write('finished' )
#                        f.write('\n')
#                        f.close()
#                        self.record_flag = False
                else:
                    # http://www.gizma.com/easing/
                    # linear easing
                    #self.current_health = (self.health - self.start_health) * (timeelapsed / self.anim_bar_time) + self.start_health 
                    
                    # cubic easing out
                    timeelapsed = timeelapsed / self.anim_bar_time
                    timeelapsed = timeelapsed - 1
                    self.current_health = (self.health - self.start_health) * (timeelapsed * timeelapsed * timeelapsed + 1) + self.start_health
                    
                    
                        #if (self.record_flag == True):
#                    f = open('out.txt', 'a')
#                    f.write('{}'.format(self.current_health) )
#                    f.write('\n')
#                    f.close()
#                        self.record_flag = False

            
            if self.current_health > 60:
                health_color = green_color
            elif self.current_health > 30:
                health_color = yellow_color
            else:
                health_color = red_color
            
            # interpolate the colors
            if self.targetcolor == 0:
                self.targetcolor = health_color
                if self.currentcolor == 0:
                    self.currentcolor = health_color
            else:            
                c1 = self.targetcolor
                c2 = health_color
                if not (c1[0] == c2[0] and c1[1] == c2[1] and c1[2] == c2[2] and c1[3] == c2[3]):
                    self.barcolor_animstart = st
                    self.targetcolor = health_color
                if (st - self.barcolor_animstart < self.anim_color_time):
                    timeelapsed = st - self.barcolor_animstart
                    self.currentcolor = self.interpolatecolor(self.currentcolor, self.targetcolor, timeelapsed, self.anim_color_time)
                    health_color = self.currentcolor
                else:
                    self.currentcolor = self.targetcolor
                    health_color = self.currentcolor     

            hpratio = float(self.current_health) / self.max_health
            halfhpbar =  1.0 / (self.barcount * 2.0)

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)
                        
            rcanvas = render.canvas()
            

            tval = (resolution / 1.95) / resolution
            start_block_x1 = startx1 - tval * curvewidth
            start_block_y1 = starty1 - math.pow(tval, 0.333) * curveheight
            start_block_x2 = startx2 - tval * curvewidth * 0.8
            start_block_y2 = starty1 - math.pow(tval, 0.333) * curveheight + barheight
            tval = (resolution / 1.6) / resolution
            end_block_x1 = startx1 - tval * curvewidth
            end_block_y1 = starty1 - math.pow(tval, 0.333) * curveheight
            end_block_x2 = startx1 - tval * curvewidth * 0.8
            end_block_y2 = starty1 - math.pow(tval, 0.333) * curveheight + barheight
            
            
            # -------------- upper arc ------------------------------
            for i in xrange(0, self.barcount):
                yshift = (self.barcount - i - 1) * offset
                a = ([[start_block_x1, start_block_y1 + yshift],[start_block_x2, start_block_y2 + yshift], [end_block_x2, end_block_y2 + yshift], [end_block_x1, end_block_y1 + yshift]])
                b = ([[start_block_x1 - 1, start_block_y1 + 1 + yshift],[start_block_x2 - 1, start_block_y2 - 1 + yshift], [end_block_x2 + 1, end_block_y2 - 1 + yshift], [end_block_x1 + 1, end_block_y1 + 1 + yshift]])
            
                # scans the bar and checks if out of range
                if (round(float(i) / self.barcount, 3) < round(hpratio, 3)):
                    rcanvas.polygon(health_color, b)
                rcanvas.polygon(outline_color, a, 1)
                
            for i in xrange(0, self.barcount):
                yshift = (self.barcount - i - 1) * offset
                a = ([[startx1, starty1 + yshift]])
                b = ([[startx2, starty2 + yshift]])
                
                #check to see if there is some health in the current bar.  Otherwise, do not draw.
                if (float(i + 1) / self.barcount < hpratio):
                    c = ([[startx1 - 1, starty1 + 1 + yshift]])
                    d = ([[startx2 - 1, starty2 - 1 + yshift]])
                else:
                    c = []
                    d = []
                    
                limit = 0.0
                # sets the bar's limit based on the current proportion of health in the bar.  Get the midrange and see if there's less health than the midrange.
                if (hpratio < float(i) / self.barcount):
                    limit = 1.0
                elif (hpratio > float(i) / self.barcount) and (hpratio <=  float(i) / self.barcount + halfhpbar):
                    #if self.current_health < 50:
                    #limit = 0.5 - float(self.current_health) / self.max_health * 2 / 2
                    limit = ( halfhpbar - (hpratio - float(i) / self.barcount) ) / (halfhpbar * 2)
                    
                
                for t in xrange(0, resolution / 2):
                    # convert so that we get a range from 0.0 -> 1.0
                    tval = float(t) / resolution
                    x1 = startx1 - tval * curvewidth
                    x2 = startx2 - tval * curvewidth * 0.8
                    y1 = starty1 - math.pow(tval, 0.333) * curveheight + yshift
                    y2 = starty2 - math.pow(tval, 0.333) * curveheight + yshift
                    a.append([x1,y1])
                    b.append([x2,y2])
                    if tval > limit:
                        c.append([x1 + 1,y1 + 1])
                        d.append([x2 + 1,y2 - 1])
                
                b.reverse()
                a = a + b
                c.reverse()
                c = c + d
                
                rcanvas.polygon((200, 200, 200, backalpha), a)
                if len(c) > 2:
                    rcanvas.polygon(health_color, c)
                
                rcanvas.lines(outline_color, True, a, 1)
            
            # -------------- lower arc ------------------------------
            for i in xrange(0, self.barcount):
                yshift = (self.barcount - i - 1) * offset
                a = ([[startx1, starty1 + yshift]])
                b = ([[startx2, starty2 + yshift]])

                #check to see if there is some health in the current bar.  Otherwise, do not draw.
                if (float(i + 1) / self.barcount < hpratio):
                    c = ([[startx1 - 1, starty1 + 1 + yshift]])
                    d = ([[startx2 - 1, starty2 - 1 + yshift]])
                else:
                    c = []
                    d = []
                
                #if self.current_health < 50:
                #    limit = 0.0
                #else:
                #    limit = float(self.current_health - 50) / self.max_health * 2
                
                if (hpratio < float(i) / self.barcount):
                    limit = 0.0
                elif (hpratio >= float(i) / self.barcount) and (hpratio <=  float(i) / self.barcount + halfhpbar):
                    limit = 0.0
                elif (hpratio > float(i) / self.barcount) and (hpratio <  float(i) / self.barcount + 1.0 / self.barcount):
                    #if self.current_health < 50:
                    #limit = 0.5 - float(self.current_health) / self.max_health * 2 / 2
                    limit = (hpratio - float(i) / self.barcount - halfhpbar) / halfhpbar 
                else:
                    limit = 1.0
                
                for t in xrange(0, resolution):
                    # convert so that we get a range from 0.0 -> 1.0
                    tval = float(t) / resolution
                    x1 = startx1 - tval * curvewidth * 0.9
                    x2 = startx2 - tval * curvewidth
                    y1 = starty1 + math.pow(tval, 0.333) * curveheight + yshift
                    y2 = starty2 + math.pow(tval, 0.333) * curveheight + yshift
                    a.append([x1,y1])
                    b.append([x2,y2])
                    if (tval < limit):
                        c.append([x1 + 1,y1 + 1])
                        d.append([x2 + 1,y2 - 1])
                
                
                b.reverse()
                a = a + b
                c.reverse()
                c = c + d
                
#                if (self.record_flag == True):                
#                    f = open('out.txt', 'a')
#                    f.write('time needed: ' + '{}'.format(self.anim_bar_time) + ' elapsed time: ' + '{}'.format( st - self.bar_animstart))
#                    f.write('\n')
#                    f.write('time: ' + '{}'.format(st) + ' limit: ' + '{}'.format( limit ) + ' hpratio: ' + '{}'.format( hpratio ) )
#                    f.write('\n')
#                    #f.write('{}'.format(c))
#                    f.write('\n')
#                    f.write('{}'.format(len(c)))
#                    f.write('\n')
#                    f.close()
                
                
                rcanvas.polygon((200, 200, 200, backalpha), a)
                if len(c) > 2:
                    rcanvas.polygon(health_color, c)
                
                rcanvas.lines(outline_color, False, a, 1)
            
            return render
                
        def event(self, ev, x, y, st):

            if (self.lastevent == 0):
                self.lastevent = st

            if (st - self.lastevent) > (float(1) / self.framerate):
                self.lastevent = st
                renpy.redraw(self, 0)

            if (self.framerate == 60):
                renpy.timeout(float(1) / self.framerate)
                
            return None
            
        def setHealth(self, hp):
            self.health = hp
            self.new_health_flag = True
            
#            self.record_flag = True
#            if (self.record_flag == True):
#                f = open('out.txt', 'a')
#                f.write('start' )
#                f.write('\n')
#                f.close()
            renpy.redraw(self, 0)                # forces this control to redraw itself.  When attached to a composite, it should automatically update.
    
        def resize(self, width, height, barcount, barheight):
            self.width = width
            self.height = height
            self.barcount = barcount
            self.barheight = barheight
            
            
        def visit(self):
            #return [self.child]
            return []
            
        def interpolatecolor(self, currentcolor, targetcolor, timeelapsed, timespan):
            c0 = currentcolor[0] + (targetcolor[0] - currentcolor[0]) * timeelapsed / timespan
            c1 = currentcolor[1] + (targetcolor[1] - currentcolor[1]) * timeelapsed / timespan
            c2 = currentcolor[2] + (targetcolor[2] - currentcolor[2]) * timeelapsed / timespan
            c3 = currentcolor[3] + (targetcolor[3] - currentcolor[3]) * timeelapsed / timespan
            return (c0, c1, c2, c3)
    