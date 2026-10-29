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
1.  Navigate to the [Releases page](https://github.com/diamondrubinny/Devguard/releases).
2.  Download the latest `DevGuard.exe`.
3.  Run the application.

### Option 2: Run from Source
1.  Clone the repository:
    ```bash
    git clone https://github.com/diamondrubinny/Devguard.git
    cd Devguard
    ```
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
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## 💼 Commercial license & rights acquisition

DevGuard is free and open source under the MIT License. If you are interested in a **commercial agreement** or custom licensing terms, **white-label / exclusive rights**, or **acquiring full rights to the code**, send your proposal to **[d@rubinny.net](mailto:d@rubinny.net)**.

Please include: who you are (company / contact), how you intend to use the code, and your offer.

> 🇮🇱 מעוניינים ברישיון מסחרי, בזכויות בלעדיות או ברכישת הזכויות בקוד? שלחו הצעה ל-**[d@rubinny.net](mailto:d@rubinny.net)** — כולל פרטי קשר, אופן השימוש המתוכנן וההצעה שלכם.

---

<sub>Created by **Diamond Rubinny** · © 2025–2026 Diamond Rubinny · [rubinny.co.il](https://rubinny.co.il)</sub>
