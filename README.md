# Ukulele Music Generator

A Python-based music generation tool that creates ukulele songs from chord progressions and converts them to playable audio.

## Features

- Generates MIDI files from chord progressions
- Converts MIDI to MP3 using ukulele soundfonts
- Creates detailed note tables for analysis
- Customizable music parameters (tempo, volume, octave)

## Requirements

- Python 3.x
- FluidSynth
- ukulele.sf2 soundfont file

## Project Structure

## Usage

1. Place your chord progression in a text file (e.g., "Breaking Through to You.txt")
2. Run the main script:


python main.py


3. The generated MIDI and MP3 files will be saved in the output directory
4. Check the console output for the note table and additional information

## Output

- MIDI file: Contains the generated ukulele music
- MP3 file: Playable audio file using ukulele soundfont
- Note table: Detailed breakdown of notes, durations, and timings

## Customization

You can adjust the following parameters in the `config.py` file:
- Tempo
- Volume
- Octave range
- Strumming patterns

## Troubleshooting

If you encounter any issues, please check the following:
- Ensure all required libraries are installed
- Verify the ukulele.sf2 soundfont file is in the correct directory
- Check input chord progression file format

For more information, refer to the documentation or open an issue on the project's GitHub page.
