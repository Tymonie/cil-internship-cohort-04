from PIL import Image





img = Image.open("cgirl.jpg")

resized_img = img.resize((400, 400))

resized_img.save("resized_girl_d.jpg")





