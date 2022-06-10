import os
import sys
from rich.console import RenderableType

from rich.syntax import Syntax
from rich.traceback import Traceback

from textual.app import App
from textual.widgets import Header, Footer, FileClick, ScrollView, DirectoryTree


class ContentView(App): 
    async def on_load(self) -> None:
        """Sent before going in to application mode."""
        await self.bind("b", "view.toggle('sidebar')", "Toggle sidebar")
        await self.bind("q", "quit", "Quit")
        try:
            self.path = sys.argv[1]
        except IndexError:
            self.path = os.path.abspath(
                os.path.join(os.path.basename(__file__), "../../")
            )

    async def on_mount(self) -> None:
        self.body = ScrollView()
        self.directory = DirectoryTree(self.path, "Code")

        # for some reason, the header has to have that ladybug and i hate it but so it goes i guess
        await self.view.dock(Header(), edge="top")
        await self.view.dock(Footer(), edge="bottom")

        # the directory is also in scroll view
        await self.view.dock(
            ScrollView(self.directory), edge="left", size=48, name="sidebar"
        )
        await self.view.dock(self.body, edge="top")

    async def handle_file_click(self, message: FileClick) -> None:
        """A message sent by the directory tree when a file is clicked."""

        syntax: RenderableType
        try:
            syntax = Syntax.from_path(
                message.path,
                line_numbers=True,
                word_wrap=True,
                indent_guides=True,
                theme="monokai",
            )
        except Exception:
            pass
        self.app.sub_title = os.path.basename(message.path)
        await self.body.update(syntax)

ContentView.run(title="Snakeskin", log="textual.log")