<p align="center"><svg xmlns="http://www.w3.org/2000/svg" width="120" height="120" viewBox="0 0 120 120"><rect width="120" height="120" fill="#000000"/><path d="M60 14 L84 52 L64 52 L64 106 L56 106 L56 52 L36 52 Z" fill="none" stroke="#ff2a2a" stroke-width="4"/></svg></p>

# THE BLACKLOCK INSTRUMENTS

## LANCEPOINT

**ShatterPoint Security research suite. Author: Gavin Blacklock (Epsilon0xCell).**

> Invariant: An AI application endpoint that answers without authentication is an exposure, and it can be checked in one request.

LANCEPOINT ships original Nuclei-style YAML templates for AI application exposures, plus a Python matcher harness that validates each template against a local vulnerable fixture and a patched fixture. The nuclei binary is not required to validate the logic here; the templates are written in standard nuclei YAML shape for use with nuclei itself.

## Run it in one command

```bash
python3 run_demo.py
```

## Results and limits

The demo validates all templates: each fires on the vulnerable fixture and does not fire on the patched fixture. Limits: fixture responses model the exposure conditions; live use belongs on authorised targets only.

## Detection

Every template doubles as a detection specification: the same path and matcher describe what access logs should alert on from untrusted sources.


## Disclosure

Coordinated disclosure first. Findings from these fixtures are reported to the
affected maintainer with a reproducer, affected versions, a proposed fix, and
a regression test before publication. See SECURITY.md.

## Licence

MIT. Copyright (c) 2026 Gavin Blacklock.
