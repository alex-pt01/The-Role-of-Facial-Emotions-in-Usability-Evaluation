import cv2
import tkinter as tk
from tkinter import filedialog

# Define a function to resample a video file to 30 fps
def resample_video(filename):
    video = cv2.VideoCapture(filename)
    fps = video.get(cv2.CAP_PROP_FPS)
    print("FPS:", fps)
    
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

   # Create a writer object to write the new video
    output_filename = '30fps_' + filename.split("/")[-1]
    writer = cv2.VideoWriter(output_filename, cv2.VideoWriter_fourcc(*'mp4v'), 30, frame_size)

    for i in range(frame_count):
        print(i)
        ret, frame = video.read()
        if not ret:
            break
        if i % round(fps / 30) == 0:
            writer.write(frame)

    # Release the video objects and writer
    video.release()
    writer.release()

    print("Resampled video saved to:", output_filename)  

def select_video():
    filename = filedialog.askopenfilename()
    if not filename:
        return

    file_label.config(text="Selected Video: " + filename)
    select_video.filename = filename

def start_resampling():
    if not hasattr(select_video, 'filename'):
        print("Please select a video file first.")
        return

    resample_video(select_video.filename)

root = tk.Tk()
root.title("Video frames to 30 fps converter")
root.geometry("295x90")

file_label = tk.Label(root, text="No video file selected.")
file_label.pack()

select_button = tk.Button(root, text="Select Video", command=select_video, width=30, font="arial 12 ")
select_button.pack()

resample_button = tk.Button(root, text="Resample Video", command=start_resampling,  width=30, font="arial 12 ")

resample_button.pack()

root.mainloop()