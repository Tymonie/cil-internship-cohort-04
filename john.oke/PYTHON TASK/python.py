from PIL import Image
​
def resize(width,height): 
​
    img = Image.open("snapshot.png")
    resized_img = img.resize((width,height ))
    resized_img.save("resized_snapshot.png")
resize(700,600) 