import qrcode
import os
data = input("Enter data : ")

x = type(data)

print(" Your data was : ",data)
print(" THat the type of data is :", x)
img = qrcode.make(data)

folder_path = r"D:\Python"
file_path = os.path.join(folder_path, "qrcode.png")
img.save(file_path)

print("Saved to :", folder_path)