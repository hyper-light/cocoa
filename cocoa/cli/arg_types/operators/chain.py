from __future__ import annotations
import asyncio
from typing import Generic, TypeVarTuple, Any, get_args, get_origin, TypeVar, Callable


T = TypeVarTuple("T")
K = TypeVar("K")


from cocoa.cli.arg_types.data_types import (
    AssertSet,
    Env,
    ImportFile,
    JsonData,
    JsonFile,
    Paths,
    Pattern,
    RawFile,
)


class Chain(Generic[*T]):
    def __init__(
        self,
        name: str,
        data_type: Chain[tuple[*T]],
    ):
        super().__init__()

        self.name = name
        self._types: tuple[*T] = get_args(data_type)

        self._data_type = [
            subtype_type.__name__
            for subtype_type in self._types
            if hasattr(data_type, "__name__")
        ]

        self.data: Any | None = None

        self._complex_types: dict[
            AssertSet | Env | ImportFile | JsonData | JsonData | Pattern | RawFile,
            Callable[
                [str, type[Any]],
                AssertSet | Env | ImportFile | JsonData | JsonData | Pattern | RawFile,
            ],
        ] = {
            AssertSet: lambda name, subtype: AssertSet(name, subtype),
            Env: lambda envar, subtype: Env(envar, subtype),
            ImportFile: lambda _, subtype: ImportFile(subtype),
            JsonFile: lambda _, subtype: JsonFile(subtype),
            JsonData: lambda _, subtype: JsonData(subtype),
            Paths: lambda _, subtype: Paths(subtype),
            Pattern: lambda _, subtype: Pattern(subtype),
            RawFile: lambda _, subtype: RawFile(subtype),
        }

        self._loop = asyncio.get_event_loop()

    def __contains__(self, value: Any):
        return type(value) in self._types

    @property
    def data_type(self):
        return ", ".join(self._data_type)

    async def parse(self, arg: str | None = None):
        result: Any | Exception | str = arg
        err: Exception | None = None

        for subtype in self._types:
            if complex_type_factory := self._complex_types.get(get_origin(subtype)):
                complex_type = complex_type_factory(self.name, subtype)

                err = await complex_type.parse(result)
                result = complex_type.data

            if isinstance(err, Exception):
                return err

        self.data = result

        return self
