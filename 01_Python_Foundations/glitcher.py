import random
import os

class FileCorruptionError(Exception):
    #Raised if we accidently destroy the header
    pass

def glitch_image(test_image , intensity=0.05):
    #will read img in binary mode .corrupts random bytes,
    if not os.path.exists(test_image):
        raise FileNotFoundError(f"target {test_image} not found!")
    
    with open(test_image , "rb") as f:
        data = f.read()

        #converting immutables bytes to mutable bytearray
        mutable_data = bytearray(data)

        file_size = len(mutable_data)
        print(f"file size: {file_size} bytes")

        header_safe_zone = int(file_size * 0.10)

        num_glitches = int((file_size - header_safe_zone) * intensity)
        #intensity controls corruption

        print(f"Injecting {num_glitches} errors...")

        try:
            for _ in range(num_glitches):
                #picking a random byte location after header
                position = random.randint(header_safe_zone,file_size-1)

                #injecting noise 
                mutable_data[position] = random.randint(0,255)

        except IndexError:
            raise FileCorruptionError("Index out of bounds! Calculation error.")

        output_name = "glitched_" + test_image
        with open(output_name,"wb") as f:
            f.write(mutable_data)

        print(f"Success! Created {output_name}")

if __name__ == "__main__":
    target = "test_image.jpg"  # Replace with your image file

    try:
        # Try a small glitch first
        glitch_image(target, intensity=0.02) 
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Something went wrong in the surgery: {e}")
