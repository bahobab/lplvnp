import os
import uuid
import shutil

base_dir = './static/img/projects'
src_path = base_dir + '/carshow/src'
# dest_path = src_path + '/dest'

my_images = [f for f in os.listdir(
    src_path) if os.path.isfile(os.path.join(src_path, f))]

print(f'{my_images}')

for image in my_images:
    print(os.path.basename(image))
    new_name = uuid.uuid4().hex
    os.rename(os.path.join(src_path, os.path.basename(image)), os.path.join(src_path,
                                                                            os.path.basename(str(new_name) + '.jpg')))
    # shutil.move(os.path.join(src_path, os.path.basename(image)), os.path.join(dest_path,
    #                                                                           os.path.basename(str(new_name) + '.jpg')))


# os.rename
"""
read images from a source folder move the images to a destination folder with new uuid-generated name
src_path: source path for the imaes
dest_path: destination path for the images

"""
