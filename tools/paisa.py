#! /usr/bin/env python3
from textual.app import App
from textual.widgets import Placeholder

class PaisaApp(App):
    async def on_mount(self) -> None:
        await self.view.dock(Placeholder(), edge="left", size=40)
        await self.view.dock(Placeholder(), Placeholder(), edge="top")

PaisaApp.run(log="paisa.log")


