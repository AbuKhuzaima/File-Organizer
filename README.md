# File Organizer

A Python application that helps organize files in a directory by automatically sorting them into appropriate folders based on their file types.

## Features

- **Automatic File Sorting**: Organizes files into categorized folders (Images, Documents, Videos, etc.)
- **Multiple File Type Support**: Handles various file formats including:
  - Images (.jpg, .png, .gif, etc.)
  - Documents (.pdf, .doc, .txt, etc.)
  - Videos (.mp4, .avi, .mkv, etc.)
  - Audio (.mp3, .wav, etc.)
  - Archives (.zip, .rar, etc.)
- **Custom Directory Support**: Allows users to specify which directory to organize
- **Real-time Processing**: Shows progress as files are being organized
- **Safe Operation**: Creates folders only when needed and handles existing files safely

## How to Use

1. Run the application
2. Enter the path of the directory you want to organize
3. The program will automatically:
   - Scan for files
   - Create necessary folders
   - Move files to appropriate locations
   - Display the organization progress

## File Categories

The organizer sorts files into the following categories:
- Images
- Documents
- Videos
- Audio
- Archives
- Others (for unrecognized file types)

## Requirements

- Python 3.x
- OS: Windows/Linux/MacOS
- Required Python packages:
  - os
  - shutil
  - pathlib

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Run the script using Python:

python file_organizer.py


## Contributing

Feel free to fork this repository and contribute to improve the functionality.

## License

This project is open source and available under the MIT License.
EOF
