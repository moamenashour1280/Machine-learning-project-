import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np

# Load the Keras model
# model = tf.keras.models.load_model('Image_classify.keras')
# Assuming your model outputs text labels

def predict_image_label(image_path):
    # Load and preprocess the image
    img = Image.open(image_path).resize((224, 224))  # Adjust size as needed
    img_array = np.array(img) / 255.0  # Normalize pixel values
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Perform prediction using the loaded model
    prediction = model.predict(img_array)
    predicted_label = 'Predicted Label: ' + str(prediction)  # Replace this with your label processing logic
    return predicted_label

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        label_text.set("Loading and predicting...")
        predicted_label = predict_image_label(file_path)
        label_text.set(predicted_label)
        # Load and display the selected image in the GUI
        img = Image.open(file_path).resize((300, 300))  # Adjust size as needed
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img

# Create Tkinter window
root = tk.Tk()
root.title("Image Classification")

# Create GUI components
button = tk.Button(root, text="Select Image", command=select_image)
button.pack()

image_label = tk.Label(root)
image_label.pack()

label_text = tk.StringVar()
result_label = tk.Label(root, textvariable=label_text)
result_label.pack()

root.mainloop()
