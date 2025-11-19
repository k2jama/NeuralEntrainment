#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Terminal Detection Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Terminal Detection Utility - Consciousness-aware terminal capability detection.

This module provides comprehensive terminal capability detection for optimal
consciousness visualization and user experience. It adapts the interface based
on terminal features, ensuring beautiful displays across all environments.
"""

import os
import sys
import shutil
import platform
import subprocess
from typing import Dict, Any, Optional, Tuple, List
from dataclasses import dataclass
from enum import Enum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TERMINAL CAPABILITY CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class TerminalType(Enum):
    """Types of terminal environments."""
    XTERM = "xterm"
    TMUX = "tmux"
    SCREEN = "screen"
    KONSOLE = "konsole"
    GNOME_TERMINAL = "gnome-terminal"
    ITERM2 = "iterm2"
    WINDOWS_TERMINAL = "windows-terminal"
    CMD = "cmd"
    POWERSHELL = "powershell"
    VSCODE = "vscode"
    PYCHARM = "pycharm"
    JUPYTER = "jupyter"
    UNKNOWN = "unknown"

class ColorSupport(Enum):
    """Levels of color support."""
    NONE = 0
    BASIC_8 = 8
    EXTENDED_16 = 16  
    COLOR_256 = 256
    TRUE_COLOR = 16777216

@dataclass
class TerminalCapabilities:
    """
    Complete terminal capability profile for consciousness-aware adaptation.
    """
    
    # Basic capabilities
    supports_color: bool = False
    supports_unicode: bool = False
    supports_cursor_movement: bool = False
    supports_clear_screen: bool = False
    supports_alternate_buffer: bool = False
    
    # Advanced features
    supports_mouse: bool = False
    supports_bracketed_paste: bool = False
    supports_focus_events: bool = False
    supports_rgb_color: bool = False
    supports_hyperlinks: bool = False
    
    # Display characteristics
    color_support: ColorSupport = ColorSupport.NONE
    width: int = 80
    height: int = 24
    max_width: int = 120
    max_height: int = 50
    
    # Terminal identification
    terminal_type: TerminalType = TerminalType.UNKNOWN
    terminal_name: str = "unknown"
    terminal_version: str = "unknown"
    
    # Operating system
    os_type: str = "unknown"
    is_windows: bool = False
    is_macos: bool = False
    is_linux: bool = False
    
    # Performance characteristics
    supports_fast_updates: bool = True
    recommended_fps: int = 5
    supports_animations: bool = False
    
    # Consciousness-aware features
    optimal_for_meditation: bool = False
    supports_sacred_geometry: bool = False
    biofield_visualization_quality: str = "basic"  # "basic", "enhanced", "premium"

# Known terminal capabilities database
TERMINAL_CAPABILITIES_DB = {
    'iterm2': {
        'supports_unicode': True,
        'supports_rgb_color': True,
        'supports_hyperlinks': True,
        'biofield_visualization_quality': 'premium',
        'optimal_for_meditation': True,
        'supports_sacred_geometry': True,
        'supports_animations': True,
        'recommended_fps': 10
    },
    'gnome-terminal': {
        'supports_unicode': True,
        'supports_rgb_color': True,
        'biofield_visualization_quality': 'enhanced',
        'supports_sacred_geometry': True,
        'supports_animations': True,
        'recommended_fps': 8
    },
    'konsole': {
        'supports_unicode': True,
        'supports_rgb_color': True,
        'biofield_visualization_quality': 'enhanced',
        'supports_sacred_geometry': True,
        'supports_animations': True,
        'recommended_fps': 8
    },
    'windows-terminal': {
        'supports_unicode': True,
        'supports_rgb_color': True,
        'supports_hyperlinks': True,
        'biofield_visualization_quality': 'enhanced',
        'supports_sacred_geometry': True,
        'supports_animations': True,
        'recommended_fps': 7
    },
    'vscode': {
        'supports_unicode': True,
        'supports_rgb_color': True,
        'supports_hyperlinks': True,
        'biofield_visualization_quality': 'enhanced',
        'supports_sacred_geometry': True,
        'optimal_for_meditation': True,
        'recommended_fps': 6
    },
    'xterm': {
        'supports_unicode': True,
        'supports_rgb_color': False,
        'biofield_visualization_quality': 'basic',
        'supports_sacred_geometry': True,
        'recommended_fps': 5
    },
    'cmd': {
        'supports_unicode': False,
        'supports_rgb_color': False,
        'biofield_visualization_quality': 'basic',
        'supports_sacred_geometry': False,
        'recommended_fps': 3
    },
    'powershell': {
        'supports_unicode': True,
        'supports_rgb_color': True,
        'biofield_visualization_quality': 'basic',
        'supports_sacred_geometry': True,
        'recommended_fps': 5
    }
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TERMINAL DETECTOR CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class TerminalDetector:
    """
    Comprehensive terminal capability detection for consciousness-aware interfaces.
    
    This class intelligently detects terminal capabilities and provides optimal
    configuration for consciousness visualization, biofield displays, and sacred
    geometry rendering based on the detected environment.
    """
    
    def __init__(self):
        self.capabilities = TerminalCapabilities()
        self._detection_cache = {}
        
    def detect_capabilities(self, force_redetect: bool = False) -> TerminalCapabilities:
        """
        Perform comprehensive terminal capability detection.
        
        Args:
            force_redetect: Force re-detection even if cached
            
        Returns:
            Complete terminal capabilities profile
        """
        if not force_redetect and hasattr(self, '_cached_capabilities'):
            return self._cached_capabilities
        
        # Create new capabilities object
        caps = TerminalCapabilities()
        
        # Detect operating system
        self._detect_operating_system(caps)
        
        # Detect terminal type and basic info
        self._detect_terminal_type(caps)
        
        # Detect display characteristics
        self._detect_display_characteristics(caps)
        
        # Detect color support
        self._detect_color_support(caps)
        
        # Detect Unicode support
        self._detect_unicode_support(caps)
        
        # Detect advanced features
        self._detect_advanced_features(caps)
        
        # Apply consciousness-aware optimizations
        self._apply_consciousness_optimizations(caps)
        
        # Cache results
        self._cached_capabilities = caps
        return caps
    
    def _detect_operating_system(self, caps: TerminalCapabilities) -> None:
        """Detect operating system and set OS-specific flags."""
        
        system = platform.system().lower()
        caps.os_type = system
        
        if system == 'windows':
            caps.is_windows = True
        elif system == 'darwin':
            caps.is_macos = True
        elif system in ['linux', 'unix']:
            caps.is_linux = True
    
    def _detect_terminal_type(self, caps: TerminalCapabilities) -> None:
        """Detect terminal type and version."""
        
        # Check environment variables for terminal identification
        term_env = os.environ.get('TERM', '').lower()
        term_program = os.environ.get('TERM_PROGRAM', '').lower()
        term_program_version = os.environ.get('TERM_PROGRAM_VERSION', '')
        
        # Windows-specific detection
        if caps.is_windows:
            if 'windows terminal' in term_program or os.environ.get('WT_SESSION'):
                caps.terminal_type = TerminalType.WINDOWS_TERMINAL
                caps.terminal_name = 'Windows Terminal'
            elif 'powershell' in term_program or 'pwsh' in os.environ.get('PSModulePath', ''):
                caps.terminal_type = TerminalType.POWERSHELL
                caps.terminal_name = 'PowerShell'
            else:
                caps.terminal_type = TerminalType.CMD
                caps.terminal_name = 'Command Prompt'
        
        # macOS-specific detection
        elif caps.is_macos:
            if 'iterm' in term_program:
                caps.terminal_type = TerminalType.ITERM2
                caps.terminal_name = 'iTerm2'
                caps.terminal_version = term_program_version
            elif 'apple_terminal' in term_program:
                caps.terminal_type = TerminalType.XTERM
                caps.terminal_name = 'Terminal.app'
        
        # Linux/Unix detection
        else:
            if 'gnome' in term_program or 'gnome-terminal' in term_env:
                caps.terminal_type = TerminalType.GNOME_TERMINAL
                caps.terminal_name = 'GNOME Terminal'
            elif 'konsole' in term_program or 'konsole' in term_env:
                caps.terminal_type = TerminalType.KONSOLE
                caps.terminal_name = 'Konsole'
            elif 'tmux' in term_env:
                caps.terminal_type = TerminalType.TMUX
                caps.terminal_name = 'tmux'
            elif 'screen' in term_env:
                caps.terminal_type = TerminalType.SCREEN
                caps.terminal_name = 'GNU Screen'
        
        # IDE/Editor detection
        if os.environ.get('VSCODE_PID') or 'vscode' in term_program:
            caps.terminal_type = TerminalType.VSCODE
            caps.terminal_name = 'VS Code Terminal'
        elif os.environ.get('PYCHARM_HOSTED'):
            caps.terminal_type = TerminalType.PYCHARM
            caps.terminal_name = 'PyCharm Terminal'
        elif os.environ.get('JPY_PARENT_PID'):
            caps.terminal_type = TerminalType.JUPYTER
            caps.terminal_name = 'Jupyter Terminal'
        
        # Fallback to xterm if unknown
        if caps.terminal_type == TerminalType.UNKNOWN and 'xterm' in term_env:
            caps.terminal_type = TerminalType.XTERM
            caps.terminal_name = 'xterm'
    
    def _detect_display_characteristics(self, caps: TerminalCapabilities) -> None:
        """Detect terminal size and display characteristics."""
        
        # Get terminal size
        try:
            size = shutil.get_terminal_size()
            caps.width = size.columns
            caps.height = size.lines
        except:
            caps.width = 80
            caps.height = 24
        
        # Set maximum recommended dimensions for consciousness displays
        caps.max_width = min(120, caps.width)
        caps.max_height = min(50, caps.height)
        
        # Basic capability detection
        caps.supports_cursor_movement = True  # Most terminals support this
        caps.supports_clear_screen = True     # Most terminals support this
        
        # Alternate buffer support (for full-screen applications)
        if caps.terminal_type in [TerminalType.XTERM, TerminalType.TMUX, 
                                 TerminalType.GNOME_TERMINAL, TerminalType.KONSOLE,
                                 TerminalType.ITERM2]:
            caps.supports_alternate_buffer = True
    
    def _detect_color_support(self, caps: TerminalCapabilities) -> None:
        """Detect terminal color capabilities."""
        
        # Check COLORTERM environment variable
        colorterm = os.environ.get('COLORTERM', '').lower()
        if 'truecolor' in colorterm or '24bit' in colorterm:
            caps.color_support = ColorSupport.TRUE_COLOR
            caps.supports_color = True
            caps.supports_rgb_color = True
            return
        
        # Check TERM environment variable
        term = os.environ.get('TERM', '').lower()
        
        if '256color' in term:
            caps.color_support = ColorSupport.COLOR_256
            caps.supports_color = True
        elif 'color' in term:
            caps.color_support = ColorSupport.EXTENDED_16
            caps.supports_color = True
        elif term in ['xterm', 'screen', 'tmux']:
            caps.color_support = ColorSupport.BASIC_8
            caps.supports_color = True
        
        # Windows-specific color detection
        if caps.is_windows:
            try:
                # Try to enable ANSI escape sequences on Windows
                import ctypes
                from ctypes import wintypes
                
                kernel32 = ctypes.windll.kernel32
                handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
                
                # Get current console mode
                mode = wintypes.DWORD()
                kernel32.GetConsoleMode(handle, ctypes.byref(mode))
                
                # Enable virtual terminal processing
                ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
                new_mode = mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING
                
                if kernel32.SetConsoleMode(handle, new_mode):
                    caps.supports_color = True
                    if caps.terminal_type == TerminalType.WINDOWS_TERMINAL:
                        caps.color_support = ColorSupport.TRUE_COLOR
                        caps.supports_rgb_color = True
                    else:
                        caps.color_support = ColorSupport.EXTENDED_16
            except:
                # Fallback for older Windows or if ctypes fails
                if caps.terminal_type == TerminalType.WINDOWS_TERMINAL:
                    caps.supports_color = True
                    caps.color_support = ColorSupport.COLOR_256
    
    def _detect_unicode_support(self, caps: TerminalCapabilities) -> None:
        """Detect Unicode and special character support."""
        
        # Check locale settings
        import locale
        try:
            locale_name = locale.getlocale()[1] or locale.getdefaultlocale()[1]
            if locale_name and 'utf' in locale_name.lower():
                caps.supports_unicode = True
        except:
            pass
        
        # Platform-specific Unicode detection
        if caps.is_macos or caps.is_linux:
            caps.supports_unicode = True  # Generally good Unicode support
        elif caps.is_windows:
            # Windows Unicode support varies by terminal
            if caps.terminal_type == TerminalType.WINDOWS_TERMINAL:
                caps.supports_unicode = True
            elif caps.terminal_type == TerminalType.POWERSHELL:
                caps.supports_unicode = True
            # CMD has limited Unicode support
        
        # Terminal-specific overrides
        if caps.terminal_type in [TerminalType.ITERM2, TerminalType.GNOME_TERMINAL, 
                                 TerminalType.KONSOLE, TerminalType.VSCODE]:
            caps.supports_unicode = True
        
        # Test Unicode support with a simple character
        if caps.supports_unicode:
            try:
                # Test if we can encode/decode Unicode
                test_char = '◆'
                test_char.encode('utf-8').decode('utf-8')
            except:
                caps.supports_unicode = False
    
    def _detect_advanced_features(self, caps: TerminalCapabilities) -> None:
        """Detect advanced terminal features."""
        
        # Mouse support detection
        if caps.terminal_type in [TerminalType.XTERM, TerminalType.TMUX, 
                                 TerminalType.GNOME_TERMINAL, TerminalType.KONSOLE,
                                 TerminalType.ITERM2]:
            caps.supports_mouse = True
        
        # Bracketed paste mode
        if caps.terminal_type in [TerminalType.XTERM, TerminalType.GNOME_TERMINAL, 
                                 TerminalType.KONSOLE, TerminalType.ITERM2]:
            caps.supports_bracketed_paste = True
        
        # Focus events
        if caps.terminal_type in [TerminalType.ITERM2, TerminalType.GNOME_TERMINAL]:
            caps.supports_focus_events = True
        
        # Hyperlink support
        if caps.terminal_type in [TerminalType.ITERM2, TerminalType.GNOME_TERMINAL,
                                 TerminalType.WINDOWS_TERMINAL, TerminalType.VSCODE]:
            caps.supports_hyperlinks = True
        
        # Performance characteristics
        if caps.terminal_type in [TerminalType.ITERM2, TerminalType.WINDOWS_TERMINAL]:
            caps.supports_fast_updates = True
            caps.recommended_fps = 10
        elif caps.terminal_type in [TerminalType.GNOME_TERMINAL, TerminalType.KONSOLE]:
            caps.supports_fast_updates = True
            caps.recommended_fps = 8
        else:
            caps.recommended_fps = 5
    
    def _apply_consciousness_optimizations(self, caps: TerminalCapabilities) -> None:
        """Apply consciousness-aware optimizations based on detected capabilities."""
        
        terminal_key = caps.terminal_type.value
        
        # Apply known optimizations from database
        if terminal_key in TERMINAL_CAPABILITIES_DB:
            db_caps = TERMINAL_CAPABILITIES_DB[terminal_key]
            
            for key, value in db_caps.items():
                if hasattr(caps, key):
                    setattr(caps, key, value)
        
        # Consciousness-specific feature detection
        if caps.supports_unicode and caps.supports_color:
            caps.supports_sacred_geometry = True
        
        if caps.color_support in [ColorSupport.COLOR_256, ColorSupport.TRUE_COLOR]:
            caps.biofield_visualization_quality = 'enhanced'
        
        if (caps.supports_rgb_color and caps.supports_unicode and 
            caps.supports_fast_updates):
            caps.biofield_visualization_quality = 'premium'
        
        # Animation support based on performance
        if caps.recommended_fps >= 6:
            caps.supports_animations = True
        
        # Meditation optimization for certain terminals
        if caps.terminal_type in [TerminalType.ITERM2, TerminalType.VSCODE]:
            caps.optimal_for_meditation = True
        
        # Adjust for low-capability terminals
        if caps.terminal_type == TerminalType.CMD:
            caps.biofield_visualization_quality = 'basic'
            caps.supports_sacred_geometry = False
            caps.supports_animations = False
            caps.recommended_fps = 3
    
    def get_optimal_display_settings(self) -> Dict[str, Any]:
        """
        Get optimal display settings based on detected capabilities.
        
        Returns:
            Dictionary of optimal settings for consciousness visualization
        """
        caps = self.detect_capabilities()
        
        settings = {
            'use_color': caps.supports_color,
            'use_unicode': caps.supports_unicode,
            'use_animations': caps.supports_animations,
            'fps': caps.recommended_fps,
            'max_width': caps.max_width,
            'max_height': caps.max_height,
            'biofield_quality': caps.biofield_visualization_quality,
            'sacred_geometry': caps.supports_sacred_geometry,
            'meditation_optimized': caps.optimal_for_meditation,
            'color_depth': caps.color_support.value if caps.supports_color else 0,
            'rgb_color': caps.supports_rgb_color
        }
        
        return settings
    
    def get_fallback_recommendations(self) -> List[str]:
        """Get recommendations for improving terminal capabilities."""
        
        caps = self.detect_capabilities()
        recommendations = []
        
        if not caps.supports_unicode:
            recommendations.append("Consider using a terminal with Unicode support for enhanced sacred geometry visualization")
        
        if not caps.supports_color:
            recommendations.append("Enable color support in your terminal for biofield intelligence visualization")
        
        if caps.color_support == ColorSupport.BASIC_8:
            recommendations.append("Upgrade to a terminal with 256-color or true-color support for optimal consciousness displays")
        
        if not caps.supports_animations:
            recommendations.append("Use a modern terminal for animated biofield flow visualization")
        
        if caps.biofield_visualization_quality == 'basic':
            recommendations.append("Consider iTerm2, Windows Terminal, or GNOME Terminal for premium consciousness visualization")
        
        return recommendations
    
    def test_specific_feature(self, feature_name: str) -> bool:
        """
        Test a specific terminal feature.
        
        Args:
            feature_name: Name of the feature to test
            
        Returns:
            True if feature is supported
        """
        caps = self.detect_capabilities()
        return getattr(caps, feature_name, False)
    
    def generate_capability_report(self) -> str:
        """Generate a detailed capability report for debugging."""
        
        caps = self.detect_capabilities()
        
        report_lines = [
            "🧠 Neural Entrainment Terminal Capability Report",
            "=" * 50,
            f"Terminal: {caps.terminal_name} ({caps.terminal_type.value})",
            f"Version: {caps.terminal_version}",
            f"OS: {caps.os_type}",
            f"Size: {caps.width}x{caps.height}",
            "",
            "Basic Capabilities:",
            f"  Color Support: {'✓' if caps.supports_color else '✗'} ({caps.color_support.name})",
            f"  Unicode Support: {'✓' if caps.supports_unicode else '✗'}",
            f"  Cursor Movement: {'✓' if caps.supports_cursor_movement else '✗'}",
            f"  Clear Screen: {'✓' if caps.supports_clear_screen else '✗'}",
            "",
            "Advanced Features:",
            f"  RGB Colors: {'✓' if caps.supports_rgb_color else '✗'}",
            f"  Mouse Support: {'✓' if caps.supports_mouse else '✗'}",
            f"  Hyperlinks: {'✓' if caps.supports_hyperlinks else '✗'}",
            f"  Animations: {'✓' if caps.supports_animations else '✗'}",
            "",
            "Consciousness Features:",
            f"  Sacred Geometry: {'✓' if caps.supports_sacred_geometry else '✗'}",
            f"  Biofield Quality: {caps.biofield_visualization_quality}",
            f"  Meditation Optimized: {'✓' if caps.optimal_for_meditation else '✗'}",
            f"  Recommended FPS: {caps.recommended_fps}",
        ]
        
        return "\n".join(report_lines)

def detect_terminal_capabilities() -> TerminalCapabilities:
    """
    Convenience function to detect terminal capabilities.
    
    Returns:
        Terminal capabilities object
    """
    detector = TerminalDetector()
    return detector.detect_capabilities()

def get_optimal_consciousness_settings() -> Dict[str, Any]:
    """
    Convenience function to get optimal consciousness display settings.
    
    Returns:
        Dictionary of optimal display settings
    """
    detector = TerminalDetector()
    return detector.get_optimal_display_settings()