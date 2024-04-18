import pyautogui
import tkinter as tk
import threading
import random
import time

class MouseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mouse Tracker")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.label = tk.Label(root, text="Coordenadas do Mouse: (X, Y)")
        self.label.pack()

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

    def on_close(self):
        self.keep_running = False
        self.root.destroy()

def main():
    root = tk.Tk()
    app = MouseTrackerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()