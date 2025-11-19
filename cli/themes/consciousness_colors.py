# 🧠 Neural Entrainment System v2.0 - Consciousness Color Schemes
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Consciousness Color Schemes - Beautiful terminal colors aligned with consciousness states.

This module provides consciousness-aware color schemes that resonate with different
neural states and biofield frequencies, creating a harmonious and supportive
visual environment for consciousness work.
"""

import os
from typing import Dict, Callable, Optional
from enum import Enum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# COLOR CONSTANTS & CONSCIOUSNESS MAPPINGS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessColors:
    """ANSI color codes mapped to consciousness states and biofield frequencies."""
    
    # Reset
    RESET = '\033[0m'
    
    # Basic colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Style attributes
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    
    # 256 color support (consciousness-aware colors)
    DEEP_DELTA = '\033[38;5;17m'        # Deep indigo for profound healing
    DELTA = '\033[38;5;21m'             # Deep blue for restoration
    THETA = '\033[38;5;29m'             # Emerald green for transformation
    ALPHA = '\033[38;5;208m'            # Amber for bridge consciousness
    BETA = '\033[38;5;196m'             # Coral red for active awareness
    GAMMA = '\033[38;5;93m'             # Violet for transcendent states
    
    # Biofield intelligence colors
    SCHUMANN = '\033[38;5;34m'          # Earth connection green
    SOLFEGGIO = '\033[38;5;214m'        # Healing frequency gold
    GOLDEN_RATIO = '\033[38;5;129m'     # Sacred geometry purple
    
    # Safety protocol colors
    SAFE = '\033[38;5;28m'              # Deep forest green
    CAUTION = '\033[38;5;220m'          # Attention amber
    DANGER = '\033[38;5;196m'           # Alert red
    CRITICAL = '\033[38;5;9m'           # Critical red (bright)
    
    # Interface element colors
    HEADER = '\033[38;5;39m'            # Sky blue for headers
    ACCENT = '\033[38;5;201m'           # Magenta for accents
    GENTLE = '\033[38;5;250m'           # Soft gray for gentle text
    EMPHASIS = '\033[38;5;226m'         # Bright yellow for emphasis

class ColorMode(Enum):
    """Color support modes for different terminal capabilities."""
    
    NONE = "none"           # No color support
    BASIC = "basic"         # 16 colors
    EXTENDED = "extended"   # 256 colors  
    TRUECOLOR = "truecolor" # 24-bit colors

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS COLOR SCHEME CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessColorScheme:
    """
    Consciousness-aware color scheme with adaptive terminal support.
    
    This class provides beautiful, consciousness-aligned colors that adapt
    to terminal capabilities and neural sensitivity preferences.
    """
    
    def __init__(self, color_mode: Optional[ColorMode] = None):
        self.color_mode = color_mode or self._detect_color_mode()
        self.colors = ConsciousnessColors()
        self.neural_sensitivity = 1.0  # Will be set based on profile
        
        # Build color functions
        self._build_color_functions()
    
    def _detect_color_mode(self) -> ColorMode:
        """Detect terminal color capabilities."""
        
        # Check for NO_COLOR environment variable
        if os.environ.get('NO_COLOR'):
            return ColorMode.NONE
        
        # Check for forced color
        if os.environ.get('FORCE_COLOR'):
            return ColorMode.EXTENDED
        
        # Check TERM environment variable
        term = os.environ.get('TERM', '').lower()
        
        if 'truecolor' in term or '24bit' in term:
            return ColorMode.TRUECOLOR
        elif '256color' in term or 'xterm' in term:
            return ColorMode.EXTENDED
        elif any(color_term in term for color_term in ['color', 'ansi']):
            return ColorMode.BASIC
        else:
            return ColorMode.NONE
    
    def _build_color_functions(self) -> None:
        """Build color functions based on terminal capabilities."""
        
        if self.color_mode == ColorMode.NONE:
            # No color support - return text as-is
            self._create_no_color_functions()
        else:
            # Color support available
            self._create_color_functions()
    
    def _create_no_color_functions(self) -> None:
        """Create functions that return text without color codes."""
        
        def no_color(text: str) -> str:
            return str(text)
        
        # Assign all color functions to return plain text
        self.consciousness_header = no_color
        self.consciousness_title = no_color
        self.consciousness_subtitle = no_color
        self.consciousness_accent = no_color
        self.biofield_accent = no_color
        self.safety_accent = no_color
        self.neural_profile = no_color
        self.status_active = no_color
        self.status_safe = no_color
        self.status_caution = no_color
        self.status_danger = no_color
        self.command_highlight = no_color
        self.gentle_text = no_color
        self.error_symbol = lambda: "❌"
        self.error_text = no_color
        
        # Consciousness state colors
        self.deep_delta = no_color
        self.delta = no_color
        self.theta = no_color
        self.alpha = no_color
        self.beta = no_color
        self.gamma = no_color
        
        # Biofield colors
        self.schumann = no_color
        self.solfeggio = no_color
        self.golden_ratio = no_color
    
    def _create_color_functions(self) -> None:
        """Create colored text functions based on consciousness principles."""
        
        # Header and title functions
        self.consciousness_header = lambda text: f"{self.colors.CYAN}{self.colors.BOLD}{text}{self.colors.RESET}"
        self.consciousness_title = lambda text: f"{self.colors.BRIGHT_BLUE}{self.colors.BOLD}{text}{self.colors.RESET}"
        self.consciousness_subtitle = lambda text: f"{self.colors.BRIGHT_CYAN}{text}{self.colors.RESET}"
        
        # Accent functions
        self.consciousness_accent = lambda text: f"{self.colors.BRIGHT_MAGENTA}{text}{self.colors.RESET}"
        self.biofield_accent = lambda text: f"{self.colors.SCHUMANN}{text}{self.colors.RESET}"
        self.safety_accent = lambda text: f"{self.colors.SAFE}{text}{self.colors.RESET}"
        
        # Profile and status functions
        self.neural_profile = lambda text: f"{self.colors.GOLDEN_RATIO}{text}{self.colors.RESET}"
        self.status_active = lambda text: f"{self.colors.BRIGHT_GREEN}{text}{self.colors.RESET}"
        self.status_safe = lambda text: f"{self.colors.SAFE}{text}{self.colors.RESET}"
        self.status_caution = lambda text: f"{self.colors.CAUTION}{text}{self.colors.RESET}"
        self.status_danger = lambda text: f"{self.colors.DANGER}{text}{self.colors.RESET}"
        
        # Interface element functions
        self.command_highlight = lambda text: f"{self.colors.BRIGHT_YELLOW}{self.colors.BOLD}{text}{self.colors.RESET}"
        self.gentle_text = lambda text: f"{self.colors.GENTLE}{text}{self.colors.RESET}"
        self.error_symbol = lambda: "🚨"
        self.error_text = lambda text: f"{self.colors.BRIGHT_RED}{text}{self.colors.RESET}"
        
        # Consciousness state color functions
        self.deep_delta = lambda text: f"{self.colors.DEEP_DELTA}{text}{self.colors.RESET}"
        self.delta = lambda text: f"{self.colors.DELTA}{text}{self.colors.RESET}"
        self.theta = lambda text: f"{self.colors.THETA}{text}{self.colors.RESET}"
        self.alpha = lambda text: f"{self.colors.ALPHA}{text}{self.colors.RESET}"
        self.beta = lambda text: f"{self.colors.BETA}{text}{self.colors.RESET}"
        self.gamma = lambda text: f"{self.colors.GAMMA}{text}{self.colors.RESET}"
        
        # Biofield intelligence color functions
        self.schumann = lambda text: f"{self.colors.SCHUMANN}{text}{self.colors.RESET}"
        self.solfeggio = lambda text: f"{self.colors.SOLFEGGIO}{text}{self.colors.RESET}"
        self.golden_ratio = lambda text: f"{self.colors.GOLDEN_RATIO}{text}{self.colors.RESET}"
    
    def adapt_to_neural_sensitivity(self, sensitivity_level: str) -> None:
        """Adapt colors based on neural sensitivity level."""
        
        sensitivity_mapping = {
            'sensitive': 1.8,    # Softer, less intense colors
            'standard': 1.0,     # Normal color intensity
            'resilient': 0.7     # More vibrant colors allowed
        }
        
        self.neural_sensitivity = sensitivity_mapping.get(sensitivity_level, 1.0)
        
        # For sensitive users, we might want to use dimmer alternatives
        if sensitivity_level == 'sensitive':
            self._create_gentle_color_functions()
    
    def _create_gentle_color_functions(self) -> None:
        """Create gentler color functions for sensitive users."""
        
        # Override with dimmer alternatives for sensitive neural architecture
        self.consciousness_header = lambda text: f"{self.colors.DIM}{self.colors.CYAN}{text}{self.colors.RESET}"
        self.consciousness_title = lambda text: f"{self.colors.DIM}{self.colors.BRIGHT_BLUE}{text}{self.colors.RESET}"
        self.error_symbol = lambda: "⚠️"  # Gentler error symbol
        
        # Reduce color intensity for other functions
        # This could be expanded to create fully dimmed versions
    
    def get_consciousness_state_color(self, state: str) -> Callable[[str], str]:
        """Get color function for specific consciousness state."""
        
        state_colors = {
            'deep_delta': self.deep_delta,
            'delta': self.delta,
            'theta': self.theta,
            'alpha': self.alpha,
            'beta': self.beta,
            'gamma': self.gamma
        }
        
        return state_colors.get(state.lower(), self.gentle_text)
    
    def get_biofield_color(self, biofield_type: str) -> Callable[[str], str]:
        """Get color function for specific biofield type."""
        
        biofield_colors = {
            'schumann': self.schumann,
            'solfeggio': self.solfeggio,
            'golden_ratio': self.golden_ratio
        }
        
        return biofield_colors.get(biofield_type.lower(), self.biofield_accent)
    
    def get_safety_color(self, safety_level: str) -> Callable[[str], str]:
        """Get color function for safety level."""
        
        safety_colors = {
            'safe': self.status_safe,
            'caution': self.status_caution,
            'warning': self.status_caution,
            'danger': self.status_danger,
            'critical': self.status_danger
        }
        
        return safety_colors.get(safety_level.lower(), self.gentle_text)
    
    def create_progress_bar(self, progress: float, width: int = 30) -> str:
        """Create consciousness-aware progress bar."""
        
        if self.color_mode == ColorMode.NONE:
            # ASCII progress bar for no-color terminals
            filled = int(progress * width)
            bar = '█' * filled + '▒' * (width - filled)
            return f"[{bar}] {progress:.1%}"
        
        # Colored progress bar
        filled = int(progress * width)
        empty = width - filled
        
        # Color based on progress level
        if progress < 0.3:
            color = self.colors.THETA  # Green for early progress
        elif progress < 0.7:
            color = self.colors.ALPHA  # Amber for middle progress
        else:
            color = self.colors.GAMMA  # Violet for near completion
        
        filled_bar = f"{color}{'█' * filled}{self.colors.RESET}"
        empty_bar = f"{self.colors.DIM}{'▒' * empty}{self.colors.RESET}"
        
        return f"[{filled_bar}{empty_bar}] {progress:.1%}"
    
    def create_neural_load_indicator(self, load: float) -> str:
        """Create neural load indicator with appropriate colors."""
        
        # Determine color based on load level
        if load < 0.3:
            color_func = self.status_safe
            symbol = "💚"
        elif load < 0.7:
            color_func = self.status_caution
            symbol = "💛"
        else:
            color_func = self.status_danger
            symbol = "🔥"
        
        return f"{symbol} {color_func(f'{load:.1%}')}"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PREDEFINED CONSCIOUSNESS COLOR SCHEMES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def get_default_color_scheme() -> ConsciousnessColorScheme:
    """Get the default consciousness color scheme."""
    return ConsciousnessColorScheme()

def get_gentle_color_scheme() -> ConsciousnessColorScheme:
    """Get a gentle color scheme for sensitive users."""
    scheme = ConsciousnessColorScheme()
    scheme.adapt_to_neural_sensitivity('sensitive')
    return scheme

def get_vibrant_color_scheme() -> ConsciousnessColorScheme:
    """Get a vibrant color scheme for resilient users."""
    scheme = ConsciousnessColorScheme()
    scheme.adapt_to_neural_sensitivity('resilient')
    return scheme

def create_custom_color_scheme(
    color_mode: ColorMode,
    neural_sensitivity: str = 'standard'
) -> ConsciousnessColorScheme:
    """Create a custom consciousness color scheme."""
    
    scheme = ConsciousnessColorScheme(color_mode)
    scheme.adapt_to_neural_sensitivity(neural_sensitivity)
    return scheme

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS COLOR UTILITIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def strip_color_codes(text: str) -> str:
    """Strip ANSI color codes from text."""
    import re
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return ansi_escape.sub('', text)

def get_text_width(text: str) -> int:
    """Get display width of text (excluding color codes)."""
    return len(strip_color_codes(text))

def center_text(text: str, width: int, fill_char: str = ' ') -> str:
    """Center text within specified width, accounting for color codes."""
    text_width = get_text_width(text)
    if text_width >= width:
        return text
    
    padding = (width - text_width) // 2
    return fill_char * padding + text + fill_char * (width - text_width - padding)

def consciousness_gradient(text: str, start_color: str, end_color: str) -> str:
    """Create a consciousness-aware gradient effect (simplified version)."""
    # For now, just alternate between start and end colors
    # A full implementation would interpolate colors across the text
    if len(text) <= 1:
        return f"{start_color}{text}\033[0m"
    
    mid = len(text) // 2
    return f"{start_color}{text[:mid]}\033[0m{end_color}{text[mid:]}\033[0m"