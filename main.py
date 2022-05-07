import os
import click


@click.command('split')
@click.option('-f', help='Specify file to split.')
@click.option('-b', type=int, default=1024, help='Specify chunk size in bytes.')
def split(f, b=1024):
    """Function to split a file into chunks"""
    CHUNK = 0
    file = open(f, 'rb')
    byte = file.read(b)
    while byte:
        new_file = f'{f}-{str(CHUNK)}.chk'
        tmp_file = open(new_file, 'wb')
        tmp_file.write(byte)
        tmp_file.close()
        byte = file.read(b)
        CHUNK += 1


@click.command('join')
@click.option('-f', help='Specify filename')
def join(f):
    """Function to join chunks into a file"""
    return os.system(f'cat *.chk > {f}')


@click.group()
def main():
    pass


main.add_command(split)
main.add_command(join)
main.help = "Example: python main.py split -f <filename> -b 1024"
main.help = "Example: python main.py join -f <filename>"
main.add_help_option = False

if __name__ == '__main__':
    main()
