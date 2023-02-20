from typing import Union
import os
from pathlib import Path
from pydub import AudioSegment
from tqdm import tqdm

def convert_mp3_to_wav_mono_24000(dir_path: Union[Path, str]):
    dir_path = Path(dir_path).expanduser()
    for d in tqdm(dir_path.iterdir()):
        if d.is_dir():
            print(d)
            convert_mp3_to_wav_mono_24000(d)
        elif d.is_file():
            if d.suffix in ['.mp3']:
                sound = AudioSegment.from_file(d, format='mp3')
                # Set the sample rate to 24000 Hz and the number of channels to 1 (mono)
                sound = sound.set_frame_rate(24000)
                sound = sound.set_channels(1)
                # Export the audio to WAV format using pydub
                sound.export(os.path.splitext(d)[0]+".wav", format='wav')

if __name__ == '__main__':
    dataset_folder = "../../datasets/fma_medium/"
    convert_mp3_to_wav_mono_24000(dataset_folder)
