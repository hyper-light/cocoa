from __future__ import annotations

import asyncio
import itertools
from typing import (
    Any,
    Optional,
)

from cocoa.ui.config.mode import TerminalMode
from cocoa.ui.config.widget_fit_dimensions import WidgetFitDimensions
from cocoa.ui.styling import stylize, get_style
from .spinner_config import SpinnerConfig
from .spinner_factory import SpinnerFactory
from .spinner_status import (
    SpinnerStatus, 
    SpinnerStatusName, 
    SpinnerStatusMap,
)


class Spinner:
    def __init__(
        self,
        name: str,
        config: SpinnerConfig,
        subscriptions: list[str] | None = None,
    ):
        self.fit_type = WidgetFitDimensions.X_AXIS
        self._name = name

        if subscriptions is None:
            subscriptions = []

        self._config = config
        self.subscriptions = subscriptions

        # Spinner
        factory = SpinnerFactory()
        spinner = factory.get(config.spinner)

        self._spinner_size = spinner.size
        self._frames = (
            spinner.frames[::-1] if config.reverse_spinner_direction else spinner.frames
        )
        self._cycle = itertools.cycle(self._frames)

        self._last_frame: Optional[str] = None
        self._base_size: int = 0
        self._max_width: int = 0
        self._last_frame: str | None = None

        self._update_lock: asyncio.Lock | None = None
        self._updates: asyncio.Queue[SpinnerStatus] | None = None

        self._mode = TerminalMode.to_mode(config.terminal_mode)
        self._status_map = SpinnerStatusMap()

    @property
    def raw_size(self):
        return self._base_size

    @property
    def size(self):
        return self._base_size

    async def update(self, status: SpinnerStatusName):
        await self._update_lock.acquire()
        self._updates.put_nowait(
            self._status_map.map_to_status(status)
        )
        
        self._update_lock.release()

    async def fit(
        self,
        max_width: int | None = None,
    ):
        if self._update_lock is None:
            self._update_lock = asyncio.Lock()

        if self._updates is None:
            self._updates = asyncio.Queue()

        remaining_size = max_width

        remaining_size -= self._spinner_size
        if remaining_size <= 0 and self._text:
            self._text = ""

        elif self._text:
            self._text = self._text[:remaining_size]
            remaining_size -= len(self._text)

        self._base_size = self._spinner_size + len(self._text)
        self._max_width = max_width

    async def get_next_frame(self):
        status = await self._check_if_should_rerender()

        if status in [SpinnerStatus.OK, SpinnerStatus.FAILED]:
            self._last_frame = self._create_last_frame(status)
            return [self._last_frame], True

        frame = await self._create_next_spin_frame()
        return [frame], True

    async def pause(self):
        pass

    async def resume(self):
        pass

    async def stop(self):
        if self._update_lock.locked():
            self._update_lock.release()

        await self.ok()

    async def abort(self):
        if self._update_lock.locked():
            self._update_lock.release()

        await self.fail()

    async def ok(self):
        await self._update_lock.acquire()
        self._updates.put_nowait(SpinnerStatus.OK)
        self._update_lock.release()

    async def fail(self):
        await self._update_lock.acquire()
        self._updates.put_nowait(SpinnerStatus.FAILED)
        self._update_lock.release()

    async def _check_if_should_rerender(self):
        await self._update_lock.acquire()

        status: SpinnerStatus | None = None
        if self._updates.empty() is False:
            status = await self._updates.get()

        self._update_lock.release()

        return status

    async def _create_last_frame(
        self,
        status: SpinnerStatus
    ):
        """Stop spinner, compose last frame and 'freeze' it."""

        if status == SpinnerStatus.FAILED:
            return await stylize(
                self._config.fail_char,
                color=get_style(self._config.fail_color),
                highlight=get_style(self._config.fail_highlight),
                attrs=[get_style(attr) for attr in self._config.fail_attrbutes]
                if self._config.fail_attrbutes
                else None,
                mode=self._mode,
            )

        return await stylize(
            self._config.ok_char,
            color=get_style(self._config.ok_color),
            highlight=get_style(self._config.ok_highlight),
            attrs=[get_style(attr) for attr in self._config.ok_attributes]
            if self._config.ok_attributes
            else None,
            mode=self._mode,
        )

    async def _create_next_spin_frame(self):
        # Compose output
        spin_phase = next(self._cycle)

        return await stylize(
            spin_phase,
            color=get_style(self._config.color),
            highlight=get_style(self._config.highlight),
            attrs=[get_style(attr) for attr in self._config.attributes]
            if self._config.attributes
            else None,
            mode=self._mode,
        )
