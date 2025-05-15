from enum import Enum
from typing import Literal

SpinnerStatusName = Literal['active', 'failed', 'ready', 'ok']


class SpinnerStatus(Enum):
    ACTIVE = "ACTIVE"
    FAILED = "FAILED"
    OK = "OK"
    READY = "READY"


class SpinnerStatusMap:

    def __init__(self):
        self._status_map: dict[
            SpinnerStatusName,
            SpinnerStatus,
        ] = {
            'active': SpinnerStatus.ACTIVE,
            'failed': SpinnerStatus.FAILED,
            'ok': SpinnerStatus.OK,
            'ready': SpinnerStatus.READY,
        }

    def map_to_status(self, status_name: SpinnerStatusName):
        return self._status_map[status_name]