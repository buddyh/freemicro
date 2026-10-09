"""Shared test fixtures.

The single most important thing here: **no test ever touches real hardware.**
A developer running ``pytest`` with a Codex Micro plugged in must not have their
LEDs repainted or their terminal typed into, so the device layer is disabled for
the whole session and every action test uses a recording backend.
"""

from __future__ import annotations

import pytest

from freemicro.device import ENV_NO_DEVICE


@pytest.fixture(autouse=True)
def no_hardware(monkeypatch):
    """Make the pad look absent to every test."""
    monkeypatch.setenv(ENV_NO_DEVICE, "1")


@pytest.fixture(autouse=True)
def terminal_session_env(monkeypatch):
    """Run as a terminal session even when the suite runs inside Claude desktop."""
    monkeypatch.delenv("CLAUDE_CODE_ENTRYPOINT", raising=False)
    monkeypatch.delenv("CLAUDE_CODE_HOST_SESSION_ID", raising=False)


@pytest.fixture(autouse=True)
def isolated_config(monkeypatch, tmp_path):
    """Keep tests off the developer's real ``~/.freemicro`` config."""
    monkeypatch.setenv("FREEMICRO_HOME", str(tmp_path / "freemicro"))
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path / "xdg"))
    monkeypatch.delenv("FREEMICRO_KEYMAP", raising=False)
