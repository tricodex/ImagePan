# Copyright (c) 2024 Patrick Camara

import moviepy.editor as mpe
from moviepy.video.fx.resize import resize
import datetime

current_time_as_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

def create_panning_video(image_path, output_path, start_side="left", duration=8):
    """
    Creates a panning video from an image.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path for the output video.
        start_side (str, optional): Starting side for the pan ("left" or "right"). Defaults to "left".
        duration (int, optional): Duration of the video in seconds. Defaults to 8.
    """
    
    # Load the image
    clip = mpe.ImageClip(image_path)
    
    # Resize the image to maintain aspect ratio, adjusting height to 1024
    clip = resize(clip, height=1024)
    
    # Calculate the total width and the movement step
    total_width = clip.w
    movement_step = (total_width - 576) / (duration * 24)  # 24 fps
    
    # Define the function for panning effect
    def panning_effect(get_frame, t):
        frame = get_frame(t)
        x_pos = int((t / duration) * (total_width - 576)) if start_side == "left" else int((1 - t / duration) * (total_width - 576))
        return frame[:, x_pos:x_pos+576]

    # Apply the panning effect
    panning_clip = clip.fl(panning_effect, apply_to=['mask', 'video'])

    # Set the duration of the clip
    panning_clip = panning_clip.set_duration(duration)
    
    # Write the video to the output path
    panning_clip.write_videofile(output_path, fps=24)

# Example usage
image_path = r""
output_path = f"output/{current_time_as_string}_panning_video.mp4"
create_panning_video(image_path, output_path, start_side="right", duration=8)
