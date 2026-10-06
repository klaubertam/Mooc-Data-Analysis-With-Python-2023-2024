def file_extensions(filename):
    no_extension = []
    extensions = {}

    with open(filename) as file:
        for line in file:
            filename = line.strip()

            if "." in filename:
                extension = filename.split(".")[-1]

                if extension not in extensions:
                    extensions[extension] = []

                extensions[extension].append(filename)

            else:
                no_extension.append(filename)

    return no_extension, extensions


def main():
    no_extension, extensions = file_extensions("src/filenames.txt")

    print(f"{len(no_extension)} files with no extension")

    for extension in sorted(extensions):
        print(f"{extension} {len(extensions[extension])}")


if __name__ == "__main__":
    main()