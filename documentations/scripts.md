# Scripts

## Purpose

The `scripts/` directory contains helper automation used to operate, configure, test, or inspect the OT security testbed.

## Expected Role

Scripts should reduce repetitive manual steps and make experiments reproducible. Typical responsibilities include:

- Starting or stopping laboratory components
- Initializing test conditions
- Generating repeatable test traffic
- Running connectivity checks
- Collecting diagnostic information
- Supporting workshop or demonstration workflows

## Recommended Script Structure

Scripts should clearly document:

- Purpose
- Required dependencies
- Inputs/arguments
- Expected environment
- Output
- Exit codes
- Safety considerations

Example documentation pattern:

```text
Script
  ├── Preconditions
  ├── Inputs
  ├── Actions
  ├── Expected output
  └── Cleanup
```

## Reproducibility

Scripts should avoid assumptions about a developer's local machine. Prefer Docker service names, environment variables, and repository-relative paths where possible.

## Safety

Automation that generates Modbus writes or simulated attacks should clearly identify itself as a laboratory operation and should be executed only against the isolated OT testbed.

## Related Components

Scripts may coordinate:

- `openplc/`
- `scadabr/`
- `modbus-client/`
- `traffic/`
- `attacker/`
- `workshop/`
