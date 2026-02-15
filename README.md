# URL Encode Python

A Python library and CLI tool for URL encoding and decoding.

## Features

- URL encode strings
- URL decode encoded strings
- Batch processing support
- Component vs full URL encoding
- Special character handling
- Python API for integration

## Installation

```bash
pip install url-encode-python
```

Or clone and install:

```bash
git clone https://github.com/mizoz/url-encode-python.git
cd url-encode-python
pip install -e .
```

## Usage

### Command Line

```bash
# Encode a string
url-encode "Hello World!"

# Decode an encoded string
url-decode "Hello%20World%21"

# Encode multiple strings
url-encode "string1" "string2"

# Encode as URL component
url-encode --component "Hello World"
```

### Python API

```python
from url_encode import URLEncoder

encoder = URLEncoder()

# Encode a string
encoded = encoder.encode("Hello World!")
print(encoded)  # Hello%20World%21

# Decode a string
decoded = encoder.decode("Hello%20World%21")
print(decoded)  # Hello World!

# Encode as component
encoded = encoder.encode_component("Hello World!")
print(encoded)  # Hello%20World%21
```

## Options

- `-d, --decode` - Decode instead of encode
- `-c, --component` - Encode as URL component

## License

MIT License

## Author

mizoz
