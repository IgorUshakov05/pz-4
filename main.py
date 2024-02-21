from PIL import Image, ImageDraw, ImageFont
img = Image.open('img.png')
img.show()

img = img.resize((170, 100))
img.save('test_text.jpg')
img = Image.open('test_text.jpg')
img.show()

print(img.format) # Просмотр формата изображения. Выведет 'JPEG'
print(img.mode) # Просмотр типа цветового пространства. Выведет 'RGB'
print(img.size) # Просмотр размера изображения.
print(img.filename) # Просмотр имени файла.
r, g, b = img.split()
histogram = img.histogram()
print(histogram) # Просмотр значений RGB изображения.

cropped = img.crop((0, 0, 100, 200))
cropped.save('cropped_test.jpg')
img = Image.open('cropped_test.jpg')
img.show()

rotated = img.rotate(180)
rotated.save('rotated_test.jpg')
img = Image.open('rotated_test.jpg')
img.show()
img.save('test_png.png', 'png')
img.show()

font = ImageFont.truetype("arial.ttf", size=20)
idraw = ImageDraw.Draw(img)
idraw.text((25, 25), 'TEST test TeSt', font=font)
img.save('test_text.jpg')
img = Image.open('test_text.jpg')
img.show()

img = Image.new('RGB', (200, 200), 'black')
img.save('test1.jpg')
img = Image.open('test1.jpg')
img.show()

img = Image.new('RGB', (200, 200), 'black')
idraw = ImageDraw.Draw(img)
idraw.rectangle((0, 0, 100, 100), fill='white')
img.save('test1.jpg')
img = Image.open('test1.jpg')
img.show()

# Мы разобрали основные методы библиотеки Pillow в Python: научились писать текст на изображениях, изменять размер, поворачивать их и даже обрезать.