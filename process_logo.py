from PIL import Image, ImageChops, ImageDraw
import base64

img = Image.open('images_to_use/Logo_KG_Headliner.png').convert('RGBA')

bg = Image.new('RGBA', img.size, (255, 255, 255, 255))
diff = ImageChops.difference(img, bg)
bbox = diff.getbbox()

if bbox:
    img = img.crop(bbox)

# Create a circular mask based on the bounding box dimension (assuming it's roughly a square)
width, height = img.size
size = min(width, height)
# crop to a perfect square centered
left = (width - size) // 2
top = (height - size) // 2
img = img.crop((left, top, left+size, top+size))

mask = Image.new('L', img.size, 0)
draw = ImageDraw.Draw(mask)
# Leave a tiny margin to prevent cutting the very edge
draw.ellipse((2, 2, img.size[0]-2, img.size[1]-2), fill=255)

img.putalpha(mask)
img.save('images_to_use/logo_transparent.png', 'PNG')

with open('images_to_use/logo_transparent.png', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {img.size[0]} {img.size[1]}">
  <image href="data:image/png;base64,{b64}" width="100%" height="100%" />
</svg>'''

with open('images_to_use/logo.svg', 'w') as f:
    f.write(svg)
print('Successfully processed logo!')
