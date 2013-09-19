init:
    python:
        import math
        import random
        
        class ExplodeFactory: # the factory that makes the particles
            
            def __init__(self, theDisplayable, explodeTime=0, numParticles=20):
                self.displayable = theDisplayable
                self.time = explodeTime
                self.particleMax = numParticles
                
            def create(self, partList, timePassed):
                newParticles = None
                if partList == None or len(partList) < self.particleMax:
                    if timePassed < self.time or self.time == 0:
                        newParticles = self.createParticles(timePassed)
                return newParticles
                
            
            def createParticles(self, timePassed):
                timeDelay = 0.4 #renpy.random.random() * 0.2
                
                # We'll generate all of the particles at once instead of generating one each frame
                particleList = []      
                
                for i in range(0, self.particleMax):
                    index = random.randint(0, len(self.displayable) - 1)
                    particleList = particleList + [ExplodeParticle(self.displayable[index], timeDelay, timePassed + self.time)]
                
                
                return particleList
            
            def predict(self):
                return [self.displayable]

        class ExplodeParticle:
            
            def __init__(self, theDisplayable, timeDelay, lifeTime):
                self.displayable = theDisplayable
                self.delay = timeDelay
                #self.xSpeed = (renpy.random.random() - 0.5) * 0.02
                #self.ySpeed = (renpy.random.random() - 0.5) * 0.02
                #self.xPos = 0.5
                #self.yPos = 0.5
                
                #self.xSpeed = (renpy.random.random() - 0.5) * 10
                #self.ySpeed = (renpy.random.random() - 0.5) * 10
                #self.xPos = renpy.config.screen_width / 2
                #self.yPos = renpy.config.screen_height / 2
                
                self.originPoint = (random.random() * renpy.config.screen_height * 0.15)
                self.angle = (random.random() * 2 * math.pi)
                
                xcomp = math.cos(self.angle)
                ycomp = math.sin(self.angle)
                
                self.xPos = renpy.config.screen_width / 2 + xcomp * self.originPoint
                self.yPos = renpy.config.screen_height / 2 + ycomp * self.originPoint
                
                self.xSpeed = xcomp * self.originPoint / 10
                self.ySpeed = ycomp * self.originPoint / 10
                
                self.lifeSpan = lifeTime
                
            
            def update(self, theTime):
                
                if (theTime > self.delay):
                    self.xPos += self.xSpeed
                    self.yPos += self.ySpeed
                    
                    #if self.xPos > 1.05 or self.xPos < -1.05 or self.yPos > 1.05 or self.yPos < -1.05:
                    #    return None
                        
                    # verify if the particle went out of the screen so we can destroy it.
                    if self.yPos > renpy.config.screen_height or self.yPos < 0 or\
                        self.xPos < 0 or self.xPos > renpy.config.screen_width or\
                        theTime > self.lifeSpan:
                        ##  print "Dead"
                        return None
                
                return (self.xPos, self.yPos, theTime, self.displayable)
                