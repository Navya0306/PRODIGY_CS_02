from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    # Load the image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Perform a simple encryption by adding the key to the pixel values
    encrypted_array = (img_array + key) % 256

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    # Load the encrypted image
    img = Image.open(input_image_path)
    img_array = np.array(img)

    # Perform decryption by subtracting the key from the pixel values
    decrypted_array = (img_array - key) % 256

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_image_path)

# Example usage
if __name__ == "__main__":
    key = 50  # Example key
    encrypt_image('input.jpg', 'encrypted_image.png', key)
    decrypt_image('encrypted_image.png', 'decrypted_image.png', key)