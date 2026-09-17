# Number System Converter

A simple web app built with [Streamlit](https://streamlit.io/) that converts numbers between **Binary**, **Octal**, **Decimal**, and **Hexadecimal** number systems.

## Features

- Convert between any two of the four supported number systems: Binary, Octal, Decimal, Hexadecimal
- Clean, minimal UI with a custom-styled gradient background
- Instant conversion as you type or click "Convert"

## Demo

Live app: https://minulsandith-number-system-converter-main-g0s8xs.streamlitapp.com/

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone https://github.com/minulsandith/number-system-converter.git
cd number-system-converter
pip install -r requirements.txt
```

### Run locally

```bash
streamlit run main.py
```

Then open the URL shown in your terminal (usually `http://localhost:8501`).

## Usage

1. Select the number system you're converting **from** in the "From" dropdown.
2. Select the number system you're converting **to** in the "To" dropdown.
3. Enter the number you want to convert.
4. Click **Convert** to see the result, rendered as `<Format> - <Result>`.

## Known Limitations

- Input is not validated against the selected source format before conversion, so an invalid number (e.g. letters in a "Binary" input) shows a generic "Enter a number" message rather than a specific error.
- Only positive whole numbers are supported for Decimal input.

## Project Structure

```
.
├── main.py             # Streamlit app entry point and conversion logic
├── style.css            # Custom styling for the app
└── requirements.txt      # Python dependencies
```

## Built With

- [Streamlit](https://streamlit.io/) — web app framework
- [numbersystem](https://pypi.org/project/numbersystem/) — number base conversion library

## Status

Actively maintained. Please open an issue if you find a bug.
