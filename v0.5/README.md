# Euler v0.5

Euler is a lightweight command-based desktop assistant built in Python. The project is being developed incrementally with a focus on clean architecture, modular design, and gradual operating system integration.

## Current Features

### Time and Date

* Retrieve the current system time.
* Retrieve the current system date.

### Timers

* Create system timers.
* Timer completion notifications.

### Logging System

* Records user inputs.
* Records Euler responses.
* Records errors for debugging and development.

### Response Builder

* Converts structured facts into natural language responses.
* Supports multiple facts in a single response.

### Application Launcher (v0.5)

Euler can launch selected desktop applications, websites and some system settings using natural language commands.

Examples:

* Open Calculator
* Open Firefox
* Open Edge
* Open Spotify
* Open LinkedIn
* Open GitHub
* Open Wifi
* Open Bluetooth

The application launcher uses an alias system, allowing multiple names for the same application.

Example:

* calculator
* calc

Both resolve to the Calculator application.

### Web Search Feature

Euler can now do a bing search on you browser and it can be done using 'search' keyword

## Architecture

Euler follows a modular design:

### Router

Determines user intent and routes commands to the correct module.

### Parser

Extracts command arguments from user input.

### Command Modules

Perform actual actions such as:

* Getting time
* Getting date
* Starting timers
* Launching applications

### Response Builder

Formats structured facts into human-readable responses.

### Logger

Stores command history and error information.

## Example Flow

User Input:

open calc

Router:

Detects "open" intent.

Parser:

Extracts "calc".

Application Launcher:

Resolves alias and launches Calculator.

Response Builder:

Sir, Calculator has been opened.

## Status

Euler is currently in active development.

Current Version: v0.5
Language: Python
Platform: Windows
License: Personal Project
