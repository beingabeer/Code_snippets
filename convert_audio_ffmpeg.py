from subprocess import check_call

ok = check_call(['ffmpeg', '-i', 'input.wav', 'output.mp3'])
if ok:
    with open('output.wav', 'rb') as f:
        wav_file = f.read()
