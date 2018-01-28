from UIElement import *


class Panel(UIElement):
    elements = []

    def __init__(self, position: Vector2, size: Vector2):
        super().__init__(position, size, Styles.gray_panel)

        self.id = Iders.panelIder.add(self)

        print("Initialized Panel with id " + self.id + ", in coordinates (" + str(position.x) + ", " + str(
            position.y) + "), with size(" + str(self.size.x) + ", " + str(self.size.y) + ")")

    def add(self, element: UIElement):
        if isinstance(element, InteractableUIElement):
            element.set_pos(element.position + self.position)
        self.elements.append(element)

    def draw(self, starting_point: Vector2 = None):
        super().draw()
        for element in self.elements:
            element.draw(self.position)
