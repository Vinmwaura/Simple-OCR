import numpy as np
import tkinter


class OCR:
    def __init__(self):
        self.key_state = 0
        self.x_val, self.y_val = None, None
        self.window = None
        self.drawing_area = None
        self.character_option = None
        self.initWindow()

    def initWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Simple OCR")
        # self.window.geometry("300x300")
        self.points = []
        
        self.drawing_area = tkinter.Canvas(self.window, width=256, height=256, background="white")

        self.character_option = tkinter.IntVar()
        self.character_option.set(0)
        self.number = tkinter.Radiobutton(self.window, text="Number", value=0,variable=self.character_option)
        self.letter = tkinter.Radiobutton(self.window, text="Letter", value=1,variable=self.character_option)
        
        self.lblCharacter = tkinter.Label(self.window, text="Character: ")

        self.btnClear = tkinter.Button(self.window, text="Clear", command=self.clear_canvas)
        self.btnCompute = tkinter.Button(self.window, text="Compute", command=self.compute_character)
  
        self.drawing_area.bind("<Motion>", self.mouse_moved)
        self.drawing_area.bind("<ButtonPress-1>", self.mouse_key_pressed)
        self.drawing_area.bind("<ButtonRelease-1>", self.mouse_key_released)
        
        self.drawing_area.pack()
        self.number.pack()
        self.letter.pack()
        self.lblCharacter.pack(pady=10)
        self.btnClear.pack()
        self.btnCompute.pack()

        self.window.mainloop()

    def clear_canvas(self):
        self.drawing_area.delete("all")
        self.points = []

    def compute_character(self):
        print(self.points)

    def mouse_key_pressed(self, event):
        self.key_state = 1

    def mouse_key_released(self, event):
        self.key_state = 0

    def mouse_moved(self, event):
        if self.key_state == 1:
            if self.x_val is not None and self.y_val is not None:
                event.widget.create_line(self.x_val,self.y_val,event.x,event.y,smooth=True)
            self.x_val = event.x
            self.y_val = event.y
            if self.x_val > 0 and self.y_val > 0:
                self.points.append((self.y_val, self.x_val))
            # print("X: ", self.x_val, "Y: ", self.y_val)

def main():
    ocr = OCR()

if __name__ == '__main__':
    main()
