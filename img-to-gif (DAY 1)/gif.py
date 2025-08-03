from PIL import Image

image_files = ["1.jpg", "2.jpg", "3.jpg"]

images = [Image.open(image) for image in image_files]

images[0].save(
    "output2.gif", # name of output file
    save_all=True,
    append_images=images[1:],
    duration=400,  # 300 milli secondz
    loop=1         # 0 means forever and ever and ever, 1,2,3 would mean loop that many times
)