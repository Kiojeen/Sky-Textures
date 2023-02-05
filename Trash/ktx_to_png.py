import os
import subprocess



def ktx_to_png():

    input_folder = "Input"
    png_folder = "PNG"
    pvr_tool_path = "PVRTexToolCLI.exe"

    # make the output folder if it doesn't exist
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".ktx"):
            ktx_path = os.path.join(input_folder, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(png_folder, png_filename)
            command = f'"{pvr_tool_path}" PVRTexToolCLI -i "{ktx_path}" -d "{png_path}"'
            subprocess.run(command, shell=True)
            # delete all .pvr files
            pvr_files = [f for f in os.listdir(input_folder) if f.endswith(".pvr")]
            for pvr_file in pvr_files:
                os.remove(f"{input_folder}/{pvr_file}")


ktx_to_png()