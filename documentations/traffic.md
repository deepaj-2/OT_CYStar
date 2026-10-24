# Traffic

## Purpose

The `traffic/` component generates or manages normal OT network traffic for the laboratory environment. Its primary purpose is to establish realistic background Modbus/TCP communication against the simulated PLC.

## Role in the Testbed

Normal traffic provides the baseline against which controlled abnormal activity can be compared.

```text
          Normal OT Traffic
                 │
                 ▼
          ┌─────────────┐
          │   OpenPLC   │
          └─────────────┘
                 │
                 ▼
             ScadaBR
```

The attacker component can operate alongside this baseline so that packet captures contain both normal and test traffic.

## Objectives

- Generate repeatable Modbus/TCP communication.
- Keep the PLC exercised during experiments.
- Provide a realistic background for packet analysis.
- Make it possible to compare normal and abnormal Modbus operations.

## Traffic Analysis

Wireshark can be used to inspect:

- TCP sessions
- Modbus/TCP requests and responses
- Function codes
- Register addresses
- Values
- Request timing
- Differences between normal and controlled write traffic

## Recommended Test Procedure

1. Start the OT environment.
2. Allow normal traffic to run.
3. Capture traffic with Wireshark.
4. Establish a baseline.
5. Run a controlled security test.
6. Compare the resulting packets with baseline traffic.
7. Record observations.

## Safety

Traffic generation should target only the simulated PLC inside the laboratory network.
