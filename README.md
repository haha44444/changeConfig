# YAML MOTD Processing Tools

A Python tool for processing YAML format MOTD configurations, allowing for one click import of random server descriptions.
![GitHub](https://img.shields.io/badge/Version-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)

## Features
- Two MOTD formatting modes
- Customizable line prefixes
- YAML configuration preservation
- Automatic text wrapping
- UTF-8 encoding support

## Installation
1. Ensure Python 3.8+ is installed
2. Install dependencies:
    ```bash
    pip install ruamel.yaml
    ```
## Usage
1. Prepare your ```config.yml``` and ```motd.txt``` files
2. Run the script:
    ```bash
    python motd_processor.py
    ```
3. Follow interactive prompts:
   - Choose MOTD format (1/2)
   - Enter prefixes for both lines
   - Specify YAML key path (e.g. ```description.text```)

Output will be saved to ```config_done.yml```

## File Configuration
### motd.txt (One message per line)
```
First MOTD message
Second MOTD message
...
```
