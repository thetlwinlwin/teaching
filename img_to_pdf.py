from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()
image_paths = [
    "/Users/thetlwin/Desktop/IMG_7896.heic",
    "/Users/thetlwin/Desktop/IMG_7897.heic",
    "/Users/thetlwin/Desktop/IMG_7898.heic",
    "/Users/thetlwin/Desktop/IMG_7899.heic",
    "/Users/thetlwin/Desktop/IMG_7917.heic",
    "/Users/thetlwin/Desktop/IMG_7918.heic",
    "/Users/thetlwin/Desktop/IMG_7919.heic",
]
pdf_path = '/Users/thetlwin/Desktop/SEC_1_MOCK.pdf'

images = []

for path in image_paths:
    try:
        # Convert to RGB to ensure compatibility
        img = Image.open(path).convert('RGB')
        images.append(img)
    except FileNotFoundError:
        print(f"Error: Image file not found at {path}")
    except Exception as e:
        print(f"Error opening image {path}: {e}")

images[0].save(pdf_path, save_all=True, append_images=images[1:])
print(f"PDF successfully created at: {pdf_path}")
