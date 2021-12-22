import pysftp
import os.path


def fetch_files_from_ftp(server_conn, user_name, password,
                         source_files, target_files,
                         port=22):
    """
    fetch files from the SFTP server
    :param server_conn: server ip or endpoint (e.g. datafeed-upload.visenze.com)
    :param user_name: user name
    :param password: user password
    :param source_files: list of files to be fetched, can be a path
    :param target_files: list of targeted local path the source files to be saved to
    :param port: optional port number, should be 22
    :return: return True if all the source files provided being located and fetch successfully otherwise False
    """
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    server = pysftp.Connection(host=server_conn, port=port, username=user_name, password=password, cnopts=cnopts)

    # create dir for the output files
    for file in target_files:
        create_dir(file)

    for source_file, target_file in zip(source_files, target_files):
        try:
            server.get(source_file,target_file)
        except Exception as e:
            server.close()
            print(e)
            return False

    server.close()
    return True

def sftp_file_exists(sftp, filename):
    try:
        sftp.get(filename)
        return True
    except FileNotFoundError:
        return False

def delete_files_on_ftp(server_conn, user_name, password, file_names, port=22):
    """
    delete files on the ftp server
    :param server_conn: server ip or endpoint (e.g. datafeed-upload.visenze.com)
    :param user_name: user name
    :param password: user password
    :param file_names: list of file paths on the FTP server that needs to be deleted
    :param port: optional, default is 22
    :return:
    """
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    server = pysftp.Connection(host=server_conn, port=port, username=user_name, password=password, cnopts=cnopts)

    for file_name in file_names:
        if sftp_file_exists(server, file_name):
            try:
                server.remove(file_name)
            except Exception as e:
                print(e)
        else:
            print("There is no old file")

    server.close()
    return True

def change_filename_on_ftp(server_conn, user_name, password, file_names, postfix, port=22):
    """
    delete files on the ftp server
    :param server_conn: server ip or endpoint (e.g. datafeed-upload.visenze.com)
    :param user_name: user name
    :param password: user password
    :param file_names: list of file paths on the FTP server that needs to be deleted
    :param port: optional, default is 22
    :return:
    """
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    server = pysftp.Connection(host=server_conn, port=port, username=user_name, password=password, cnopts=cnopts)

    for file_name in file_names:
        try:
            server.rename(file_name,file_name + postfix)
        except Exception as e:
            print(e)

    server.close()
    return True

def put_file_to_ftp(server_conn, user_name, password, local_file, target_file, port=22):
    """
    put a file to sftp
    :param server_conn: server ip or endpoint (e.g. datafeed-upload.visenze.com)
    :param user_name: user name
    :param password: user password
    :param local_file: local path to the file to be uploaded
    :param target_file: the path on the FTP server the file need to put to
    :param port: optional, default is 22
    :return:
    """
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    with pysftp.Connection(host=server_conn, port=port, username=user_name, password=password, cnopts=cnopts) as sftp:
        sftp.put(local_file, target_file)


def create_dir(filename):
    local_folder = os.path.dirname(filename)

    try:
        os.makedirs(local_folder)
    except OSError:
        if not os.path.isdir(local_folder):
            raise

if __name__ == '__main__':
    d = ['folder/' + 'name' + '.csv.gz']
    postfix = "_old"
    change_filename_on_ftp('server','user','password',d,postfix)