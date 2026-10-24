# OpenPLC

## Purpose

The `openplc/` component provides the simulated programmable logic controller (PLC) used as the control-system endpoint of the OT testbed.

## Role in the Architecture

OpenPLC represents the field-control layer of the laboratory environment. It exposes PLC data that can be accessed through Modbus/TCP and consumed by SCADA.

Conceptually:

```text
Modbus Client ─┐
Traffic Gen. ──┼──> OpenPLC ──> SCADA/HMI
Attacker ──────┘
```

## Responsibilities

- Execute the simulated PLC control logic.
- Maintain process-related variables.
- Provide Modbus/TCP communication.
- Serve as the authoritative simulated process-control endpoint.
- Provide a target for controlled OT security experiments.

## PLC Logic

The PLC logic should represent a deterministic industrial process suitable for experimentation. Changes to registers, coils, or process variables should be observable from the SCADA layer where applicable.

## Testing

OpenPLC should be tested in stages:

1. Confirm the container starts successfully.
2. Confirm the PLC runtime is operational.
3. Confirm Modbus/TCP connectivity.
4. Read known PLC values with `modbus-client/`.
5. Confirm normal background traffic from `traffic/`.
6. Validate controlled writes from the laboratory attacker.
7. Confirm corresponding SCADA changes.

## Security-Lab Role

The PLC is intentionally exposed to simulated OT traffic so that communication, monitoring, and controlled security-testing workflows can be studied without using a production controller.

## Related Components

- `modbus-client/`
- `traffic/`
- `attacker/`
- `scadabr/`
