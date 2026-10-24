# Attacker

## Purpose

The `attacker/` component contains controlled security-testing functionality for the OT/ICS testbed. Its role is to emulate an authorized attacker interacting with the industrial network and to validate how the PLC and SCADA environment responds to abnormal Modbus/TCP write operations.

## Role in the Testbed

The repository describes the attacker container as a controlled Modbus write-test component. It is intended for isolated laboratory use rather than deployment against production systems.

Typical flow:

1. The attacker container joins the OT test network.
2. The target PLC exposes Modbus/TCP services.
3. The attacker sends a controlled Modbus request.
4. The PLC state changes according to its configured logic.
5. SCADA reflects the resulting process state.
6. Traffic can be captured and inspected with Wireshark.

## Testing Objectives

- Validate that the PLC accepts expected Modbus/TCP requests.
- Understand Modbus function codes and packet fields.
- Observe the difference between normal traffic and controlled write activity.
- Verify that SCADA reflects PLC state changes.
- Provide repeatable traffic for defensive monitoring experiments.

## Safety and Scope

Use this component only inside the isolated Docker-based OT laboratory. Tests should be deterministic, reversible, and documented before execution.

## Related Components

- `openplc/` — simulated PLC and control logic
- `scadabr/` — SCADA/HMI
- `modbus-client/` — normal PLC read/write verification
- `traffic/` — background normal Modbus traffic
- `scripts/` — environment and workflow automation
