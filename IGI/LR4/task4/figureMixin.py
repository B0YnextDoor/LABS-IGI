class FigureMixin(object):
    def __str__(self) -> str:
        ''' Method returns figure info. '''
        return 'Name: {}\nColor: {}\nSide: {}\nArea: {}'.format(self.name, self.color.color, self.side, self.area())
