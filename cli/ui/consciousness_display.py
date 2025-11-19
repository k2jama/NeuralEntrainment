# 🧠 Neural Entrainment System v2.0 - Consciousness Display UI Component
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Consciousness Display UI Component - Beautiful consciousness state visualization.

This module provides sophisticated consciousness state visualization including:
- Real-time consciousness state display with sacred geometry
- Consciousness journey mapping and progression tracking
- Neural state transitions with smooth visual indicators  
- Brainwave frequency visualization and analysis
- Consciousness coherence meters and flow indicators
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
# CONSCIOUSNESS STATE MAPPING
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONSCIOUSNESS_FREQUENCIES = {
    'deep_delta': {'range': (0.1, 2.0), 'peak': 1.0, 'color': 'deep_delta', 'depth': 'profound'},
    'delta': {'range': (1.0, 4.0), 'peak': 2.5, 'color': 'delta', 'depth': 'deep'},
    'theta': {'range': (4.0, 8.0), 'peak': 6.0, 'color': 'theta', 'depth': 'transformative'},
    'alpha': {'range': (8.0, 13.0), 'peak': 10.0, 'color': 'alpha', 'depth': 'bridge'},
    'beta': {'range': (13.0, 30.0), 'peak': 18.0, 'color': 'beta', 'depth': 'active'},
    'gamma': {'range': (30.0, 100.0), 'peak': 40.0, 'color': 'gamma', 'depth': 'transcendent'}
}

