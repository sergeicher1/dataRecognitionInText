```markdown
# Data Recognition in Text

This Python program leverages Microsoft's `recognizers-text` library to extract structured data (dates, times, and numbers) from a text input. It's a simple yet powerful tool for processing and extracting natural language data, useful for building intelligent applications.

## Features

- Recognizes **dates**, **times**, and **numbers** from natural language text.
- Handles cases where no recognizable data is found.
- Includes error handling for invalid inputs or library failures.
- Easily customizable for extracting other types of entities.

## Example

**Input Text**:  
`The meeting is scheduled for July 15, 2024, at 3:00 PM.`

**Output**:
```
Extracted Data:
- Date(s): July 15, 2024
- Time(s): 3:00 PM
```

## Installation

To set up and run this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/dataRecognitionInText.git
   cd dataRecognitionInText
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the `recognizers-text` and other required libraries**:
   ```bash
   pip install recognizers-text-suite emoji==1.7
   ```

## Usage

Once you've installed the necessary packages, you can run the program with a sample input text to extract dates, times, and numbers.

1. **Run the program**:
   ```bash
   python main.py
   ```

2. **Modify the text**:
   Edit the `input_text` variable in `main.py` with the desired text.

For example:
```python
input_text = "The event will happen on December 5, 2025, at 10:30 AM."
```

### Output:

The program will print the recognized dates, times, and numbers in a structured format:
```
Extracted Data:
- Date(s): December 5, 2025
- Time(s): 10:30 AM
```

## Error Handling

If the input text contains no recognizable data, the program will notify you:
```
No recognizable data found.
```

In case of any issues with the libraries or the input data, the program will display an error message.

## Troubleshooting

### `ImportError: cannot import name 'UNICODE_EMOJI' from 'emoji'`

This error occurs due to incompatibility with the latest version of the `emoji` library. To fix this issue:

1. Install version 1.7 of the `emoji` library:
   ```bash
   pip install emoji==1.7
   ```

2. Re-run the program.

## Contributing

Feel free to contribute to this project! Here's how you can help:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Sections:

1. **Features**: Highlights the core capabilities of the program.
2. **Installation**: Explains how to set up the environment and install dependencies.
3. **Usage**: Provides detailed instructions for running the program.
4. **Error Handling**: Describes common issues and how to resolve them.
5. **Contributing**: Encourages others to contribute to the project.
6. **License**: References the license file for legal information.

You can customize this `README.md` with your repository link and any additional information you want to include.