# 🧠 Neural Entrainment System v2.0 - Interface Abstraction Layer
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Interface Abstraction Layer - Common patterns for consciousness-aware interfaces.

This module provides base interface abstractions that can be implemented by different
interface types (CLI, Desktop App, Web App, etc.) while maintaining consistency
in consciousness sovereignty principles and biofield intelligence integration.
"""

__version__ = "2.0.0"
__author__ = "Dr. KB Jama"

from .base_interface import (
    ConsciousnessInterface,
    InterfaceCapability,
    InterfaceMode,
    NeuralAdaptiveInterface,
    BiofieldIntelligenceInterface,
    SafetyProtocolInterface,
    SessionControlInterface
)

from .cli_interface import (
    ConsciousnessCLIInterface,
    CLIDisplayCapabilities,
    TerminalConsciousnessAdapter
)

# Desktop interface will be implemented in Phase 3B
# from .desktop_interface import ConsciousnessDesktopInterface

__all__ = [
    # Base interface abstractions
    "ConsciousnessInterface",
    "InterfaceCapability", 
    "InterfaceMode",
    "NeuralAdaptiveInterface",
    "BiofieldIntelligenceInterface",
    "SafetyProtocolInterface",
    "SessionControlInterface",
    
    # CLI interface
    "ConsciousnessCLIInterface",
    "CLIDisplayCapabilities",
    "TerminalConsciousnessAdapter",
]