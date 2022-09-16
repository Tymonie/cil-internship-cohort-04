Question: Simple function to copy and resize a jpg file, submit in your student folder,
# Image.open()  #can also open other image types#
img = Image.open   #some_random_image.jpg#
# To Measure WIDTH and HEIGHT are integers#
resized_img = img.resize((WIDTH, HEIGHT))
resized_img.save("resized_image.jpg")
