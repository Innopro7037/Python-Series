import qrcode
import tkinter as tk
from PIL import ImageTk, Image
from ttkbootstrap import Style 
import tkinter.ttk as ttk

root = tk.Tk()
root.title('QR Code Generator')
root.geometry('500x500')
style = Style(theme='flatly')
style.theme_use()

def generate_qr_code():
    # get text
    text = text_entry.get()

    # create qr code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    #display
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.configure(image=img_tk)
    qr_label.image = img_tk

text_label = ttk.Label(master=root, text='Enter Text or URL:')
text_label.pack(pady=10)

text_entry = ttk.Entry(master=root, width=50)
text_entry.pack()

generate_button = ttk.Button(master=root, text='Generate QR Code', command=generate_qr_code, style='success.TButton')
generate_button.pack(pady=10)

qr_label = ttk.Label(master=root)
qr_label.pack()

root.mainloop()