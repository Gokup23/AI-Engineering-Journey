from PIL import Image

class ASCIIConverter:
    def __init__(self, image_path, new_width=100):
        self.path = image_path
        self.new_width = new_width
        # The list of characters from Dark (@) to Light (.)
        self.ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    def load_image(self):
        try:
            # We use Image.open from PIL, not standard open()
            img = Image.open(self.path)
            return img
        except Exception as e:
            print(f"Unable to find image: {e}")
            return None

    def resize_image(self, image):
        # 1. Get current dimensions
        width, height = image.size
        
        # 2. Calculate aspect ratio
        # We multiply height by 0.55 because terminal characters are rectangular
        # If we dont do this, the image looks stretched vertically
        ratio = height / width / 1.65 
        new_height = int(self.new_width * ratio)
        
        # 3. Resize the image
        resized_image = image.resize((self.new_width, new_height))
        return resized_image

    def grayscale_image(self, image):
        # Convert the image to L mode (Luminance)
        # This turns every pixel into a number from 0 (black) to 255 (white)
        return image.convert("L")

    def pixels_to_ascii(self, image):
        # Get list of pixel data
        pixels = image.getdata()
        characters = ""
        
        for pixel in pixels:
            # Pixel is 0-255. We divide by 25 to get a number 0-10
            # This matches the index of our ascii_chars list
            characters += self.ascii_chars[pixel // 25]
            
        return characters

    def convert(self):
        print("Processing...")
        
        # Step 1: Load
        img = self.load_image()
        if img is None:
            return

        # Step 2: Resize (Crucial for text alignment)
        img = self.resize_image(img)

        # Step 3: Grayscale (Color to Brightness)
        img = self.grayscale_image(img)

        # Step 4: Map pixels to characters
        ascii_str = self.pixels_to_ascii(img)
        
        # Step 5: Formatting
        # The ascii_str is currently one giant line. We need to break it
        # into multiple lines based on the width.
        img_width = self.new_width
        ascii_img = ""
        
        for i in range(0, len(ascii_str), img_width):
            ascii_img += ascii_str[i:i+img_width] + "\n"

        # Step 6: Save to file
        with open("ascii_art.txt", "w") as f:
            f.write(ascii_img)
            
        print("Done. Check ascii_art.txt")

# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    # Get input from user here, not in the class
    user_path = input("Enter image filename (e.g., bike.jpg): ")
    
    # Create the object
    converter = ASCIIConverter(user_path)
    
    # Run the process
    converter.convert()