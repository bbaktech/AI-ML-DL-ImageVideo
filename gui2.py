import tkinter as tk
from tkinter import *
from tkinter import ttk
import numpy as np
from PIL import ImageTk, Image
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator

emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('emotion_model.h5')

cv2.ocl.setUseOpenCL(False)

emotion_dict = {0: "   Angry   ", 1: "Disgusted", 2: "  Fearful  ", 3: "   Happy   ", 4: "  Neutral  ", 5: "    Sad    ", 6: "Surprised"}

emoji_dist={0:"./emojis/angry.png", 1:"./emojis/disgusted.png", 2:"./emojis/fearful.png", 3:"./emojis/happy.png", 4:"./emojis/neutral.png", 5:"./emojis/sad.png", 6:"./emojis/surpriced.png"}
global last_frame1
last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
global cap1
show_text = [0]

class karl( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.pack()
        self.master.title("Emotion Recognation App")

        img = ImageTk.PhotoImage(Image.open("./emojis/angry.png"))
        self.vcapture = Label(self, image = img)
        self.vcapture.grid( row = 0, column = 1, columnspan = 2, sticky = W+E+N+S )

        self.button1 = Button( self, text = "Display Emotion", width = 25,
                               command = self.new_window )
        self.button1.grid( row = 1, column = 1, columnspan = 2, sticky = W+E+N+S )
        img1 = ImageTk.PhotoImage(Image.open("./emojis/angry.png"))
        self.vcapture2 = Label(self, image = img1)
        self.vcapture2.grid( row = 2, column = 1, columnspan = 2, sticky = W+E+N+S )
        self.vcapture3 = Label(self,text = "")
        self.vcapture3.grid( row = 3, column = 1, columnspan = 2, sticky = W+E+N+S )

    def new_window(self):
        vid = cv2.VideoCapture(0)
        if not vid.isOpened():
            print("cant open the camera")
        while True:
            ret, frame1 = vid.read()
            frame1 = cv2.resize(frame1,(300,250))
            bounding_box = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            num_faces = bounding_box.detectMultiScale(gray_frame,scaleFactor=1.3, minNeighbors=5)
            #detectMultiScale function must return detected object otherwise emotion will not be detected
            if len(num_faces) > 0:
                break

        for (x, y, w, h) in num_faces:
            cv2.rectangle(frame1, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
            roi_gray_frame = gray_frame[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
            prediction = emotion_model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            cv2.putText(frame1, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            show_text[0]=maxindex

        global last_frame1
        last_frame1 = frame1.copy()
        pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(pic)

        imgtk = ImageTk.PhotoImage(image=img)
        self.vcapture.imgtk = imgtk
        self.vcapture.configure(image=imgtk)

        frame2=cv2.imread(emoji_dist[show_text[0]])
        pic2=cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        img2=Image.fromarray(frame2)

        imgtk2=ImageTk.PhotoImage(image=img2)
        self.vcapture2.imgtk = imgtk2
        self.vcapture2.configure(image=imgtk2)
        self.vcapture3.configure(text= emoji_dist[show_text[0] ])
        vid.release()
        cv2.destroyAllWindows()
        self.pack()

def main():
    karl().mainloop()

if __name__ == '__main__':
    main()
