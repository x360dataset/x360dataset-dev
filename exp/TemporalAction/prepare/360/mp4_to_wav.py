import os
from glob import glob



root =  '../360x/360data/360x_feat/360_panoramic'
target = '../360x/360data/360x_feat/audio/360'

os.makedirs(target, exist_ok=True)

video_list =  glob(os.path.join(root, "*"))

from tqdm import tqdm


def generate_wav_from_mp4list(_list, force=False):

    for i, item in tqdm(enumerate(_list)):
        if i % 500 == 0:
            print('*******************************************')
            print('{}/{}'.format(i, len(_list)))
            print('*******************************************')

        mp4_filename = item
        mp4name = item.split("/")[-1]

        wav_filename = os.path.join(target, mp4name.replace(".mp4", ".wav"))
        #.replace("video", "audio")

        if os.path.exists(wav_filename) and not force:
            pass
        else:
            os.system('ffmpeg -i {} -acodec pcm_s16le -ar 16000 {}'.format(mp4_filename, wav_filename))

    print("Done")




# video_list =  glob(os.path.join(root, "video", "*"))


print(f"processing {len(video_list)} videos...")

generate_wav_from_mp4list(video_list)
