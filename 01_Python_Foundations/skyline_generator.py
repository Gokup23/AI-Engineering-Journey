import random

def generate_skyline(city_name):

    filename = f"{city_name}.html"

    with open(filename, "w") as f:

        f.write(f"<html><body><h1>The Skyline of {city_name}</h1>")

        #SVG(Scalable Vector Graphics) canvas
        f.write('<svg width="800" height="400" style="background-color:midnightblue">')

        x_position = 0
        while x_position < 800:
            # Randomize  dimensions
            width = random.randint(30, 80)
            height = random.randint(100, 350)
            
            # Randomize color 
            r = random.randint(50, 100)
            g = random.randint(0, 50)
            b = random.randint(100, 255)
            color = f"rgb({r},{g},{b})"
            
            # 4. Write the shape to the file
            # In HTML, a rectangle is: <rect x="..." y="..." width="..." height="..." />
            # Note: y is calculated from top (400 - height) so buildings sit on bottom
            rect_code = f'<rect x="{x_position}" y="{400-height}" width="{width}" height="{height}" fill="{color}" stroke="black" />\n'
            f.write(rect_code)
            
            # Add some "Windows" (Math + Nested Loop)
            # Only add windows if the building is wide enough
            if width > 40:
                window_rows = height // 40
                for row in range(window_rows):
                    win_y = (400 - height) + (row * 30) + 10
                    f.write(f'<rect x="{x_position+10}" y="{win_y}" width="10" height="15" fill="yellow" />\n')
                    f.write(f'<rect x="{x_position+width-20}" y="{win_y}" width="10" height="15" fill="yellow" />\n')

            # Move X to the next building spot
            x_position += width

        # 5. Close the tags
        f.write('</svg></body></html>')
        
    print(f"City generated! Open '{filename}' in Chrome/Edge to see it.")

# --- RUN IT ---
name = input("Name your city: ")
generate_skyline(name)