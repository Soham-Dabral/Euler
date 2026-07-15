# Euler

*An extensible, offline-first desktop assistant built around a modular architecture.*

Euler is a desktop assistant focused on speed, modularity, and local execution. It is designed as a long-term project that emphasizes clean software architecture and extensibility rather than relying on a single large script.

Version **0.6** introduces the first complete graphical user interface and the modular architecture that future releases will build upon.

---

## Features

### Interface

* Modern desktop interface built with CustomTkinter
* Scrollable conversation view
* Separate user and assistant message bubbles
* Keyboard shortcuts
* Responsive and resizable window

### Commands

* Open applications
* Close applications
* Display current date
* Display current time
* Perform web searches
* Intent-based command routing

### Architecture

* Modular project structure
* Event-driven design
* Independent UI, routing, response handling and logging modules
* Easily extendable command system

---

## Planned Roadmap

### Version 0.7

* Voice interaction
* Persistent memory
* Improved routing
* Local configuration system

### Future Versions

* Local language model integration
* Calculator
* Notes
* Weather
* Reminder system
* To-do manager
* Plugin support
* Cross-platform support
* Linux version

---

## Project Structure

```text
Euler/
├── core/
│   ├── router.py
│   └── response_builder.py
│
├── manager/
│   └── manager.py
│
├── memory/
│   └── logger.py
│
├── ui/
│   └── ui.py
│
├── assets/
├── maintest.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Installation

### Running from Source

Clone the repository:

```bash
git clone https://github.com/<username>/Euler.git
```

Enter the project directory:

```bash
cd Euler
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python maintest.py
```

---

### Windows Executable

A standalone Windows executable is available from the **Releases** section.

No Python installation is required.

---

## Technologies

* Python
* CustomTkinter
* psutil

---

## Design Philosophy

Euler is built around a modular architecture where every component has a single responsibility.

Rather than coupling the interface directly to the command logic, the project separates responsibilities into independent modules. This makes the codebase easier to understand, maintain and extend as new capabilities are introduced.

---

## License

Euler is released under the **Euler Non-Commercial License**.

You are free to:

* Use the software for personal, educational and research purposes.
* Study and modify the source code.
* Share the project while preserving the original copyright notice.

Commercial use, resale, redistribution for profit or inclusion in commercial software is prohibited without prior written permission from the copyright holder.

See the **LICENSE** file for complete details.

---

## Author

**Soham Dabral**

---

If you find a bug, have an idea for an improvement or would like to contribute, feel free to open an issue or submit a pull request or mail at quantummechanicstheorist@gmail.com
