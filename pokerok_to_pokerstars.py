import argparse
import datetime
import os
import re
import zipfile


def extract_zip_files(zip_file):
    """Extracts all text files from a zip archive"""
    with zipfile.ZipFile(zip_file, 'r') as archive:
        for file in archive.namelist():
            if file.endswith('.txt'):
                archive.extract(file)


def process_txt_files(folder, new_folder):
    """Processes all text files in a folder and saves them to a new folder"""
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    for file in os.listdir(folder):
        if file.endswith('.txt'):
            with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                content = f.read()

                # Some text processing using regex
                content = re.sub(r'Poker Hand #HD', 'PokerStars Hand #20', content, flags=re.MULTILINE)
                content = re.sub(r' won ', ' collected ', content, flags=re.MULTILINE)
                content = re.sub(r' and collected ', ' and won ', content, flags=re.MULTILINE)
                content = re.sub(r'\n\n', '\n', content, flags=re.MULTILINE)
                content = re.sub(r'Dealt to (?!Hero\b)[^ ]+ \n', '', content, flags=re.MULTILINE)

                with open(os.path.join(new_folder, file), 'w', encoding='utf-8') as f_new:
                    f_new.write(content)

    for file in os.listdir(folder):
        if file.endswith('.txt'):
            os.remove(os.path.join(folder, file))


def main():
    parser = argparse.ArgumentParser(description='Converts Pokerok hand history files converts to PokerStars format for Hand2Note')
    parser.add_argument('-if', '--input_folder', default='./', help='Path to the input folder')
    parser.add_argument('-of', '--output_folder', default=None, help='Path to the output folder. If not provided, the folder will be named with the current date in the format YY.MM.DD')
    args = parser.parse_args()
    input_folder = args.input_folder
    output_folder = args.output_folder
    if not output_folder:
        today = datetime.datetime.today()
        output_folder = os.path.join(input_folder, '{}'.format(today.strftime('%y.%m.%d.')))
    for file in os.listdir(input_folder):
        if file.endswith('.zip'):
            extract_zip_files(os.path.join(input_folder, file))
    process_txt_files(input_folder, output_folder)


if __name__ == '__main__':
    main()
