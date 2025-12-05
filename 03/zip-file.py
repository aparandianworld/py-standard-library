import zipfile

with zipfile.ZipFile("archive.zip", "w") as zf:
    zf.write("input.txt")
    zf.write("input_2.txt")

print(zipfile.is_zipfile("archive.zip"))

with zipfile.ZipFile("archive.zip", "r") as zf:
    print(zf.namelist())
    print(zf.infolist())

    info = zf.getinfo("input.txt")
    print(info.file_size)
    print(info.filename)
    print(zf.read("input.txt"))

    zf.extract("input.txt", "extracted-12052025")
    zf.extractall("extracted-all-12052025")
