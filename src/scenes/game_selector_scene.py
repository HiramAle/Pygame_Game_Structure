import src.assets as assets
import src.input as input
import src.scenes.scene_manager as scene_manager
from src.scenes.scene import Scene
from src.ui_objects import *
from src.modules.cables.order_cable_scene import OrderCableScene
from src.modules.subnetting.select_area_scene import SelectAreaScene


class GameSelectorScene(Scene):
    def __init__(self):
        super().__init__("gameSelectorScene")
        self.cablesIcon = Image((320 / 4, 70), assets.misc["cables_icon"])
        self.cablesIcon.interactive = True
        self.cablesTitle = Text((320 / 4, 110), "Cables", WHITE_MOTION)

        self.subnettingIcon = Image((320 / 4 * 2, 70), assets.misc["subnetting_icon"])
        self.subnettingIcon.interactive = True
        self.subnettingTitle = Text((320 / 4 * 2, 110), "Subnetting", WHITE_MOTION)

        self.routingIcon = Image((320 / 4 * 3, 70), assets.misc["routing_icon"])
        self.routingIcon.interactive = True
        self.routingTitle = Text((320 / 4 * 3, 110), "Routing", WHITE_MOTION)

        self.back = SquareButton((15, 15), "back")

        self.sprites.add(self.cablesIcon)
        self.sprites.add(self.subnettingIcon)
        self.sprites.add(self.routingIcon)
        self.sprites.add(self.cablesTitle)
        self.sprites.add(self.subnettingTitle)
        self.sprites.add(self.routingTitle)
        self.sprites.add(self.back)

    def update(self) -> None:
        self.update_cursor()

        if self.back.released() or input.keyboardKeys["ESC"]:
            scene_manager.exit_scene()

        if self.cablesIcon.clicked():
            self.transitionPosition = self.cablesIcon.position
            scene_manager.transition_scene(self, OrderCableScene())

        if self.subnettingIcon.clicked():
            self.transitionPosition = self.subnettingIcon.position
            scene_manager.transition_scene(self, SelectAreaScene())

    def render(self) -> None:
        self.display.fill(YELLOW_MOTION)
        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.sprites.render(self.display)
