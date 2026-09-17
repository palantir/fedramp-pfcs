# Maintainer guide

## Source files

- `data/pfcs-public-information.json` is the authoritative public-information data.
- `README.template.md` owns the README Markdown, formatting, and Jinja expressions.
- `README.md` is generated. Do not edit it directly.
- `scripts/update_readme.py` renders the template with the JSON data.
- `scripts/validate_json.py` validates the JSON against `FedRAMP/schemas@main`.

Install Go (1.23 or newer) and Python 3 with virtual environment support. Validation and the first Godel run require network access. `scripts/python.sh` automatically creates `.venv` and installs the pinned Python dependencies when needed. Godel downloads its pinned distribution and plugins from GitHub.

## Updating public information

Edit the JSON, the template, or both, then regenerate the README:

```bash
./godelw generate
```

Run all validation and tests:

```bash
./godelw verify --apply=false
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

## Commands

```bash
./godelw generate                                  # Regenerate README.md
./godelw verify --apply=false                       # Verify generated output and run tests
./godelw test                                      # Run the Python suite through Godel
sh scripts/python.sh scripts/update_readme.py --check  # Read-only README check
sh scripts/python.sh scripts/validate_json.py       # Validate JSON
```

The GitHub branch-protection check should require the `ci/circleci: verify` job.

## Automatic README regeneration with Nit

Godel's generate plugin runs the Python renderer through the directive in `generate.go`.
The JSON, Jinja template, and Python renderer remain the source of the README.
`tests/godel_pytest_adapter_test.go` connects Godel's test task to pytest, including JSON
schema validation. It forwards pytest's stdout/stderr and propagates failures.
Verbose Go test output keeps pytest's results visible on successful runs too.
`go.mod` supports these two entry points; there are no Go dependencies.
Go test caching is disabled because it cannot track Python's JSON/template inputs.
Generation renders the expected content in memory and leaves README.md untouched
when it already matches.

CircleCI runs `./godelw verify --apply=false` for generation verification and all tests.
If generation changes `README.md`, Godel fails and includes `generate --verify` in
its failed-task summary. Nit recognizes this existing Godel task and, on a PR
with the `🤖 fix nits` label, runs `./godelw generate` and pushes the repaired README.
This requires the OSS Nit app to have repository access and its deployed version
to include the `godelw-generate` task. CircleCI itself needs no push credentials.
Nit uses its own signing identity; enabling automatic commits requires allowing
that identity alongside maintainer YubiKey signatures.

Godel verifies generation by running it and comparing outputs. Even with
`--apply=false`, a stale README is rewritten locally and verification fails.
Use `sh scripts/python.sh scripts/update_readme.py --check` for a check that does not modify files.

The Python suite validates the JSON against its schema and checks that README.md
matches the JSON and template.
