from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os

def make_square(im, min_size=300, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
dir, a = os.path.split(file_path)
test_image = Image.open(file_path)
new_image = make_square(test_image, fill_color=(255, 255, 255, 0))
new_image.save(dir + '/parced.png')

