import os
import moviepy.editor as mpe
import datetime
import argparse

def create_bouncing_video(image_path, output_path, frame_width, frame_height, speed=2, duration=8, start_position='center-center'):
    """
    Creates a bouncing video frame from an image with specified frame dimensions.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path for the output video.
        frame_width (int): Width of the bouncing frame.
        frame_height (int): Height of the bouncing frame.
        speed (float, optional): Speed of the bouncing effect. Defaults to 2.
        duration (int, optional): Duration of the video in seconds. Defaults to 8.
        start_position (str, optional): Starting position of the frame. Defaults to 'center-center'.
    """
    
    # Load the image
    clip = mpe.ImageClip(image_path)
    
    # Get image dimensions
    img_width, img_height = clip.size
    
    # Calculate the boundaries for the bouncing frame
    x_max = img_width - frame_width
    y_max = img_height - frame_height
    
    # Initial position based on start_position
    if start_position == 'center-center':
        x_start = (img_width - frame_width) // 2
        y_start = (img_height - frame_height) // 2
    elif start_position == 'center-left':
        x_start = 0
        y_start = (img_height - frame_height) // 2
    elif start_position == 'center-right':
        x_start = x_max
        y_start = (img_height - frame_height) // 2
    elif start_position == 'top-left':
        x_start = 0
        y_start = 0
    elif start_position == 'top-right':
        x_start = x_max
        y_start = 0
    elif start_position == 'bot-left':
        x_start = 0
        y_start = y_max
    elif start_position == 'bot-right':
        x_start = x_max
        y_start = y_max
    else:
        raise ValueError("Invalid start_position. Use 'center-center', 'center-left', 'center-right', 'top-left', 'top-right', 'bot-left', or 'bot-right'.")
    
    # Define the function for bouncing effect
    def bouncing_effect(get_frame, t):
        frame = get_frame(t)
        
        # Calculate x and y positions using a bouncing logic
        vx = speed  # horizontal velocity (pixels per frame)
        vy = speed * 0.75  # vertical velocity (pixels per frame)
        
        x = (x_start + vx * t * 24) % (2 * x_max)
        y = (y_start + vy * t * 24) % (2 * y_max)
        
        if x > x_max:
            x = 2 * x_max - x
        if y > y_max:
            y = 2 * y_max - y
        
        return frame[int(y):int(y)+frame_height, int(x):int(x)+frame_width]

    # Apply the bouncing effect
    bouncing_clip = clip.fl(bouncing_effect, apply_to=['mask', 'video'])

    # Set the duration of the clip
    bouncing_clip = bouncing_clip.set_duration(duration)
    
    # Write the video to the output path
    bouncing_clip.write_videofile(output_path, fps=24)

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create bouncing videos from images.")
    parser.add_argument("--single", type=str, help="Path to a single image file.")
    parser.add_argument("--multiple", nargs='+', help="Paths to multiple image files.")
    parser.add_argument("--directory", type=str, help="Path to a directory containing images.")
    parser.add_argument("--output", type=str, required=True, help="Output directory for the video files.")
    parser.add_argument("--frame_width", type=int, required=True, help="Width of the bouncing frame.")
    parser.add_argument("--frame_height", type=int, required=True, help="Height of the bouncing frame.")
    parser.add_argument("--speed", type=float, default=2, help="Speed of the bouncing effect.")
    parser.add_argument("--duration", type=int, default=8, help="Duration of the video in seconds.")
    parser.add_argument("--start_position", type=str, choices=["center-center", "center-left", "center-right", "top-left", "top-right", "bot-left", "bot-right"], default="center-center", help="Starting position of the frame.")
    
    args = parser.parse_args()
    
    if args.single:
        image_path = args.single
        base_name = os.path.splitext(os.path.basename(image_path))[0]
        current_time_as_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        output_path = os.path.join(args.output, f"{base_name}_{current_time_as_string}_bouncing_video.mp4")
        create_bouncing_video(image_path, output_path, args.frame_width, args.frame_height, args.speed, args.duration, args.start_position)
    elif args.multiple:
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        for image_path in args.multiple:
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            current_time_as_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            output_path = os.path.join(args.output, f"{base_name}_{current_time_as_string}_bouncing_video.mp4")
            create_bouncing_video(image_path, output_path, args.frame_width, args.frame_height, args.speed, args.duration, args.start_position)
    elif args.directory:
        if not os.path.exists(args.output):
            os.makedirs(args.output)
        supported_formats = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
        image_paths = [os.path.join(args.directory, fname) for fname in os.listdir(args.directory) if os.path.splitext(fname)[1].lower() in supported_formats]
        for image_path in image_paths:
            base_name = os.path.splitext(os.path.basename(image_path))[0]
            current_time_as_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            output_path = os.path.join(args.output, f"{base_name}_{current_time_as_string}_bouncing_video.mp4")
            create_bouncing_video(image_path, output_path, args.frame_width, args.frame_height, args.speed, args.duration, args.start_position)
    else:
        print("Please specify --single, --multiple, or --directory option.")

