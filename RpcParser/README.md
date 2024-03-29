# Overview

The markdown generator script parses the `MOBILE_API.xml` specification and creates a human-readable markdown file for the API.

## Dependencies

The markdown generator requires python3 and pip3 installed in order to use, these can be installed using the following commands depending on your system:

**Linux (using apt-get)**

```bash
sudo apt install python3 python3-pip -y
```

**Mac (using Homebrew)**

```bash
brew install python3
```

The markdown generator also requires the use the interface parser included in this project, which has its own set of dependencies. These dependency libraries are described in the interface parser's `requirements.txt` and should be pre-installed by the following command:

```bash
pip3 install -r ../InterfaceParser/requirements.txt
```

## Usage

The markdown generator script can be started using the following command:

```bash
python3 markdown_generator.py
```

From there, follow the prompts in the terminal to verify the input and output directories for the generator (default values should be used in most cases).

For information about additional options for the interface generator script, you can run the following command:

```bash
python3 markdown_generator.py --help
```
