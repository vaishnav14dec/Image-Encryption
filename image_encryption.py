from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    data = np.array(img)
    encrypted_data = data ^ key
    encrypted_img = Image.fromarray(encrypted_data)
    encrypted_img.save("encrypted_image.png")

def decrypt_image(image_path, key):
    img = Image.open(image_path)
    data = np.array(img)
    decrypted_data = data ^ key
    decrypted_img = Image.fromarray(decrypted_data)
    decrypted_img.save("decrypted_image.png")

image_path = input("Enter image file path: ")
key = int(input("Enter an encryption key (integer): "))
encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)
