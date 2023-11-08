from moviepy.video.io.VideoFileClip import VideoFileClip

clip = VideoFileClip("1.mp4")

# Обрізаємо відео від 3 до 7 секунди
clip = clip.subclip(0, 1657)

clip.write_videofile("11.mp4")



"""
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

video_file = "1.mp4"
clip = VideoFileClip(video_file)

# Set the start and end times for the part you want to cut
start_time = 32  # Start time in seconds
end_time = 49   # End time in seconds

# Cut the video from start_time to end_time
subclip = clip.subclip(start_time, end_time)

subclip.write_videofile("11.mp4")
"""




'''
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import concatenate_videoclips

video_file = "6.mp4"
clip = VideoFileClip(video_file)

# Set the start and end times for the parts you want to keep
start_time_1 = 0       # Start of the video to keep
end_time_1 = 53.4        # End of the first part
start_time_2 = 53.47     # Start of the second part
end_time_2 = clip.duration  # End of the video to keep

# Extract the two parts you want to keep
part1 = clip.subclip(start_time_1, end_time_1)
part2 = clip.subclip(start_time_2, end_time_2)

# Concatenate the two parts to create the final video
final_clip = concatenate_videoclips([part1, part2])

final_clip.write_videofile("7.mp4")
'''