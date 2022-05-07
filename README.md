# Space savers

A tool to split and join files, hopefully one could find a use case for it..

## Installation

```bash
pip install -r requirement.txt
```

## Usage

```python
# returns files of byte size ending with .chk
python main.py slice -f <filename> -b <byte size>

# returns one file of files specified by prefix
python main.py join -f <prefix>
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
