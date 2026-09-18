# FedRAMP PFCS

See [PFCS public information](package-information/pfcs-package.md) for the generated service information.

This README is maintained by hand.

## Generation

Every `data/*.json` file is rendered with `TEMPLATE.md` into
`package-information/<same-name>.md`. No configuration file is needed.

For example, `data/pfcs-package.json` produces
`package-information/pfcs-package.md`.

Run commands from the repository root. Add another JSON file to generate
another page. If you remove or rename a JSON file, remove its old Markdown
page too; generation does not delete files.

## Source files

- `data/pfcs-package.json` is the authoritative public-information data.
- `TEMPLATE.md` owns the public-information page Markdown and Go template expressions.
- `package-information/pfcs-package.md` is generated. Do not edit it directly.
- `generate.go` renders the template with the JSON data.
- `validate.go` validates the JSON against `FedRAMP/schemas@main`.
- `generate_test.go` and `validate_test.go` test public-information page synchronization and schema validation.

Install Go (1.23 or newer). Validation and the first Godel run require network access. Go downloads the dependencies pinned in `go.mod` and verified by `go.sum`. Godel downloads its pinned distribution and plugins from GitHub.

## Updating public information

Edit the JSON, the template, or both, then regenerate the public-information page:

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

Commit the JSON, template, generated public-information page, and related tooling together. Commits must remain GPG-signed:

```bash
git add data/ TEMPLATE.md package-information/
git commit -S -m "Update PFCS public information"
```

## Commands

```bash
./godelw generate                                  # Regenerate all package-information pages
./godelw verify --apply=false                       # Verify generated output and run tests
./godelw test                                      # Run the Go tests
go run . --check                                   # Read-only public-information page check
go run . --validate                                # Validate JSON
```

The GitHub branch-protection check should require the `ci/circleci: verify` job.

## Automatic public-information page regeneration with Nit

Godel's generate plugin runs `go run .` through the directive in `generate.go`.
The JSON and Go template remain the source of the public-information page.
Tests run natively through Godel. Test caching is disabled so each run checks
the current remote schemas.
Generation renders the expected content in memory and leaves package-information/pfcs-package.md untouched
when it already matches.

CircleCI runs `./godelw verify --apply=false` for generation verification and all tests.
If generation changes `package-information/pfcs-package.md`, Godel fails and includes `generate --verify` in
its failed-task summary. Nit recognizes this existing Godel task and, on a PR
with the `🤖 fix nits` label, runs `./godelw generate` and pushes the repaired public-information page.
This requires the OSS Nit app to have repository access and its deployed version
to include the `godelw-generate` task. CircleCI itself needs no push credentials.
Nit discovers `godelw` on the default branch, so merge this setup before testing
automatic regeneration in a later PR.
Nit uses its own signing identity; enabling automatic commits requires allowing
that identity alongside maintainer YubiKey signatures.

Godel verifies generation by running it and comparing outputs. Even with
`--apply=false`, a stale public-information page is rewritten locally and verification fails.
Use `go run . --check` for a check that does not modify files.

The Go suite validates the JSON against its schema and checks that package-information/pfcs-package.md
matches the JSON and template.
