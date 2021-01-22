############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

# Import the library
from midiutil.MidiFile3 import MIDIFile
import random

# Create the MIDIFile Object
MyMIDI = MIDIFile(1)

# improv technique 1
a_minor_scale = [69, 71, 72, 74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91]
chord_set_one = [
    (57, 60, 64),
    (53, 57, 60),
    (55, 59, 62),
    (52, 55, 59)]

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
time = 0
MyMIDI.addTrackName(track, time, "Sample Track")
MyMIDI.addTempo(track, time, 120)

# Add a note. addNote expects the following information:
channel = 0
pitch = 69
duration = 1
volume = 100


def play_music(melody, bass):
    m_time = 0
    m_duration = 2
    m_tempo = 1

    b_time = 0
    b_duration = 3
    b_tempo = 2

    for b in bass:
        for i in range(4):  # play 4 times
            for n in b:
                # Now add the note.
                MyMIDI.addNote(track, channel, n, b_time, b_duration, volume)

                m_key = random.choice(melody)
                MyMIDI.addNote(track, channel, m_key,
                               b_time, b_duration, volume)
                m_time += m_tempo
            b_time += b_tempo
    binfile = open("output_test.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()


play_music(a_minor_scale, chord_set_one)

# And write it to disk.
# binfile = open("test.mid", 'wb')
# MyMIDI.writeFile(binfile)
# binfile.close()
