# Workshop

## Purpose

The `workshop/` directory contains material intended to support demonstrations, guided exercises, experiments, or training activities using the OT security testbed.

## Learning Goals

A workshop based on this repository can introduce participants to:

1. OT/ICS architecture
2. PLC and SCADA interaction
3. Modbus/TCP communication
4. Normal industrial traffic
5. Packet capture and protocol analysis
6. Controlled security testing
7. The relationship between network activity and physical/process state

## Suggested Exercise Flow

### 1. Start the Environment

Launch the Docker-based OT services and verify that the containers are healthy.

### 2. Inspect the PLC

Use OpenPLC to understand the simulated control logic and available process variables.

### 3. Observe SCADA

Open ScadaBR and confirm that the operator interface reflects PLC state.

### 4. Generate Normal Traffic

Run the normal traffic generator and capture the resulting Modbus/TCP packets.

### 5. Analyze Packets

Use Wireshark to identify Modbus transactions, function codes, addresses, and values.

### 6. Perform a Controlled Test

Use the dedicated laboratory testing components to perform a reversible Modbus write operation.

### 7. Observe the Effect

Check the PLC state, SCADA display, and network capture.

### 8. Document Findings

Record the request, response, affected data point, observed process change, and relevant packet fields.

## Workshop Safety

All exercises should remain inside the isolated test environment. Security-testing activities should be authorized, controlled, reversible, and limited to the simulated OT assets.

## Related Components

- `openplc/`
- `scadabr/`
- `traffic/`
- `modbus-client/`
- `attacker/`
