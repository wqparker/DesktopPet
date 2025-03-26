import sys
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel

def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller/py2app
    """
    if hasattr(sys, '_MEIPASS'):
        # For older versions of py2app, it might be sys._MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    # Fallback to the current file directory (development mode)
    return os.path.join(os.path.dirname(__file__), relative_path)

class DesktopPet(QLabel):
    def __init__(self, gif_path):
        super().__init__()

        # Load the GIF
        self.movie = QMovie(gif_path)
        print("Loading GIF from:", gif_path)
        print("Movie valid?", self.movie.isValid())
        print("Frame count:", self.movie.frameCount())

        # Make window frameless & always on top
        # Qt.Tool hides it from the Dock on macOS
        self.setWindowFlags(Qt.FramelessWindowHint | 
                            Qt.WindowStaysOnTopHint |
                            Qt.Tool)

        # Enable per-pixel alpha (transparent background)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # Optionally force an initial size to ensure the label isn't 0x0
        self.resize(200, 200)

        # Assign & start the GIF
        self.setMovie(self.movie)
        self.movie.start()

    def position_at_bottom_left(self, y_offset=63):
        """Place the pet near the bottom-left corner."""
        screen_rect = QApplication.desktop().availableGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()

        pet_width = self.width()
        pet_height = self.height()

        x = 0
        y = screen_height - pet_height + y_offset
        self.move(x, y)

    def position_at_bottom_right(self, y_offset=63):
        """Place the pet near the bottom-right corner."""
        screen_rect = QApplication.desktop().availableGeometry()
        screen_width = screen_rect.width()
        screen_height = screen_rect.height()

        pet_width = self.width()
        pet_height = self.height()

        x = screen_width - 128
        y = screen_height - pet_height + y_offset
        self.move(x, y)

def main():
    app = QApplication(sys.argv)

    # Create first pet (bottom-left)
    pet_left = DesktopPet(resource_path("Gifs/Johnny_Idle_4x.gif"))
    pet_left.show()
    # Let PyQt update the widget size
    app.processEvents()
    pet_left.position_at_bottom_left()

    # Create second pet (bottom-right) - can be the same or a different GIF
    pet_right = DesktopPet(resource_path("Gifs/Nelly_Idle_4x.gif"))
    pet_right.show()
    app.processEvents()
    pet_right.position_at_bottom_right()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
