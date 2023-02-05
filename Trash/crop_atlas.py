import re
import os
from PIL import Image

input_folder = "Input"
png_folder = "PNG"
pvr_tool_path = "PVRTexToolCLI.exe"
output_folder = "Output"
remove_black = False

def main():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    with open("UIPackedAtlas.lua") as f:
        data = f.read()
 
    image_regions = re.findall(r'resource "ImageRegion" "([\w]+)" {\s+image = "([\w]+)",\s+uv = { ([\d\.\/, ]+) }\s+}', data)

    images = {}
    for region in image_regions:
        name, image_name, uv_str = region
        try:
            if image_name not in images:
                images[image_name] = Image.open(f"{png_folder}/{image_name}.png")
                image = images[image_name]
        except FileNotFoundError:
            print(f"Skipping region '{name}' because '{image_name}.png' was not found.")
            continue
        
        if image_name not in images:
            images[image_name] = Image.open(f"{image_name}.png")
        image = images[image_name]

        uv = [eval(x) for x in uv_str.split(", ")]
        if len(uv) != 4:
            raise ValueError(f"Incorrect number of values in UV for region '{name}'")

        x0, y0, x1, y1 = uv
        width, height = image.size
        left, upper = int(x0 * width), int(y0 * height)
        right, lower = int(x1 * width), int(y1 * height)
        crop_box = (left, upper, right, lower)
        cropped_image = image.crop(crop_box)
        if remove_black:
            cropped_image = cropped_image.convert("RGBA")
            datas = cropped_image.getdata()
            new_data = []
            for item in datas:
                if item[0] == 0 and item[1] == 0 and item[2] == 0:
                    new_data.append((255, 255, 255, 0))
                else:
                    new_data.append(item)
            cropped_image.putdata(new_data)
        cropped_image.save(f"{output_folder}/{name}.png")
 

if __name__ == "__main__":
    main()
