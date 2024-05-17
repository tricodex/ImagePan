# Copyright (c) 2024 Patrick Camara

import os
import moviepy.editor as mpe
from moviepy.video.fx.resize import resize
import datetime
import argparse

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


def process_images(image_paths, output_dir, start_side="left", duration=8):
    """
    Process a list of image paths to create panning videos.

    Args:
        image_paths (list): List of paths to input images.
        output_dir (str): Directory for the output videos.
        start_side (str, optional): Starting side for the pan ("left" or "right"). Defaults to "left".
        duration (int, optional): Duration of the video in seconds. Defaults to 8.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for image_path in image_paths:
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        current_time_as_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_path = os.path.join(output_dir, f"{base_name}_{current_time_as_string}_panning_video.mp4")
        create_panning_video(image_path, output_path, start_side, duration)


def process_directory(input_dir, output_dir, start_side="left", duration=8):
    """
    Process all images in a directory to create panning videos.

    Args:
        input_dir (str): Directory containing input images.
        output_dir (str): Directory for the output videos.
        start_side (str, optional): Starting side for the pan ("left" or "right"). Defaults to "left".
        duration (int, optional): Duration of the video in seconds. Defaults to 8.
    """
    supported_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    image_paths = [os.path.join(input_dir, fname) for fname in os.listdir(input_dir) if os.path.splitext(fname)[1].lower() in supported_formats]
    
    process_images(image_paths, output_dir, start_side, duration)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create panning videos from images.")
    parser.add_argument("--single", type=str, help="Path to a single image file.")
    parser.add_argument("--multiple", nargs='+', help="Paths to multiple image files.")
    parser.add_argument("--directory", type=str, help="Path to a directory containing images.")
    parser.add_argument("--output", type=str, required=True, help="Output directory for the video files.")
    parser.add_argument("--start_side", type=str, choices=["left", "right"], default="left", help="Starting side for the pan ('left' or 'right').")
    parser.add_argument("--duration", type=int, default=8, help="Duration of the video in seconds.")
    
    args = parser.parse_args()
    
    if args.single:
        image_path = args.single
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        current_time_as_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_path = os.path.join(args.output, f"{base_name}_{current_time_as_string}_panning_video.mp4")
        create_panning_video(image_path, output_path, args.start_side, args.duration)
    elif args.multiple:
        process_images(args.multiple, args.output, args.start_side, args.duration)
    elif args.directory:
        process_directory(args.directory, args.output, args.start_side, args.duration)
    else:
        print("Please specify --single, --multiple, or --directory option.")
