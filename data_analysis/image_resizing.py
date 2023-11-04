from PIL import Image # pip install Pillow
img = Image.open('img/photo1.jpg')
img.thumbnail((300,500))
img.save('img/new_photo1.jpg', quality=95)