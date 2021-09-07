from .Image import Image
from constants.constant import *
from objects.Particle import *

class ParticleList:
    def __init__(self):
        self.particleList = []

        
    
    def addParticle(self, screen, x, y, image, width, height):
        particle = Particle(screen,x,y,image,width,height)
        self.particleList.append(particle)


    def update(self,delta):
        [particle.update(delta) for particle in self.particleList]

        self.particleList[:] = [x for x in self.particleList if not x.isSafeToDelete()]


    def draw(self):
        [particle.draw() for particle in self.particleList]

