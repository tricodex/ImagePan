# Image Panning Video Creator

This script allows you to create panning videos from images. It supports creating videos from a single image, multiple images specified in a list, or all images in a directory. The output video will pan from one side of the image to the other, and you can specify the direction of the pan and the duration of the video.

## Features

- Create panning videos from a single image.
- Create panning videos from multiple images specified in a list.
- Create panning videos from all images in a directory.
- Specify the starting side for the pan (left or right).
- Specify the duration of the video.

## Requirements

- Python 3.x
- moviepy

## Installation

Install the required library using pip:

```sh
pip install moviepy
```

## Usage

### Command Line Arguments

- `--single`: Path to a single image file.
- `--multiple`: Paths to multiple image files.
- `--directory`: Path to a directory containing images.
- `--output`: Output directory for the video files (required).
- `--start_side`: Starting side for the pan (`'left'` or `'right'`). Defaults to `'left'`.
- `--duration`: Duration of the video in seconds. Defaults to 8 seconds.

### Examples

#### Single Image

```sh
python create_panning_video.py --single path/to/image.jpg --output path/to/output
```

#### Multiple Images

```sh
python create_panning_video.py --multiple path/to/image1.jpg path/to/image2.jpg --output path/to/output
```

#### Directory of Images

```sh
python create_panning_video.py --directory path/to/images --output path/to/output
```

#### Ratio Sizes

| Aspect Ratio | Size 1   | Size 2   | Size 3   | Size 4   | Size 5   | Size 6   | Size 7   | Size 8   | Size 9   | Size 10  | Size 11  | Size 12  |
|--------------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 9:16         | 288x512  | 360x640  | 405x720  | 450x800  | 540x960  | 576x1024 | 630x1120 | 675x1200 | 720x1280 | 810x1440 | 900x1600 | 1080x1920|
| 16:9         | 256x144  | 320x180  | 426x240  | 640x360  | 854x480  | 1024x576 | 1280x720 | 1600x900 | 1920x1080| 2560x1440| 3200x1800| 3840x2160|
| 4:3          | 320x240  | 400x300  | 640x480  | 800x600  | 960x720  | 1024x768 | 1280x960 | 1400x1050| 1440x1080| 1600x1200| 1920x1440| 2048x1536|
| 3:2          | 300x200  | 450x300  | 600x400  | 750x500  | 900x600  | 1050x700 | 1200x800 | 1350x900 | 1500x1000| 1800x1200| 2100x1400| 2400x1600|
| 1:1          | 128x128  | 256x256  | 320x320  | 480x480  | 512x512  | 640x640  | 800x800  | 1024x1024| 1280x1280| 1600x1600| 1920x1920| 2048x2048|
| 3:4          | 180x240  | 240x320  | 360x480  | 450x600  | 540x720  | 600x800  | 720x960  | 768x1024 | 900x1200 | 1080x1440| 1200x1600| 1350x1800|
| 2:3          | 160x240  | 240x360  | 320x480  | 400x600  | 480x720  | 600x900  | 640x960  | 800x1200 | 960x1440 | 1200x1800| 1400x2100| 1600x2400|

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
