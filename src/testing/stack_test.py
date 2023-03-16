class StackManager:
    def __init__(self):
        self._stack = []

    def enter(self, element: str):
        if not self.has_element(element):
            self._stack.append(element)
        else:
            self._stack = self._stack[:self._stack.index(element) + 1]

    def exit(self):
        if self.is_empty():
            return
        self._stack.pop()

    @property
    def stack(self) -> list:
        return self._stack

    def has_element(self, element: str) -> bool:
        if self.is_empty():
            return False
        if element not in self._stack:
            return False
        return True

    def is_empty(self) -> bool:
        return False if self._stack else True


if __name__ == '__main__':
    # Removable Scene: When scene ends, it's removed from the stack and enter the new scene
    manager = StackManager()
    manager.enter("loading")  # Removable Scene
    manager.enter("main_menu")
    manager.enter("options_menu")
    manager.exit()
    manager.enter("cinematic_1")  # Removable Scene
    manager.enter("game_house")
    manager.enter("town")
    manager.enter("city")
    manager.enter("cables")
    manager.exit()
    manager.enter("cables")
    manager.exit()
    manager.enter("subnetting")
    manager.enter("map")
    manager.enter("town")
    print(manager.stack)
    manager.enter("pause")
    print(manager.stack)
    manager.enter("main_menu")
    print(manager.stack)
