from grc.core.utils.hide_bokeh_gui_options_if_not_installed import (
    hide_bokeh_gui_options_if_not_installed,
)


def test_bokeh_gui_option_is_removed_when_bokeh_is_not_installed(monkeypatch):
    monkeypatch.setitem(__import__("sys").modules, "bokehgui", None)

    options_blk = type("Options", (), {
        "parameters_data": [{
            "id": "generate_options",
            "options": ["qt_gui", "bokeh_gui"],
            "option_labels": ["QT GUI", "Bokeh GUI"],
        }]
    })()

    hide_bokeh_gui_options_if_not_installed(options_blk)

    param = options_blk.parameters_data[0]
    assert param["options"] == ["qt_gui"]
    assert param["option_labels"] == ["QT GUI"]


def test_missing_bokeh_gui_option_does_not_raise(monkeypatch):
    monkeypatch.setitem(__import__("sys").modules, "bokehgui", None)

    options_blk = type("Options", (), {
        "parameters_data": [{
            "id": "generate_options",
            "options": ["qt_gui"],
            "option_labels": ["QT GUI"],
        }]
    })()

    hide_bokeh_gui_options_if_not_installed(options_blk)
