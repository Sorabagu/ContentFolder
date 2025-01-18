# ContentFolder

**ContentFolder** is a Python application built with wxPython that allows users to explore directory structures and copy the directory tree to their clipboard. This application features a modern dark theme and provides an intuitive interface for managing file structures.

## Features

- **Folder Selection**: Choose any directory on your system to analyze.
- **Directory Tree Visualization**: Displays the directory tree structure in a clean and organized format.
- **Clipboard Export**: Copy the displayed directory tree to your clipboard with a single click.
- **Dark Theme**: The interface is designed with a modern, dark aesthetic for comfortable usage.

## Requirements

- **Python 3.7 or higher**
- **wxPython** library

Install wxPython using pip:
```bash
pip install wxPython
```

## How to Use

1. Clone this repository or download the script.
2. Ensure that the `icon.ico` file is placed in the same directory as the script.
3. Run the script:
   ```bash
   python ContentFolder.pyw
   ```
4. Use the **Browse** button to select a folder.
5. The directory tree will appear in the text area.
6. Click **Copy** to copy the tree structure to your clipboard.

## Application Interface

- **Text Area**: Displays the directory structure.
- **Browse Button**: Opens a dialog to select a folder.
- **Export Button**: Copies the directory tree to the clipboard (enabled after folder selection).

## File Structure

```
.
├── script_name.py   # Main script
├── icon.ico         # Application icon
└── README.md        # Documentation
```

## Screenshots

![ContentFolder UI](https://github.com/Sorabagu/contentfolder/blob/main/screenshot.png?raw=true))  

## Customization

You can customize the button labels and other aspects of the UI by modifying the following lines in the script:

```python
frame = ContentFolderApp(btn_choose_text="Your Browse Text", btn_copy_text="Your Export Text")
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
