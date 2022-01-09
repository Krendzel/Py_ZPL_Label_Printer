# Python ZPL Label Printer

![Py ZPL Label Printer](https://i.imgur.com/mIFREfS.png)

Simple python script with GUI based on PyQt5 that sends ZPL label to Zebra printer. You can define multiple templates and send them directly to printer using `socket` library (you don't need any external drivers.)

You can use variables in template by using `{variable_name}` in template file and override them in GUI

Example template:
```angular2html
^XA
^CF0,40
^FO50,300^FD{var1}^FS
^FO50,360^FD100{street_name}^FS
^FO50,420^FD{city} TN 39021^FS
^FO50,480^FDUnited States (USA)^FS
XZ
```


## Prerequisites

### Install dependencies
Run command `pip install -r requirements.txt`

## Usage
Run script: `python app.py`

### Running locally 
If You don't have any Zebra printer, You can emulate prints by installing extension 'Zpl Printer' from [Chrome web store](https://chrome.google.com/webstore/detail/zpl-printer/phoidlklenidapnijkabnfdgmadlcmjo) 
After installing, you can select "DEV" printer (default: 127.0.0.1:5500) in GUI and print labels in browser.

For now, to add more printers You need edit script `app.py` and add new printer by duplicating line `27`
```python 
self.printer_select.addItem('printer_name', '127.0.0.1')
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## TODO

* [ ] Add support for multiple printers
* [ ] Add option to print labels from .csv file
* [ ] Redesign GUI (dark mode)


## License
[MIT](https://choosealicense.com/licenses/mit/)