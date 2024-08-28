from textual import events
from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Button


class Keyboard(Widget):
    DEFAULT_CSS = """
    Keyboard {
        background: $panel;
        width: auto;
        height: auto;
        layout: grid;
        grid-size: 30;
        grid-columns: 2;
        grid-rows: 2;
        grid-gutter: 1;
        keyline: thin $panel-darken-1;

        Button {
            column-span: 2;
            min-width: 5;
            width: 100%;
            height: 2;
            border: none;
            background: $panel-lighten-1;
            content-align: center bottom;

            &:hover {
                border: none;
            }

            &.-active {
                border: none;
            }

            &.tab {
                column-span: 4;
                content-align: left bottom;
                text-align: left;
            }

            &.backspace {
                column-span: 4;
                content-align: right bottom;
                text-align: right;
            }

            &.caps_lock {
                column-span: 4;
                content-align: left bottom;
                text-align: left;
            }

            &.enter {
                column-span: 4;
                content-align: right bottom;
                text-align: right;
            }

            &.shift {
                column-span: 5;
            }


            &.ctrl {
                column-span: 3;
            }

            &.super {
                column-span: 3;
            }

            &.alt {
                column-span: 3;
            }

            &.fn {
                column-span: 3;
            }

            &.space {
                column-span: 12;
            }

            &.left-hand {
                &.shift {
                    content-align: left bottom;
                    text-align: left;
                }
            }

            &.right-hand {
                &.shift {
                    content-align: right bottom;
                    text-align: right;
                }
            }
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("esc", classes="escape left-hand")
        yield Button("!\n1", classes="left-hand")
        yield Button("@\n2", classes="left-hand")
        yield Button("#\n3", classes="left-hand")
        yield Button("$\n4", classes="left-hand")
        yield Button("%\n5", classes="left-hand")
        yield Button("^\n6", classes="right-hand")
        yield Button("&\n7", classes="right-hand")
        yield Button("*\n8", classes="right-hand")
        yield Button("(\n9", classes="right-hand")
        yield Button(")\n0", classes="right-hand")
        yield Button("_\n—", classes="right-hand")
        yield Button("+\n=", classes="right-hand")
        yield Button("backspace", classes="backspace right-hand")

        yield Button("tab", classes="tab left-hand")
        for idx, key in enumerate(list("QWERTYUIOP")):
            hand = "left-hand" if idx < 5 else "right-hand"
            yield Button(key, classes=f"{key.lower()} {hand}")
        yield Button("{\n[", classes="right-hand")
        yield Button("}\n]", classes="right-hand")
        yield Button("|\n\\", classes="right-hand")

        yield Button("caps lock", classes="caps_lock left-hand")
        for idx, key in enumerate(list("ASDFGHJKL")):
            hand = "left-hand" if idx < 5 else "right-hand"
            yield Button(key, classes=f"{key.lower()} {hand}")
        yield Button(":\n;", classes="right-hand")
        yield Button("“\n'", classes="right-hand")
        yield Button("enter", classes="enter right-hand")

        yield Button("shift", classes="shift left-hand")
        for idx, key in enumerate(list("ZXCVBNM")):
            hand = "left-hand" if idx < 5 else "right-hand"
            yield Button(key, classes=f"{key.lower()} {hand}")
        yield Button("<\n,", classes="comma less_than_sign right-hand")
        yield Button(">\n.", classes="full_stop greater_than_sign right-hand")
        yield Button("?\n/", classes="slash question_mark right-hand")
        yield Button("shift", classes="shift right-hand")

        yield Button("ctrl", classes="ctrl left-hand")
        yield Button("super", classes="super left-hand")
        yield Button("alt", classes="alt left-hand")
        yield Button("", classes="space")
        yield Button("alt\ngr", classes="alt right-hand")
        yield Button("fn", classes="fn right-hand")
        yield Button("ctrl", classes="ctrl right-hand")


class KeyboardApp(App):
    AUTO_FOCUS = None

    CSS = """
    Screen {
        align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Keyboard()

    def on_key(self, event: events.Key) -> None:
        self.log(event.key)


if __name__ == "__main__":
    app = KeyboardApp()
    app.run()
