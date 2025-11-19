# 🧠 Neural Entrainment System v2.0 - CLI UI Package  
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
CLI UI Package - Consciousness-aware user interface components for terminal display.

This package provides beautiful, consciousness-aware UI components for the CLI interface
including consciousness state visualization, biofield intelligence display, safety
monitoring, session progress tracking, and interactive forms.

UI Components:
- consciousness_display.py: Consciousness state visualization and journey mapping
- biofield_display.py: Biofield intelligence visualization and coherence display  
- safety_monitor.py: Safety protocol monitoring and neural load visualization
- progress_tracker.py: Session progress tracking and phase visualization
- interactive_forms.py: Consciousness-aware input forms and interactions
"""

__version__ = "2.0.0"
__author__ = "Dr. KB Jama"

# UI component imports
from .consciousness_display import ConsciousnessDisplay
from .biofield_display import BiofieldDisplay
from .safety_monitor import SafetyMonitor
from .progress_tracker import ProgressTracker
from .interactive_forms import ConsciousnessInteractiveForms

__all__ = [
    "ConsciousnessDisplay",
    "BiofieldDisplay", 
    "SafetyMonitor",
    "ProgressTracker",
    "ConsciousnessInteractiveForms",
]