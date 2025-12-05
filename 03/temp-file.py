from tempfile import TemporaryFile
from tempfile import TemporaryDirectory

import os

with TemporaryFile(mode="w+t") as tf:
    tf.write("The quick brown fox jumps over the lazy dog\n")
    tf.write("The quick brown fox jumps over the tired dog\n")
    tf.seek(0)
    data = tf.read()
    if data:
        print(data)

with TemporaryDirectory() as td:
    temp_path = os.path.join(td, "temp.txt")
    with open(temp_path, "w+t") as tf:
        tf.write("This is a temporary text in a temporary file...")
        tf.seek(0)
        print(tf.read())
