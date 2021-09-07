from .Image import Image
from constants.constant import *
from objects.Particle import *

class ParticleList:
    def __init__(self):
        self.ParticleList = []

        
    
    def addParticle(self, screen, x, y, image, width, height):
        particle = Particle(screen,x,y,image,width,height)
        self.ParticleList.append(particle)


    def update(self,delta):
        [particle.update(delta) for particle in self.ParticleList]


    def draw(self):
        [particle.draw() for particle in self.ParticleList]

