from typing import ClassVar, Literal, TypeAlias

SynchronizeSessionValue: TypeAlias = Literal["fetch", "evaluate", False]


class SynchronizeSessionEnum:
    FETCH: ClassVar[Literal["fetch"]] = "fetch"
    EVALUATE: ClassVar[Literal["evaluate"]] = "evaluate"
    FALSE: ClassVar[Literal[False]] = False
