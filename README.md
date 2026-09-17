# Number System Converter

A small [Streamlit](https://streamlit.io/) web app that converts numbers between Binary, Octal, Decimal, and Hexadecimal.

## Features

- Convert between any two of: Binary, Octal, Decimal, Hexadecimal
- Simple two-dropdown + text input UI (`From` / `To` / `Number`)
- Custom gradient styling via `style.css`

## Live Demo

https://minulsandith-number-system-converter-main-g0s8xs.streamlitapp.com/

## Tech Stack

- [Streamlit](https://streamlit.io/) – web UI framework
- [`numbersystem`](https://pypi.org/project/numbersystem/) – conversion logic

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone https://github.com/minulsandith/number-system-converter.git
cd number-system-converter
pip install -r requirements.txt
pip install streamlit
```

(`streamlit` itself is not pinned in `requirements.txt`, so install it separately if it isn't already on your machine.)

### Run locally

```bash
streamlit run main.py
```

Then open the local URL Streamlit prints (typically http://localhost:8501).

## How It Works

1. Pick the source format (`From`) and target format (`To`).
2. Enter a number in that source format.
3. Click **Convert** to see the result rendered as `<Format> - <Result>`.

Under the hood, `main.py` maps the selected `From`/`To` combination to the matching conversion function from the `numbersystem` package (e.g. `decimalToHexa`, `binaryToOctal`, etc.).

## Project Structure

```
.
├── main.py            # Streamlit app + conversion logic
├── style.css           # Custom page styling
└── requirements.txt     # Python dependencies
```

## Known Limitations

- Input is not validated against the selected source format before conversion, so an invalid number (e.g. letters in a "Binary" input) will show a generic "Enter a number" message rather than a specific error.
- Only positive whole numbers are supported for Decimal input.

## Status

Actively maintained. Bug reports and pull requests are welcome — please open an issue if you find one.
