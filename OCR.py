import numpy as np
import tkinter

import process
import neural_network


class OCR:
    def __init__(self):
        self.key_state = 0
        self.x_val, self.y_val = None, None
        self.window = None
        self.drawing_area = None

        self.process = process.Process()
        self.neural_net = neural_network.NeuralNetwork()

        self.character_option = None
        self.initWindow()

    def initWindow(self):
        self.window = tkinter.Tk()
        self.window.title("Simple OCR")
        self.points = []
        
        self.drawing_area = tkinter.Canvas(self.window, width=256, height=256, background="white")

        self.character_option = tkinter.IntVar()
        self.character_option.set(0)
        self.number = tkinter.Radiobutton(self.window, text="Number", value=0,variable=self.character_option)
        self.letter = tkinter.Radiobutton(self.window, text="Letter", value=1,variable=self.character_option)
        
        self.lblCharacter = tkinter.Label(self.window, text="Character: ")
        self.lblComputed = tkinter.Label(self.window, text="")

        self.btnClear = tkinter.Button(self.window, text="Clear", command=self.clear_canvas)
        self.btnCompute = tkinter.Button(self.window, text="Compute", command=self.compute_character)
  
        self.drawing_area.bind("<Motion>", self.mouse_moved)
        self.drawing_area.bind("<ButtonPress-1>", self.mouse_key_pressed)
        self.drawing_area.bind("<ButtonRelease-1>", self.mouse_key_released)
        
        self.drawing_area.grid(column = 0, row = 0, columnspan=2)
        self.number.grid(column = 0, row = 1)
        self.letter.grid(column = 1, row = 1)
        self.lblCharacter.grid(column = 0, row = 2)
        self.lblComputed.grid(column = 1, row = 2)
        self.btnClear.grid(column = 0, row = 3)
        self.btnCompute.grid(column = 1, row = 3)

        self.window.mainloop()

    def clear_canvas(self):
        self.drawing_area.delete("all")
        self.points = []
        self.x_val, self.y_val = None, None
        self.lblComputed.config(text="")

    def compute_character(self):
        if len(self.points) > 0:
            status = self.character_option.get()
            pixels = self.get_pixel_points()
            input_image = self.process.process_image(pixels)
            character = self.neural_net.compute_character(input_image, status)
            self.lblComputed.config(text=character)
        
    def mouse_key_pressed(self, event):
        self.key_state = 1

    def get_pixel_points(self):
        pixel_point = []
        if len(self.points):
            for point in self.points:
                x, y = point
                
                for num in range(1,3):
                    neighbours = [
                        (x, y-num),
                        (x-num, y-num),
                        (x-num, y),
                        (x-num, y+num),
                        (x, y+num),
                        (x+num, y+num),
                        (x+num, y),
                        (x+num, y-num),
                    ]

                    for neighbour in neighbours:
                        if neighbour not in pixel_point:
                            pixel_point.append(neighbour)
                pixel_point.extend(self.points)
        return pixel_point 

    def mouse_key_released(self, event):
        self.key_state = 0
        self.x_val, self.y_val = None, None

    def mouse_moved(self, event):
        if self.key_state == 1:
            if self.x_val is not None and self.y_val is not None:
                event.widget.create_line(self.x_val,self.y_val,event.x,event.y,smooth=True, width=7)
            self.x_val = event.x
            self.y_val = event.y
            if self.x_val > 0 and self.y_val > 0:
                self.points.append((self.y_val, self.x_val))
            # print("X: ", self.x_val, "Y: ", self.y_val)

def main():
    ocr = OCR()

if __name__ == '__main__':
    main()
