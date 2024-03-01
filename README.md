# Python Keylogger

This Python script serves as a basic keylogger, capturing keyboard inputs and logging them to a text file. It offers the following functionalities:

## Functionalities:

### 1. Keylogging:
- Captures all keyboard inputs, including regular characters, special keys, and combinations.

### 2. Timestamps:
- Appends timestamps to each entered text block, indicating when the Enter key is pressed.

### 3. Special Key Handling:
- Handles special keys such as Space, Enter, Shift, Ctrl, and Alt appropriately, ensuring they are logged as intended.

## Usage:

1. **Running the Keylogger:**
   - Navigate to the `Keylogger Project` folder.
   - Run the Python script `keylogger.py`.
   - It will start capturing keyboard inputs and logging them to a file named `log.txt`.

2. **Customization:**
   - Modify the script to customize logging behavior, such as changing the log file name, adding additional functionalities, or adjusting key handling.
  
3. **Repository:**
   - To clone the repository, use the following command:

```sh
git clone https://github.com/om-ghate/key-logger.git
```

## Notes:

- **Usage Warning:** Ensure that the usage of this script complies with all applicable laws and regulations. Using keyloggers without proper authorization may violate privacy rights and legal restrictions.

- **Security Considerations:** Exercise caution when handling the log files, especially if they contain sensitive information. Protect them from unauthorized access and ensure proper disposal when no longer needed.

- **Ethical Use:** Use this script responsibly and ethically. Avoid logging sensitive information without explicit consent and adhere to ethical guidelines when deploying keyloggers for legitimate purposes such as parental control or employee monitoring.

## Dependencies:

- `pynput`: Python library used for monitoring and controlling input devices such as keyboards and mice.
- `time`: Standard Python module used for time-related functionalities.
