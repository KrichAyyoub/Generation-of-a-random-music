import music21 as mc
import glob
import time

notes = []

for file in glob.glob("midiData/*.mid"):

    #each file.midi to format => <music21.stream.Score 0x7fd9712bba20>
    midi = mc.converter.parse(file)

    #partition look like <music21.stream.Score 0x7f28aaf954a8>
    partition = mc.instrument.partitionByInstrument(midi)

    #notesMIDI is a set of events (all played notes, chord and other informations)
    notesMIDI = partition.parts[0].recurse()

    # Notes creations (a sequence of played notes)
    for event in notesMIDI:
        if isinstance(event, mc.note.Note):
            #to get the pitch of every played note
            #print(event)
            notes.append(str(event.pitch))
        elif isinstance(event, mc.chord.Chord):
            #played Chord, we have to encode id each note alone
            notes.append('.'.join(str(n) for n in event.normalOrder))
            print(event.commonName)
            print(event)
            print(event.beatDuration)

    print(notes)
    print("----------------------------------")
    time.sleep(15)



