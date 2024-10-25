# Deep Nude Detection - Browser Extension

This is a browser extension that detects nudity in images on the web. Users can right-click on any image and select the option to detect nudity. The extension communicates with a backend server that uses the **NudeNet** model to classify the images and determine if they contain nudity.

## Features

- Detects nudity in images with a right-click.
- Returns a message indicating whether the image contains nudity or not.
- Easy to use with a simple context menu option.

## Requirements

- Google Chrome browser (compatible with Manifest V3).
- Python backend running Flask and NudeNet.

## How It Works

1. The user installs the extension in the browser.
2. Right-click on an image and select "Detect Nudity in Image".
3. The image is sent to the backend for processing and classification.
4. A pop-up in the browser shows whether the image contains inappropriate content.

## Installation Instructions

1. Clone or download this repository.
2. Open Google Chrome and go to `chrome://extensions/`.
3. Enable "Developer mode".
4. Click on "Load unpacked" and select the folder where the extension files are located.
5. Ensure that the Python backend is running correctly.
6. The extension is now ready to use!

## Setting Up the Backend

The backend uses Flask and NudeNet to process the images. Check the `app.py` file and follow the instructions to run the server locally.

1. Install the required dependencies.
2. Start the server with the command:
   ```
   python app.py
   ```

## License

This project is licensed under the MIT License.
