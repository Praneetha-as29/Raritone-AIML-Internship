from rembg import remove

with open("garment5.png", "rb") as inp:
    input_image = inp.read()

output_image = remove(input_image)

with open("garment6.png", "wb") as out:
    out.write(output_image)

print("Background removed successfully")