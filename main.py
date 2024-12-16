from src.music_generator import MidiHandler, AudioConverter
import os

# Example usage
def create_song():
    # Create MIDI
    midi = MidiHandler(measures_per_second=2, volume=100, octave=5)
    chord_progression = midi.extract_chords_from_txt("Breaking Through to You.txt")
    midi.create_from_progression(chord_progression)
    midi.save("output.mid")
    
    # Convert to MP3
    converter = AudioConverter("ukulele.sf2")
    converter.midi_to_mp3("output.mid", "output.mp3")

    # Convert output.mid to a table showing the note numbers
    converter = AudioConverter("ukulele.sf2")
    table = converter.midi_to_table("output.mid")
    # Save the table to a CSV file
    with open("output.csv", "w") as f:
        for row in table:
            f.write(f"{row['start']},{row['end']},{row['pitch']},{row['velocity']}\n")


if __name__ == "__main__":
    create_song()
