import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir("."):
        if os.path.isdir(filename):
            continue
        new_path = filename.split(".")[-1]
        try:
            os.mkdir(new_path)
        except FileExistsError:
            pass
        os.rename(filename, "{}/{}".format(new_path, filename))
main()