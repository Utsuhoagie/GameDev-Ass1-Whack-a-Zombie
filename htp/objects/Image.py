class Image:
    def __init__(self, screen, x, y, image, width, height):
        self._screen = screen
        self._image = image
        self._width = width
        self._height = height
        self._x = x
        self._y = y

    def update(self, delta):
        pass

    def draw(self):
        self._screen.blit(self._image, (self._x, self._y))