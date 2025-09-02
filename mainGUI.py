import os
from tkinter import filedialog
import customtkinter as ctk
import pyautogui
import pygetwindow
from PIL import ImageTk, Image
from predictions import predict
project_folder = os.path.dirname(os.path.abspath(__file__))
folder_path = project_folder + '/images/'
filename = ""
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Arabic Sign Language Reader")
        self.geometry(f"{500}x{700}")
        self.head_frame = ctk.CTkFrame(master=self)
        self.head_frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.main_frame = ctk.CTkFrame(master=self)
        self.main_frame.pack(pady=20, padx=60, fill="both", expand=True)
        self.head_label = ctk.CTkLabel(master=self.head_frame, text="Arabic Sign Language Reader",
                                       font=(ctk.CTkFont("Roboto"), 20))
        self.head_label.pack(pady=20, padx=10, anchor="nw", side="left")
        self.info_label = ctk.CTkLabel(master=self.main_frame,
                                       text="Upload an image of a hand sign to predict the Arabic letter.",
                                       wraplength=300, font=(ctk.CTkFont("Roboto"), 20))
        self.info_label.pack(pady=10, padx=10)
        self.upload_btn = ctk.CTkButton(master=self.main_frame, text="Upload Image", command=self.upload_image)
        self.upload_btn.pack(pady=0, padx=1)
        self.frame2 = ctk.CTkFrame(master=self.main_frame, fg_color="transparent", width=256, height=256)
        self.frame2.pack(pady=10, padx=1)
        img = Image.open(folder_path + "Question_Mark.jpg")
        img_resized = img.resize((int(256 / img.height * img.width), 256))
        img = ImageTk.PhotoImage(img_resized)
        self.img_label = ctk.CTkLabel(master=self.frame2, text="", image=img)
        self.img_label.pack(pady=1, padx=10)
        self.predict_btn = ctk.CTkButton(master=self.main_frame, text="Predict", command=self.predict_gui)
        self.predict_btn.pack(pady=0, padx=1)
        self.result_frame = ctk.CTkFrame(master=self.main_frame, fg_color="transparent", width=200, height=100)
        self.result_frame.pack(pady=5, padx=5)
        self.loader_label = ctk.CTkLabel(master=self.main_frame, width=100, height=100, text="")
        self.loader_label.pack(pady=3, padx=3)
        self.res_label = ctk.CTkLabel(master=self.result_frame, text="")
        self.res_label.pack(pady=5, padx=20)
        self.save_btn = ctk.CTkButton(master=self.result_frame, text="Save Result", command=self.save_result)
        self.save_label = ctk.CTkLabel(master=self.result_frame, text="")
    def upload_image(self):
        global filename
        f_types = [("All Files", "*.*")]
        filename = filedialog.askopenfilename(filetypes=f_types, initialdir=project_folder+'/RGB ArSL dataset/')
        self.save_label.configure(text="")
        self.res_label.configure(text="")
        self.img_label.configure(self.frame2, text="", image="")
        img = Image.open(filename)
        img_resized = img.resize((int(256 / img.height * img.width), 256))
        img = ImageTk.PhotoImage(img_resized)
        self.img_label.configure(self.frame2, image=img, text="")
        self.img_label.image = img
        self.save_btn.pack_forget()
        self.save_label.pack_forget()
    def predict_gui(self):
        global filename
        result = predict(filename)
        print(result)
        self.res_label.configure(text_color="GREEN", text=f"letter: {result}", font=(ctk.CTkFont("Roboto"), 24))
        self.save_btn.pack(pady=10, padx=1)
        self.save_label.pack(pady=5, padx=20)
    def save_result(self):
        tempdir = filedialog.asksaveasfilename(parent=self, initialdir=project_folder + '/PredictResults/',
                                               title='Please select a directory and filename', defaultextension=".png")
        screenshots_dir = tempdir
        window = pygetwindow.getWindowsWithTitle('Arabic Sign Language Reader')[0]
        left, top = window.topleft
        right, bottom = window.bottomright
        pyautogui.screenshot(screenshots_dir)
        im = Image.open(screenshots_dir)
        im = im.crop((left + 10, top + 35, right - 10, bottom - 10))
        im.save(screenshots_dir)
        self.save_label.configure(text_color="WHITE", text="Saved!", font=(ctk.CTkFont("Roboto"), 16))
    def open_image_window(self):
        im = Image.open(folder_path + "rules.jpg")
        im = im.resize((700, 700))
        im.show()
if __name__ == "__main__":
    app = App()
    app.mainloop()