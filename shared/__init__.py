# Package initialization
# 🧠 Neural Entrainment System v2.0 - Shared Package
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Shared Package - Common utilities and constants across the Neural Entrainment System.

This package provides shared utilities, constants, and functions used throughout
the Neural Entrainment System v2.0, ensuring consistency across CLI, desktop,
and core modules while maintaining consciousness-aware design principles.

Modules:
- consciousness_constants.py: Consciousness state and brainwave definitions
- biofield_constants.py: Biofield intelligence frequency and harmonic constants
- safety_constants.py: Safety protocol thresholds and guidelines
- neural_profile_utils.py: Neural profile processing utilities
- validation_utils.py: Shared validation functions and schemas
"""

__version__ = "2.0.0"
__author__ = "Dr. KB Jama"

# Import key shared utilities for easy access
from .consciousness_constants import (
    CONSCIOUSNESS_STATES,
    BRAINWAVE_FREQUENCIES,
    CONSCIOUSNESS_STATE_TRANSITIONS,
    get_consciousness_state_info,
    validate_consciousness_state
)

from .biofield_constants import (
    SCHUMANN_RESONANCE_FREQUENCIES,
    SOLFEGGIO_FREQUENCIES,
    GOLDEN_RATIO_HARMONICS,
    BIOFIELD_COHERENCE_LEVELS,
    calculate_biofield_coherence
)

from .safety_constants import (
    SAFETY_THRESHOLDS,
    NEURAL_LOAD_LIMITS,
    COMFORT_LEVEL_GUIDELINES,
    SAFETY_PROTOCOLS,
    check_safety_compliance
)

from .neural_profile_utils import (
    NeuralProfile,
    create_default_profile,
    validate_neural_profile,
    calculate_profile_compatibility
)

from .validation_utils import (
    ValidationResult,
    validate_session_config,
    validate_preset_config,
    sanitize_user_input
)

__all__ = [
    # Consciousness constants
    "CONSCIOUSNESS_STATES",
    "BRAINWAVE_FREQUENCIES", 
    "CONSCIOUSNESS_STATE_TRANSITIONS",
    "get_consciousness_state_info",
    "validate_consciousness_state",
    
    # Biofield constants
    "SCHUMANN_RESONANCE_FREQUENCIES",
    "SOLFEGGIO_FREQUENCIES",
    "GOLDEN_RATIO_HARMONICS", 
    "BIOFIELD_COHERENCE_LEVELS",
    "calculate_biofield_coherence",
    
    # Safety constants
    "SAFETY_THRESHOLDS",
    "NEURAL_LOAD_LIMITS",
    "COMFORT_LEVEL_GUIDELINES",
    "SAFETY_PROTOCOLS",
    "check_safety_compliance",
    
    # Neural profile utilities
    "NeuralProfile",
    "create_default_profile",
    "validate_neural_profile",
    "calculate_profile_compatibility",
    
    # Validation utilities
    "ValidationResult",
    "validate_session_config",
    "validate_preset_config", 
    "sanitize_user_input",
]