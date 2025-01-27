import os
import re
import subprocess


copy_command = "cp -r ~/Library/Mobile\ Documents/iCloud\~md\~obsidian/Documents/Omar\'s\ Vault/* ~/Developer/Repos/Obsidian/notes/content"
subprocess.run(copy_command, shell=True)


# Function to remove the specified code block from a Markdown file
def remove_dataviewjs_code(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Define the regular expression to match the code block
    code_block_pattern = r'```dataviewjs[\s\S]*?```'

    # Remove the code block using re.sub
    modified_content = re.sub(code_block_pattern, '', content)

    with open(filename, 'w') as file:
        file.write(modified_content)

# Specify the directory where your Markdown files are located
directory = 'content/Unsorted/Daily Notes/'

# Iterate through all files in the directory
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(root, file)
            remove_dataviewjs_code(file_path)
            print(f'Removed code block from {file_path}')


git_commands = [
    "cd ~/Developer/Repos/Obsidian/notes/",
    "git add .",
    "git commit -m 'note update' --no-gpg-sign",
    "git push"
]

for command in git_commands:
    subprocess.run(command, shell=True)

