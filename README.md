# DevGuard - Clipboard Protector & Formatter

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)

DevGuard is a lightweight background utility designed to prevent accidental data leaks and improve developer workflow. It monitors the clipboard for sensitive information and automatically formats raw JSON strings.

## Key Features

* **Secret Detection:** Monitors clipboard content for AWS Keys, Private Keys, tokens, and email addresses.
* **Desktop Alerts:** Provides immediate system notifications when sensitive data is detected.
* **Auto-Format JSON:** Detects unformatted JSON strings and replaces them with a pretty-printed version automatically.
* **Background Operation:** Runs silently in the system tray.
* **Local Processing:** All processing is done locally in RAM. No data is stored or transmitted.

## Installation

### Option 1: Download Executable
1.  Navigate to the Releases page.
2.  Download the latest `DevGuard.exe`.
3.  Run the application.

### Option 2: Run from Source
1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the script:
    ```bash
    python app.py
    ```

## Configuration
The application uses a predefined set of Regex patterns to identify sensitive data. You can modify these patterns in the `app.py` file under the `self.patterns` dictionary.

## Security Policy
DevGuard is designed with privacy as a priority:
* No internet connection is required.
* Clipboard data is processed in memory and never saved to disk.
* No telemetry data is collected.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
Distributed under the MIT License. See LICENSE for more information.
