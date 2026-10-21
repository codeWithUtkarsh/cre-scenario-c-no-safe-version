# Scenario C: no safe version exists

`ecdsa` has CVE-2024-23342 (Minerva timing attack) in every release, including
the latest, and the maintainers don't plan a fix. Updating can't make it safe.

Expected: a PR with the safe updates (requests, pytest), and a story telling a
developer that ecdsa must be replaced (for example with `cryptography`).
