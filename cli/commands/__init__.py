# 🧠 Neural Entrainment System v2.0 - CLI Commands Package
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
CLI Commands Package - Consciousness-aware command implementations.

This package provides comprehensive CLI command implementations for the Neural 
Entrainment System, featuring consciousness-aware session management, neural 
profile assessment, preset browsing, and real-time monitoring capabilities.

Command Modules:
- session.py: Session management and execution
- profile.py: Neural profile assessment and management
- preset.py: Preset browsing and customization
- monitor.py: Real-time monitoring and analysis
"""

__version__ = "2.0.0"
__author__ = "Dr. KB Jama"

# Command module imports
from .session import SessionCommands
from .profile import ProfileCommands
from .preset import PresetCommands
from .monitor import MonitorCommands

__all__ = [
    "SessionCommands",
    "ProfileCommands", 
    "PresetCommands",
    "MonitorCommands",
]