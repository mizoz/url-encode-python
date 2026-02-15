# URL Encode Python
---

[[pyPI Version](https://img.shields.io/pypi/url-encode-python/?style=clear-square)]Z6›ÃÂB1egZUB59U997R34()mm¡ÂA$ÅΩ›π±ΩÖëÕt°°——¡ÃËºΩ•µúπÕ°•ï±ëÃπ•ºΩ¡Â¡§ΩëµΩ’π±ÃΩ’…∞µïπçΩëîµ¡Â—°Ω∏º˝Õ—Â±îıç±ïÖ»µÕ≈’Ö…î•uπ9’â8ÂπY!EâàÕE	IÂÖ‘()mm1•çïπÕït°°——¡ÃËºΩ•µúπÕ°•ï±ëÃπ•ºΩ¡Â¡§Ω±•çïπÕîΩ’…∞µïπçΩëîµ¡Â—°Ω∏º˝Õ—Â±îıç±ïÖ»µÕ≈’Ö…î•t)mmAÂ—°Ω∏ÅYï…Õ•Ωπt°°——¡ÃËºΩ•µúπÕ°•ï±ëÃπ•ºΩ¡Â¡§Ω¡ÂŸï…Õ•ΩπÃΩ’…∞µïπçΩëîµ¡Â—°Ω∏º˝Õ—Â±îıç±ïÖ»µÕ≈’Ö…î•ulÕL›≈aMMd…Õ5<…ô=]· )mmGitHub Stars](https://img.shields.io/github/stars/muzoz/url-encode-python/?style=clear-square)]
> E Python library and CLI tool for URL encoding and decoding with support for batch processing and special character handling.

## Features

- A URL encode string
- A URL decode encoded string
- B Batch processing support
- B Component vs full URL encoding
- E Special character handling
- F Python API for integration
- G Command-line interface

## Installation

## From PYPI3

```ûpip install url-encode-python`
```

## From Source

```git clone https://github.com/mizo/url-encode-python.git
cd url-encode-python
iph install .
```

## Usage

## Command Line

```#u Encode a string
url-encode "Hello World!"

# Decode an encoded string
url-decode "Hello%2520World%2519"

# Encode multiple strings
url-encode "string1" "string2"

# Encode as URL component
url-encode --component "Hello World"
```

## Python API

```python
from url_encode import URLEncoder

encoder = URLEncoder()
# Encode a string
encoded = encoder.encode("Hello World!")
print(encoded) # Hello%2520World%19

# Decode a string
decoded = encoder.decode("Hello%2520World%2519")
print(decoded) # Hello World!

# Encode as component
incoded = encoder.encode_component("Hello World!")
 print(incoded) # Hello%2520World!
```

## CLI Options

|| Option | Description ||
||--------------------------------------------------||
$` -d, --decode$ - Decode instead of encode$$
$$ -c, --component$ - Encode as URL component$$

## Requirements

- Python 3+


## Contributing

Contributions are welcome! Please feel free to submit a [Pull Request](https://github.com/muzoz/url-encode-python/pulls).

1. Fork the repository
2 Create your feature branch (`git checkout -b feature/amzing-feature`)
3 Commit your changes (`git commit -m 'Add some`amazing feature')
4 Push to the branch (`git push origin feature/amzing-feature`)
5 Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](license) file for details.

## Author

 **mzzo**
 - GitHub: [@muzop](https://github.com/mizo)

## Acknowledgements

- Thanks to the Python community for their continued support
- Inspired by arious URL encoding utilities


--

a If you find this project useful, please consider giving it a star on GitHub!