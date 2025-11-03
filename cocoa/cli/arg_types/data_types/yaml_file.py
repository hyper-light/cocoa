from __future__ import annotations
import asyncio
import io
from pydantic import BaseModel
from typing import Any, TypeVar, Generic
from .reduce_pattern_type import reduce_pattern_type

try:
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedBase

except (Exception, ImportError):

    class CommentedBase:

        def __init__(self):
            pass

    class YAML:
        def __init__(
            self,
            typ: str | None = None
        ):
            pass

        def load(self, file_pointer: Any):
            return ImportError('You must install the [yaml] option to use the YamlFile operator!')


class YamlFile:
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

            return await self._load_file(arg)

        except Exception as e:
            return Exception(
                f"encountered error {str(e)} parsing file at {arg} to JSON"
            )

    async def _load_file(self, arg: str):
        try:

            file_handle: io.TextIOWrapper = await self._loop.run_in_executor(
                None,
                open,
                arg,
            )

            yaml = YAML(typ='rt')
            file_data = await self._loop.run_in_executor(None, yaml.load, file_handle)

            await self._loop.run_in_executor(None, file_handle.close)

            return file_data

        except Exception as e:
            return Exception(f"encountered error {str(e)} opening file at {arg}")
