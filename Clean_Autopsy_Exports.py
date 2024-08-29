#Clean Autopsy Exports
import os
import re
import argparse

def rename_files(directory):
    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        # Match filenames starting with numbers followed by a hyphen
        new_name = re.sub(r'^\d+-', '', filename)

        # Construct full paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)

        # Rename the file
        try:
            os.rename(old_file, new_file)
        except FileExistsError:
            print(f"Skipping {old_file} as it already exists in folder.")
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Rename files by removing leading numbers and a hyphen.")
    parser.add_argument('directory', help="Directory containing the files to rename")
    
    args = parser.parse_args()
    
    # Call the rename function with the provided directory
    rename_files(args.directory)

