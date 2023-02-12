#Pokerok to PokerStars Hand History Converter

This Python script is used to convert hand history files from Pokerok to PokerStars format for use in [Hand2Note](https://hand2note.com/).

##Requirements

* Python 3.x

## Usage

To run the script, you need to pass two arguments:

* -if or --input_folder: Path to the input folder where the Pokerok hand history files are stored in zip format. The default value is an empty string.
* -of or --output_folder: Path to the output folder where the converted PokerStars hand history files will be stored. If not provided, the folder will be named with the current date in the format YY.MM.DD.

## Example

python

``` python pokerok_to_pokerstars.py -if /path/to/input/folder -of /path/to/output/folder ```

This will convert all hand history files in the input folder and save the converted files in the specified output folder.

## Contact

If you have any questions or issues with the script, feel free to reach out to us at [bebumqi@gmail.com](mailto:bebumqi@gmail.com)