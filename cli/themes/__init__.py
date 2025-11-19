# 🧠 Neural Entrainment System v2.0 - Themes Package
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Consciousness-Aware Themes Package - Beautiful visual themes for consciousness interaction.

This package provides comprehensive theming for the CLI interface including:
- Consciousness-aware color schemes that adapt to neural states
- Sacred geometry symbols and patterns for consciousness visualization
- Biofield aesthetics with natural frequency representations
- Adaptive theming based on terminal capabilities and user preferences

Theme Components:
- consciousness_colors.py: Advanced color schemes with consciousness state awareness
- sacred_geometry.py: Sacred symbols and geometric patterns for visualization
- biofield_aesthetics.py: Biofield intelligence visual representations and animations

Design Philosophy:
- Beauty serves consciousness: Visual elements inspire and support rather than distract
- Adaptive presentation: Graceful degradation across different terminal capabilities
- Sacred geometry integration: Honor consciousness traditions through visual design
- Natural frequency alignment: Visual patterns that resonate with biofield intelligence
"""

__version__ = "2.0.0"
__author__ = "Dr. KB Jama"

# Core theme imports
from .consciousness_colors import ConsciousnessColorScheme
from .sacred_geometry import SacredGeometrySymbols, ConsciousnessVisualization
from .biofield_aesthetics import BiofieldAesthetics

# Theme management utilities
from typing import Dict, Any, Optional
import os

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# THEME MANAGEMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessThemeManager:
    """
    Consciousness-aware theme management system.
    
    This class provides centralized theme management with awareness of consciousness
    states, terminal capabilities, and user preferences.
    """
    
    def __init__(self):
        self.color_scheme = ConsciousnessColorScheme()
        self.symbols = SacredGeometrySymbols()
        self.biofield = BiofieldAesthetics()
        
        # Theme state
        self.current_theme = "default"
        self.consciousness_state = "neutral"
        self.neural_profile = {}
        
        # Theme customizations
        self.user_preferences = {}
        
    def apply_consciousness_state(self, state: str) -> None:
        """Apply consciousness state to all theme components."""
        self.consciousness_state = state
        self.color_scheme.set_consciousness_context(state)
        
    def apply_neural_profile(self, profile: Dict[str, Any]) -> None:
        """Apply neural profile preferences to theming."""
        self.neural_profile = profile
        
        # Adjust color intensity for sensitive users
        sensitivity = profile.get('sensitivity_level', 'standard')
        if sensitivity == 'sensitive':
            self.color_scheme.set_intensity_level(0.7)
        elif sensitivity == 'resilient':
            self.color_scheme.set_intensity_level(1.3)
    
    def get_theme_components(self) -> Dict[str, Any]:
        """Get all theme components configured for current state."""
        return {
            'colors': self.color_scheme,
            'symbols': self.symbols,
            'biofield': self.biofield
        }

# Default theme manager instance
default_theme_manager = ConsciousnessThemeManager()

# Convenience functions for theme access
def get_colors() -> ConsciousnessColorScheme:
    """Get configured color scheme."""
    return default_theme_manager.color_scheme

def get_symbols() -> SacredGeometrySymbols:
    """Get sacred geometry symbols."""
    return default_theme_manager.symbols

def get_biofield_aesthetics() -> BiofieldAesthetics:
    """Get biofield aesthetics."""
    return default_theme_manager.biofield

def apply_consciousness_state(state: str) -> None:
    """Apply consciousness state to default theme."""
    default_theme_manager.apply_consciousness_state(state)

def apply_neural_profile(profile: Dict[str, Any]) -> None:
    """Apply neural profile to default theme."""
    default_theme_manager.apply_neural_profile(profile)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# THEME PRESETS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONSCIOUSNESS_THEMES = {
    'default': {
        'name': 'Default Consciousness',
        'description': 'Balanced consciousness-aware theme',
        'color_intensity': 1.0,
        'symbol_style': 'unicode',
        'animation_level': 'full'
    },
    'gentle': {
        'name': 'Gentle Consciousness',
        'description': 'Soft, gentle theme for sensitive users',
        'color_intensity': 0.6,
        'symbol_style': 'simple',
        'animation_level': 'minimal'
    },
    'vibrant': {
        'name': 'Vibrant Consciousness',
        'description': 'Rich, vibrant theme for immersive experience',
        'color_intensity': 1.4,
        'symbol_style': 'elaborate',
        'animation_level': 'enhanced'
    },
    'minimal': {
        'name': 'Minimal Consciousness',
        'description': 'Clean, minimal theme for focus',
        'color_intensity': 0.8,
        'symbol_style': 'ascii',
        'animation_level': 'none'
    }
}

def load_theme_preset(theme_name: str) -> bool:
    """Load a predefined theme preset."""
    if theme_name not in CONSCIOUSNESS_THEMES:
        return False
    
    theme_config = CONSCIOUSNESS_THEMES[theme_name]
    
    # Apply theme configuration
    intensity = theme_config.get('color_intensity', 1.0)
    default_theme_manager.color_scheme.set_intensity_level(intensity)
    
    # Set symbol style
    symbol_style = theme_config.get('symbol_style', 'unicode')
    default_theme_manager.symbols.set_style(symbol_style)
    
    # Set animation level
    animation_level = theme_config.get('animation_level', 'full')
    default_theme_manager.biofield.set_animation_level(animation_level)
    
    default_theme_manager.current_theme = theme_name
    return True

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# THEME UTILITIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def detect_terminal_capabilities() -> Dict[str, bool]:
    """Detect terminal capabilities for theme adaptation."""
    
    capabilities = {
        'color_support': True,
        'unicode_support': True,
        'animation_support': True,
        'true_color_support': False
    }
    
    # Check color support
    term = os.environ.get('TERM', '').lower()
    colorterm = os.environ.get('COLORTERM', '').lower()
    
    if 'color' not in term and not colorterm:
        capabilities['color_support'] = False
    
    # Check for true color support
    if 'truecolor' in colorterm or '24bit' in colorterm:
        capabilities['true_color_support'] = True
    
    # Check Unicode support (basic heuristic)
    try:
        print('\u2502', end='')  # Box drawing character
        print('\b \b', end='')  # Backspace to erase
        capabilities['unicode_support'] = True
    except (UnicodeEncodeError, UnicodeDecodeError):
        capabilities['unicode_support'] = False
    
    return capabilities

def auto_configure_theme() -> None:
    """Automatically configure theme based on terminal capabilities."""
    
    capabilities = detect_terminal_capabilities()
    
    if not capabilities['color_support']:
        load_theme_preset('minimal')
    elif not capabilities['unicode_support']:
        load_theme_preset('gentle')
    else:
        load_theme_preset('default')

# Auto-configure on import
auto_configure_theme()

# Export public interface
__all__ = [
    "ConsciousnessColorScheme",
    "SacredGeometrySymbols", 
    "ConsciousnessVisualization",
    "BiofieldAesthetics",
    "ConsciousnessThemeManager",
    "get_colors",
    "get_symbols", 
    "get_biofield_aesthetics",
    "apply_consciousness_state",
    "apply_neural_profile",
    "load_theme_preset",
    "CONSCIOUSNESS_THEMES",
    "auto_configure_theme"
]