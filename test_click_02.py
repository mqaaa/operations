from __future__ import print_function
import click


@click.command()
@click.option('--hash', type=click.Choice(['md5', 'sha1']))
def digest(hash):
    click.echo(hash)


if __name__ == '__main__':
    digest()
