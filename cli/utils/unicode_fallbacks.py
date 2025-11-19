#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Unicode Fallbacks Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Unicode Fallbacks Utility - Consciousness-aware character fallback handling.

This module provides intelligent Unicode to ASCII fallback mapping for terminals
with limited Unicode support, ensuring beautiful consciousness visualizations
work across all environments while preserving sacred geometry meaning.
"""

import sys
from typing import Dict, Any, List, Optional, Tuple, Union
from dataclasses import dataclass
from enum import Enum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS SYMBOL MAPPINGS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class FallbackLevel(Enum):
    """Levels of fallback support."""
    FULL_UNICODE = "full_unicode"      # Full Unicode support
    EXTENDED_ASCII = "extended_ascii"   # Extended ASCII (CP437/Latin-1)
    BASIC_ASCII = "basic_ascii"        # Basic 7-bit ASCII only
    MINIMAL = "minimal"                # Absolute minimum characters

# Sacred Geometry and Consciousness Symbol Mappings
CONSCIOUSNESS_SYMBOL_MAP = {
    # Sacred Geometry Symbols
    '◆': {'extended': '♦', 'basic': '*', 'minimal': '*'},  # Diamond
    '◇': {'extended': '♦', 'basic': 'o', 'minimal': 'o'},  # Hollow diamond
    '○': {'extended': '°', 'basic': 'o', 'minimal': 'o'},  # Circle
    '●': {'extended': '•', 'basic': '*', 'minimal': '*'},  # Filled circle
    '◯': {'extended': 'O', 'basic': 'O', 'minimal': 'O'},  # Large circle
    '◉': {'extended': '()', 'basic': '()', 'minimal': '()'},  # Bullseye
    '△': {'extended': '^', 'basic': '^', 'minimal': '^'},  # Triangle up
    '▽': {'extended': 'v', 'basic': 'v', 'minimal': 'v'},  # Triangle down
    '□': {'extended': '[]', 'basic': '[]', 'minimal': '[]'},  # Square
    '■': {'extended': '▪', 'basic': '#', 'minimal': '#'},  # Filled square
    '◈': {'extended': '<>', 'basic': '<>', 'minimal': '<>'},  # Diamond with cross
    '✦': {'extended': '*', 'basic': '*', 'minimal': '*'},  # Star
    '✧': {'extended': '*', 'basic': '*', 'minimal': '*'},  # Hollow star
    '✪': {'extended': '*', 'basic': '*', 'minimal': '*'},  # Circled star
    '⭐': {'extended': '*', 'basic': '*', 'minimal': '*'},  # Star emoji
    '🌟': {'extended': '*', 'basic': '*', 'minimal': '*'},  # Glowing star
    
    # Biofield Flow Symbols
    '∿': {'extended': '~', 'basic': '~', 'minimal': '~'},  # Sine wave
    '⌇': {'extended': '|', 'basic': '|', 'minimal': '|'},  # Broken bar
    '∾': {'extended': '~', 'basic': '~', 'minimal': '~'},  # Inverted lazy s
    '≈': {'extended': '≈', 'basic': '~~', 'minimal': '~~'},  # Almost equal
    '∞': {'extended': '∞', 'basic': 'oo', 'minimal': 'oo'},  # Infinity
    '∽': {'extended': '~', 'basic': '~', 'minimal': '~'},  # Reversed tilde
    '⟡': {'extended': '<>', 'basic': '<>', 'minimal': '<>'},  # Lozenge
    '◊': {'extended': '<>', 'basic': '<>', 'minimal': '<>'},  # Lozenge
    
    # Consciousness State Symbols
    '◔': {'extended': '(', 'basic': '(', 'minimal': '('},  # Quarter circle
    '◑': {'extended': '[]', 'basic': '[', 'minimal': '['},  # Half circle
    '◕': {'extended': ')', 'basic': ')', 'minimal': ')'},  # Three-quarter circle
    '◐': {'extended': '[]', 'basic': ']', 'minimal': ']'},  # Half circle reverse
    '◓': {'extended': '°', 'basic': '.', 'minimal': '.'},  # Circle with upper half
    
    # Progress and Status Symbols
    '█': {'extended': '█', 'basic': '#', 'minimal': '#'},  # Full block
    '▓': {'extended': '▓', 'basic': '#', 'minimal': '#'},  # Dark shade
    '▒': {'extended': '▒', 'basic': '.', 'minimal': '.'},  # Medium shade
    '░': {'extended': '░', 'basic': '.', 'minimal': '.'},  # Light shade
    '▬': {'extended': '─', 'basic': '-', 'minimal': '-'},  # Horizontal bar
    '─': {'extended': '─', 'basic': '-', 'minimal': '-'},  # Box horizontal
    '━': {'extended': '═', 'basic': '=', 'minimal': '='},  # Heavy horizontal
    '═': {'extended': '═', 'basic': '=', 'minimal': '='},  # Double horizontal
    '╌': {'extended': '┄', 'basic': '.', 'minimal': '.'},  # Dashed horizontal
    '┄': {'extended': '┄', 'basic': '-', 'minimal': '-'},  # Triple dash horizontal
    
    # Directional and Flow Symbols
    '→': {'extended': '→', 'basic': '->', 'minimal': '>'},  # Right arrow
    '←': {'extended': '←', 'basic': '<-', 'minimal': '<'},  # Left arrow
    '↑': {'extended': '↑', 'basic': '^', 'minimal': '^'},  # Up arrow
    '↓': {'extended': '↓', 'basic': 'v', 'minimal': 'v'},  # Down arrow
    '↗': {'extended': '/', 'basic': '/', 'minimal': '/'},  # Up-right arrow
    '↘': {'extended': '\\', 'basic': '\\', 'minimal': '\\'},  # Down-right arrow
    '↖': {'extended': '\\', 'basic': '\\', 'minimal': '\\'},  # Up-left arrow
    '↙': {'extended': '/', 'basic': '/', 'minimal': '/'},  # Down-left arrow
    '⟲': {'extended': 'o', 'basic': 'o', 'minimal': 'o'},  # Counterclockwise
    '⟳': {'extended': 'o', 'basic': 'o', 'minimal': 'o'},  # Clockwise
    
    # Mathematical and Sacred Symbols
    'Φ': {'extended': 'Φ', 'basic': 'PHI', 'minimal': 'P'},  # Golden ratio
    'φ': {'extended': 'φ', 'basic': 'phi', 'minimal': 'p'},  # Small phi
    '∝': {'extended': 'α', 'basic': 'a', 'minimal': 'a'},  # Proportional to
    '∫': {'extended': 'S', 'basic': 'S', 'minimal': 'S'},  # Integral
    '∑': {'extended': 'E', 'basic': 'E', 'minimal': 'E'},  # Summation
    '∆': {'extended': '^', 'basic': '^', 'minimal': '^'},  # Delta
    '∇': {'extended': 'v', 'basic': 'v', 'minimal': 'v'},  # Nabla
    
    # Frequency and Sound Symbols
    '♫': {'extended': '♪', 'basic': '♪', 'minimal': '8'},  # Musical note
    '♪': {'extended': '♪', 'basic': '♪', 'minimal': '8'},  # Musical note
    '♩': {'extended': '♩', 'basic': '♩', 'minimal': '4'},  # Quarter note
    '𝄞': {'extended': '&', 'basic': '&', 'minimal': '&'},  # Treble clef
    '♯': {'extended': '#', 'basic': '#', 'minimal': '#'},  # Sharp
    '♮': {'extended': 'n', 'basic': 'n', 'minimal': 'n'},  # Natural
    '♭': {'extended': 'b', 'basic': 'b', 'minimal': 'b'},  # Flat
    
    # Status and Safety Symbols
    '✓': {'extended': '√', 'basic': 'V', 'minimal': 'Y'},  # Check mark
    '✗': {'extended': 'X', 'basic': 'X', 'minimal': 'N'},  # X mark
    '⚠': {'extended': '!', 'basic': '!', 'minimal': '!'},  # Warning
    '🚨': {'extended': '!!!', 'basic': '!!!', 'minimal': '!'},  # Alarm
    '🛡️': {'extended': '[S]', 'basic': '[S]', 'minimal': 'S'},  # Shield
    '💚': {'extended': '<3', 'basic': '<3', 'minimal': 'H'},  # Green heart
    
    # Nature and Earth Symbols
    '🌍': {'extended': '(E)', 'basic': '(E)', 'minimal': 'E'},  # Earth
    '🌊': {'extended': '~w~', 'basic': '~~~', 'minimal': '~'},  # Water wave
    '🔥': {'extended': '^f^', 'basic': '^^^', 'minimal': '^'},  # Fire
    '🌬️': {'extended': 'o~o', 'basic': 'o~o', 'minimal': 'o'},  # Wind
    '🌱': {'extended': '^|^', 'basic': '|^|', 'minimal': '|'},  # Seedling
    '🌿': {'extended': '~|~', 'basic': '~|~', 'minimal': '|'},  # Herb
    '🌙': {'extended': '()', 'basic': '()', 'minimal': 'C'},  # Crescent moon
    '☀️': {'extended': '*O*', 'basic': '*O*', 'minimal': 'O'},  # Sun
    
    # Consciousness and Meditation Symbols
    '🧠': {'extended': '{o}', 'basic': '{o}', 'minimal': 'B'},  # Brain
    '👁️': {'extended': '(o)', 'basic': '(o)', 'minimal': 'I'},  # Eye
    '🙏': {'extended': '||', 'basic': '||', 'minimal': 'P'},  # Prayer hands
    '🤲': {'extended': 'UU', 'basic': 'UU', 'minimal': 'U'},  # Cupped hands
    '🕉️': {'extended': 'OM', 'basic': 'OM', 'minimal': 'O'},  # Om symbol
    '☯': {'extended': 'YY', 'basic': 'YY', 'minimal': 'Y'},  # Yin yang
    '🔮': {'extended': '(o)', 'basic': '(o)', 'minimal': 'C'},  # Crystal ball
    '✨': {'extended': '***', 'basic': '***', 'minimal': '*'},  # Sparkles
    '🌈': {'extended': '^^^', 'basic': '^^^', 'minimal': '^'},  # Rainbow
    
    # Emotional and Expression Symbols
    '😊': {'extended': ':)', 'basic': ':)', 'minimal': ')'},  # Smiling
    '😌': {'extended': ':-', 'basic': ':-', 'minimal': '-'},  # Relieved
    '😐': {'extended': ':|', 'basic': ':|', 'minimal': '|'},  # Neutral
    '😟': {'extended': ':(', 'basic': ':(', 'minimal': '('},  # Worried
    '😰': {'extended': ':O', 'basic': ':O', 'minimal': 'O'},  # Anxious
}

# Box drawing fallbacks
BOX_DRAWING_MAP = {
    '┌': {'extended': '┌', 'basic': '+', 'minimal': '+'},  # Top left
    '┐': {'extended': '┐', 'basic': '+', 'minimal': '+'},  # Top right
    '└': {'extended': '└', 'basic': '+', 'minimal': '+'},  # Bottom left
    '┘': {'extended': '┘', 'basic': '+', 'minimal': '+'},  # Bottom right
    '├': {'extended': '├', 'basic': '+', 'minimal': '+'},  # Left tee
    '┤': {'extended': '┤', 'basic': '+', 'minimal': '+'},  # Right tee
    '┬': {'extended': '┬', 'basic': '+', 'minimal': '+'},  # Top tee
    '┴': {'extended': '┴', 'basic': '+', 'minimal': '+'},  # Bottom tee
    '┼': {'extended': '┼', 'basic': '+', 'minimal': '+'},  # Cross
    '│': {'extended': '│', 'basic': '|', 'minimal': '|'},  # Vertical
    '─': {'extended': '─', 'basic': '-', 'minimal': '-'},  # Horizontal
}

# Combine all mappings
ALL_SYMBOL_MAPPINGS = {**CONSCIOUSNESS_SYMBOL_MAP, **BOX_DRAWING_MAP}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# UNICODE FALLBACK MANAGER CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@dataclass
class FallbackSettings:
    """Settings for Unicode fallback behavior."""
    fallback_level: FallbackLevel = FallbackLevel.BASIC_ASCII
    preserve_meaning: bool = True
    use_spacing_compensation: bool = True
    maintain_alignment: bool = True
    consciousness_aware: bool = True

class UnicodeFallbackManager:
    """
    Intelligent Unicode fallback management for consciousness visualization.
    
    This class provides seamless fallback from Unicode symbols to ASCII
    alternatives while preserving the sacred meaning and visual structure
    of consciousness displays.
    """
    
    def __init__(self, fallback_level: FallbackLevel = FallbackLevel.BASIC_ASCII):
        self.fallback_level = fallback_level
        self.settings = FallbackSettings(fallback_level=fallback_level)
        self.encoding_cache = {}
        self.test_cache = {}
    
    def can_display_unicode(self) -> bool:
        """
        Test if the current terminal can display Unicode characters.
        
        Returns:
            True if Unicode is supported
        """
        if 'unicode_support' in self.test_cache:
            return self.test_cache['unicode_support']
        
        try:
            # Test encoding capabilities
            test_chars = ['◆', '∿', '🧠']
            for char in test_chars:
                char.encode(sys.stdout.encoding or 'utf-8')
            
            # Test if we can write Unicode to stdout
            original_stdout = sys.stdout.write
            test_successful = True
            
            try:
                # Try to write a test Unicode character
                sys.stdout.write('◆')
                sys.stdout.flush()
            except (UnicodeEncodeError, UnicodeDecodeError):
                test_successful = False
            
            self.test_cache['unicode_support'] = test_successful
            return test_successful
            
        except Exception:
            self.test_cache['unicode_support'] = False
            return False
    
    def determine_optimal_fallback_level(self) -> FallbackLevel:
        """
        Automatically determine the optimal fallback level.
        
        Returns:
            Optimal fallback level for the current environment
        """
        if self.can_display_unicode():
            return FallbackLevel.FULL_UNICODE
        
        # Test extended ASCII
        try:
            test_chars = ['•', '°', '▪']
            encoding = sys.stdout.encoding or 'ascii'
            
            for char in test_chars:
                char.encode(encoding)
            
            return FallbackLevel.EXTENDED_ASCII
            
        except UnicodeEncodeError:
            return FallbackLevel.BASIC_ASCII
    
    def convert_symbol(self, symbol: str, preserve_length: bool = False) -> str:
        """
        Convert a Unicode symbol to its appropriate fallback.
        
        Args:
            symbol: Unicode symbol to convert
            preserve_length: Whether to preserve string length
            
        Returns:
            Fallback representation of the symbol
        """
        if symbol not in ALL_SYMBOL_MAPPINGS:
            # If no mapping exists, try to handle gracefully
            if self.fallback_level == FallbackLevel.FULL_UNICODE:
                return symbol
            else:
                # Find a reasonable ASCII substitute
                return self._find_ascii_substitute(symbol)
        
        mapping = ALL_SYMBOL_MAPPINGS[symbol]
        
        if self.fallback_level == FallbackLevel.FULL_UNICODE:
            return symbol
        elif self.fallback_level == FallbackLevel.EXTENDED_ASCII:
            fallback = mapping.get('extended', symbol)
        elif self.fallback_level == FallbackLevel.BASIC_ASCII:
            fallback = mapping.get('basic', mapping.get('extended', symbol))
        else:  # MINIMAL
            fallback = mapping.get('minimal', 
                                 mapping.get('basic', 
                                           mapping.get('extended', symbol)))
        
        # Length preservation
        if preserve_length and len(fallback) != len(symbol):
            if len(fallback) < len(symbol):
                # Pad with spaces
                fallback = fallback.ljust(len(symbol))
            else:
                # Truncate
                fallback = fallback[:len(symbol)]
        
        return fallback
    
    def convert_text(self, text: str, preserve_spacing: bool = True) -> str:
        """
        Convert text containing Unicode symbols to fallback representation.
        
        Args:
            text: Text to convert
            preserve_spacing: Whether to preserve spacing alignment
            
        Returns:
            Text with Unicode symbols converted to fallbacks
        """
        if self.fallback_level == FallbackLevel.FULL_UNICODE and self.can_display_unicode():
            return text
        
        result = ""
        i = 0
        original_length = len(text)
        
        while i < len(text):
            char = text[i]
            
            if char in ALL_SYMBOL_MAPPINGS:
                fallback = self.convert_symbol(char, preserve_length=preserve_spacing)
                result += fallback
            else:
                # Check if character can be displayed
                if self._can_display_char(char):
                    result += char
                else:
                    result += self._find_ascii_substitute(char)
            
            i += 1
        
        # Ensure alignment is preserved if requested
        if preserve_spacing and self.settings.maintain_alignment:
            result = self._adjust_alignment(text, result, original_length)
        
        return result
    
    def convert_consciousness_display(self, display_lines: List[str]) -> List[str]:
        """
        Convert consciousness display with intelligent layout preservation.
        
        Args:
            display_lines: List of display lines to convert
            
        Returns:
            Converted display lines with fallbacks
        """
        converted_lines = []
        max_original_width = max(len(line) for line in display_lines) if display_lines else 0
        
        for line in display_lines:
            converted_line = self.convert_text(line, preserve_spacing=True)
            
            # Ensure sacred geometry structures remain aligned
            if self.settings.consciousness_aware:
                converted_line = self._preserve_sacred_geometry_alignment(line, converted_line)
            
            converted_lines.append(converted_line)
        
        # Post-process for overall alignment
        if self.settings.maintain_alignment:
            converted_lines = self._align_consciousness_display(converted_lines, max_original_width)
        
        return converted_lines
    
    def create_fallback_progress_bar(self, progress: float, width: int, 
                                   filled_char: str = '█', 
                                   empty_char: str = '░') -> str:
        """
        Create a progress bar with appropriate fallback characters.
        
        Args:
            progress: Progress value (0.0 to 1.0)
            width: Width of the progress bar
            filled_char: Character for filled portion
            empty_char: Character for empty portion
            
        Returns:
            Progress bar string with fallback characters
        """
        filled_count = int(progress * width)
        empty_count = width - filled_count
        
        filled_fallback = self.convert_symbol(filled_char)
        empty_fallback = self.convert_symbol(empty_char)
        
        return filled_fallback * filled_count + empty_fallback * empty_count
    
    def create_fallback_mandala(self, size: int) -> List[str]:
        """
        Create a sacred geometry mandala with fallback characters.
        
        Args:
            size: Radius of the mandala
            
        Returns:
            List of strings representing the mandala
        """
        lines = []
        
        for y in range(-size, size + 1):
            line = ""
            for x in range(-size, size + 1):
                distance = (x * x + y * y) ** 0.5
                
                if distance <= size:
                    if distance < 1:
                        symbol = '◉'  # Center
                    elif distance < size * 0.3:
                        symbol = '●'  # Inner circle
                    elif distance < size * 0.6:
                        symbol = '◆'  # Middle ring
                    elif distance < size * 0.9:
                        symbol = '○'  # Outer ring
                    else:
                        symbol = '·'  # Edge
                else:
                    symbol = ' '
                
                line += self.convert_symbol(symbol)
            
            lines.append(line.rstrip())
        
        return lines
    
    def _can_display_char(self, char: str) -> bool:
        """Test if a specific character can be displayed."""
        
        if char in self.encoding_cache:
            return self.encoding_cache[char]
        
        try:
            encoding = sys.stdout.encoding or 'ascii'
            char.encode(encoding)
            self.encoding_cache[char] = True
            return True
        except (UnicodeEncodeError, UnicodeDecodeError):
            self.encoding_cache[char] = False
            return False
    
    def _find_ascii_substitute(self, char: str) -> str:
        """Find a reasonable ASCII substitute for an unknown character."""
        
        # Get character category and find appropriate substitute
        try:
            import unicodedata
            category = unicodedata.category(char)
            
            if category.startswith('P'):  # Punctuation
                return '.'
            elif category.startswith('S'):  # Symbols
                return '*'
            elif category.startswith('M'):  # Marks
                return '~'
            elif category.startswith('N'):  # Numbers
                return '#'
            else:
                return '?'
        except:
            return '?'
    
    def _adjust_alignment(self, original: str, converted: str, target_length: int) -> str:
        """Adjust converted string to maintain alignment."""
        
        current_length = len(converted)
        
        if current_length == target_length:
            return converted
        elif current_length < target_length:
            # Pad with spaces
            padding = target_length - current_length
            return converted + ' ' * padding
        else:
            # Truncate carefully, preserving important symbols
            return converted[:target_length]
    
    def _preserve_sacred_geometry_alignment(self, original: str, converted: str) -> str:
        """Preserve sacred geometry alignment in converted text."""
        
        # Ensure centered symbols remain centered
        original_center = len(original) // 2
        converted_center = len(converted) // 2
        
        if abs(original_center - converted_center) > 1:
            # Re-center if necessary
            target_length = len(original)
            if len(converted) < target_length:
                padding_total = target_length - len(converted)
                left_padding = padding_total // 2
                right_padding = padding_total - left_padding
                return ' ' * left_padding + converted + ' ' * right_padding
        
        return converted
    
    def _align_consciousness_display(self, lines: List[str], target_width: int) -> List[str]:
        """Align consciousness display lines for visual consistency."""
        
        aligned_lines = []
        
        for line in lines:
            if len(line) < target_width:
                # Center-align consciousness displays
                padding = target_width - len(line)
                left_padding = padding // 2
                right_padding = padding - left_padding
                aligned_line = ' ' * left_padding + line + ' ' * right_padding
            else:
                aligned_line = line[:target_width]
            
            aligned_lines.append(aligned_line)
        
        return aligned_lines
    
    def get_fallback_summary(self) -> Dict[str, Any]:
        """Get summary of current fallback configuration."""
        
        return {
            'fallback_level': self.fallback_level.value,
            'unicode_support': self.can_display_unicode(),
            'total_mappings': len(ALL_SYMBOL_MAPPINGS),
            'consciousness_symbols': len(CONSCIOUSNESS_SYMBOL_MAP),
            'box_drawing_symbols': len(BOX_DRAWING_MAP),
            'settings': {
                'preserve_meaning': self.settings.preserve_meaning,
                'maintain_alignment': self.settings.maintain_alignment,
                'consciousness_aware': self.settings.consciousness_aware
            }
        }

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS SYMBOL MAPPER CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessSymbolMapper:
    """
    Specialized symbol mapper for consciousness-aware applications.
    
    This class provides intelligent symbol mapping that preserves the sacred
    meaning and consciousness significance of symbols when falling back to
    ASCII representations.
    """
    
    def __init__(self, fallback_manager: UnicodeFallbackManager = None):
        self.fallback_manager = fallback_manager or UnicodeFallbackManager()
        self.consciousness_context = {}
    
    def map_consciousness_state_symbol(self, consciousness_state: str) -> str:
        """
        Map consciousness state to appropriate symbol with fallback.
        
        Args:
            consciousness_state: Name of consciousness state
            
        Returns:
            Symbol representing the consciousness state
        """
        state_symbols = {
            'deep_delta': '●',
            'delta': '◉',
            'theta': '◆',
            'alpha': '△',
            'beta': '□',
            'gamma': '✦',
            'neutral': '○',
            'integration': '∞',
            'transcendent': '🌟'
        }
        
        symbol = state_symbols.get(consciousness_state, '○')
        return self.fallback_manager.convert_symbol(symbol)
    
    def map_biofield_symbol(self, biofield_type: str) -> str:
        """
        Map biofield type to appropriate symbol with fallback.
        
        Args:
            biofield_type: Type of biofield (schumann, solfeggio, etc.)
            
        Returns:
            Symbol representing the biofield type
        """
        biofield_symbols = {
            'schumann': '🌍',
            'solfeggio': '♫',
            'golden_ratio': 'Φ',
            'natural_frequency': '🌿',
            'coherence': '∿',
            'harmony': '≈',
            'resonance': '∞'
        }
        
        symbol = biofield_symbols.get(biofield_type, '∿')
        return self.fallback_manager.convert_symbol(symbol)
    
    def create_consciousness_progress_bar(self, progress: float, width: int,
                                        consciousness_state: str = 'neutral') -> str:
        """
        Create consciousness-aware progress bar with state-appropriate symbols.
        
        Args:
            progress: Progress value (0.0 to 1.0)
            width: Width of progress bar
            consciousness_state: Current consciousness state
            
        Returns:
            Progress bar with consciousness-aware symbols
        """
        # Choose symbols based on consciousness state
        if consciousness_state in ['deep_delta', 'delta']:
            filled_char = '●'
            empty_char = '○'
        elif consciousness_state == 'theta':
            filled_char = '◆'
            empty_char = '◇'
        elif consciousness_state == 'alpha':
            filled_char = '△'
            empty_char = '▽'
        elif consciousness_state in ['beta', 'gamma']:
            filled_char = '■'
            empty_char = '□'
        else:
            filled_char = '█'
            empty_char = '░'
        
        return self.fallback_manager.create_fallback_progress_bar(
            progress, width, filled_char, empty_char
        )
    
    def create_biofield_wave_pattern(self, coherence: float, width: int) -> str:
        """
        Create biofield wave pattern with fallback symbols.
        
        Args:
            coherence: Biofield coherence level (0.0 to 1.0)
            width: Width of pattern
            
        Returns:
            Wave pattern string
        """
        import math
        
        pattern = ""
        for i in range(width):
            x = i / width * 4 * math.pi
            wave_value = math.sin(x) * coherence
            
            if wave_value > 0.7:
                symbol = '∿'
            elif wave_value > 0.3:
                symbol = '⌇'
            elif wave_value > 0.0:
                symbol = '∙'
            elif wave_value > -0.3:
                symbol = '·'
            else:
                symbol = ' '
            
            pattern += self.fallback_manager.convert_symbol(symbol)
        
        return pattern
    
    def create_sacred_geometry_pattern(self, pattern_type: str, size: int) -> List[str]:
        """
        Create sacred geometry pattern with fallback support.
        
        Args:
            pattern_type: Type of pattern ('mandala', 'spiral', 'flower_of_life')
            size: Size/radius of the pattern
            
        Returns:
            List of strings representing the pattern
        """
        if pattern_type == 'mandala':
            return self.fallback_manager.create_fallback_mandala(size)
        elif pattern_type == 'spiral':
            return self._create_spiral_pattern(size)
        elif pattern_type == 'flower_of_life':
            return self._create_flower_of_life_pattern(size)
        else:
            return self.fallback_manager.create_fallback_mandala(size)
    
    def _create_spiral_pattern(self, size: int) -> List[str]:
        """Create a spiral pattern with fallback symbols."""
        
        lines = []
        import math
        
        for y in range(-size, size + 1):
            line = ""
            for x in range(-size, size + 1):
                distance = (x * x + y * y) ** 0.5
                angle = math.atan2(y, x)
                
                # Golden spiral equation
                spiral_value = distance - (size * angle / (2 * math.pi))
                
                if abs(spiral_value) < 1:
                    symbol = '◆'
                elif abs(spiral_value) < 2:
                    symbol = '◇'
                else:
                    symbol = ' '
                
                line += self.fallback_manager.convert_symbol(symbol)
            
            lines.append(line.rstrip())
        
        return lines
    
    def _create_flower_of_life_pattern(self, size: int) -> List[str]:
        """Create a Flower of Life pattern with fallback symbols."""
        
        lines = []
        import math
        
        # Simplified Flower of Life using overlapping circles
        for y in range(-size, size + 1):
            line = ""
            for x in range(-size, size + 1):
                # Check multiple circle centers for overlapping pattern
                on_pattern = False
                
                centers = [(0, 0), (1, 0), (-1, 0), (0.5, 0.866), (-0.5, 0.866), (0.5, -0.866), (-0.5, -0.866)]
                
                for cx, cy in centers:
                    distance = ((x - cx * size/2) ** 2 + (y - cy * size/2) ** 2) ** 0.5
                    if abs(distance - size/2) < 0.5:
                        on_pattern = True
                        break
                
                symbol = '○' if on_pattern else ' '
                line += self.fallback_manager.convert_symbol(symbol)
            
            lines.append(line.rstrip())
        
        return lines

def create_fallback_manager(auto_detect: bool = True) -> UnicodeFallbackManager:
    """
    Convenience function to create a Unicode fallback manager.
    
    Args:
        auto_detect: Whether to automatically detect optimal fallback level
        
    Returns:
        Configured UnicodeFallbackManager instance
    """
    manager = UnicodeFallbackManager()
    
    if auto_detect:
        optimal_level = manager.determine_optimal_fallback_level()
        manager.fallback_level = optimal_level
    
    return manager

def create_consciousness_symbol_mapper(auto_detect: bool = True) -> ConsciousnessSymbolMapper:
    """
    Convenience function to create a consciousness symbol mapper.
    
    Args:
        auto_detect: Whether to automatically detect optimal fallback level
        
    Returns:
        Configured ConsciousnessSymbolMapper instance
    """
    fallback_manager = create_fallback_manager(auto_detect)
    return ConsciousnessSymbolMapper(fallback_manager)