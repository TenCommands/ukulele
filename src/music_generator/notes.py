NOTES = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
OCTAVES = list(range(11))
NOTES_IN_OCTAVE = len(NOTES)

def swap_accidentals(note):
    accidental_map = {
        'Db': 'C#', 'D#': 'Eb', 'E#': 'F', 
        'Gb': 'F#', 'G#': 'Ab', 'A#': 'Bb', 'B#': 'C'
    }
    return accidental_map.get(note, note)

def note_to_number(note: str, octave: int) -> int:
    note = swap_accidentals(note)
    if note not in NOTES or octave not in OCTAVES:
        raise ValueError('Invalid note or octave')
    
    note_index = NOTES.index(note)
    note_number = note_index + (NOTES_IN_OCTAVE * octave)
    
    if not 0 <= note_number <= 127:
        raise ValueError('Note number out of MIDI range')
    
    return note_number
