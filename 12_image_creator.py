#!/usr/bin/env python3
"""
Digital Image Creator - Create and save digital images
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_digital_image():
    """Create a digital image with customizable properties"""
    print("=== Digital Image Creator ===")
    
    # Get image dimensions
    try:
        width = int(input("Enter image width (pixels, default 400): ") or "400")
        height = int(input("Enter image height (pixels, default 300): ") or "300")
    except ValueError:
        width, height = 400, 300
        print("Invalid input. Using default dimensions: 400x300")
    
    # Get background color
    print("\nColor options:")
    print("1. Enter hex color (e.g., #FF0000 for red)")
    print("2. Enter RGB values")
    print("3. Use color name (e.g., red, blue, green)")
    
    color_choice = input("Choose option (1-3, default 1): ") or "1"
    
    if color_choice == "1":
        color = input("Enter hex color (default #FFFFFF): ") or "#FFFFFF"
    elif color_choice == "2":
        try:
            r = int(input("Red (0-255): "))
            g = int(input("Green (0-255): "))
            b = int(input("Blue (0-255): "))
            color = (r, g, b)
        except ValueError:
            color = "#FFFFFF"
            print("Invalid RGB values. Using white.")
    else:
        color = input("Enter color name (default white): ") or "white"
    
    # Get filename
    filename = input("Enter filename (default my_image.png): ") or "my_image.png"
    if not filename.endswith(('.png', '.jpg', '.jpeg')):
        filename += '.png'
    
    try:
        # Create image
        img = Image.new("RGB", (width, height), color)
        
        # Optional: Add text to image
        add_text = input("Add text to image? (y/n, default n): ").lower()
        if add_text == 'y':
            text = input("Enter text: ")
            
            # Create drawing context
            draw = ImageDraw.Draw(img)
            
            # Try to use a font, fallback to default if not available
            try:
                font_size = int(input("Font size (default 20): ") or "20")
                # Try to load a system font
                try:
                    font = ImageFont.truetype("arial.ttf", font_size)
                except:
                    font = ImageFont.load_default()
            except ValueError:
                font = ImageFont.load_default()
            
            # Get text color
            text_color = input("Text color (default black): ") or "black"
            
            # Calculate text position (centered)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (width - text_width) // 2
            y = (height - text_height) // 2
            
            # Draw text
            draw.text((x, y), text, fill=text_color, font=font)
        
        # Save image
        img.save(filename)
        print(f"✅ Image created successfully!")
        print(f"Filename: {filename}")
        print(f"Dimensions: {width}x{height} pixels")
        print(f"File size: {os.path.getsize(filename)} bytes")
        
        # Optional: Show image info
        show_info = input("Show detailed image info? (y/n): ").lower()
        if show_info == 'y':
            print(f"\nImage Details:")
            print(f"Format: {img.format}")
            print(f"Mode: {img.mode}")
            print(f"Size: {img.size}")
            
    except Exception as e:
        print(f"❌ Error creating image: {e}")

if __name__ == "__main__":
    create_digital_image() 