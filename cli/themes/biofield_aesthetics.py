# 🧠 Neural Entrainment System v2.0 - Biofield Aesthetics
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Biofield Aesthetics - Visual patterns aligned with biofield intelligence principles.

This module creates beautiful terminal visualizations that resonate with natural 
frequencies, sacred geometry, and biofield coherence patterns. All aesthetics
are designed to support consciousness work and neural entrainment visualization.
"""

import math
import time
from typing import List, Dict, Tuple, Optional
from enum import Enum
from .sacred_geometry import SacredGeometrySymbols, ConsciousnessVisualization
from .consciousness_colors import ConsciousnessColorScheme

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BIOFIELD FREQUENCY CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Golden Ratio and Sacred Mathematics
PHI = 1.618033988749894
PHI_SQUARED = PHI * PHI
PHI_INVERSE = 1 / PHI

# Schumann Resonance Frequencies (Hz)
SCHUMANN_FUNDAMENTAL = 7.83
SCHUMANN_HARMONICS = [7.83, 14.3, 20.8, 27.3, 33.8, 39.3, 45.9, 52.8]

# Solfeggio Frequencies (Hz)
SOLFEGGIO_FREQUENCIES = {
    'UT': 174,    # Foundation, security, grounding
    'RE': 285,    # Healing, regeneration
    'MI': 396,    # Liberation from fear and guilt
    'FA': 417,    # Change, transformation
    'SOL': 528,   # Love, DNA repair, miracles
    'LA': 639,    # Connection, relationships
    'TI': 741,    # Awakening intuition
    'SI': 852,    # Spiritual order
    'SO': 963     # Unity consciousness
}

# Natural Frequency Ratios
NATURAL_RATIOS = [
    1.0,          # Unison
    PHI,          # Golden ratio
    1.5,          # Perfect fifth
    2.0,          # Octave
    PHI_SQUARED,  # Golden ratio squared
    3.0,          # Perfect twelfth
]

class BiofieldPattern(Enum):
    """Types of biofield visualization patterns."""
    
    SCHUMANN_WAVE = "schumann_wave"
    SOLFEGGIO_SPECTRUM = "solfeggio_spectrum"
    GOLDEN_RATIO_SPIRAL = "golden_ratio_spiral"
    COHERENCE_FIELD = "coherence_field"
    RESONANCE_MANDALA = "resonance_mandala"
    FREQUENCY_HARMONICS = "frequency_harmonics"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BIOFIELD VISUALIZATION SYSTEM
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class BiofieldAesthetics:
    """
    Biofield-aligned visual aesthetics for consciousness-aware CLI interface.
    
    This class creates beautiful terminal visualizations based on natural frequency
    patterns, sacred geometry, and biofield coherence principles that support
    consciousness work and neural entrainment visualization.
    """
    
    def __init__(self, 
                 color_scheme: Optional[ConsciousnessColorScheme] = None,
                 unicode_support: bool = True):
        self.color_scheme = color_scheme or ConsciousnessColorScheme()
        self.unicode_support = unicode_support
        self.symbols = SacredGeometrySymbols()
        self.consciousness_viz = ConsciousnessVisualization(unicode_support)
        
    def create_schumann_resonance_wave(self,
                                     resonance_strength: float = 1.0,
                                     width: int = 60,
                                     height: int = 8) -> List[str]:
        """
        Create Schumann resonance wave visualization.
        
        Args:
            resonance_strength: Strength of resonance (0.0-1.0)
            width: Width of the visualization
            height: Height of the visualization
            
        Returns:
            List of strings forming the wave pattern
        """
        lines = []
        
        # Create wave pattern based on Schumann fundamental frequency
        center_line = height // 2
        
        for y in range(height):
            line = ""
            for x in range(width):
                # Calculate wave position based on Schumann resonance
                wave_position = (x / width) * 4 * math.pi  # Two complete wavelengths
                amplitude = (height // 2 - 1) * resonance_strength
                
                # Primary Schumann wave (7.83 Hz representation)
                primary_wave = math.sin(wave_position) * amplitude
                
                # Add harmonic for richness (14.3 Hz harmonic)
                harmonic_wave = math.sin(wave_position * 1.83) * amplitude * 0.3
                
                combined_wave = primary_wave + harmonic_wave
                wave_y = center_line + int(combined_wave)
                
                # Choose character based on wave strength and position
                if y == wave_y:
                    if resonance_strength > 0.8:
                        char = '🌍'  # Strong Earth connection
                    elif resonance_strength > 0.5:
                        char = '●'   # Moderate connection
                    else:
                        char = '○'   # Weak connection
                elif abs(y - wave_y) == 1 and resonance_strength > 0.6:
                    char = '·'   # Wave aura
                else:
                    char = ' '
                
                line += char
            
            lines.append(line)
        
        # Add header with Schumann frequency info
        header = f"🌍 Schumann Resonance: {SCHUMANN_FUNDAMENTAL}Hz (Strength: {resonance_strength:.1%})"
        lines.insert(0, header.center(width))
        lines.insert(1, "∿" * width)
        
        return lines
    
    def create_solfeggio_spectrum(self,
                                active_frequencies: Dict[str, float],
                                width: int = 50,
                                height: int = 12) -> List[str]:
        """
        Create Solfeggio frequency spectrum visualization.
        
        Args:
            active_frequencies: Dict of Solfeggio frequencies and their levels
            width: Width of the spectrum
            height: Height of the spectrum
            
        Returns:
            List of strings forming the spectrum
        """
        lines = []
        
        # Get all Solfeggio frequencies
        solfeggio_keys = list(SOLFEGGIO_FREQUENCIES.keys())
        bar_width = max(1, width // len(solfeggio_keys))
        
        # Header
        header = "🎵 Solfeggio Frequency Spectrum"
        lines.append(header.center(width))
        lines.append("═" * width)
        
        # Create spectrum bars from top to bottom
        spectrum_height = height - 4  # Reserve space for header and labels
        
        for level in range(spectrum_height, 0, -1):
            line = ""
            for freq_key in solfeggio_keys:
                frequency_level = active_frequencies.get(freq_key, 0.0)
                bar_height = int(frequency_level * spectrum_height)
                
                # Choose visualization character based on frequency and level
                if bar_height >= level:
                    if freq_key in ['UT', 'RE']:
                        char = '▓'  # Grounding frequencies
                    elif freq_key in ['MI', 'FA']:
                        char = '▒'  # Transformational frequencies  
                    elif freq_key == 'SOL':
                        char = '♥'  # Love frequency (528 Hz)
                    elif freq_key in ['LA', 'TI']:
                        char = '◆'  # Higher consciousness frequencies
                    elif freq_key in ['SI', 'SO']:
                        char = '✦'  # Transcendent frequencies
                    else:
                        char = '█'
                        
                    # Add some sparkle at peak levels
                    if level == bar_height and frequency_level > 0.8:
                        char = '✨'
                else:
                    char = ' '
                
                # Fill bar width
                line += char * bar_width
                
                # Add separator between frequencies
                if freq_key != solfeggio_keys[-1]:
                    line += ' '
            
            lines.append(line)
        
        # Add frequency labels
        label_line = ""
        value_line = ""
        
        for freq_key in solfeggio_keys:
            frequency = SOLFEGGIO_FREQUENCIES[freq_key]
            level = active_frequencies.get(freq_key, 0.0)
            
            # Frequency name label
            label = freq_key.center(bar_width)
            label_line += label
            
            # Frequency value
            if bar_width >= 4:
                value = f"{frequency}Hz".center(bar_width)
            else:
                value = str(frequency)[:bar_width].center(bar_width)
            value_line += value
            
            # Add separators
            if freq_key != solfeggio_keys[-1]:
                label_line += ' '
                value_line += ' '
        
        lines.append('─' * width)
        lines.append(label_line)
        lines.append(value_line)
        
        return lines
    
    def create_golden_ratio_coherence(self,
                                    coherence_level: float = 1.0,
                                    size: int = 15) -> List[str]:
        """
        Create golden ratio coherence visualization.
        
        Args:
            coherence_level: Level of golden ratio coherence (0.0-1.0)
            size: Size of the visualization
            
        Returns:
            List of strings forming the golden ratio pattern
        """
        lines = []
        center = size // 2
        
        # Header
        header = f"Φ Golden Ratio Coherence: {coherence_level:.1%}"
        lines.append(header)
        lines.append("◆" * len(header))
        
        # Create golden ratio spiral pattern
        for y in range(size):
            line = ""
            for x in range(size):
                dx = x - center
                dy = y - center
                distance = math.sqrt(dx*dx + dy*dy)
                
                if distance == 0:
                    char = "Φ"  # Center - golden ratio source
                else:
                    # Calculate spiral based on golden ratio
                    angle = math.atan2(dy, dx)
                    spiral_distance = distance * PHI_INVERSE
                    spiral_angle = angle + spiral_distance * 0.618
                    
                    # Golden ratio harmonic pattern
                    harmonic = math.sin(spiral_angle * PHI) * coherence_level
                    
                    # Choose character based on harmonic strength and distance
                    if distance <= 2 and harmonic > 0.5:
                        char = "◉"
                    elif distance <= 4 and harmonic > 0.3:
                        char = "◆"
                    elif distance <= 6 and harmonic > 0.1:
                        char = "◊"
                    elif distance <= 8 and harmonic > -0.1:
                        char = "·"
                    else:
                        char = " "
                
                line += char
            
            lines.append(line)
        
        return lines
    
    def create_biofield_coherence_mandala(self,
                                       coherence_data: Dict[str, float],
                                       size: int = 21) -> List[str]:
        """
        Create comprehensive biofield coherence mandala.
        
        Args:
            coherence_data: Dict of biofield types and their coherence levels
            size: Size of the mandala
            
        Returns:
            List of strings forming the biofield mandala
        """
        lines = []
        center = size // 2
        
        # Header
        header = "🌊 Biofield Coherence Mandala"
        lines.append(header.center(size * 2))
        lines.append("═" * (size * 2))
        
        for y in range(size):
            line = ""
            for x in range(size):
                dx = x - center
                dy = y - center
                distance = math.sqrt(dx*dx + dy*dy)
                angle = math.atan2(dy, dx)
                
                # Create layered mandala based on different biofield types
                char = " "
                
                if distance <= 1:
                    char = "◉"  # Center - unified biofield
                elif distance <= 3:
                    # Inner ring - Schumann resonance
                    schumann_coherence = coherence_data.get('schumann', 0.0)
                    if schumann_coherence > 0.7:
                        char = "🌍"
                    elif schumann_coherence > 0.4:
                        char = "●"
                    else:
                        char = "○"
                elif distance <= 6:
                    # Middle ring - Solfeggio frequencies
                    solfeggio_coherence = coherence_data.get('solfeggio', 0.0)
                    segment = int((angle + math.pi) / (math.pi / 4)) % 8
                    
                    if solfeggio_coherence > 0.8:
                        char = "♫"
                    elif solfeggio_coherence > 0.5:
                        char = "♪" if segment % 2 == 0 else "♫"
                    elif solfeggio_coherence > 0.2:
                        char = "·"
                    else:
                        char = " "
                elif distance <= 9:
                    # Outer ring - Golden ratio harmonics
                    golden_coherence = coherence_data.get('golden_ratio', 0.0)
                    
                    # Golden ratio spiral pattern
                    spiral_angle = angle + distance * PHI_INVERSE
                    spiral_strength = math.sin(spiral_angle) * golden_coherence
                    
                    if spiral_strength > 0.6:
                        char = "Φ"
                    elif spiral_strength > 0.3:
                        char = "φ"
                    elif spiral_strength > 0.0:
                        char = "◊"
                    else:
                        char = " "
                elif distance <= center:
                    # Edge energy pattern
                    overall_coherence = sum(coherence_data.values()) / len(coherence_data)
                    if overall_coherence > 0.6 and (x + y) % 3 == 0:
                        char = "·"
                
                line += char
            
            lines.append(line)
        
        # Add coherence summary
        lines.append("─" * (size * 2))
        for field_type, coherence in coherence_data.items():
            symbol = {
                'schumann': '🌍',
                'solfeggio': '🎵', 
                'golden_ratio': 'Φ'
            }.get(field_type, '○')
            
            coherence_bar = self.color_scheme.create_progress_bar(coherence, 15)
            summary_line = f"{symbol} {field_type}: {coherence_bar}"
            lines.append(summary_line)
        
        return lines
    
    def create_frequency_harmony_display(self,
                                       frequency_data: Dict[str, Dict[str, float]],
                                       width: int = 60) -> List[str]:
        """
        Create frequency harmony visualization showing relationships.
        
        Args:
            frequency_data: Nested dict of frequency categories and their values
            width: Width of the display
            
        Returns:
            List of strings forming the harmony display
        """
        lines = []
        
        # Header
        header = "🎼 Frequency Harmony Matrix"
        lines.append(header.center(width))
        lines.append("♫" * width)
        
        # Process each frequency category
        for category, frequencies in frequency_data.items():
            # Category header
            category_symbol = {
                'schumann': '🌍',
                'solfeggio': '🎵',
                'golden_ratio': 'Φ',
                'natural': '🌿'
            }.get(category.lower(), '○')
            
            category_line = f"{category_symbol} {category.upper()} FREQUENCIES"
            lines.append(category_line.center(width))
            
            # Frequency bars
            for freq_name, freq_value in frequencies.items():
                # Create harmony indicator
                bar_width = width - 20
                filled = int(freq_value * bar_width)
                empty = bar_width - filled
                
                # Choose pattern based on frequency value
                if freq_value > 0.8:
                    fill_char = '█'
                    harmony_symbol = '✨'
                elif freq_value > 0.6:
                    fill_char = '▓'
                    harmony_symbol = '♫'
                elif freq_value > 0.4:
                    fill_char = '▒'
                    harmony_symbol = '♪'
                elif freq_value > 0.2:
                    fill_char = '░'
                    harmony_symbol = '·'
                else:
                    fill_char = '.'
                    harmony_symbol = ' '
                
                bar = fill_char * filled + '.' * empty
                freq_line = f"{harmony_symbol} {freq_name[:8]:<8} [{bar}] {freq_value:.1%}"
                lines.append(freq_line)
            
            lines.append("")  # Spacing between categories
        
        # Overall harmony assessment
        all_values = []
        for frequencies in frequency_data.values():
            all_values.extend(frequencies.values())
        
        if all_values:
            overall_harmony = sum(all_values) / len(all_values)
            harmony_assessment = self._get_harmony_assessment(overall_harmony)
            
            lines.append("═" * width)
            lines.append(f"Overall Harmony: {overall_harmony:.1%} - {harmony_assessment}".center(width))
        
        return lines
    
    def create_consciousness_resonance_field(self,
                                           resonance_data: Dict[str, float],
                                           field_size: int = 25) -> List[str]:
        """
        Create consciousness resonance field visualization.
        
        Args:
            resonance_data: Dict of resonance types and their strengths
            field_size: Size of the field visualization
            
        Returns:
            List of strings forming the resonance field
        """
        lines = []
        center = field_size // 2
        
        # Header
        header = "∞ Consciousness Resonance Field ∞"
        lines.append(header.center(field_size * 2))
        
        for y in range(field_size):
            line = ""
            for x in range(field_size):
                dx = x - center
                dy = y - center
                distance = math.sqrt(dx*dx + dy*dy)
                angle = math.atan2(dy, dx)
                
                # Calculate resonance field strength at this point
                total_resonance = 0
                for resonance_type, strength in resonance_data.items():
                    # Different resonance types create different field patterns
                    if resonance_type == 'theta':
                        # Theta creates gentle spiral patterns
                        theta_angle = angle + distance * 0.3
                        theta_resonance = math.sin(theta_angle) * strength
                        total_resonance += theta_resonance * 0.4
                    elif resonance_type == 'alpha':
                        # Alpha creates bridge wave patterns
                        alpha_wave = math.sin(distance * 0.5) * strength
                        total_resonance += alpha_wave * 0.3
                    elif resonance_type == 'gamma':
                        # Gamma creates high-frequency oscillations
                        gamma_freq = math.sin(distance * 1.5 + angle * 3) * strength
                        total_resonance += gamma_freq * 0.2
                    elif resonance_type == 'delta':
                        # Delta creates deep, slow waves
                        delta_wave = math.sin(distance * 0.2) * strength
                        total_resonance += delta_wave * 0.1
                
                # Normalize and choose visualization character
                normalized_resonance = max(0, min(1, total_resonance + 0.5))
                
                if distance <= 1:
                    char = "◉"  # Center consciousness point
                elif normalized_resonance > 0.9:
                    char = "✧"  # High resonance
                elif normalized_resonance > 0.7:
                    char = "◆"  # Strong resonance
                elif normalized_resonance > 0.5:
                    char = "◊"  # Moderate resonance
                elif normalized_resonance > 0.3:
                    char = "○"  # Mild resonance
                elif normalized_resonance > 0.1:
                    char = "·"  # Weak resonance
                else:
                    char = " "  # No resonance
                
                line += char
            
            lines.append(line)
        
        return lines
    
    def _get_harmony_assessment(self, harmony_level: float) -> str:
        """Get textual assessment of harmony level."""
        
        if harmony_level > 0.9:
            return "Transcendent Harmony"
        elif harmony_level > 0.8:
            return "Deep Coherence" 
        elif harmony_level > 0.7:
            return "Strong Alignment"
        elif harmony_level > 0.6:
            return "Good Resonance"
        elif harmony_level > 0.5:
            return "Emerging Harmony"
        elif harmony_level > 0.3:
            return "Seeking Balance"
        else:
            return "Foundational Phase"
    
    def create_animated_biofield_frame(self,
                                     frame_number: int,
                                     coherence_level: float = 1.0,
                                     width: int = 40,
                                     height: int = 10) -> List[str]:
        """
        Create animated biofield frame for real-time display.
        
        Args:
            frame_number: Animation frame number
            coherence_level: Overall biofield coherence level
            width: Width of the frame
            height: Height of the frame
            
        Returns:
            List of strings forming the animated frame
        """
        lines = []
        
        # Create animated wave pattern
        time_offset = frame_number * 0.1
        
        for y in range(height):
            line = ""
            for x in range(width):
                # Multi-layered wave animation
                primary_wave = math.sin((x / width) * 4 * math.pi + time_offset)
                secondary_wave = math.sin((x / width) * 6 * math.pi + time_offset * 1.5)
                tertiary_wave = math.sin((x / width) * 8 * math.pi - time_offset * 0.7)
                
                combined_wave = (primary_wave + secondary_wave * 0.5 + tertiary_wave * 0.3) * coherence_level
                
                wave_intensity = (combined_wave + 1) / 2  # Normalize to 0-1
                
                # Choose character based on wave intensity
                if wave_intensity > 0.9:
                    char = "◉"
                elif wave_intensity > 0.8:
                    char = "●"
                elif wave_intensity > 0.6:
                    char = "◆"
                elif wave_intensity > 0.4:
                    char = "◊"
                elif wave_intensity > 0.2:
                    char = "·"
                else:
                    char = " "
                
                line += char
            
            lines.append(line)
        
        return lines

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BIOFIELD AESTHETIC UTILITIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def get_biofield_pattern(pattern_type: BiofieldPattern,
                        data: Dict[str, float],
                        size: int = 20) -> List[str]:
    """
    Get biofield pattern visualization.
    
    Args:
        pattern_type: Type of biofield pattern to create
        data: Biofield data for visualization
        size: Size of the pattern
        
    Returns:
        List of strings forming the pattern
    """
    aesthetics = BiofieldAesthetics()
    
    if pattern_type == BiofieldPattern.SCHUMANN_WAVE:
        return aesthetics.create_schumann_resonance_wave(
            resonance_strength=data.get('schumann', 0.5),
            width=size * 3,
            height=size // 2
        )
    elif pattern_type == BiofieldPattern.SOLFEGGIO_SPECTRUM:
        return aesthetics.create_solfeggio_spectrum(
            active_frequencies=data,
            width=size * 3,
            height=size
        )
    elif pattern_type == BiofieldPattern.GOLDEN_RATIO_SPIRAL:
        return aesthetics.create_golden_ratio_coherence(
            coherence_level=data.get('golden_ratio', 0.5),
            size=size
        )
    elif pattern_type == BiofieldPattern.COHERENCE_FIELD:
        return aesthetics.create_biofield_coherence_mandala(
            coherence_data=data,
            size=size
        )
    else:
        return ["Pattern not implemented"]

def calculate_biofield_harmony(frequency_data: Dict[str, float]) -> float:
    """
    Calculate overall biofield harmony from frequency data.
    
    Args:
        frequency_data: Dict of frequencies and their strengths
        
    Returns:
        Harmony level (0.0-1.0)
    """
    if not frequency_data:
        return 0.0
    
    # Weight different frequency types
    weights = {
        'schumann': 0.4,      # Earth connection - highest weight
        'solfeggio': 0.3,     # Healing frequencies - high weight
        'golden_ratio': 0.2,  # Sacred geometry - moderate weight
        'natural': 0.1        # Other natural frequencies - low weight
    }
    
    weighted_sum = 0.0
    total_weight = 0.0
    
    for freq_type, strength in frequency_data.items():
        weight = weights.get(freq_type, 0.1)
        weighted_sum += strength * weight
        total_weight += weight
    
    return weighted_sum / total_weight if total_weight > 0 else 0.0

def create_biofield_status_line(biofield_data: Dict[str, float],
                              width: int = 60) -> str:
    """
    Create single-line biofield status display.
    
    Args:
        biofield_data: Biofield coherence data
        width: Width of the status line
        
    Returns:
        Formatted status line string
    """
    symbols = SacredGeometrySymbols()
    
    # Calculate overall coherence
    overall_coherence = sum(biofield_data.values()) / len(biofield_data)
    
    # Create compact display
    status_parts = []
    
    for field_type, coherence in biofield_data.items():
        if field_type == 'schumann':
            symbol = '🌍'
        elif field_type == 'solfeggio':
            symbol = '♫'
        elif field_type == 'golden_ratio':
            symbol = symbols.PHI
        else:
            symbol = '○'
        
        # Create mini bar
        bar_chars = int(coherence * 3)
        mini_bar = '█' * bar_chars + '░' * (3 - bar_chars)
        status_parts.append(f"{symbol}[{mini_bar}]")
    
    status_line = " ".join(status_parts)
    coherence_text = f"Overall: {overall_coherence:.1%}"
    
    # Center the complete status line
    complete_status = f"{status_line} | {coherence_text}"
    return complete_status.center(width)