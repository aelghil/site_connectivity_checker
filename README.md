# Use Request library instead of http.client

Ahmed is using requests instead of the http.client library to be able to download more content from the webpage and not only the output of the HEAD method

# New features

- If the site is offline, send a continuous ping to the site until it's online and then send a notification to the user
- Check what other ports are open on that URL other than 80 and 443

# Build a Site Connectivity Checker in Python

RP Checker is a site connectivity checker utility. It takes one or more website URLs and checks if those sites are online. It can perform the connectivity checks either synchronously or asynchronously.

## Installation

1. Create a Python virtual environment

```sh
$ python -m venv ./venv
$ source venv/bin/activate
(venv) $
```

2. Install the requirements

```
(venv) $ python -m pip install -r requirements.txt
```

## Run the Project

```sh
(venv) $ python -m rpchecker -u python.org
The status of "python.org" is: "Online!" 👍
```

## Features

RP Checker provides the following options:

- `-u` or `--urls` takes one or more URLs and checks if they're online.
- `-f` or `--input-file` takes a file containing a list of URLs to check.
- `-a` or `--asynchronous` runs the check asynchronously.

## About the Author

Leodanis Pozo Ramos - Email: leodanis@realpython.com

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.
