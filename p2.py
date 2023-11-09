import subprocess
import re

class VideoConverter:
    def __init__(self, input_file):
        self.input_file = input_file

    def convert_to_mp2(self, output_file):
        #Ejecuta comando 'ffmpeg -i BBB.mp4 -c:v mpeg2video BBB.mp2, el cual convierte BBB.mp4 a un video en mpeg2
        subprocess.run(['ffmpeg', '-i', self.input_file, '-c:v', 'mpeg2video', output_file])
        self.get_video_info(output_file)

    def modify_resolution(self, output_file, width, height):
        #
        subprocess.run(['ffmpeg', '-i', self.input_file, '-vf', f'scale={width}:{height}', output_file])

        self.get_video_info(output_file)

    def change_chroma_subsampling(self, output_file, subsampling):
        subprocess.run(['ffmpeg', '-i', self.input_file, '-c:v', 'libx264', '-pix_fmt', subsampling, output_file])

        self.get_video_info(output_file)

    def get_video_info(self, video_file):
        result = subprocess.Popen(['ffmpeg', '-i', video_file], stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        output = result.stderr.read().decode()
        match = re.search(r"Duration: (\d{2}:\d{2}:\d{2}\.\d{2})", output)
        if match:
            duration = match.group(1)
            print(f"Duration: {duration}")

        match = re.search(r"Stream #0:0: Video: ([\w]+)", output)
        if match:
            video_codec = match.group(1)
            print(f"Video Codec: {video_codec}")



converter = VideoConverter('BBB.mp4')
converter.convert_to_mp2('BBB.mp2')
converter.modify_resolution('resized_BBB.mp4', 1280, 720)
converter.change_chroma_subsampling('subsampled_BBB.mp4', 'yuv420p')
