#  ****************************************************************************************
#                       _       __
#    ____ ___  ______ _(_)___  / /_
#   / __ `/ / / / __ `/ / __ \/ __/     A Multi-Agent Framework
#  / /_/ / /_/ / /_/ / / / / / /_       for Analysis and Control
#  \__, /\__,_/\__,_/_/_/ /_/\__/       of Superconducting Quantum Circuits
#    /_/
#
#  Copyright (c) 2021-2022 FarSimple Oy.
#
#  The MIT License (MIT)
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of this
#  software and associated documentation files (the "Software"), to deal in the Software
#  without restriction, including without limitation the rights to use, copy, modify,
#  merge, publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included
#  in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#  ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#  OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#  ****************************************************************************************
import click
import confuse


@click.command()
@click.argument(
    "path",
    type=click.Path(
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
        allow_dash=False,
        path_type=str,
    ),
)
def run(path: str) -> None:
    """
    Run quaint2 with specified configuration.

    Args:
        path: Path to configuration file.
    """
    print(f"Configuration file path: {path}")
    config = confuse.Configuration("quaint2")
    config.set_file(path)
    print(config)
