import click
import sys

def extract(file_data):
    byte_count = 0
    line_count = 0
    word_count = 0
    char_count = 0
    
    lines = file_data.readlines()
    for line in lines:
        byte_count += len(line)
        line_count +=1
        word_count += len(line.split())
        char_count += len(line.decode())
    return byte_count, line_count, word_count, char_count

@click.command()
@click.argument("file", nargs=-1, type=click.Path(exists=True))
@click.option('-c', is_flag=True)
@click.option('-l', is_flag=True)
@click.option('-w', is_flag=True)
@click.option('-m', is_flag=True)
def wc(file, c, l, w, m):
    if not file:
        file_data = sys.stdin.buffer
        byte_count, line_count, word_count, char_count = extract(file_data)
    else:
        with open(file, 'rb') as file_data:
            byte_count, line_count, word_count, char_count = extract(file_data)
    output = ""
    if not (l or c or w or m):
        output += f'{line_count}\t{word_count}\t{byte_count}\t'
    else:

        if l:
            output += f'{line_count}\t'
        if w:
            output += f'{word_count}\t'
        if c:
            output += f'{byte_count}\t'
        if m:
            output += f'{char_count}\t'
    if file:
        output += f'{file}\n'.strip()
    else:
        output+='\n'.strip()
    
    click.echo(output)

if __name__ == "__main__":
    wc()