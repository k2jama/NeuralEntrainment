# 🧠 Neural Entrainment System v2.0 - Sacred Geometry & ASCII Art
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Sacred Geometry & ASCII Art - Beautiful terminal patterns for consciousness work.

This module provides sacred geometry symbols, biofield patterns, and consciousness-aware
ASCII art that create a harmonious and inspiring visual environment for CLI interactions.
All patterns are designed with respect for consciousness sovereignty and neural sensitivity.
"""

import math
from typing import List, Dict, Optional, Tuple
from enum import Enum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SACRED GEOMETRY SYMBOLS & CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class SacredGeometrySymbols:
    """Sacred geometry symbols for consciousness-aware CLI interface."""
    
    # Mathematical constants
    PHI = "Φ"               # Golden ratio symbol
    PHI_LOWER = "φ"         # Lowercase phi
    INFINITY = "∞"          # Infinity symbol
    APPROXIMATELY = "≈"     # Approximately equal
    THEREFORE = "∴"         # Therefore symbol
    BECAUSE = "∵"          # Because symbol
    
    # Geometric shapes
    CIRCLE = "○"           # Circle
    FILLED_CIRCLE = "●"    # Filled circle
    DIAMOND = "◊"          # Diamond
    FILLED_DIAMOND = "◆"   # Filled diamond
    TRIANGLE_UP = "△"      # Triangle up
    TRIANGLE_DOWN = "▽"    # Triangle down
    SQUARE = "□"           # Square
    FILLED_SQUARE = "■"    # Filled square
    
    # Energy and consciousness symbols
    STAR = "✦"            # Star symbol
    SPARKLE = "✨"         # Sparkle
    SPIRAL = "🌀"         # Spiral
    YIN_YANG = "☯"        # Yin-yang balance
    FLOWER_OF_LIFE = "⚛"   # Atom/flower of life approximation
    
    # Directional and flow symbols
    ARROW_UP = "↑"         # Up arrow
    ARROW_DOWN = "↓"       # Down arrow  
    ARROW_LEFT = "←"       # Left arrow
    ARROW_RIGHT = "→"      # Right arrow
    DOUBLE_ARROW = "↔"     # Double arrow
    WAVY_ARROW = "↝"       # Wavy arrow
    
    # Consciousness state symbols
    ALPHA_WAVE = "∿"       # Alpha wave pattern
    THETA_WAVE = "⌇"       # Theta wave pattern
    MEDITATION = "🧘"      # Meditation symbol
    BRAIN = "🧠"           # Brain symbol
    
    # Biofield symbols
    EARTH = "🌍"           # Earth (Schumann resonance)
    SOUND_WAVE = "♫"       # Sound wave
    FREQUENCY = "⩙"        # Frequency symbol
    RESONANCE = "※"        # Resonance symbol
    
    # Safety and protection symbols
    SHIELD = "🛡"          # Shield
    CHECK_MARK = "✓"       # Check mark
    WARNING = "⚠"          # Warning
    EMERGENCY = "🚨"       # Emergency
    HEART = "💚"           # Heart (comfort/well-being)
    
    # Progress and time symbols
    HOURGLASS = "⧖"        # Hourglass
    CLOCK = "🕐"           # Clock
    PROGRESS_DOT = "●"     # Progress indicator
    EMPTY_DOT = "○"        # Empty progress indicator

class GeometricPattern(Enum):
    """Types of geometric patterns for different contexts."""
    
    FIBONACCI_SPIRAL = "fibonacci_spiral"
    FLOWER_OF_LIFE = "flower_of_life"
    GOLDEN_RATIO_GRID = "golden_ratio_grid"
    CONSCIOUSNESS_MANDALA = "consciousness_mandala"
    BIOFIELD_GRID = "biofield_grid"
    NEURAL_NETWORK = "neural_network"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS VISUALIZATION PATTERNS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessVisualization:
    """
    ASCII art patterns for consciousness state visualization.
    
    Provides beautiful terminal-based visualizations of consciousness states,
    biofield patterns, and sacred geometry aligned with neural entrainment work.
    """
    
    def __init__(self, unicode_support: bool = True):
        self.unicode_support = unicode_support
        self.symbols = SacredGeometrySymbols()
        
    def create_consciousness_journey_line(self, 
                                        states: List[str], 
                                        current_index: int = 0,
                                        width: int = 60) -> List[str]:
        """
        Create a horizontal consciousness journey visualization.
        
        Args:
            states: List of consciousness states
            current_index: Index of current state
            width: Total width of the visualization
            
        Returns:
            List of strings forming the visualization
        """
        if not states:
            return ["No journey defined"]
            
        # State symbols mapping
        state_symbols = {
            'deep_delta': '●',    # Deep circle
            'delta': '●',         # Circle
            'theta': '◆',         # Diamond
            'alpha': '△',         # Triangle
            'beta': '■',          # Square
            'gamma': '★',         # Star
            'integration': '※'    # Special resonance symbol
        }
        
        # Create the journey line
        lines = []
        
        # Calculate spacing
        if len(states) <= 1:
            spacing = width
        else:
            spacing = max(2, width // (len(states) - 1))
        
        # Top line with state names
        top_line = ""
        for i, state in enumerate(states):
            symbol = state_symbols.get(state.lower(), '○')
            if i == current_index:
                symbol = f"[{symbol}]"  # Highlight current state
            else:
                symbol = f" {symbol} "
            
            if i == 0:
                top_line += symbol
            else:
                padding = spacing - len(symbol)
                top_line += "━" * max(0, padding) + symbol
        
        lines.append(top_line)
        
        # Connection line
        connection_line = ""
        for i in range(len(states)):
            if i == 0:
                connection_line += "   "
            elif i <= current_index:
                connection_line += "━━━"  # Completed connection
            else:
                connection_line += "╌╌╌"  # Future connection (dashed)
            
            if i < len(states) - 1:
                connection_line += "●" if i < current_index else "○"
        
        lines.append(connection_line)
        
        # State labels line
        label_line = ""
        for i, state in enumerate(states):
            state_display = state.replace('_', ' ').title()
            if i == current_index:
                state_display = f"→{state_display}←"
            
            if i == 0:
                label_line += state_display[:8].center(8)
            else:
                padding = spacing - 8
                label_line += " " * max(0, padding) + state_display[:8].center(8)
        
        lines.append(label_line)
        
        return lines
    
    def create_biofield_coherence_display(self, 
                                         coherence_data: Dict[str, float],
                                         width: int = 40) -> List[str]:
        """
        Create biofield coherence visualization.
        
        Args:
            coherence_data: Dict with biofield coherence values (0.0-1.0)
            width: Width of the display
            
        Returns:
            List of strings forming the biofield display
        """
        lines = []
        
        # Header
        lines.append("🌊 Biofield Coherence".center(width))
        lines.append("═" * width)
        
        # Coherence meters
        for field_type, value in coherence_data.items():
            # Create progress bar
            bar_width = width - 15
            filled = int(value * bar_width)
            empty = bar_width - filled
            
            # Choose symbol based on field type
            if field_type.lower() in ['schumann', 'earth']:
                symbol = '🌍'
                bar_char = '▓'
            elif field_type.lower() == 'solfeggio':
                symbol = '🎵'
                bar_char = '♫'
            elif field_type.lower() in ['golden_ratio', 'phi']:
                symbol = 'Φ'
                bar_char = '◆'
            else:
                symbol = '○'
                bar_char = '█'
            
            bar = bar_char * filled + '░' * empty
            percentage = f"{value:.0%}"
            
            line = f"{symbol} {field_type[:8]:<8} [{bar}] {percentage:>4}"
            lines.append(line)
        
        return lines
    
    def create_safety_monitoring_panel(self,
                                     neural_load: float,
                                     comfort_level: float,
                                     safety_status: str,
                                     width: int = 35) -> List[str]:
        """
        Create safety monitoring panel.
        
        Args:
            neural_load: Neural processing load (0.0-1.0)
            comfort_level: User comfort level (0.0-1.0)
            safety_status: Current safety status
            width: Width of the panel
            
        Returns:
            List of strings forming the safety panel
        """
        lines = []
        
        # Header with safety symbol
        safety_symbol = "🛡️" if safety_status.lower() == 'safe' else "⚠️"
        lines.append(f"{safety_symbol} Safety Monitor".center(width))
        lines.append("━" * width)
        
        # Neural load indicator
        load_bar_width = width - 12
        load_filled = int(neural_load * load_bar_width)
        load_empty = load_bar_width - load_filled
        
        if neural_load < 0.3:
            load_char, load_color = '▓', '💚'
        elif neural_load < 0.7:
            load_char, load_color = '▒', '💛'
        else:
            load_char, load_color = '█', '🔥'
        
        load_bar = load_char * load_filled + '░' * load_empty
        lines.append(f"🧠 Load: [{load_bar}] {neural_load:.0%}")
        
        # Comfort level indicator
        comfort_filled = int(comfort_level * load_bar_width)
        comfort_empty = load_bar_width - comfort_filled
        
        if comfort_level > 0.7:
            comfort_char, comfort_symbol = '♥', '😌'
        elif comfort_level > 0.4:
            comfort_char, comfort_symbol = '▓', '😐'
        else:
            comfort_char, comfort_symbol = '▒', '😓'
        
        comfort_bar = comfort_char * comfort_filled + '░' * comfort_empty
        lines.append(f"{comfort_symbol} Comfort: [{comfort_bar}] {comfort_level:.0%}")
        
        # Safety status
        status_line = f"Status: {safety_status.upper()}"
        lines.append(status_line.center(width))
        
        return lines
    
    def create_golden_ratio_pattern(self, size: int = 21) -> List[str]:
        """
        Create a golden ratio spiral pattern using ASCII art.
        
        Args:
            size: Size of the pattern (should be odd for centering)
            
        Returns:
            List of strings forming the spiral pattern
        """
        lines = []
        center = size // 2
        
        for y in range(size):
            line = ""
            for x in range(size):
                # Calculate distance from center
                dx = x - center
                dy = y - center
                distance = math.sqrt(dx*dx + dy*dy)
                
                # Calculate angle for spiral effect
                if distance > 0:
                    angle = math.atan2(dy, dx) + distance * 0.5
                    spiral_value = math.sin(angle) * math.exp(-distance/10)
                else:
                    spiral_value = 1.0
                
                # Choose character based on spiral value and distance
                if distance <= 1:
                    char = "◉"  # Center
                elif distance <= 3 and spiral_value > 0.3:
                    char = "◆"  
                elif distance <= 6 and spiral_value > 0.1:
                    char = "◊"
                elif distance <= 10 and spiral_value > -0.1:
                    char = "·"
                else:
                    char = " "
                
                line += char
            
            lines.append(line)
        
        return lines
    
    def create_consciousness_mandala(self, radius: int = 8) -> List[str]:
        """
        Create a consciousness mandala pattern.
        
        Args:
            radius: Radius of the mandala
            
        Returns:
            List of strings forming the mandala
        """
        size = radius * 2 + 1
        lines = []
        center = radius
        
        for y in range(size):
            line = ""
            for x in range(size):
                dx = x - center
                dy = y - center
                distance = math.sqrt(dx*dx + dy*dy)
                
                # Create layered mandala effect
                if distance <= 1:
                    char = "◉"  # Center - source consciousness
                elif distance <= 2:
                    char = "◆"  # First ring - awareness
                elif distance <= 4:
                    angle = math.atan2(dy, dx)
                    segment = int((angle + math.pi) / (math.pi / 4)) % 8
                    char = "◊" if segment % 2 == 0 else "○"  # Alternating pattern
                elif distance <= 6:
                    char = "·" if (x + y) % 2 == 0 else " "  # Outer ring
                elif distance <= radius:
                    char = "." if (x + y) % 3 == 0 else " "  # Edge energy
                else:
                    char = " "
                
                line += char
            
            lines.append(line)
        
        return lines
    
    def create_neural_network_pattern(self, width: int = 30, height: int = 10) -> List[str]:
        """
        Create a neural network connection pattern.
        
        Args:
            width: Width of the pattern
            height: Height of the pattern
            
        Returns:
            List of strings forming the neural network
        """
        lines = []
        
        # Create nodes at specific positions
        nodes = [
            (5, 2), (10, 1), (15, 3), (20, 2), (25, 1),
            (3, 5), (8, 6), (13, 5), (18, 7), (23, 6),
            (6, 8), (11, 9), (16, 8), (21, 9), (26, 8)
        ]
        
        # Initialize grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Place nodes
        for x, y in nodes:
            if 0 <= x < width and 0 <= y < height:
                grid[y][x] = '●'
        
        # Add connections (simplified)
        for i, (x1, y1) in enumerate(nodes):
            for j, (x2, y2) in enumerate(nodes[i+1:], i+1):
                if abs(x1 - x2) <= 8 and abs(y1 - y2) <= 3:
                    # Draw simplified connection
                    mid_x = (x1 + x2) // 2
                    mid_y = (y1 + y2) // 2
                    if 0 <= mid_x < width and 0 <= mid_y < height and grid[mid_y][mid_x] == ' ':
                        grid[mid_y][mid_x] = '─' if abs(y1 - y2) <= 1 else '│'
        
        # Convert grid to strings
        for row in grid:
            lines.append(''.join(row))
        
        return lines
    
    def create_frequency_spectrum(self, 
                                frequencies: Dict[str, float], 
                                width: int = 50,
                                max_height: int = 8) -> List[str]:
        """
        Create a frequency spectrum visualization.
        
        Args:
            frequencies: Dict of frequency names and their amplitudes (0.0-1.0)
            width: Width of the spectrum
            max_height: Maximum height of the bars
            
        Returns:
            List of strings forming the spectrum
        """
        if not frequencies:
            return ["No frequency data"]
        
        lines = []
        freq_names = list(frequencies.keys())
        freq_values = list(frequencies.values())
        
        # Calculate bar width
        bar_width = max(1, width // len(freq_names))
        
        # Create spectrum from top to bottom
        for level in range(max_height, 0, -1):
            line = ""
            for i, (name, value) in enumerate(zip(freq_names, freq_values)):
                bar_height = int(value * max_height)
                
                if bar_height >= level:
                    # Choose character based on frequency type and level
                    if 'schumann' in name.lower():
                        char = '🌍' if level == bar_height else '█'
                    elif 'solfeggio' in name.lower():
                        char = '♫' if level == bar_height else '▓'
                    elif any(keyword in name.lower() for keyword in ['golden', 'phi']):
                        char = 'Φ' if level == bar_height else '◆'
                    else:
                        char = '█'
                else:
                    char = ' '
                
                # Repeat character for bar width
                line += char * bar_width
                
                # Add separator
                if i < len(freq_names) - 1:
                    line += ' '
            
            lines.append(line)
        
        # Add frequency labels at bottom
        label_line = ""
        for i, name in enumerate(freq_names):
            label = name[:bar_width]
            if i == 0:
                label_line += label.center(bar_width)
            else:
                label_line += ' ' + label.center(bar_width)
        
        lines.append('─' * len(label_line))
        lines.append(label_line)
        
        return lines

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS BORDER AND FRAME PATTERNS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessBorders:
    """Beautiful border patterns for consciousness-aware interface elements."""
    
    @staticmethod
    def create_simple_border(width: int, height: int, style: str = "single") -> List[str]:
        """Create a simple rectangular border."""
        
        if style == "double":
            h_line, v_line = "═", "║"
            corners = ["╔", "╗", "╚", "╝"]
        elif style == "rounded":
            h_line, v_line = "─", "│"
            corners = ["╭", "╮", "╰", "╯"]
        else:  # single
            h_line, v_line = "─", "│"
            corners = ["┌", "┐", "└", "┘"]
        
        lines = []
        
        # Top border
        lines.append(corners[0] + h_line * (width - 2) + corners[1])
        
        # Side borders
        for _ in range(height - 2):
            lines.append(v_line + " " * (width - 2) + v_line)
        
        # Bottom border
        lines.append(corners[2] + h_line * (width - 2) + corners[3])
        
        return lines
    
    @staticmethod
    def create_consciousness_frame(title: str, content: List[str], 
                                 width: Optional[int] = None) -> List[str]:
        """Create a consciousness-aware frame with title."""
        
        # Calculate width if not provided
        if width is None:
            max_content_width = max(len(line) for line in content) if content else 20
            title_width = len(title) + 4
            width = max(max_content_width + 4, title_width, 30)
        
        lines = []
        
        # Top border with title
        title_line = f"╔══ {title} ═══"
        title_line += "═" * (width - len(title_line) - 1) + "╗"
        lines.append(title_line)
        
        # Content lines
        for line in content:
            padded_line = f"║ {line:<{width-4}} ║"
            lines.append(padded_line)
        
        # Bottom border
        lines.append("╚" + "═" * (width - 2) + "╝")
        
        return lines
    
    @staticmethod
    def create_sacred_geometry_border(width: int, height: int) -> List[str]:
        """Create a border using sacred geometry patterns."""
        
        lines = []
        symbols = SacredGeometrySymbols()
        
        # Top border with sacred symbols
        top_pattern = [symbols.PHI, symbols.DIAMOND, symbols.INFINITY, symbols.STAR]
        top_line = ""
        for i in range(width):
            symbol_index = i % len(top_pattern)
            top_line += top_pattern[symbol_index]
        lines.append(top_line[:width])
        
        # Side borders
        side_pattern = [symbols.FILLED_CIRCLE, symbols.CIRCLE, symbols.DIAMOND, symbols.TRIANGLE_UP]
        for row in range(height - 2):
            left_symbol = side_pattern[row % len(side_pattern)]
            right_symbol = side_pattern[(row + 2) % len(side_pattern)]
            middle = " " * (width - 2)
            lines.append(left_symbol + middle + right_symbol)
        
        # Bottom border (mirrored top)
        bottom_pattern = list(reversed(top_pattern))
        bottom_line = ""
        for i in range(width):
            symbol_index = i % len(bottom_pattern)
            bottom_line += bottom_pattern[symbol_index]
        lines.append(bottom_line[:width])
        
        return lines

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# UTILITY FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def get_consciousness_symbol(state: str) -> str:
    """Get appropriate symbol for consciousness state."""
    
    symbols = SacredGeometrySymbols()
    
    symbol_mapping = {
        'deep_delta': symbols.FILLED_CIRCLE,
        'delta': symbols.CIRCLE,
        'theta': symbols.DIAMOND,
        'alpha': symbols.TRIANGLE_UP,
        'beta': symbols.SQUARE,
        'gamma': symbols.STAR,
        'integration': symbols.RESONANCE
    }
    
    return symbol_mapping.get(state.lower(), symbols.CIRCLE)

def get_biofield_symbol(field_type: str) -> str:
    """Get appropriate symbol for biofield type."""
    
    symbols = SacredGeometrySymbols()
    
    biofield_mapping = {
        'schumann': symbols.EARTH,
        'solfeggio': symbols.SOUND_WAVE,
        'golden_ratio': symbols.PHI,
        'phi': symbols.PHI_LOWER,
        'frequency': symbols.FREQUENCY
    }
    
    return biofield_mapping.get(field_type.lower(), symbols.RESONANCE)

def create_loading_animation(frame: int, style: str = "consciousness") -> str:
    """Create consciousness-aware loading animation frame."""
    
    symbols = SacredGeometrySymbols()
    
    if style == "consciousness":
        frames = [symbols.CIRCLE, symbols.FILLED_CIRCLE, symbols.DIAMOND, symbols.STAR]
        return frames[frame % len(frames)]
    elif style == "spiral":
        frames = ["◐", "◓", "◑", "◒"]
        return frames[frame % len(frames)]
    elif style == "biofield":
        frames = [symbols.EARTH, symbols.SOUND_WAVE, symbols.PHI, symbols.RESONANCE]
        return frames[frame % len(frames)]
    else:
        return "◌"

def create_consciousness_separator(width: int, style: str = "wave") -> str:
    """Create consciousness-aware separator line."""
    
    symbols = SacredGeometrySymbols()
    
    if style == "wave":
        return "∿" * (width // 2)
    elif style == "sacred":
        pattern = f"{symbols.PHI}{symbols.DIAMOND}{symbols.INFINITY}"
        return (pattern * (width // len(pattern) + 1))[:width]
    elif style == "simple":
        return "─" * width
    else:
        return "═" * width