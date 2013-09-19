# http://direct-lemmasoft.renai.us/forums/viewtopic.php?f=8&t=20081&view=next
init python:

    import math
    import random
    
    # initialize random numbers
    random.seed()
    

    class PartyBar(renpy.Displayable):

        def __init__(self, index, name, value, prev_value, char_level=0, max_hp=100, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(PartyBar, self).__init__(**kwargs)
            
            #The values that we'll need for rendering later
            self.position_index = index
            self.char_name = Text('{b}' + name + '{/b}')
            
            if index == 0:
                self.transform_nametext = Transform(child=self.char_name, xzoom=0.4)
                
                self.height_correct = 10
                self.char_hptext = Text('{b}' + str(value) + ' / ' + str(max_hp).rjust(5) + '{/b}')
                self.char_leveltext = Text('{b}LV:' + str(char_level) + '{/b}')
                self.transform_healthtext = Transform(child=self.char_hptext, xzoom=0.3, yzoom = 0.6)
                self.transform_leveltext = Transform(child=self.char_leveltext, xzoom=0.3, yzoom = 0.6)
            else:
                self.transform_nametext = Transform(child=self.char_name, xzoom=0.35, yzoom = 0.875)
            
            self.char_health = value
            self.max_char_health = max_hp
            
            # The current health level for animation
            self.current_health = prev_value

            # The width and height of us, and our child.
            self.width = 0
            self.height = 0
            
            self.lastevent = 0
            self.lastdraw = 0
            self.bar_animstart = 0
            self.health_inc = 0
            self.framerate = 10
            self.targetcolor = 0
            self.currentcolor = 0
            self.barcolor_animstart = 0
            self.showwarningcolor = False
            self.pulse_start = None
            self.outline_targetcolor = (0, 0, 0, 200)
            self.outline_currentcolor = (0, 0, 0, 200)

            
        def render(self, width, height, st, at):

            # Create a transform, that can adjust the alpha channel of the
            # child.
            #t = Transform(child=self.child, alpha=self.alpha)

            # Create a render from the child.
            #child_render = renpy.render(t, width, height, st, at)

            # Get the size of the child.
            # self.width, self.height = child_render.get_size()

            self.width = width
            self.height = height
            

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)
            text_render = renpy.render(self.transform_nametext, width, height, st, at)
             
            #render.fill((200, 200, 200, 128))
            

            if (self.current_health != self.char_health or self.bar_animstart != 0):
                self.framerate = 60
                        
                if self.bar_animstart == 0:
                    self.bar_animstart = st
                        
                timeelapsed = st - self.bar_animstart
                    
                if (timeelapsed > 1.0):
                    self.current_health = self.char_health
                    self.framerate = 10
                    self.bar_animstart = 0
                    if (self.char_health < 0.3 * self.max_char_health):                     # reset just in case
                        self.showwarningcolor = False    
                        self.targetcolor = (150, 150, 255, 200)
                        self.currentcolor = (190, 0, 0, 200)
                        self.outline_targetcolor = (190, 0, 0, 200)
                        self.outline_currentcolor = (0, 0, 0, 200)
                        self.barcolor_animstart = st
                else:
                    self.current_health = self.current_health + (self.char_health - self.current_health) * (timeelapsed / 1.0)
                
            
            
            rcanvas = render.canvas()
            
            #draw the background
            if self.position_index == 0:
                top = 0
                bot = height - self.height_correct
                seg2_end = width
            else:
                top = height / 8
                bot = height - top
                seg2_end = (width - width / 3) / 2 + width/3
            seg1_end = 15
            s1wh = seg1_end / 2
            s1q1 = (bot - top) / 4
            s1q2 = bot - s1q1
            s1q1 = s1q1 + top
            
            seg2_start = seg1_end + 2
            backalpha = 128
            
            seg2_half = (seg2_end - seg2_start) / 2
            steps = 20
            stepsize = (seg2_half) / (steps)
            alphastep = (0 - backalpha) / (steps)
            
            seg2_half = seg2_half + seg2_start
            posoffset = seg2_half
            alphaoffset = backalpha
            
            rcanvas.polygon((200, 200, 200, backalpha), [[0, top], [seg1_end, top], [seg1_end, bot], [0, bot], [0, s1q2], [s1wh, s1q2], [s1wh, s1q1], [0, s1q1]])
            rcanvas.polygon((200, 200, 200, backalpha),[[seg2_start, top], [seg2_half, top], [seg2_half, bot], [seg2_start, bot]])
            
            for i in range(0, steps / 3):
                    rcanvas.polygon((200, 200, 200, alphaoffset),[[posoffset, top], [posoffset + stepsize, top], [posoffset + stepsize, bot], [posoffset, bot]])
                    alphaoffset += alphastep
                    if alphaoffset < 0:
                        alphaoffset = 0
                    posoffset += stepsize
            
            if self.position_index == 0:
                rcanvas.polygon((200, 200, 200, alphaoffset),[[posoffset, top], [posoffset + stepsize, top], [posoffset + stepsize, bot / 2], [posoffset, bot]])
                bot = bot / 2
            else:                
                rcanvas.polygon((200, 200, 200, alphaoffset),[[posoffset, top], [posoffset + stepsize, top], [posoffset + stepsize, bot], [posoffset, bot]])
            
            alphaoffset += alphastep
            if alphaoffset < 0:
                alphaoffset = 0
            posoffset += stepsize
            
            for i in range(steps / 3 + 1, steps):
                    rcanvas.polygon((200, 200, 200, alphaoffset),[[posoffset, top], [posoffset + stepsize, top], [posoffset + stepsize, bot], [posoffset, bot]])
                    alphaoffset += alphastep
                    if alphaoffset < 0:
                        alphaoffset = 0
                    posoffset += stepsize
            
            text_start = 25
            
            if self.position_index == 0:
                text_top = 3
            else:
                text_top = 5
            #draw the character names
            render.blit(text_render, (text_start, text_top))
            
            bar_color = (0, 190, 0, 200)
            outline_color = (0, 0, 0, 200)
            
            if self.current_health < 0.3 * self.max_char_health:
                bar_color = (190, 0, 0, 200)
            elif self.current_health <= 0.5 * self.max_char_health:
                bar_color = (190, 190, 0, 200) 
                
            if self.targetcolor == 0:
                self.targetcolor = bar_color
                if self.currentcolor == 0:
                    self.currentcolor = bar_color
            else:
                if self.framerate >= 60:
                    c1 = self.targetcolor
                    c2 = bar_color
                    if not (c1[0] == c2[0] and c1[1] == c2[1] and c1[2] == c2[2] and c1[3] == c2[3]):
                        self.barcolor_animstart = st
                        self.targetcolor = bar_color
                    if (st - self.barcolor_animstart < 0.3):
                        timeelapsed = st - self.barcolor_animstart
                        self.currentcolor = self.interpolatecolor(self.currentcolor, self.targetcolor, timeelapsed, 0.3)
                        bar_color = self.currentcolor
                    else:
                        self.currentcolor = self.targetcolor
                        bar_color = self.currentcolor        
                else:
                    if self.char_health < 0.3 * self.max_char_health:
                        timeelapsed = st - self.barcolor_animstart
                        pingtime = 2.0
                        if self.char_health < 0.1 * self.max_char_health:
                            pingtime = 0.25
                        elif self.char_health < 0.2 * self.max_char_health:
                            pingtime = 1.0
                            
                        if not self.showwarningcolor:
                            pingtime = pingtime / 2.0           # it's a ping.  Not a slow on/off
                            
                        if timeelapsed > pingtime:
                            self.barcolor_animstart = st
                            self.currentcolor = self.targetcolor
                            self.outline_currentcolor = self.outline_targetcolor
                            bar_color = self.currentcolor
                            outline_color = self.outline_currentcolor
                            self.showwarningcolor = not self.showwarningcolor
                            if not self.showwarningcolor:
                                self.targetcolor = (150, 150, 255, 200)
                                self.outline_targetcolor = (190, 0, 0, 200)
                            else:
                                self.targetcolor = (190, 0, 0, 200)
                                self.outline_targetcolor = (0, 0, 0, 200)

                        else:
                            self.currentcolor = self.interpolatecolor(self.currentcolor, self.targetcolor, timeelapsed, pingtime)
                            bar_color = self.currentcolor
                            self.outline_currentcolor = self.interpolatecolor(self.outline_currentcolor, self.outline_targetcolor, timeelapsed, pingtime)
                            outline_color = self.outline_currentcolor

                            
                
            
            #draw the bars
            # a bit hacky, did not account for when we're in the midpoint segments.  That can be addressed later.
            if self.position_index == 0:
                bar_start = width / 3
                barheight = (height - self.height_correct) / 2 
                barheight_top =  (height - self.height_correct) / 4
                barheight_bot = barheight + barheight_top
                bar_width = width - 2 - bar_start - 4
                barwidth_half = bar_start + bar_width / 2
                barheight_half = barheight * 2 / 3 + barheight_top
                fullbar_end = bar_start + bar_width
                if self.current_health < self.max_char_health:
                    bar_end = bar_start + ((self.current_health / float(self.max_char_health)) * bar_width)
                    
                    if bar_end < barwidth_half:
                        rcanvas.line((230, 230, 230, 200), [bar_end, barheight_bot], [bar_end + 7, barheight_top], 2)
                        rcanvas.polygon(bar_color, [[bar_start, barheight_bot], [bar_end, barheight_bot], [bar_end + 7, barheight_top], [bar_start, barheight_top]])
                    else:
                        rcanvas.line((230, 230, 230, 200), [bar_end, barheight_half], [bar_end + 4, barheight_top], 2)
                        rcanvas.polygon(bar_color, [[bar_start, barheight_bot], [barwidth_half - 3, barheight_bot], [barwidth_half, barheight_half], [bar_end, barheight_half], [bar_end + 4, barheight_top], [bar_start, barheight_top]])
                else:
                    rcanvas.polygon((0, 190, 0, 200), [[bar_start, barheight_bot], [barwidth_half - 2, barheight_bot], [barwidth_half, barheight_half], [fullbar_end, barheight_half], [fullbar_end + 4, barheight_top], [bar_start, barheight_top]])
                rcanvas.polygon((230, 230, 230, 200), [[bar_start, barheight_bot], [barwidth_half - 2, barheight_bot], [barwidth_half, barheight_half], [fullbar_end, barheight_half], [fullbar_end + 4, barheight_top], [bar_start, barheight_top]], 2)
                rcanvas.polygon((0, 0, 0, 200), [[bar_start + 1, barheight_bot - 1], [barwidth_half - 3, barheight_bot - 1], [barwidth_half - 1, barheight_half - 1], [fullbar_end - 1, barheight_half - 1], [fullbar_end + 3, barheight_top + 1], [bar_start + 1, barheight_top + 1]], 1)
                
                text_margin = 2
                text_height = (height - barheight_half) * 0.65
                text_top = height - text_height
                text_bot = height
                avail_textspace = (bar_width / 2 + 4)
                healthtext_start = avail_textspace * 0.05 + barwidth_half
                healthtext_end = avail_textspace * 0.71 + barwidth_half
                #healthtext_textstart = avail_textspace * 0.07 + barwidth_half
                leveltext_start = avail_textspace * 0.74 + barwidth_half
                leveltext_end = avail_textspace * 1.00 + barwidth_half
                leveltext_textstart = avail_textspace * 0.76 + barwidth_half
                rcanvas.polygon((200, 200, 200, 128), [[healthtext_start, text_top], [healthtext_end, text_top], [healthtext_end, text_bot], [healthtext_start, text_bot]])
                rcanvas.polygon((200, 200, 200, 128), [[leveltext_start, text_top], [leveltext_end, text_top], [leveltext_end, text_bot], [leveltext_start, text_bot]])
                
                textHP_render = renpy.render(self.transform_healthtext, width, height, st, at)
                childwidth, childheight = textHP_render.get_size()
                healthtext_width = healthtext_end - text_margin - healthtext_start - text_margin
                healthtext_textstart = healthtext_width - childwidth + healthtext_start + text_margin
                render.blit(textHP_render, (healthtext_textstart, text_top))
                
                textLV_render = renpy.render(self.transform_leveltext, width, height, st, at)
                childwidth, childheight = textLV_render.get_size()
                leveltext_width = leveltext_end - text_margin - leveltext_start - text_margin
                leveltext_textstart = leveltext_width - childwidth + leveltext_start + text_margin
                
                render.blit(textLV_render, (leveltext_textstart, text_top))
                
            else:
                bar_start = width / 3
                barheight = height / 3
                barheight_top = height / 3
                barheight_bot = barheight + barheight_top
                bar_width = (width - 2 - bar_start) / 2 - 5
                fullbar_end = bar_start + bar_width
                if self.current_health < self.max_char_health:
                    bar_end = bar_start + ((self.current_health / float(self.max_char_health )) * bar_width)
                    rcanvas.line((230, 230, 230, 200), [bar_end, barheight_bot], [bar_end + 5, barheight_top], 2)
                    rcanvas.polygon(bar_color, [[bar_start, barheight_bot], [bar_end, barheight_bot], [bar_end + 5, barheight_top], [bar_start, barheight_top]])
                else:
                    rcanvas.polygon((0, 190, 0, 200), [[bar_start, barheight_bot], [fullbar_end, barheight_bot], [fullbar_end + 5, barheight_top], [bar_start, barheight_top]])
                rcanvas.polygon((230, 230, 230, 200), [[bar_start, barheight_bot], [fullbar_end, barheight_bot], [fullbar_end + 5, barheight_top], [bar_start, barheight_top]], 2)
                rcanvas.polygon(outline_color, [[bar_start + 1, barheight_bot - 1], [fullbar_end - 1, barheight_bot - 1], [fullbar_end + 4, barheight_top + 1], [bar_start + 1, barheight_top + 1]], 1)

            if self.pulse_start != None:
                timeelapsed = st - self.pulse_start
                if (timeelapsed > 4.0):
                    self.pulse_start = None
                elif (timeelapsed < 1.0):
                    pulse_start = seg2_start
                    pulse_top = top + 1
                    pulse_maxlen = bot - top
                    pulse_pos = pulse_maxlen * timeelapsed / 1.0 + pulse_top
                    rcanvas.rect((200, 200, 230, 200), [pulse_start, pulse_pos, 2, 2], 1)
                else:
                    pulse_start = seg2_start
                    pulse_top = bot - 1
                    pulse_maxlen = width / 3 - seg2_start
                    pulse_pos = pulse_maxlen * (timeelapsed - 1.0) / 3.0 + pulse_start
                    rcanvas.rect((200, 200, 230, 200), [pulse_pos, pulse_top, 2, 2], 1)

            # Blit (draw) the child's render to our render.
            #render.blit(child_render, (0, 0))

            # Return the render.
            return render
            
        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.

            if (self.lastevent == 0):
                self.lastevent = st

            if (st - self.lastevent) > (float(1) / self.framerate):
                self.lastevent = st
                renpy.redraw(self, 0)
                
                if (self.pulse_start == None):
                    randval = random.randint(0, 1000)
                    
                    if randval > 990:
                        self.pulse_start = st
                
                # print st
                

                
                
            
            renpy.timeout(float(1) / self.framerate)
         
            # Base on the distance, figure out an alpha.
            #if distance <= self.opaque_distance:
            #    alpha = 1.0
            #elif distance >= self.transparent_distance:
            #    alpha = 0.0
            #else:
            #    alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            # If the alpha has changed, trigger a redraw event.
            #if alpha != self.alpha:
            #    self.alpha = alpha
            #    renpy.redraw(self, 0)

            # Pass the event to our child.
            #return self.child.event(ev, x, y, st)
            return None
            
        def visit(self):
            if (self.position_index == 0):
                return [self.transform_healthtext, self.transform_leveltext, self.transform_nametext]
            else:
                return [self.transform_nametext]
            
        def interpolatecolor(self, currentcolor, targetcolor, timeelapsed, timespan):
            c0 = currentcolor[0] + (targetcolor[0] - currentcolor[0]) * timeelapsed / timespan
            c1 = currentcolor[1] + (targetcolor[1] - currentcolor[1]) * timeelapsed / timespan
            c2 = currentcolor[2] + (targetcolor[2] - currentcolor[2]) * timeelapsed / timespan
            c3 = currentcolor[3] + (targetcolor[3] - currentcolor[3]) * timeelapsed / timespan
            return (c0, c1, c2, c3)
        
    # this is used to globally store the previous character data.
    class PartyData:
        def __init__(self):
            self.prev_char = None
            self.max_hp = 100                # Used for the player data
            self.char_level = 0              # Used for the player data
            
        def setCharLevel(self, lvl, hp):
            self.char_level = lvl
            self.max_hp = hp
            
        def getCharLevel(self):
            return (self.char_level, self.max_hp)
        
        def update(self, characters):
            
#            try:
#                self.prev_char
#                self.new_chars = zip(characters, self.prev_char)
#            except NameError:
#                self.new_chars = zip(characters, characters)
                
#            self.prev_char = characters
#            return self.new_chars
            
            if self.prev_char != None:
                
                if (len(characters) != len(self.prev_char)):
                    if (len(characters) < len(self.prev_char)):
                        self.new_chars = zip(characters, self.prev_char)        # rely on zip's "smallest array" feature
                    else:
                        length = len(characters) - len(self.prev_char)
                        for i in range (0, length):
                            self.prev_char = self.prev_char + [["None", 0]]
                        self.new_chars = zip(characters, self.prev_char)
                else:    
                    self.new_chars = zip(characters, self.prev_char)
            else:
                arr = [["None", 0, 1, 100]]
                if len(characters) > 1:
                    for i in range(1, len(characters)):
                        arr = arr + [["None",0]]
                self.new_chars = zip(characters, arr)
               
            self.prev_char = characters
            
            return self.new_chars