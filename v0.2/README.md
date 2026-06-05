# Euler v0.2

Euler is a Python-based AI assistant project developed as a long-term systems engineering and software architecture project.

## Current Features

* Provides the current date.
* Provides the current time.
* Creates timers from natural language input.
* Supports text-to-speech responses.
* Supports multiple commands within a single prompt.
* Uses a modular routing and command execution system.

### Example Commands

* `What is the time?`
* `Tell me today's date.`
* `Set a timer for 5 minutes.`
* `Tell me the date and set a timer for 10 seconds.`

## Architecture

Euler v0.2 is built around a modular structure consisting of:

* Command Routing
* Intent Detection
* Command Metadata
* Parser System
* Command Execution Engine
* Text-to-Speech Subsystem

The project separates command detection, argument extraction, and execution to make future expansion easier.

## Current Limitations

* Command execution order is not fully deterministic in all situations.
* Timer and parser systems are still under development.
* Error handling can be improved.
* Limited command library.
* No voice input support yet.

## Development Goals

Future versions aim to introduce:

* Improved command ordering
* Better parser architecture
* Background task handling
* Additional system commands
* Voice input support
* Expanded assistant capabilities

## Version

Current Release: **Euler v0.2**

## Author

Soham

---

*"Every system begins as a prototype."*
