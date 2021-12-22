import gzip
import shutil
import os


def extract_datafeed_zip_file(source_zip_file, target_file_name, delete_source=False):
    dir_name = os.path.dirname(target_file_name)

    with gzip.open(source_zip_file, 'rb') as f_in:
        with open(target_file_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

    if (delete_source):
        os.remove(source_zip_file)

if __name__ == '__main__':
    extract_datafeed_zip_file('./file.csv.gz', './test.csv')