# Modbus Client

## Purpose

The `modbus-client/` component provides client-side interaction with the simulated PLC over Modbus/TCP. It is used to verify connectivity and inspect or modify PLC data points during laboratory experiments.

## Role in the Testbed

The client provides a controlled way to exercise the PLC independently from the SCADA system.

A typical workflow is:

1. Start the OT services with Docker Compose.
2. Ensure the OpenPLC service is running.
3. Connect the Modbus client to the PLC.
4. Read configured registers/coils.
5. Optionally perform an authorized test write.
6. Confirm the resulting PLC and SCADA state.

## Main Uses

- PLC connectivity verification
- Modbus/TCP read testing
- Controlled write testing
- Register/coil validation
- Troubleshooting Modbus communication

## Protocol Focus

The project uses Modbus/TCP as the industrial communication protocol. When troubleshooting, inspect:

- TCP connectivity
- Modbus transaction identifiers
- Unit/slave identifier
- Function code
- Register or coil address
- Quantity
- Payload/value
- Modbus exception responses

## Relationship to Other Components

`modbus-client/` is primarily a verification and experimentation component. It complements the automated traffic in `traffic/` and the controlled security tests in `attacker/`.

## Safety

Only use write operations against the simulated PLC in the isolated testbed.
