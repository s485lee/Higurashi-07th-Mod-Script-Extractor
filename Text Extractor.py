import os
import re
import pandas as pd

def process_script_files(input_folder, output_folder):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Compile the regex pattern for extracting dialogues
    pattern_dialogue = re.compile(r'OutputLine\(NULL, "(.*?)",\s*NULL, "(.*?)",', re.DOTALL)
    
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_folder, filename)
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find all dialogues
            dialogues = pattern_dialogue.findall(content)
            
            # Create a DataFrame and save to Excel
            df = pd.DataFrame(dialogues, columns=['Japanese', 'Korean'])
            output_file_path = os.path.join(output_folder, filename.replace('.txt', '.xlsx'))
            df.to_excel(output_file_path, index=False)
    
    print(f"All files have been processed and saved to {output_folder}.")

# Example usage
input_folder = 'PATH1'  # Replace with the path to your input folder
output_folder = 'PATH2'  # Replace with the path to your output folder
process_script_files(input_folder, output_folder)
