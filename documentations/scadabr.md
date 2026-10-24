# ScadaBR

## Purpose

The `scadabr/` component provides the SCADA/HMI layer of the OT/ICS testbed. It presents process information from the simulated PLC and allows the laboratory environment to be observed from an operator-oriented interface.

## Role in the Architecture

ScadaBR sits above the PLC/control layer:

```text
        SCADA / HMI
             │
          ScadaBR
             │
        Modbus/TCP
             │
          OpenPLC
```

## Responsibilities

- Display simulated process values.
- Provide an operator-facing view of the OT process.
- Consume PLC data over the industrial communication path.
- Make PLC state changes visible during experiments.
- Support observation of normal and abnormal laboratory activity.

## Normal Operation

During normal operation, the SCADA interface should reflect the values produced by the PLC and updated by the normal traffic/process simulation.

## Security Experiments

Controlled write tests can be used to demonstrate how a change at the PLC level propagates into the SCADA view. This is useful for understanding the relationship between:

- Field/control data
- PLC state
- Industrial protocol traffic
- Operator visualization

## Troubleshooting

If SCADA does not show expected values, check in order:

1. ScadaBR container status.
2. Network connectivity to the PLC.
3. PLC runtime status.
4. Modbus/TCP endpoint configuration.
5. Register/address mapping.
6. Whether the PLC values are actually changing.

## Related Components

- `openplc/` — data/control source
- `traffic/` — normal Modbus traffic
- `attacker/` — controlled abnormal activity
- `modbus-client/` — independent verification
