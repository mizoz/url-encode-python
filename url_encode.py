#!/usr/bin/env python3
"""URL encode/decode tool."""

import sys
import urllib.parse


def main():
    if len(sys.argv) < 2:
        print("Usage: url_encode.py <string> [--decode]")
        sys.exit(1)
    
    decode = '--decode' in sys.argv
    text = ' '.join([a for a in sys.argv[1:] if not a.startswith('--')])
    
    if decode:
        result = urllib.parse.unquote(text)
    else:
        result = urllib.parse.quote(text)
    
    print(result)


if __name__ == "__main__":
    main()
