from __future__ import print_function
import click


@click.command()
@click.option(
    '--password',
    prompt=True,
    hide_input=True,
    confirmation_prompt=True)
def encrypt(password):
    click.echo('Encrypt password to %s ' % password)


if __name__ == '__main__':
    encrypt()
