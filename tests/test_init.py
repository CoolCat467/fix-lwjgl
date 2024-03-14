from __future__ import annotations

import os

import fix_lwjgl
import pytest


def test_get_paths() -> None:
    assert fix_lwjgl.get_paths(
        {
            "": [
                "main.py",
                "waffles.txt",
            ],
            "folder": {
                "": [
                    "folder_one.txt",
                ],
                "inner": {
                    "": [
                        "folder_two.txt",
                    ],
                    "inner_two": [
                        "folder_three.txt",
                    ],
                },
            },
        },
    ) == [
        "main.py",
        "waffles.txt",
        os.path.join("folder", "folder_one.txt"),
        os.path.join("folder", "inner", "folder_two.txt"),
        os.path.join("folder", "inner", "inner_two", "folder_three.txt"),
    ]


def test_get_address() -> None:
    assert (
        fix_lwjgl.get_address("CoolCat467", "fix-lwjgl", "HEAD", "README.md")
        == "https://raw.githubusercontent.com/CoolCat467/fix-lwjgl/HEAD/README.md"
    )


def test_get_lwjgl_file_url() -> None:
    assert (
        fix_lwjgl.get_lwjgl_file_url("bin/lwjgl/lwjgl.jar")
        == "https://build.lwjgl.org/release/latest/bin/lwjgl/lwjgl.jar"
    )


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("17w43b", 3),
        ("17w42b", 2),
        ("1.12.2", 2),
        ("1.13.0", 3),
        ("1.7.10", 2),
        ("1.20.1", 3),
    ],
)
def test_discover_lwjgl_version(version: str, expected: int) -> None:
    assert fix_lwjgl.discover_lwjgl_version(version) == expected
