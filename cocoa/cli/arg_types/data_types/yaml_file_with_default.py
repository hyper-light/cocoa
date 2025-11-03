import asyncio
import os
import pathlib
from typing import Any

try:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedBase
    from ruamel.yaml.comments import CommentedMap

except (Exception, ImportError):

    class CommentedBase:

        def __init__(self):
            pass

    class CommentedMap:

        def __init__(self):
            pass

    class YAML:
        def __init__(
            self,
            typ: str | None = None
        ):
            self.preserve_quotes: bool = False
            self.width: int = 0 

        def indent(
            mapping: int | None = None, 
            sequence: int | None = None, 
            offset: int | None = None,
        ):
            pass

        def load(self, file_pointer: Any):
            return ImportError('You must install the [yaml] option to use the YamlFileWithDefault operator!')
        
        def dump(self, file_pointer: Any, data: Any):
            return ImportError('You must install the [yaml] option to use the YamlFileWithDefault operator!')


class YamlFileWithDefault:
    def __init__(self):
        super().__init__()

        self.data: CommentedBase | None = None

        self._data_types = [str]
        self._types = [str]

        self._loop = asyncio.get_event_loop()

    def __contains__(self, value: Any):
        return type(value) in [self._types]

    @property
    def data_type(self):
        return "Yaml"

    async def parse(self, arg: str | None = None):
        result = await self._load_yaml_file(arg)
        if isinstance(result, Exception):
            return result

        self.data = result

        return self

    async def _load_yaml_file(self, arg: str | None = None):
        try:
            if arg is None:
                return Exception("no argument passed for filepath")

            return await self._loop.run_in_executor(
                None,
                self._load_yaml_or_default,
                arg,
            )

        except Exception as e:
            return Exception(
                f"encountered error {str(e)} parsing file at {arg} to YAML"
            )

    def _load_yaml_or_default(self, arg: str):

        if arg.startswith('~/'):
            arg.replace('~/', '')
            arg = os.path.join(
                str(pathlib.Path.home()),
                arg,
            )

        elif arg == '.':
            arg = os.getcwd()

        yaml = YAML(typ='rt')
        if not pathlib.Path(arg).absolute().exists():

            yaml.preserve_quotes = True
            yaml.width = 4096
            yaml.indent(mapping=2, sequence=4, offset=2)
            data = CommentedMap()
            with open(arg, 'w') as file:
                yaml.dump(data, file)

            return data
        
        with open(arg) as file:
            data = yaml.load(file)

            if data is None:
                return CommentedMap()
            
            return data

                

