class FigureColor():
    def __init__(self, color: str) -> None:
        self._color = color

    @property
    def color(self) -> str:
        ''' Square name getter. '''
        return self._color
