import pyautogui
import os
import tkinter as tk
import threading
import random
import time
from tkinter import messagebox
from tkinter import *


class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Tracker")
       
        #Botão que chama a função kill_process
        kill = Button(self.root, text="Sair", command=self.kill_process)
        kill.pack(pady=20)      

        #Textos apresentados dentro da janela. Não conheço outro modo de adicionar duas linhas de texto se não assim.
        #O código fica um pouco poluído, vou aprimorar essa parte.
        self.label = tk.Label(root, text="Coordenadas do Mouse: (X, Y)")
        self.label2 = tk.Label(root, text="Utilize Alt + Tab para selecionar a janela desejada")
        self.label3 = tk.Label(root, text="Pressione Tab e em seguida espaço para encerrar o programa")
        self.label.pack()
        self.label2.pack()
        self.label3.pack()
        root.geometry("400x200")
        
        
         
        

        self.keep_running = True
        self.start_mouse_movement()

        self.update_coordinates()

    def start_mouse_movement(self):
        self.mouse_thread = threading.Thread(target=self.move_mouse_randomly)
        self.mouse_thread.start()

    def move_mouse_randomly(self):
        try:
            while self.keep_running:
                x = random.randint(1, 1919)
                y = random.randint(1, 1078)
                pyautogui.moveTo(x, y, 0.5)
                time.sleep(0.5)
        except Exception as e:
            print("Erro:", e)

    def update_coordinates(self):
        x, y = pyautogui.position()
        self.label.config(text=f"Coordenadas do Mouse: ({x}, {y})")
        if self.keep_running:
            self.root.after(5, self.update_coordinates)  # Atualiza a cada 100 milissegundos

    def kill_process(self):
        pid = os.getpid()
        os.kill(pid, 9)


def main():
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    app = MouseTrackerApp(root)
    root.mainloop()



if __name__ == "__main__":
    main()
