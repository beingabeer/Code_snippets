from pydub import AudioSegment


def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    print(f'current sound dbfs {sound.dBFS}')
    print(f'target dbfs is {target_dBFS}')
    print(f'change in dbfs is {change_in_dBFS}')

    return sound.apply_gain(change_in_dBFS)


sound = AudioSegment.from_file("your_file.mp3", "mp3")
normalized_sound = match_target_amplitude(sound, -20.0)
normalized_sound.export("normalizedAudio.mp3", format="mp3")
