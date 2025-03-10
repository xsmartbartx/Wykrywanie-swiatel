from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import object_detection as od
import imageio
import cv2

class Window(Frame):
    def__init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pos = []
        self.line = []
        self.rect = []
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        self.counter = 0
        menu = Menu(self.master)
        self.master.config(menu)
        file = Menu(menu)
        file.add_command(label="Open", command=self.open_file)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(labe="File", menu=file)
        analyze = Menu(menu)
        analyze.add_command(label="Region of Interest", command=self.regionOfInterest)
        menu.add_cascade(labe="File", menu=analyze)
        self.filename = "Images/home.jpg"
        self.imgSize = Image.open(self.filename)
        self.tkimage = = ImageTk.PhotoImage(self.imgSize)
        self.w, self.h = (1366, 768)
        self.canvas = Canvas(master=root, width=self.w, height=self.h)
        self.canvas.create_image(20, 20, image=self.tkimage, anchor='nw')
        self.canvas.pack()
    def open_file(self):
        self.filename = filedialog.askopenfilename()
        cap = cv2.VideoCapture(self.filename)
        reader = imageio.get.reader(self.filename)
        fps = reader.get_meta_data()['fps']
        ret, image = cap.read()
        cv2.imwrite('G:/Traffic Violation Detection/Traffic Signal Violation Detection System/Images/preview.jpg', image)
        self.show_image('')
    def show_image(self, frame):
        self.imgSize = Image.open(frame)
        self.tkimage = ImageTk.PhotoImage(self.imgSize)
        self.w, self.h = (1366, 768)
        self.canvas.destroy()
        self.canvas = Canvas(master=root, width=self.w, height=self.h)
        self.canvas.create_image(0, 0, image=self.tkimage, anchor 'nw')
        self.canvas.pack()
    def regionOfInterest(self):
        root.config(cursor="plus")
        self.canvas.bind("<Button-1>", self.imgClick)
    def client_exit(self):
        exit()
