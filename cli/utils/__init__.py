#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - CLI Utilities Package
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
CLI Utilities Package - Consciousness-aware terminal utilities.

This package provides comprehensive utilities for terminal interaction, 
display optimization, and consciousness-aware visualization across 
different terminal environments and capabilities.
"""

import sys
import os
from typing import Dict, Any, List, Optional, Tuple, Union

# Import the main utilities
from .terminal_detection import (
    TerminalDetector,
    TerminalCapabilities,
    TerminalType,
    ColorSupport,
    detect_terminal_capabilities,
    get_optimal_consciousness_settings
)

from .unicode_fallbacks import (
    UnicodeFallbackManager,
    ConsciousnessSymbolMapper,
    FallbackLevel,
    FallbackSettings,
    create_fallback_manager,
    create_consciousness_symbol_mapper
)

from .real_time_updater import (
    RealTimeUpdater,
    SmoothAnimationManager,
    UpdateType,
    AnimationStyle,
    UpdateFrame,
    AnimationState,
    create_real_time_updater,
    create_smooth_animation_manager
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PACKAGE LEVEL EXPORTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

__all__ = [
    # Terminal Detection
    'TerminalDetector',
    'TerminalCapabilities', 
    'TerminalType',
    'ColorSupport',
    'detect_terminal_capabilities',
    'get_optimal_consciousness_settings',
    
    # Unicode Fallbacks
    'UnicodeFallbackManager',
    'ConsciousnessSymbolMapper',
    'FallbackLevel',
    'FallbackSettings',
    'create_fallback_manager',
    'create_consciousness_symbol_mapper',
    
    # Real-time Updates
    'RealTimeUpdater',
    'SmoothAnimationManager',
    'UpdateType',
    'AnimationStyle',
    'UpdateFrame',
    'AnimationState',
    'create_real_time_updater',
    'create_smooth_animation_manager'
]