"""
Test the casing (snake_case vs camelCase) used by the converters
"""
import pytest

from acclimatise.converter import WrapperGenerator
from acclimatise.model import EmptyFlagArg, Flag


@pytest.fixture()
def snake_gen():
    return WrapperGenerator(case="snake", generate_names=True)


@pytest.fixture()
def camel_gen():
    return WrapperGenerator(case="camel", generate_names=True)


def test_camel_short(camel_gen):
    flag = Flag(
        synonyms=["-t"], description="number of threads [1]", args=EmptyFlagArg()
    )
    name = camel_gen.choose_variable_name(flag)
    assert name == "numberThreads"


def test_snake_short(snake_gen):
    flag = Flag(
        synonyms=["-t"], description="number of threads [1]", args=EmptyFlagArg()
    )
    name = snake_gen.choose_variable_name(flag)
    assert name == "number_threads"


def test_camel_long(camel_gen):
    flag = Flag(
        synonyms=["-g", "--genomepaths", "--genomefolders"],
        description="number of threads [1]",
        args=EmptyFlagArg(),
    )
    name = camel_gen.choose_variable_name(flag)
    assert name == "genomeFolders"


def test_snake_long(snake_gen):
    flag = Flag(
        synonyms=["-g", "--genomepaths", "--genomefolders"],
        description="number of threads [1]",
        args=EmptyFlagArg(),
    )
    name = snake_gen.choose_variable_name(flag)
    assert name == "genome_folders"