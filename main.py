import tkinter as t
import random as r
    
class Slide():
        def __init__(self, root, color1, statement1, color2, statement2):
            self.colors = (color1, color2)
            self.label = t.Label(root, text=statement1+"\t\t"+statement2)
            self.scale = t.Scale(root, from_=-100, to_=100, orient=t.HORIZONTAL, showvalue=0, length=200)
        def pack(self):
            self.label.pack()
            self.scale.pack()
        def f(self, n, pos=True): # silly function to format slider inputs
            if pos:
                if n > 0:
                    return n
                else:
                    return 0
            else:
                if n < 0:
                    return -n
                else:
                    return 0
        def get_score(self, color):
            self.score = {self.colors[0]:self.f(self.scale.get(),pos=False), self.colors[1]:self.f(self.scale.get(),pos=True)}
            try:
                result = self.score[color]
            except KeyError:
                result = 0
            finally:
                return result
class Menu():
    def __init__(self):
        root = t.Tk()
        root.geometry('{}x{}'.format(500, 500))
        root.wm_title("Color Quiz")
        
        title = t.Label(root, text="Change the slider to show how much you agree")

        slides = []
        slides.append(Slide(root, "white", "people should help others", "black", "people should help themselves"))
        slides.append(Slide(root, "white", "people should have safety", "red", "people should have freedom"))
        slides.append(Slide(root, "blue", "people should think decisions through", "red", "people should follow their hearts"))
        slides.append(Slide(root, "blue", "people should change who they are", "green", "people should accept who they are"))
        slides.append(Slide(root, "black", "people should have agency over their lives", "green", "people should follow their destiny"))
        r.shuffle(slides)
        self.slides = slides

        bframe = t.Frame(root)
        button1 = t.Button(bframe, text="EVALUATE", command=self.button_press)
        self.result = t.Label(root, text="")

        title.pack()
        for item in slides: item.pack()
        bframe.pack()
        button1.pack()
        self.result.pack()

        self.root = root
    def button_press(self):
        color_score ={"white":0, "blue":0, "black":0, "red":0, "green":0}
        for s in self.slides:
            for c in s.colors:
                color_score[c] += s.get_score(c)
        # insertion sort
        text = "In order of most points to least: "
        last_max = -1
        tot = sum(color_score.values())
        if tot == 0: tot = 1
        for i in range(len(color_score)):
            maximum = 0
            for c in color_score:
                if color_score[c] >= maximum:
                    maximum = color_score[c]
                    color = c
            percent = color+"-"+str(int(100*maximum/tot))+"%"
            if last_max != maximum:
                text += "\n" + str(i+1) + ". " + percent
            else:
                text += ", " + percent
            last_max = color_score.pop(color)
        
        self.result.config(text=text)
Menu()