TRANSITION_ANIMATIONS = {
    'ascending': ['○', '◔', '◑', '◕', '●'],
    'descending': ['●', '◕', '◑', '◔', '○'], 
    'pulsing': ['○', '◔', '●', '◔', '○'],
    'flowing': ['∿', '⌇', '∿', '⌇', '∿'],
    'expanding': ['·', '○', '◯', '⭕', '🌟']
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS DISPLAY CLASS  
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessDisplay:
    """
    Beautiful consciousness state visualization component.
    
    This class provides real-time consciousness state visualization with sacred
    geometry, consciousness journey mapping, neural state transitions, and
    brainwave frequency analysis in a beautiful terminal interface.
    """
    
    def __init__(self, terminal_adapter: TerminalConsciousnessAdapter):
        self.terminal_adapter = terminal_adapter
        self.color_scheme = ConsciousnessColorScheme()
        self.symbols = SacredGeometrySymbols()
        self.consciousness_viz = ConsciousnessVisualization()
        self.biofield = BiofieldAesthetics()
        
        # Display state
        self.current_state = 'neutral'
        self.target_state = 'neutral' 
        self.transition_progress = 0.0
        self.animation_frame = 0
        self.last_update = time.time()
        
        # Journey tracking
        self.journey_history = []
        self.current_phase = 0
        self.phase_progress = 0.0
        
        # Visualization cache
        self._mandala_cache = {}
        self._journey_cache = {}
    
    def show_consciousness_state(self, 
                               state: str, 
                               coherence: float = 1.0,
                               transition_type: str = 'smooth') -> None:
        """
        Display current consciousness state with beautiful visualization.
        
        Args:
            state: Current consciousness state
            coherence: Consciousness coherence level (0.0-1.0) 
            transition_type: Type of transition animation
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        # Update state if changed
        if state != self.current_state:
            self.target_state = state
            self.transition_progress = 0.0
        
        # Get state information
        state_info = CONSCIOUSNESS_FREQUENCIES.get(state, {
            'range': (8.0, 13.0), 'peak': 10.0, 'color': 'alpha', 'depth': 'bridge'
        })
        
        state_color = colors.get_consciousness_state_color(state)
        frequency_range = state_info['range']
        peak_frequency = state_info['peak']
        depth_quality = state_info['depth']
        
        # Create state header
        print(f"\n{colors.consciousness_header('─' * 50)}")
        print(f"{colors.consciousness_title('🧠 Consciousness State')}")
        print(f"{colors.consciousness_header('─' * 50)}")
        
        # State information display
        state_symbol = self._get_state_symbol_animated(state, coherence)
        
        print(f"\n{colors.biofield_accent('Current State:')} {state_color(f'{state_symbol} {state.title()}')}")
        print(f"{colors.biofield_accent('Frequency:')} {colors.gentle_text(f'{frequency_range[0]:.1f}-{frequency_range[1]:.1f} Hz')} "
              f"({colors.consciousness_accent(f'Peak: {peak_frequency:.1f} Hz')})")
        print(f"{colors.biofield_accent('Depth Quality:')} {colors.neural_profile(depth_quality.title())}")
        print(f"{colors.biofield_accent('Coherence:')} {colors.create_progress_bar(coherence, 20)}")
        
        # Consciousness visualization mandala
        if self.terminal_adapter.capabilities.supports_unicode:
            mandala = self._create_consciousness_mandala(state, coherence)
            print(f"\n{colors.gentle_text('Consciousness Mandala:')}")
            for line in mandala:
                print(f"  {line}")
        
        # Frequency visualization
        frequency_viz = self._create_frequency_visualization(state, coherence)
        print(f"\n{colors.gentle_text('Brainwave Pattern:')}")
        for line in frequency_viz:
            print(f"  {line}")
    
    def show_consciousness_journey(self, journey_data: Dict[str, Any]) -> None:
        """
        Display consciousness journey progress and mapping.
        
        Args:
            journey_data: Journey information including phases, progress, history
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        phases = journey_data.get('phases', [])
        current_phase = journey_data.get('current_phase', 0)
        overall_progress = journey_data.get('overall_progress', 0.0)
        phase_progress = journey_data.get('phase_progress', 0.0)
        
        # Journey header
        print(f"\n{colors.consciousness_header('✧' * 60)}")
        print(f"{colors.consciousness_title('✨ Consciousness Journey Map')}")
        print(f"{colors.consciousness_header('✧' * 60)}")
        
        # Overall progress
        progress_bar = colors.create_progress_bar(overall_progress, 40)
        print(f"\n{colors.consciousness_accent('Journey Progress:')} {progress_bar}")
        
        # Current phase information
        if current_phase < len(phases):
            current_phase_data = phases[current_phase]
            phase_name = current_phase_data.get('name', f'Phase {current_phase + 1}')
            target_state = current_phase_data.get('consciousness_target_state', 'neutral')
            phase_duration = current_phase_data.get('duration', 300)
            
            print(f"{colors.biofield_accent('Current Phase:')} {colors.consciousness_accent(phase_name)}")
            print(f"{colors.biofield_accent('Target State:')} {colors.get_consciousness_state_color(target_state)(target_state.title())}")
            
            phase_progress_bar = colors.create_progress_bar(phase_progress, 30)
            print(f"{colors.biofield_accent('Phase Progress:')} {phase_progress_bar}")
        
        # Journey timeline
        if phases:
            phase_states = [p.get('consciousness_target_state', 'neutral') for p in phases]
            journey_timeline = self.consciousness_viz.create_consciousness_journey_line(
                phase_states, current_phase, 55
            )
            
            print(f"\n{colors.gentle_text('Consciousness Journey Timeline:')}")
            for line in journey_timeline:
                print(f"  {line}")
        
        # Phase details
        if len(phases) <= 6:  # Show all phases if 6 or fewer
            print(f"\n{colors.consciousness_accent('Journey Phases:')}")
            for i, phase in enumerate(phases):
                phase_name = phase.get('name', f'Phase {i+1}')
                target_state = phase.get('consciousness_target_state', 'neutral')
                duration = phase.get('duration', 300)
                biofield_target = phase.get('biofield_coherence_target', 0.7)
                
                # Phase status indicator
                if i < current_phase:
                    status_symbol = colors.status_safe('✓')
                elif i == current_phase:
                    status_symbol = colors.consciousness_accent('●')
                else:
                    status_symbol = colors.gentle_text('○')
                
                print(f"  {status_symbol} {colors.gentle_text(f'{i+1:2}.')} {colors.gentle_text(phase_name)} "
                      f"→ {colors.get_consciousness_state_color(target_state)(target_state)} "
                      f"({colors.gentle_text(self._format_duration(duration))}) "
                      f"[{colors.biofield_accent(f'{biofield_target:.0%}')} coherence]")
    
    def show_neural_state_transition(self, 
                                   from_state: str, 
                                   to_state: str,
                                   progress: float,
                                   transition_type: str = 'smooth') -> None:
        """
        Show neural state transition with animation.
        
        Args:
            from_state: Starting consciousness state
            to_state: Target consciousness state  
            progress: Transition progress (0.0-1.0)
            transition_type: Type of transition animation
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_header('◊' * 45)}")
        print(f"{colors.consciousness_title('🔄 Neural State Transition')}")
        print(f"{colors.consciousness_header('◊' * 45)}")
        
        # State transition display
        from_color = colors.get_consciousness_state_color(from_state)
        to_color = colors.get_consciousness_state_color(to_state)
        
        print(f"\n{colors.biofield_accent('Transition:')} "
              f"{from_color(from_state.title())} → {to_color(to_state.title())}")
        
        # Progress with animated indicator
        transition_bar = self._create_transition_progress_bar(progress, transition_type, 40)
        print(f"{colors.biofield_accent('Progress:')} {transition_bar}")
        
        # Transition visualization
        if self.terminal_adapter.capabilities.supports_unicode:
            transition_viz = self._create_transition_visualization(
                from_state, to_state, progress, transition_type
            )
            print(f"\n{colors.gentle_text('Neural Transition Pattern:')}")
            for line in transition_viz:
                print(f"  {line}")
    
    def show_brainwave_analysis(self, frequency_data: Dict[str, float]) -> None:
        """
        Show brainwave frequency analysis and visualization.
        
        Args:
            frequency_data: Dict of frequency bands and their amplitudes
        """
        colors = self.color_scheme
        
        print(f"\n{colors.consciousness_header('∿' * 50)}")
        print(f"{colors.consciousness_title('🧠 Brainwave Frequency Analysis')}")
        print(f"{colors.consciousness_header('∿' * 50)}")
        
        # Frequency spectrum visualization
        spectrum_viz = self.consciousness_viz.create_frequency_spectrum(
            frequency_data, 50, 8
        )
        
        for line in spectrum_viz:
            print(f"  {line}")
        
        # Dominant frequency analysis
        if frequency_data:
            dominant_freq = max(frequency_data.items(), key=lambda x: x[1])
            dominant_state = self._frequency_to_state(dominant_freq[0])
            
            print(f"\n{colors.consciousness_accent('Dominant Frequency:')} "
                  f"{colors.get_consciousness_state_color(dominant_state)(dominant_freq[0])} "
                  f"({colors.gentle_text(f'{dominant_freq[1]:.1%} amplitude')})")
            
            print(f"{colors.consciousness_accent('Associated State:')} "
                  f"{colors.get_consciousness_state_color(dominant_state)(dominant_state.title())}")
    
    def _get_state_symbol_animated(self, state: str, coherence: float) -> str:
        """Get animated symbol for consciousness state based on coherence."""
        
        symbols = self.symbols
        
        # Base symbols for each state
        base_symbols = {
            'deep_delta': symbols.FILLED_CIRCLE,
            'delta': symbols.CIRCLE,
            'theta': symbols.DIAMOND,
            'alpha': symbols.TRIANGLE_UP,
            'beta': symbols.SQUARE,
            'gamma': symbols.STAR,
            'neutral': symbols.CIRCLE
        }
        
        base_symbol = base_symbols.get(state, symbols.CIRCLE)
        
        # Add animation based on coherence
        if coherence > 0.8:
            # High coherence - add sparkle effect
            animation_symbols = ['✦', '✧', '✦', base_symbol]
            frame = self.animation_frame % len(animation_symbols)
            return animation_symbols[frame]
        elif coherence > 0.6:
            # Medium coherence - gentle pulsing
            if (self.animation_frame // 3) % 2 == 0:
                return base_symbol
            else:
                return '◯'  # Slightly larger circle
        else:
            # Low coherence - steady symbol
            return base_symbol
    
    def _create_consciousness_mandala(self, state: str, coherence: float) -> List[str]:
        """Create consciousness mandala visualization for state."""
        
        # Check cache first
        cache_key = f"{state}_{coherence:.2f}_{self.animation_frame//4}"
        if cache_key in self._mandala_cache:
            return self._mandala_cache[cache_key]
        
        # Create new mandala
        mandala_size = 11
        mandala = self.consciousness_viz.create_consciousness_mandala(mandala_size//2)
        
        # Apply state-specific coloring (simplified for text)
        state_color = self.color_scheme.get_consciousness_state_color(state)
        colored_mandala = []
        
        for line in mandala:
            if '◉' in line:  # Center
                colored_line = line.replace('◉', state_color('◉'))
            else:
                colored_line = self.color_scheme.gentle_text(line)
            colored_mandala.append(colored_line)
        
        # Cache result
        self._mandala_cache[cache_key] = colored_mandala
        
        # Limit cache size
        if len(self._mandala_cache) > 20:
            self._mandala_cache.clear()
        
        return colored_mandala
    
    def _create_frequency_visualization(self, state: str, coherence: float) -> List[str]:
        """Create brainwave frequency visualization."""
        
        state_info = CONSCIOUSNESS_FREQUENCIES.get(state, {})
        frequency_range = state_info.get('range', (8.0, 13.0))
        peak_frequency = state_info.get('peak', 10.0)
        
        # Create simple ASCII frequency display
        lines = []
        width = 40
        
        # Frequency wave pattern
        wave_line = ""
        for i in range(width):
            # Create wave based on frequency
            x = (i / width) * 4 * math.pi  # Two complete wavelengths
            # Scale by frequency - higher frequency = more oscillations
            freq_factor = peak_frequency / 10.0  # Normalize around 10 Hz
            wave_value = math.sin(x * freq_factor + self.animation_frame * 0.2)
            
            # Apply coherence to amplitude
            amplitude = wave_value * coherence
            
            # Convert to character
            if amplitude > 0.7:
                char = '█'
            elif amplitude > 0.3:
                char = '▓'
            elif amplitude > 0.0:
                char = '▒'
            elif amplitude > -0.3:
                char = '░'
            elif amplitude > -0.7:
                char = '▒'
            else:
                char = '▓'
            
            wave_line += char
        
        lines.append(wave_line)
        
        # Frequency info line
        freq_info = f"{frequency_range[0]:.1f}-{frequency_range[1]:.1f} Hz (Peak: {peak_frequency:.1f} Hz)"
        lines.append(freq_info.center(width))
        
        return lines
    
    def _create_transition_progress_bar(self, 
                                      progress: float, 
                                      transition_type: str,
                                      width: int) -> str:
        """Create animated transition progress bar."""
        
        colors = self.color_scheme
        
        filled = int(progress * width)
        empty = width - filled
        
        # Choose animation based on transition type
        if transition_type == 'smooth':
            fill_char = '█'
            empty_char = '░'
        elif transition_type == 'pulsing':
            # Pulsing animation
            if (self.animation_frame // 2) % 2 == 0:
                fill_char = '█'
            else:
                fill_char = '▓'
            empty_char = '░'
        else:
            fill_char = '█'
            empty_char = '░'
        
        # Current position indicator
        if filled > 0 and filled < width:
            position_char = '◆'
            filled_part = fill_char * (filled - 1) + position_char
        else:
            filled_part = fill_char * filled
            
        bar = filled_part + empty_char * empty
        
        return f"[{bar}] {progress:.1%}"
    
    def _create_transition_visualization(self, 
                                       from_state: str, 
                                       to_state: str,
                                       progress: float, 
                                       transition_type: str) -> List[str]:
        """Create transition visualization between states."""
        
        lines = []
        width = 30
        
        # Simple transition representation
        from_symbol = self._get_consciousness_symbol(from_state)
        to_symbol = self._get_consciousness_symbol(to_state)
        
        # Create transition line
        transition_length = width - 6  # Account for symbols and spacing
        transition_pos = int(progress * transition_length)
        
        line = from_symbol + ' '
        
        for i in range(transition_length):
            if i == transition_pos:
                line += '●'  # Current position
            elif i < transition_pos:
                line += '─'  # Completed
            else:
                line += '╌'  # Remaining
        
        line += ' ' + to_symbol
        
        lines.append(line)
        
        # Progress indicator
        progress_line = f"Progress: {progress:.1%}"
        lines.append(progress_line.center(width))
        
        return lines
    
    def _get_consciousness_symbol(self, state: str) -> str:
        """Get static symbol for consciousness state."""
        
        symbols = self.symbols
        
        symbol_mapping = {
            'deep_delta': symbols.FILLED_CIRCLE,
            'delta': symbols.CIRCLE,
            'theta': symbols.DIAMOND,
            'alpha': symbols.TRIANGLE_UP,
            'beta': symbols.SQUARE,
            'gamma': symbols.STAR,
            'neutral': symbols.CIRCLE
        }
        
        return symbol_mapping.get(state, symbols.CIRCLE)
    
    def _frequency_to_state(self, frequency_name: str) -> str:
        """Convert frequency name to consciousness state."""
        
        # Simple mapping - could be more sophisticated
        freq_to_state = {
            'delta': 'delta',
            'theta': 'theta',
            'alpha': 'alpha',
            'beta': 'beta',
            'gamma': 'gamma'
        }
        
        for freq_key, state in freq_to_state.items():
            if freq_key in frequency_name.lower():
                return state
        
        return 'neutral'
    
    def _format_duration(self, seconds: float) -> str:
        """Format duration in human-readable format."""
        
        if seconds < 60:
            return f"{seconds:.0f}s"
        elif seconds < 3600:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            if remaining_seconds == 0:
                return f"{minutes:.0f}m"
            else:
                return f"{minutes:.0f}m {remaining_seconds:.0f}s"
        else:
            hours = seconds // 3600
            remaining_minutes = (seconds % 3600) // 60
            return f"{hours:.0f}h {remaining_minutes:.0f}m"
    
    def update_animation_frame(self) -> None:
        """Update animation frame for continuous animations."""
        current_time = time.time()
        if current_time - self.last_update > 0.5:  # Update every 500ms
            self.animation_frame += 1
            self.last_update = current_time
    
    def clear_cache(self) -> None:
        """Clear visualization caches."""
        self._mandala_cache.clear()
        self._journey_cache.clear()