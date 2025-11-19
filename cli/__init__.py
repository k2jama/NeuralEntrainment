# 🧠 Neural Entrainment System v2.0 - CLI Interface Package
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
CLI Interface Package - Consciousness-Aware Command Line Interface.

This package provides a comprehensive CLI for the Neural Entrainment System v2.0,
featuring consciousness-aware interactions, biofield intelligence visualization,
neural profile adaptation, and comprehensive safety protocols.

Package Structure:
- main.py: CLI entry point and command routing
- commands/: Command modules for different functionality areas
- ui/: User interface components for consciousness visualization
- themes/: Consciousness-aware visual themes and aesthetics
- utils/: CLI utility functions and terminal adaptations
"""

__version__ = "2.0.0"
__author__ = "Dr. KB Jama"

# Core CLI components
from .main import ConsciousnessEntryPoint, main

# Command modules
from .commands import (
    session_commands,
    profile_commands, 
    preset_commands,
    monitoring_commands
)

# UI components  
from .ui import (
    consciousness_display,
    biofield_display,
    safety_monitor,
    progress_tracker,
    interactive_forms
)

# Themes and aesthetics
from .themes import (
    consciousness_colors,
    sacred_geometry,
    biofield_aesthetics
)

# Utilities
from .utils import (
    terminal_detection,
    unicode_fallbacks,
    real_time_updater
)

__all__ = [
    # Main entry point
    "ConsciousnessEntryPoint",
    "main",
    
    # Commands
    "session_commands",
    "profile_commands",
    "preset_commands", 
    "monitoring_commands",
    
    # UI components
    "consciousness_display",
    "biofield_display",
    "safety_monitor",
    "progress_tracker",
    "interactive_forms",
    
    # Themes
    "consciousness_colors",
    "sacred_geometry", 
    "biofield_aesthetics",
    
    # Utils
    "terminal_detection",
    "unicode_fallbacks",
    "real_time_updater",
]