import gzip
import argparse
from html.parser import HTMLParser
from html.parser import HTMLParser
from openpyxl import Workbook
from openpyxl import load_workbook
import os


class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        """
        recognize data, html content string
        :param data:
        :return:
        """
        if self.lasttag == 'span':
            if data.strip():
                print(data)
        if self.lasttag == 'td':
            if data.strip():
                print(data)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--log_path", required=True, help='log_path')
    parser.add_argument('-v', "--verbose", action='store_true',  default=False,  help='output verbose information if specified')
    return parser.parse_args()

def _main():
    try:
        global verbose_flag
        args = parse_args()
        if args.verbose:
            verbose_flag = True
        success = True
        Path = args.log_path
    except Exception as e:
        print("e=%s" % e)
    if success:
        parser = MyHTMLParser()
        devices = os.listdir(Path)  #device SN
        for i in range(len(devices)):
            print('~~~~~~~~~~~~~~~~~~' + devices[i] +'~~~~~~~~~~~~~~~~~~~~~~~')
            monkeyPath = Path + devices[i] + '\\' + os.listdir(Path + devices[i])[0]
            f = gzip.open( monkeyPath + '\idx.gz', 'rb')
            file_content = f.read() 
            parser.feed(file_content.decode("utf-8"))
            f.close() 
            

if __name__ == '__main__':
    _main()