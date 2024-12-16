from midiutil import MIDIFile
from mingus.core import chords
from .notes import note_to_number

class MidiHandler:
    def __init__(self, measures_per_second=2, volume=100, octave=3):
        self.track = 0
        self.channel = 0
        self.time = 0
        self.duration = 1
        # Convert measures per second to BPM (beats per minute)
        # 1 measure = 4 beats, so multiply by 4 and then by 60 for minutes
        self.tempo = measures_per_second * 4 * 60
        self.volume = volume
        self.octave = octave
        self.midi = MIDIFile(1)
        self.midi.addTempo(self.track, self.time, self.tempo)
    
    def create_from_progression(self, chord_progression):
        notes = []
    
        for chord in chord_progression:
            if chord == ' ':
                notes.append(' ')
            else:
                notes.append(chords.from_shorthand(chord)[0])

        note_numbers = []
        for note in notes:
            if note == ' ':
                note_numbers.append(-1)  # Represent REST with -1
            else:
                note_numbers.append(note_to_number(note, self.octave))

        current_time = self.time
        for pitch in note_numbers:
            if pitch != -1:  # If not a REST
                self.midi.addNote(self.track, self.channel, pitch, 
                                current_time, self.duration, self.volume)
            # Increment time whether it's a note or a REST
            current_time += 4

    def extract_chords_from_txt(self, filename):
        chords = []
        with open(filename, 'r') as f:
            for line in f:
                # Extract single letter chords and chord variations
                if line.strip() and not line.startswith('Title:') and not line.startswith('Credits:'):
                    parts = line.strip().split()
                    for part in parts:
                        if part in ['G', 'Am', 'D', 'Em', 'C', ' ']:
                            chords.append(part)
        return chords

    def save(self, filename="output.mid"):
        with open(filename, "wb") as output_file:
            self.midi.writeFile(output_file)


