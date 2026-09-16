# Maintainer guide

## Source files

- `data/pfcs-public-information.json` is the authoritative public-information data.
- `README.template.md` owns the README Markdown, formatting, and Jinja expressions.
- `README.md` is generated. Do not edit it directly.
- `scripts/update_readme.py` renders the template with the JSON data.
- `scripts/validate_json.py` validates the JSON against `FedRAMP/schemas@main`.

Validation requires network access. The Makefile automatically creates `.venv` and installs the pinned dependencies.

## Updating public information

Edit the JSON, the template, or both, then regenerate the README:

```bash
make readme
```

Run all validation and tests:

```bash
make verify
```

Review the generated output before committing:

```bash
git diff
git status --short
```

Commit the JSON, template, generated README, and related tooling together. Commits must remain GPG-signed:

```bash
git add data/pfcs-public-information.json README.template.md README.md
git commit -S -m "Update PFCS public information"
```

## Make targets

```text
make setup         Create the virtual environment and install dependencies
make readme        Generate README.md
make check-readme  Verify README.md without modifying it
make test          Run the test suite
make verify        Validate JSON, check README.md, and run tests
```

The GitHub branch-protection check should require the `ci/circleci: verify` job.
