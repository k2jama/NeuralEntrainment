#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Biofield Display UI Component
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Biofield Display UI Component - Beautiful biofield intelligence visualization.

This module provides sophisticated biofield intelligence visualization including:
- Real-time biofield coherence display with wave patterns
- Schumann resonance alignment visualization
- Solfeggio frequency integration display
- Golden ratio harmonic visualization
- Natural frequency boost indicators
- Biofield flow animations and energy patterns
"""

import time
import math
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime

from ..themes.consciousness_colors import ConsciousnessColorScheme
from ..themes.sacred_geometry import SacredGeometrySymbols, ConsciousnessVisualization
from ..themes.biofield_aesthetics import BiofieldAesthetics
from ...src.interfaces.cli_interface import TerminalConsciousnessAdapter

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BIOFIELD INTELLIGENCE CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SCHUMANN_RESONANCE_FREQUENCIES = [7.83, 14.3, 20.8, 27.3, 33.8]
SOLFEGGIO_FREQUENCIES = {
    '174_Hz': {'name': 'Foundation', 'color': 'foundation'},
    '285_Hz': {'name': 'Quantum Cognition', 'color': 'quantum'},
    '396_Hz': {'name': 'Liberation', 'color': 'liberation'},
    '417_Hz': {'name': 'Transformation', 'color': 'transformation'},
    '528_Hz': {'name': 'Love & Miracles', 'color': 'love'},
    '639_Hz': {'name': 'Harmony', 'color': 'harmony'},
    '741_Hz': {'name': 'Expression', 'color': 'expression'},
    '852_Hz': {'name': 'Intuition', 'color': 'intuition'},
    '963_Hz': {'name': 'Oneness', 'color': 'oneness'}
}

GOLDEN_RATIO = 1.618033988749895
PHI_HARMONICS = [
    GOLDEN_RATIO,
    GOLDEN_RATIO**2,
    GOLDEN_RATIO**3,
    1/GOLDEN_RATIO,
    1/(GOLDEN_RATIO**2)
]

BIOFIELD_COHERENCE_LEVELS = {
    'chaotic': {'range': (0.0, 0.3), 'symbol': '∿', 'pattern': 'chaotic'},
    'emerging': {'range': (0.3, 0.5), 'symbol': '⌇', 'pattern': 'emerging'},
    'coherent': {'range': (0.5, 0.8), 'symbol': '∿∿', 'pattern': 'flowing'},
    'highly_coherent': {'range': (0.8, 0.95), 'symbol': '≈≈', 'pattern': 'harmonic'},
    'unified': {'range': (0.95, 1.0), 'symbol': '∞', 'pattern': 'unified'}
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BIOFIELD DISPLAY CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class BiofieldDisplay:
    """
    Beautiful biofield intelligence visualization component.
    
    This class provides real-time biofield visualization including Schumann
    resonance alignment, Solfeggio frequency integration, golden ratio harmonics,
    and natural frequency patterns in a consciousness-aware terminal interface.
    """
    
    def __init__(self, terminal_adapter: TerminalConsciousnessAdapter):
        self.terminal_adapter = terminal_adapter
        self.color_scheme = ConsciousnessColorScheme()
        self.symbols = SacredGeometrySymbols()
        self.consciousness_viz = ConsciousnessVisualization()
        self.biofield = BiofieldAesthetics()
        
        # Biofield state
        self.current_coherence = {
            'schumann': 0.7,
            'solfeggio': 0.6,
            'golden_ratio': 0.8,
            'natural_frequency': 1.0
        }
        
        # Animation state
        self.animation_frame = 0
        self.last_update = time.time()
        self.wave_phase = 0.0
        
        # Visualization cache
        self._wave_cache = {}
        self._mandala_cache = {}
    
    def show_biofield_coherence(self, coherence_data: Dict[str, float]) -> None:
        """
        Display biofield coherence levels with beautiful visualization.
        
        Args:
            coherence_data: Dict of coherence levels for different biofield aspects
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        # Update current coherence
        self.current_coherence.update(coherence_data)
        
        # Calculate overall coherence
        overall_coherence = sum(coherence_data.values()) / len(coherence_data)
        coherence_level = self._get_coherence_level(overall_coherence)
        
        print(f"\n{colors.consciousness_header('∿' * 60)}")
        print(f"{colors.consciousness_title('🌊 Biofield Intelligence Display')}")
        print(f"{colors.consciousness_header('∿' * 60)}")
        
        # Overall coherence status
        level_info = BIOFIELD_COHERENCE_LEVELS[coherence_level]
        level_symbol = level_info['symbol']
        level_pattern = level_info['pattern']
        
        print(f"\n{colors.biofield_accent('Overall Coherence:')} "
              f"{colors.biofield_accent(f'{level_symbol} {overall_coherence:.1%}')} "
              f"({colors.neural_profile(level_pattern.title())})")
        
        # Individual coherence displays
        print(f"\n{colors.biofield_accent('Biofield Components:')}")
        
        # Schumann resonance
        schumann_coherence = coherence_data.get('schumann', 0.0)
        schumann_bar = colors.create_progress_bar(schumann_coherence, 25)
        print(f"  🌍 Schumann Resonance: {colors.schumann('7.83 Hz')} {schumann_bar}")
        
        # Solfeggio frequencies  
        solfeggio_coherence = coherence_data.get('solfeggio', 0.0)
        solfeggio_bar = colors.create_progress_bar(solfeggio_coherence, 25)
        print(f"  🎵 Solfeggio Integration: {colors.solfeggio('528 Hz')} {solfeggio_bar}")
        
        # Golden ratio harmonics
        golden_ratio_coherence = coherence_data.get('golden_ratio', 0.0)
        golden_ratio_bar = colors.create_progress_bar(golden_ratio_coherence, 25)
        print(f"  Φ Golden Ratio: {colors.golden_ratio('1.618')} {golden_ratio_bar}")
        
        # Natural frequency boost
        natural_frequency = coherence_data.get('natural_frequency', 1.0)
        if natural_frequency != 1.0:
            natural_bar = colors.create_progress_bar(natural_frequency / 2.0, 25)  # Scale to 0-2 range
            print(f"  🌿 Natural Frequency: {colors.gentle_text(f'{natural_frequency:.2f}x')} {natural_bar}")
        
        # Biofield flow visualization
        if self.terminal_adapter.capabilities.supports_unicode:
            flow_viz = self._create_biofield_flow_visualization(coherence_data)
            print(f"\n{colors.gentle_text('Biofield Energy Flow:')}")
            for line in flow_viz:
                print(f"  {line}")
    
    def show_schumann_resonance(self, alignment_strength: float, frequencies: List[float] = None) -> None:
        """
        Display Schumann resonance alignment visualization.
        
        Args:
            alignment_strength: Strength of Schumann resonance alignment (0.0-1.0)
            frequencies: List of active Schumann frequencies
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        if frequencies is None:
            frequencies = SCHUMANN_RESONANCE_FREQUENCIES[:3]  # Use first 3 harmonics
        
        print(f"\n{colors.consciousness_header('🌍' * 50)}")
        print(f"{colors.consciousness_title('🌍 Schumann Resonance Alignment')}")
        print(f"{colors.consciousness_header('🌍' * 50)}")
        
        # Alignment strength display
        alignment_bar = colors.create_progress_bar(alignment_strength, 30)
        print(f"\n{colors.schumann('Alignment Strength:')} {alignment_bar}")
        
        # Frequency harmonics
        print(f"\n{colors.schumann('Active Harmonics:')}")
        for i, freq in enumerate(frequencies):
            harmonic_strength = alignment_strength * (1.0 - i * 0.1)  # Decreasing strength
            freq_bar = colors.create_progress_bar(harmonic_strength, 20)
            
            print(f"  {colors.gentle_text(f'H{i+1}:')} {colors.schumann(f'{freq:.2f} Hz')} {freq_bar}")
        
        # Earth resonance visualization
        if self.terminal_adapter.capabilities.supports_unicode:
            earth_resonance_viz = self._create_earth_resonance_visualization(
                alignment_strength, frequencies
            )
            print(f"\n{colors.gentle_text('Earth Resonance Pattern:')}")
            for line in earth_resonance_viz:
                print(f"  {line}")
    
    def show_solfeggio_integration(self, active_frequencies: Dict[str, float]) -> None:
        """
        Display Solfeggio frequency integration.
        
        Args:
            active_frequencies: Dict of active Solfeggio frequencies and their strengths
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_header('🎵' * 50)}")
        print(f"{colors.consciousness_title('🎵 Solfeggio Frequency Integration')}")
        print(f"{colors.consciousness_header('🎵' * 50)}")
        
        # Active frequencies display
        print(f"\n{colors.solfeggio('Active Solfeggio Frequencies:')}")
        
        for freq_key, strength in active_frequencies.items():
            if freq_key in SOLFEGGIO_FREQUENCIES:
                freq_info = SOLFEGGIO_FREQUENCIES[freq_key]
                freq_name = freq_info['name']
                freq_hz = freq_key.replace('_Hz', ' Hz')
                
                strength_bar = colors.create_progress_bar(strength, 20)
                print(f"  {colors.solfeggio(freq_hz):>8} - {colors.gentle_text(freq_name):>15} {strength_bar}")
        
        # Harmonic integration visualization
        if active_frequencies and self.terminal_adapter.capabilities.supports_unicode:
            harmonic_viz = self._create_solfeggio_harmonic_visualization(active_frequencies)
            print(f"\n{colors.gentle_text('Harmonic Integration Pattern:')}")
            for line in harmonic_viz:
                print(f"  {line}")
    
    def show_golden_ratio_harmonics(self, harmonic_strength: float, phi_multiples: List[float] = None) -> None:
        """
        Display golden ratio harmonic visualization.
        
        Args:
            harmonic_strength: Overall strength of golden ratio harmonics
            phi_multiples: List of phi multiples being used
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        if phi_multiples is None:
            phi_multiples = PHI_HARMONICS[:3]
        
        print(f"\n{colors.consciousness_header('Φ' * 50)}")
        print(f"{colors.consciousness_title('Φ Golden Ratio Harmonics')}")
        print(f"{colors.consciousness_header('Φ' * 50)}")
        
        # Golden ratio information
        print(f"\n{colors.golden_ratio('Golden Ratio (Φ):')} {colors.gentle_text(f'{GOLDEN_RATIO:.10f}')}")
        print(f"{colors.golden_ratio('Harmonic Strength:')} {colors.create_progress_bar(harmonic_strength, 30)}")
        
        # Phi harmonics
        print(f"\n{colors.golden_ratio('Active Harmonics:')}")
        for i, phi_multiple in enumerate(phi_multiples):
            harmonic_name = f"Φ^{i+1}" if phi_multiple > 1 else f"1/Φ^{abs(i-2)}"
            harmonic_bar = colors.create_progress_bar(harmonic_strength * (1.0 - i * 0.05), 20)
            
            print(f"  {colors.gentle_text(harmonic_name):>6}: {colors.golden_ratio(f'{phi_multiple:.6f}')} {harmonic_bar}")
        
        # Sacred geometry visualization
        if self.terminal_adapter.capabilities.supports_unicode:
            golden_spiral_viz = self._create_golden_ratio_visualization(harmonic_strength)
            print(f"\n{colors.gentle_text('Sacred Geometry Pattern:')}")
            for line in golden_spiral_viz:
                print(f"  {line}")
    
    def show_biofield_flow_animation(self, coherence_data: Dict[str, float], duration: float = 5.0) -> None:
        """
        Show animated biofield flow visualization.
        
        Args:
            coherence_data: Current biofield coherence data
            duration: Animation duration in seconds
        """
        colors = self.color_scheme
        
        start_time = time.time()
        frame_count = 0
        
        print(f"\n{colors.consciousness_title('🌊 Live Biofield Flow Animation')}")
        print(f"{colors.gentle_text('Press Ctrl+C to stop...')}")
        
        try:
            while time.time() - start_time < duration:
                # Clear previous frame
                print("\033[2J\033[H", end="")  # Clear screen and move to top
                
                # Update animation frame
                self.animation_frame = frame_count
                self.wave_phase = (time.time() - start_time) * 2.0  # 2 cycles per second
                
                # Create animated biofield
                animated_frame = self._create_animated_biofield_frame(coherence_data)
                
                for line in animated_frame:
                    print(line)
                
                time.sleep(0.2)  # 5 FPS
                frame_count += 1
                
        except KeyboardInterrupt:
            pass
        
        print(f"\n{colors.gentle_text('Animation complete.')}")
    
    def _get_coherence_level(self, coherence: float) -> str:
        """Determine coherence level from value."""
        
        for level, info in BIOFIELD_COHERENCE_LEVELS.items():
            if info['range'][0] <= coherence <= info['range'][1]:
                return level
        
        return 'chaotic'
    
    def _create_biofield_flow_visualization(self, coherence_data: Dict[str, float]) -> List[str]:
        """Create biofield flow visualization."""
        
        lines = []
        width = 50
        height = 6
        
        # Create wave patterns for each biofield component
        for row in range(height):
            line = ""
            for col in range(width):
                # Calculate wave position
                x = col / width * 4 * math.pi
                t = self.wave_phase
                
                # Combine different biofield waves
                schumann_wave = coherence_data.get('schumann', 0) * math.sin(x + t)
                solfeggio_wave = coherence_data.get('solfeggio', 0) * math.sin(x * 1.618 + t * 1.5)
                golden_ratio_wave = coherence_data.get('golden_ratio', 0) * math.sin(x * GOLDEN_RATIO + t * 0.8)
                
                # Combine waves with row offset
                row_offset = row * math.pi / height
                combined_wave = (schumann_wave + solfeggio_wave + golden_ratio_wave) / 3
                wave_value = combined_wave * math.sin(row_offset + t * 0.5)
                
                # Convert to character
                if wave_value > 0.5:
                    char = '∿'
                elif wave_value > 0.2:
                    char = '⌇'
                elif wave_value > 0.0:
                    char = '∙'
                elif wave_value > -0.2:
                    char = '·'
                else:
                    char = ' '
                
                line += char
            
            lines.append(self.color_scheme.biofield_accent(line))
        
        return lines
    
    def _create_earth_resonance_visualization(self, 
                                            alignment_strength: float, 
                                            frequencies: List[float]) -> List[str]:
        """Create Earth resonance pattern visualization."""
        
        lines = []
        width = 40
        
        # Create resonance pattern
        for i in range(5):  # 5 lines for visualization
            line = ""
            for col in range(width):
                # Create standing wave pattern for Schumann resonance
                x = col / width * 2 * math.pi
                t = self.wave_phase
                
                # Primary 7.83 Hz resonance
                primary_wave = math.sin(x + t) * alignment_strength
                
                # Add harmonics if multiple frequencies
                if len(frequencies) > 1:
                    harmonic_wave = 0
                    for j, freq in enumerate(frequencies[1:], 1):
                        harmonic_factor = freq / frequencies[0]  # Ratio to fundamental
                        harmonic_wave += math.sin(x * harmonic_factor + t) * alignment_strength * (1.0 / (j + 1))
                    primary_wave += harmonic_wave * 0.3
                
                # Apply row modulation
                row_factor = 1.0 - (i * 0.15)
                wave_value = primary_wave * row_factor
                
                # Convert to character
                if abs(wave_value) > 0.7:
                    char = '●'
                elif abs(wave_value) > 0.4:
                    char = '◉'
                elif abs(wave_value) > 0.2:
                    char = '○'
                elif abs(wave_value) > 0.1:
                    char = '·'
                else:
                    char = ' '
                
                line += char
            
            lines.append(self.color_scheme.schumann(line))
        
        return lines
    
    def _create_solfeggio_harmonic_visualization(self, active_frequencies: Dict[str, float]) -> List[str]:
        """Create Solfeggio harmonic pattern visualization."""
        
        lines = []
        width = 45
        
        # Extract frequency values and strengths
        freq_data = []
        for freq_key, strength in active_frequencies.items():
            freq_hz = float(freq_key.replace('_Hz', ''))
            freq_data.append((freq_hz, strength))
        
        # Sort by frequency
        freq_data.sort(key=lambda x: x[0])
        
        # Create harmonic visualization
        for i in range(4):
            line = ""
            for col in range(width):
                x = col / width * 2 * math.pi
                t = self.wave_phase
                
                combined_wave = 0
                for freq_hz, strength in freq_data:
                    # Normalize frequency for visualization
                    freq_factor = freq_hz / 528.0  # Normalize to 528 Hz (Love frequency)
                    wave_contrib = math.sin(x * freq_factor + t) * strength
                    combined_wave += wave_contrib
                
                # Apply row offset
                row_offset = i * math.pi / 8
                wave_value = combined_wave * math.cos(row_offset + t * 0.3)
                
                # Convert to character based on Solfeggio character set
                if wave_value > 0.6:
                    char = '♫'
                elif wave_value > 0.3:
                    char = '♪'
                elif wave_value > 0.1:
                    char = '♩'
                elif wave_value > 0.0:
                    char = '·'
                else:
                    char = ' '
                
                line += char
            
            lines.append(self.color_scheme.solfeggio(line))
        
        return lines
    
    def _create_golden_ratio_visualization(self, harmonic_strength: float) -> List[str]:
        """Create golden ratio sacred geometry visualization."""
        
        lines = []
        width = 35
        
        # Create golden spiral approximation
        center_x = width // 2
        center_y = 3  # Center row for 6-row visualization
        
        for row in range(6):
            line = ""
            for col in range(width):
                # Calculate distance from center
                dx = col - center_x
                dy = row - center_y
                distance = math.sqrt(dx*dx + dy*dy)
                
                # Calculate angle
                angle = math.atan2(dy, dx)
                
                # Golden spiral equation approximation
                spiral_radius = GOLDEN_RATIO * math.exp(angle / (2 * math.pi) * math.log(GOLDEN_RATIO))
                
                # Check if point is on spiral (with some tolerance)
                spiral_tolerance = 2.0
                on_spiral = abs(distance - spiral_radius * 0.5) < spiral_tolerance
                
                # Add animation
                animated_offset = math.sin(self.wave_phase + angle) * 0.5
                
                if on_spiral and harmonic_strength > 0.3:
                    # Choose character based on position and strength
                    if harmonic_strength > 0.8:
                        char = 'Φ'
                    elif harmonic_strength > 0.6:
                        char = '◈'
                    elif harmonic_strength > 0.4:
                        char = '◇'
                    else:
                        char = '·'
                else:
                    char = ' '
                
                line += char
            
            lines.append(self.color_scheme.golden_ratio(line))
        
        return lines
    
    def _create_animated_biofield_frame(self, coherence_data: Dict[str, float]) -> List[str]:
        """Create single frame of animated biofield visualization."""
        
        lines = []
        colors = self.color_scheme
        
        # Header
        overall_coherence = sum(coherence_data.values()) / len(coherence_data)
        lines.append(colors.consciousness_title(f"🌊 Biofield Flow - Coherence: {overall_coherence:.1%}"))
        
        # Animated biofield visualization
        biofield_viz = self.biofield.create_animated_biofield_frame(
            self.animation_frame, overall_coherence, 60, 8
        )
        
        lines.extend(biofield_viz)
        
        # Component status
        lines.append("")
        for component, value in coherence_data.items():
            bar = colors.create_progress_bar(value, 20)
            symbol = {
                'schumann': '🌍',
                'solfeggio': '🎵', 
                'golden_ratio': 'Φ',
                'natural_frequency': '🌿'
            }.get(component, '○')
            
            lines.append(f"{symbol} {component.title()}: {bar}")
        
        return lines
    
    def update_animation_frame(self) -> None:
        """Update animation frame for continuous animations."""
        current_time = time.time()
        if current_time - self.last_update > 0.2:  # Update every 200ms
            self.animation_frame += 1
            self.wave_phase += 0.2
            self.last_update = current_time
    
    def clear_cache(self) -> None:
        """Clear visualization caches."""
        self._wave_cache.clear()
        self._mandala_cache.clear()