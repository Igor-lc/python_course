from moviepy.video.io.VideoFileClip import VideoFileClip

# Відкриваємо відеофайл
clip = VideoFileClip("1.mp4")

# Обрізаємо відео від 5 до 15 секунди
clip = clip.subclip(5, 15)

# Зберігаємо відео в новому файлі
clip.write_videofile("example_trimmed.mp4")
