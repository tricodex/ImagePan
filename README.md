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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
