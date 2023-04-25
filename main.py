import customtkinter as ctk
import tkinter as tk

root = ctk.CTk()
root.title("Song generator")

ctk.set_appearance_mode("dark")

input_frame = ctk.CTkFrame(root)
input_frame.pack(side = 'left', expand = True, padx = 20, pady = 20)

prompt_label = ctk.CTkLabel(input_frame, text="Prompt")
prompt_label.grid(row = 0, column = 0, padx = 20, pady = 20)

prompt_entry = ctk.CTkTextbox(input_frame, height = 10)
prompt_entry.grid(row = 0, column = 1, padx = 20, pady = 20)

generate_button = ctk.CTkButton(input_frame, text="Generate")
generate_button.grid(row = 1, column = 0,columnspan = 2, sticky = 'news', padx = 10, pady = 10)


canvas = ctk.CTkCanvas(root, width = 500, height = 500)
canvas.pack(side = 'left')




root.mainloop()