import os

def is_dialogue_line(line):
    return "NULL, \"" in line and "\"," in line

def compare_scripts_excluding_dialogue(file_path_1, file_path_2):
    with open(file_path_1, 'r', encoding='utf-8') as f1, open(file_path_2, 'r', encoding='utf-8') as f2:
        lines1 = [line.strip() for line in f1.readlines() if not is_dialogue_line(line)]
        lines2 = [line.strip() for line in f2.readlines() if not is_dialogue_line(line)]

    differences = []
    min_len = min(len(lines1), len(lines2))
    for i in range(min_len):
        if lines1[i] != lines2[i]:
            differences.append((i + 1, lines1[i], lines2[i]))

    if len(lines1) > min_len:
        for i in range(min_len, len(lines1)):
            differences.append((i + 1, lines1[i], "No equivalent line in file 2"))
    if len(lines2) > min_len:
        for i in range(min_len, len(lines2)):
            differences.append((i + 1, "No equivalent line in file 1", lines2[i]))

    return differences

def batch_compare_folders(folder_path_1, folder_path_2):
    for filename in os.listdir(folder_path_1):
        file_path_1 = os.path.join(folder_path_1, filename)
        file_path_2 = os.path.join(folder_path_2, filename)

        if os.path.isfile(file_path_2):  # Ensure the counterpart file exists in the second folder
            differences = compare_scripts_excluding_dialogue(file_path_1, file_path_2)
            if differences:
                print(f"\nDifferences in {filename}:")
                for diff in differences:  # Output all differences
                    print(f"Line {diff[0]}:\nFile 1: {diff[1]}\nFile 2: {diff[2]}")
            else:
                print(f"No differences in {filename}.")
        else:
            print(f"No counterpart for {filename} in {folder_path_2}")

# Set Folder Directory
folder_path_1 = '/PATH/TO/FIRST/SCRIPT/FOLDER'  #Change to folder containing script files
folder_path_2 = '/PATH/TO/SECOND/SCRIPT/FOLDER' #Change to folder containing script files
batch_compare_folders(folder_path_1, folder_path_2)
