from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width=600, height=350)
canvas.pack()



def Imagenes():
    my_image = PhotoImage(file="fondo.gif")
    canvas.create_image(0,0,anchor=NW, image= my_image)

    my_image1 = PhotoImage(file="arco2.gif")
    canvas.create_image(450, 100, anchor=NW, image=my_image1)

    my_image2 = PhotoImage(file="arco.gif")
    canvas.create_image(-50, 100, anchor=NW, image=my_image2)

    my_image3 = PhotoImage(file="balon.gif")
    canvas.create_image(300, 130, anchor=NW, image=my_image3)
    tk.mainloop()
#
def movebalon(event):
    marcadorA = 0;
    marcadorB = 0;
    if event.keysym == 'Left':

        for x in range(0,80):
            canvas.move(4,-3,0)
            tk.update()
            time.sleep(0.01)
        print("posicion en X es :")
        print("GOLL!!!!!!!")
        print("Equipo A")

        # canvas.move(3,-3,0)
        marcadorA=marcadorA+1;

    else:
        for x in range(0,80):
            canvas.move(4,3,0)
            tk.update()
            time.sleep(0.01)
        print("GOLL!!!!!!!")
        print("Equipo b")
        marcadorB = marcadorB+1

    print(str(marcadorA)+"--"+str(marcadorB))
canvas.bind_all('<KeyPress-Left>',movebalon)
canvas.bind_all('<KeyPress-Right>',movebalon)

Imagenes()








