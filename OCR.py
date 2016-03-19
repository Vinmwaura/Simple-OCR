import numpy as np
import tkinter


class OCR:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Simple OCR")
        self.window.geometry("300x300")
        self.window.mainloop()

def main():
    ocr = OCR()

if __name__ == '__main__':
    main()
