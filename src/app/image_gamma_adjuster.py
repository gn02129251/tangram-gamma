# -*- coding: utf-8 -*-
"""
Created on Wed 07 Feb 2024

Author: YIJU WU (gn02129251)

File: image_gamma_adjuster.py

Topic: An application for adjusting image gamma

"""
import sys
import cv2
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from src.gamma_process_lib import gamma_correction
from app import App

cv2.samples.addSamplesDataSearchPath("data/inputs/")

DEFAULT_GAMMA_VAL = 1.0
GAMMA_SLIDER_RESOLUTION = 0.01
GAMMA_VAL_LOWER_BOUND = 0.1
GAMMA_VAL_UPPER_BOUND = 3.0


class ImgGammaAdjuster(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("")
        self.resizable(width=True, height=True)
        self.create_wdigets()

    def create_wdigets(self) -> None:
        # Set the original image
        self.original_img = cv2.imread(cv2.samples.findFile("lena.jpg"))

        # Show the reference image at (0, 0)
        self.ref_img = self.cv2_to_tk_img(self.original_img)
        self.ref_img_label = ttk.Label(self, image=self.ref_img)
        self.ref_img_label.grid(row=0, column=0, sticky="wens")

        # Show the corrected image at (0, 1)
        self.corrected_img = self.cv2_to_tk_img(self.original_img)
        self.corrected_img_label = ttk.Label(self, image=self.corrected_img)
        self.corrected_img_label.grid(row=0, column=1, sticky="wens")

        # Add a button at (1,0) for changing images
        self.change_img_btn = ttk.Button(
            self, text="Change Image", width=15, command=self.change_img
        )
        self.change_img_btn.grid(row=1, column=0, sticky="ns")

        # Add a slider at (1, 1) for adjusting image gamma
        self.gamma_slider = tk.Scale(
            self,
            from_=GAMMA_VAL_LOWER_BOUND,
            to=GAMMA_VAL_UPPER_BOUND,
            resolution=GAMMA_SLIDER_RESOLUTION,
            orient="horizontal",
            command=self.update_corrected_img,
        )
        self.gamma_slider.set(DEFAULT_GAMMA_VAL)
        self.gamma_slider.grid(row=1, column=1, sticky="ew")

    def cv2_to_tk_img(self, img) -> ImageTk.PhotoImage:
        cv2_img = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(cv2_img)
        tk_img = ImageTk.PhotoImage(pil_img)

        return tk_img

    def update_corrected_img(self, gamma_val) -> None:
        self.corrected_img = gamma_correction(self.original_img.copy(), float(gamma_val))
        self.corrected_img = self.cv2_to_tk_img(self.corrected_img)
        self.corrected_img_label.configure(image=self.corrected_img)

    def change_img(self) -> None:
        # Open a file dialog to select an image file
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tif;*.tiff")]
        )

        if filepath:
            # Load the selected image
            self.original_img = cv2.imread(filepath)

            # Update the reference image
            self.ref_img = self.cv2_to_tk_img(self.original_img)
            self.ref_img_label.configure(image=self.ref_img)

            # Reset the gamma slider value
            self.gamma_slider.set(DEFAULT_GAMMA_VAL)

            # Update the corrected image
            self.update_corrected_img(DEFAULT_GAMMA_VAL)


def main(*args):
    # Create an application
    app = ImgGammaAdjuster("ImgGammaAdjuster Beta")

    # End the application when click "X" at the righttop conrner of the app window
    app.protocol("WM_DELETE_WINDOW", sys.exit)

    # Run the application
    app.mainloop()

    return 0


if __name__ == "__main__":
    main()
