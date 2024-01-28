import tkinter as tk
from ttkthemes import ThemedStyle
from PIL import Image, ImageTk
from layout.secure_vigil import Securevigil

if __name__ == "__main__":
    detector = Securevigil()
    detector.run()