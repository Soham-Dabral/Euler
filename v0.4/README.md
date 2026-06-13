# Euler v0.3

Euler is a lightweight modular command-driven assistant designed with a clear separation between intent detection, execution, response generation, and logging.

---

## Overview

Euler processes natural language commands using a keyword-based routing system and converts them into structured "facts", which are then transformed into human-readable responses.

The system is intentionally minimal in v0.3, focusing on architectural clarity rather than advanced NLP.

---

## Features (v0.3)

* Keyword-based intent detection
* Modular router system
* Fact-based command execution
* Response builder for natural language output
* Timer support (basic parser included)
* Date and time utilities
* Structured logging system
* Basic voice output integration

---

## Architecture

Euler follows a pipeline-based architecture:

```
User Input
   ↓
Router (handle_prompt)
   ↓
Facts + Errors
   ↓
Response Builder (handle_response)
   ↓
Final Response
   ↓
Logger
   ↓
Speech Output
```

---

## Project Structure

```
core/
    router.py          # Intent detection and fact generation
    response_builder.py# Converts facts into natural language
commands/
    command.py         # Core command functions (time, date, timer)
core/parser.py         # Argument parsing (e.g., timer parsing)
memory/logger.py       # Logging system
core/speech.py         # Text-to-speech engine
main.py               # Entry point
log.txt               # Execution logs
```

---

## Example Usage

### Input

```
time
```

### Output

```
Sir, the current time is 04:30 PM
```

---

### Input

```
date and time
```

### Output

```
Sir, the current time is 04:30 PM and today is Friday 12 June 2026
```

---

### Input

```
timer for 5 seconds
```

### Output

```
Sir, your timer has completed
```

---

## Logging

All interactions are logged in `log.txt` with:

* Timestamp
* User input
* Output
* Error status

---

## Design Philosophy

Euler v0.3 prioritizes:

* Clear separation of concerns
* Deterministic behavior
* Easy debugging
* Minimal complexity over intelligence

No NLP or memory systems are included in this version by design.

---

## Limitations

* No context awareness between commands
* No natural language understanding beyond keywords
* No memory system
* Basic speech integration may require stabilization

---

## Future Plans (v0.4+)

* Memory system
* Improved response naturalization
* Better speech pipeline stability
* Expanded command set
* Optional NLP layer

---

## Status

Euler v0.3 is a stable architectural milestone focusing on modular command execution and structured response generation.
