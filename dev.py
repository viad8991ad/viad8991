import os
import shutil

BUILD_FOLDER = "build"
TEMPLATES_FOLDER = "templates"
INDEX = "index.html"
STATIC_FOLDER = "static"
STUB_HTML = """<!DOCTYPE html>
<html>
    <head>
        <title>Hello World!</title>
    </head>
    <body>
        <p>This is a simple HTML page for stab.</p>
    </body>
</html>
"""

print("1/4 cleanup 'build' folder")
shutil.rmtree(BUILD_FOLDER, ignore_errors=True)
os.mkdir(BUILD_FOLDER)

print("2/4 copy business card site")
shutil.copy2(TEMPLATES_FOLDER + "/" + INDEX, BUILD_FOLDER)
shutil.copytree(STATIC_FOLDER, BUILD_FOLDER + "/" + STATIC_FOLDER, dirs_exist_ok=True)

print("3/4 create stub for HSR page")
hsr_dir = BUILD_FOLDER + "/hsr/"
os.makedirs(hsr_dir)
with open(hsr_dir + INDEX, "w+") as f:
    f.write(STUB_HTML)

print("4/4 create stub for GI page")
gi_dir = BUILD_FOLDER + "/gi/"
os.makedirs(gi_dir)
with open(gi_dir + INDEX, "w+") as f:
    f.write(STUB_HTML)
