import os
from midi2audio import FluidSynth

class AudioConverter:
    def __init__(self, soundfont_path):
        self.soundfont = soundfont_path
        os.environ['PATH'] += ';D:/Program Files/FluidSynth/bin'
        self.fs = FluidSynth(sound_font=self.soundfont)
    
    def midi_to_mp3(self, midi_file, output_file):
        self.fs.midi_to_audio(midi_file, output_file)

    def midi_to_table(self, midi_file):
        """Converts MIDI file to a table format for visualization"""
        import pretty_midi

        # Load the MIDI file
        pm = pretty_midi.PrettyMIDI(midi_file)

        # Create table data
        table_data = []
        for instrument in pm.instruments:
            for note in instrument.notes:
                row = {
                    'start': note.start,
                    'end': note.end,
                    'pitch': note.pitch,
                    'velocity': note.velocity
                }
                table_data.append(row)

        return table_data

