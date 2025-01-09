# Word Wizard


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Word Wizard](#word-wizard)
  - [Features](#features)
  - [Usage for Windows end-users](#usage-for-windows-end-users)
  - [Cross-Platform Usage](#cross-platform-usage)
    - [Prerequisites](#prerequisites)
    - [Install Required Python Libraries](#install-required-python-libraries)
    - [File Structure](#file-structure)
    - [Run](#run)
    - [Screenshots](#screenshots)
  - [How It Works](#how-it-works)
    - [Components](#components)
    - [API Key Management](#api-key-management)
  - [Troubleshooting](#troubleshooting)
    - [Common Issues](#common-issues)
    - [Debugging](#debugging)
  - [License](#license)

<!-- /code_chunk_output -->


Word Wizard is a cross-platform application that helps users build their vocabulary by reading engaging stories with highlighted SAT-level words and their meanings.
Google Gemini API is used for dynamically creating a new story every time.

## Features

- **Dynamic Story Generation**: Fetch and display stories with highlighted SAT-level vocabulary words and their meanings.
- **Settings Management**: A built-in settings menu to save and delete the Gemini API key.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## Usage for Windows end-users

Windows binary is provided in the Releases tab on Github

1. Download `word_wizard.zip` from the Releases tab on Github.
2. Since the program is not signed, windows will block it from being run. For correct functionality, do the following:
   1. Right click on `word_wizard.zip` and select `Properties` from the context menu.
   2. Select `Unblock` and click `OK` 
5. Unzip and double-click `Word Wizard.exe` to start the application.
6. The application will ask for the Gemini API key via a settings menu if it is not already set.
7. Use the settings menu to save or delete the Gemini API key as needed.
8. Fetch new stories and build your vocabulary!

## Cross-Platform Usage

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Install Required Python Libraries

Following python packages are required:

```bash
pip install flask google-generativeai keyring pywebview
```

or,

```bash
pip install -r requirements.txt
```

### File Structure

```
WordWizard
├── html/
│   ├── settings.html
│   └── word_wizard.html
├── prompts/
│   └── prompt.txt
├── requirements.txt
├── word_wizard.py
└── README.md
```

### Run

```
python word_wizard.py
```

### Screenshots

- Story Window

<!-- ![Story Window](https://github.com/user-attachments/assets/26e8ee55-df75-4e5e-8741-ebb3d880dda2) -->
<img src="https://github.com/user-attachments/assets/26e8ee55-df75-4e5e-8741-ebb3d880dda2" width="100%">

- Settings Window

<!-- ![Settings Window](https://github.com/user-attachments/assets/97e5d8a1-4850-493a-8155-b45a7c0a0ea3) -->
<img src="https://github.com/user-attachments/assets/97e5d8a1-4850-493a-8155-b45a7c0a0ea3" width="60%">

## How It Works

### Components
- **word_wizard.py**: Starts a Flask server and opens the application in a webview.

- **html/word_wizard.html**: Main HTML page for displaying stories.
- **html/settings.html**: Settings page for managing the Gemini API key.
- **prompts/prompt.txt**: Contains the prompt used by the Gemini API to generate stories.

### API Key Management

- Users must provide the application with a Google Gemini API key in order to use WordWizard
- The API key is **stored securely on their local computer** using `keyring`.
- Users can save and delete the API key via the settings menu in the application.

## Troubleshooting

### Common Issues

- **Server not starting**: Ensure that Python and all required libraries are installed correctly.
- **API key not working**: Double-check that the correct API key is entered and saved. Delete the API key in the Settings tab and enter a new one.

### Debugging

- Use console logs in the JavaScript and print statements in the Python code to debug issues.
- Check the terminal or command prompt for any error messages during execution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
