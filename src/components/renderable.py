from pygame import Surface 
import pygame

class Renderable:
    def __init__(self, image: Surface, layer=0, position=(0, 0)):
        """
        Initialize the Renderable object.
        
        :param image: The image to be rendered.
        :param layer: The layer on which the image will be rendered.
        :param position: The position of the image on the screen.
        """
        self.image = image
        self.layer = layer
        self.pos = position
        self.visible = True


