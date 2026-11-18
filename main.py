from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode
from direct.gui.OnscreenText import OnscreenText

class MultiplayerSnakeGame(ShowBase):
    """
    3D Multiplayer Snake Game built using Panda3D as a B.Tech CSE academic project.
    Supports multi-player arcade logic and 3D environment rendering.
    """
    def __init__(self):
        ShowBase.__init__(self)
        
        # Configure window title
        self.window_title = "3D Multiplayer Snake Game - B.Tech CSE Project"
        self.setBackgroundColor(0.1, 0.1, 0.15)
        
        # On-screen UI instruction banner
        self.title_text = OnscreenText(
            text="3D Multiplayer Snake Game (Panda3D)",
            pos=(0.0, 0.85),
            scale=0.07,
            fg=(1, 1, 1, 1),
            align=TextNode.ACenter
        )
        
        self.instructions = OnscreenText(
            text="Use Arrow Keys / WASD to control players. Press ESC to exit.",
            pos=(0.0, -0.85),
            scale=0.05,
            fg=(0.8, 0.8, 0.8, 1),
            align=TextNode.ACenter
        )

if __name__ == "__main__":
    game = MultiplayerSnakeGame()
    game.run()