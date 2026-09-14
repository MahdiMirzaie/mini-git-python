import hashlib         #کتابخانه داخلی پایتون برای تولید هش 
import os


def hash_file(filepath):

    # read file as binary
    with open (filepath, "rb") as f:    # rb = read Binary...
        content = f.read()

    # generate sha1 hash
    file_hash = hashlib.sha1(content).hexdigest()  # make Hash ..

    return file_hash


def save_object(filepath):

    # calculate hash
    file_hash = hash_file(filepath)

    # object path
    object_path = os.path.join(".mygit", "objects", file_hash)  # .mygit/objects + Hash ..

    # if object does not exist save it
    
    # این خط باعث میشه اگر دو فایل محتوای درونشون یکسان بود چون هش آنها یکسانه فقط یک آبجکت ذخیره بشه .

    if not os.path.exists(object_path): 
        with open(filepath, "rb") as source:
            content = source.read()

        with open(object_path, "wb") as target:
            target.write(content)

    return file_hash