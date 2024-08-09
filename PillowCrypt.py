from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image, dtype='int16')  # Convert to a higher data type to prevent overflow
    encrypted_pixels = (pixels + key) % 256
    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))  # Convert back to uint8
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image, dtype='int16')  # Convert to a higher data type to prevent overflow
    decrypted_pixels = (pixels - key) % 256
    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))  # Convert back to uint8
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    image_path = r"C:\Users\USER\Pictures\Saved Pictures\panda.jpg"
    encrypted_path = r"C:\Users\USER\Pictures\Saved Pictures\encrypted_panda.jpg"
    decrypted_path = r"C:\Users\USER\Pictures\Saved Pictures\decrypted_panda.jpg"
    key = 50  # You can change this value to any integer

    # Encrypt the image
    encrypt_image(image_path, encrypted_path, key)

    # Decrypt the image
    decrypt_image(encrypted_path, decrypted_path, key)
