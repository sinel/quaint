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
from click.testing import CliRunner

from quaint.main import run


def test_run_with_invalid_path() -> None:
    """Unit test for run method."""
    runner = CliRunner()
    result = runner.invoke(run, ["dummy.yaml"])  # type: ignore
    assert result.exit_code != 0
    assert result.exception is not None
    assert "Error: Invalid value for" in result.output


def test_run() -> None:
    """Unit test for run method."""
    runner = CliRunner()
    result = runner.invoke(run, ["tests/test.yaml"])  # type: ignore
    assert result.exit_code == 0
    assert result.exception is None
    assert "tests/test.yaml" in result.output
