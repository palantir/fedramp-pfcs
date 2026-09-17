import difflib

from scripts.update_readme import README_PATH, render_readme


def test_readme_matches_template_and_json() -> None:
    current = README_PATH.read_text(encoding="utf-8")
    expected = render_readme()
    diff = "".join(
        difflib.unified_diff(
            current.splitlines(keepends=True),
            expected.splitlines(keepends=True),
            fromfile="README.md",
            tofile="README.md (generated)",
        )
    )
    assert current == expected, f"README.md is out of date. Run `./godelw generate`.\n{diff}"
