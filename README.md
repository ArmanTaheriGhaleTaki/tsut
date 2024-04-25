# tsut
twitter(x) space uploader to telegram channel

## Requirements

- `ffmpeg` if not using portable binaries.
- A logged in user's cookies file exported from Twitter in the [Netscape format](https://curl.se/docs/http-cookies.html).
- telegram **bot toekn** and **CHAT_ID**


## Usage
at first you need to add **bot toekn** and **CHAT_ID** into *.env* file 
    
for single space 
```bash
tsut -i space_url -c COOKIE_FILE
```
to read the links with spaces from a file like **spaces.txt**. 
```bash
tsut -f spaces.txt -c COOKIE_FILE
```

## Features

Here's the output of the help option

```txt
usage: tsut [-h] -c COOKIE_FILE
                  [-i SPACE_URL] [-f spaces.txt]

Script designed to help download twitter spaces

options:
  -h, --help            show this help message and exit

  -c COOKIE_FILE        cookies file in the Netscape format. The specs of the
                        Netscape cookies format can be found here:
                        https://curl.se/docs/http-cookies.html. The cookies
                        file is now required due to the Twitter API change
                        that prohibited guest user access to Twitter API
                        endpoints on 2023-07-01.

input:
  -i SPACE_URL, --input-url SPACE_URL
  -f spaces.txt, --file spaces.txt 
```

## Known Errors

`Changing ID3 metadata in HLS audio elementary stream is not implemented....`

This is an error in ffmpeg that does not affect twspace_dl at all as far as I know.

