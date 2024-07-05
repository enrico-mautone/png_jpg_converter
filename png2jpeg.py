import os
import sys
from PIL import Image

def convert_png_to_jpeg(input_path, output_path=None):
    # Check if input_path is a file or directory
    if os.path.isfile(input_path):
        files_to_convert = [input_path]
        input_dir = os.path.dirname(input_path)
    elif os.path.isdir(input_path):
        files_to_convert = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.png')]
        input_dir = input_path
    else:
        print(f"Error: {input_path} is not a valid file or directory.")
        return
    
    # Set the output directory
    if output_path is None:
        output_path = os.path.join(input_dir, 'converted')
    else:
        output_path = os.path.join(output_path, 'converted')
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    # Convert each PNG file to JPEG
    for filepath in files_to_convert:
        filename = os.path.basename(filepath)
        png_image = Image.open(filepath)
        rgb_image = png_image.convert('RGB')
        jpeg_filename = os.path.splitext(filename)[0] + '.jpeg'
        rgb_image.save(os.path.join(output_path, jpeg_filename), 'JPEG')
        print(f'Converted {filename} to {jpeg_filename}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_png_to_jpeg.py <input_path> [output_path]")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2] if len(sys.argv) > 2 else None
        convert_png_to_jpeg(input_path, output_path)
