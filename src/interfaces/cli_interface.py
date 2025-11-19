# 🧠 Neural Entrainment System v2.0 - CLI Interface Implementation  
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
CLI Interface Implementation - Consciousness-aware command line interface.

This module implements the consciousness interface abstractions specifically for
command-line interfaces, providing beautiful terminal-based consciousness
visualization, biofield intelligence display, and neural-adaptive interaction.
"""

import os
import sys
import shutil
import platform
import subprocess
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass
import logging

from .base_interface import (
    ConsciousnessInterface,
    NeuralAdaptiveInterface,
    BiofieldIntelligenceInterface,
    SafetyProtocolInterface,
    SessionControlInterface,
    InterfaceCapability,
    InterfaceConfig,
    ConsciousnessState,
    SessionDisplayInfo
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# TERMINAL CAPABILITY DETECTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@dataclass
class CLIDisplayCapabilities:
    """Terminal display capabilities for consciousness-aware adaptation."""
    
    # Terminal properties
    width: int = 80
    height: int = 24
    supports_color: bool = False
    supports_unicode: bool = False
    supports_256_color: bool = False
    supports_true_color: bool = False
    
    # Terminal type and features
    terminal_type: str = "unknown"
    supports_cursor_positioning: bool = False
    supports_clear_screen: bool = False
    supports_alternate_buffer: bool = False
    
    # Consciousness-specific capabilities
    optimal_consciousness_width: int = 80
    supports_sacred_geometry: bool = False
    supports_biofield_animation: bool = False
    neural_sensitivity_adapted: bool = False

class TerminalConsciousnessAdapter:
    """
    Terminal adapter that detects capabilities and optimizes for consciousness work.
    """
    
    def __init__(self):
        self.capabilities = self._detect_capabilities()
        self._setup_consciousness_optimizations()
    
    def _detect_capabilities(self) -> CLIDisplayCapabilities:
        """Detect terminal capabilities for consciousness-aware adaptation."""
        
        # Get terminal size
        try:
            size = shutil.get_terminal_size()
            width, height = size.columns, size.lines
        except:
            width, height = 80, 24
        
        # Detect color support
        supports_color = self._detect_color_support()
        supports_256_color = self._detect_256_color_support()
        supports_true_color = self._detect_true_color_support()
        
        # Detect Unicode support
        supports_unicode = self._detect_unicode_support()
        
        # Detect terminal type
        terminal_type = os.environ.get('TERM', 'unknown')
        
        # Detect advanced features
        supports_cursor_positioning = terminal_type != 'dumb'
        supports_clear_screen = terminal_type != 'dumb'
        supports_alternate_buffer = terminal_type in ['xterm', 'xterm-256color', 'screen', 'tmux']
        
        # Calculate consciousness-optimized dimensions
        optimal_consciousness_width = min(max(width, 60), 120)
        
        # Determine consciousness-specific capabilities
        supports_sacred_geometry = supports_unicode and width >= 80
        supports_biofield_animation = (supports_cursor_positioning and 
                                     supports_clear_screen and 
                                     width >= 80)
        
        return CLIDisplayCapabilities(
            width=width,
            height=height,
            supports_color=supports_color,
            supports_unicode=supports_unicode,
            supports_256_color=supports_256_color,
            supports_true_color=supports_true_color,
            terminal_type=terminal_type,
            supports_cursor_positioning=supports_cursor_positioning,
            supports_clear_screen=supports_clear_screen,
            supports_alternate_buffer=supports_alternate_buffer,
            optimal_consciousness_width=optimal_consciousness_width,
            supports_sacred_geometry=supports_sacred_geometry,
            supports_biofield_animation=supports_biofield_animation
        )
    
    def _detect_color_support(self) -> bool:
        """Detect if terminal supports color output."""
        if 'NO_COLOR' in os.environ:
            return False
        
        if 'FORCE_COLOR' in os.environ:
            return True
        
        # Check TERM environment variable
        term = os.environ.get('TERM', '').lower()
        if any(color_term in term for color_term in ['color', 'ansi', 'xterm', 'screen', 'tmux']):
            return True
        
        # Check if stdout is a TTY
        return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
    
    def _detect_256_color_support(self) -> bool:
        """Detect 256 color support."""
        term = os.environ.get('TERM', '').lower()
        return '256color' in term or 'xterm' in term
    
    def _detect_true_color_support(self) -> bool:
        """Detect true color (24-bit) support."""
        if 'COLORTERM' in os.environ:
            colorterm = os.environ['COLORTERM'].lower()
            return colorterm in ['truecolor', '24bit']
        
        term = os.environ.get('TERM', '').lower()
        return 'truecolor' in term
    
    def _detect_unicode_support(self) -> bool:
        """Detect Unicode support."""
        # Check locale
        import locale
        try:
            encoding = locale.getpreferredencoding()
            return 'utf' in encoding.lower()
        except:
            pass
        
        # Check environment variables
        for env_var in ['LC_ALL', 'LC_CTYPE', 'LANG']:
            if env_var in os.environ:
                value = os.environ[env_var].lower()
                if 'utf' in value or 'unicode' in value:
                    return True
        
        return False
    
    def _setup_consciousness_optimizations(self) -> None:
        """Setup terminal optimizations for consciousness work."""
        
        # Enable UTF-8 output if supported
        if self.capabilities.supports_unicode:
            try:
                sys.stdout.reconfigure(encoding='utf-8')
            except:
                pass
        
        # Setup color environment if needed
        if self.capabilities.supports_color and 'TERM' not in os.environ:
            os.environ['TERM'] = 'xterm-256color'

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CLI CONSCIOUSNESS INTERFACE IMPLEMENTATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessCLIInterface(
    ConsciousnessInterface,
    NeuralAdaptiveInterface,
    BiofieldIntelligenceInterface,
    SafetyProtocolInterface,
    SessionControlInterface
):
    """
    Comprehensive CLI implementation of consciousness-aware interface.
    
    This class provides a beautiful, intelligent command-line interface that
    adapts to neural sensitivity, displays biofield intelligence, and maintains
    safety protocols while providing full session control capabilities.
    """
    
    def __init__(self, config: InterfaceConfig):
        super().__init__(config)
        self.terminal_adapter = TerminalConsciousnessAdapter()
        self.current_display_mode = "normal"
        self.gentle_mode_active = False
        self.session_controls = {}
        
        # Initialize display components (will be imported from CLI modules)
        self._consciousness_display = None
        self._biofield_display = None
        self._safety_monitor = None
        self._progress_tracker = None
        
    def initialize(self) -> bool:
        """Initialize CLI interface and detect capabilities."""
        try:
            # Adapt to neural profile
            neural_profile = {
                'sensitivity_level': self.config.neural_sensitivity_level,
                'experience_level': self.config.experience_level
            }
            self.adapt_to_neural_profile(neural_profile)
            
            # Initialize display components
            self._initialize_display_components()
            
            # Setup gentle mode if needed
            if self.config.gentle_mode:
                self.enable_gentle_mode(True)
            
            self.is_active = True
            logging.info("CLI consciousness interface initialized successfully")
            return True
            
        except Exception as e:
            logging.error(f"Failed to initialize CLI interface: {e}")
            return False
    
    def shutdown(self) -> None:
        """Gracefully shutdown CLI interface."""
        try:
            # Clear any running displays
            if self.terminal_adapter.capabilities.supports_clear_screen:
                print("\033[2J\033[H", end="")
            
            # Reset terminal state
            print("\033[0m", end="")  # Reset colors
            
            self.is_active = False
            logging.info("CLI consciousness interface shutdown complete")
            
        except Exception as e:
            logging.error(f"Error during CLI interface shutdown: {e}")
    
    def get_capabilities(self) -> List[InterfaceCapability]:
        """Get supported CLI interface capabilities."""
        capabilities = [
            InterfaceCapability.INTERACTIVE_FORMS,
            InterfaceCapability.REAL_TIME_FEEDBACK,
            InterfaceCapability.EMERGENCY_CONTROLS,
            InterfaceCapability.ACCESSIBILITY_SUPPORT
        ]
        
        if self.terminal_adapter.capabilities.supports_color:
            capabilities.append(InterfaceCapability.COLOR_SUPPORT)
        
        if self.terminal_adapter.capabilities.supports_unicode:
            capabilities.extend([
                InterfaceCapability.UNICODE_SUPPORT,
                InterfaceCapability.SACRED_GEOMETRY_DISPLAY
            ])
        
        if self.terminal_adapter.capabilities.supports_biofield_animation:
            capabilities.extend([
                InterfaceCapability.ANIMATION_SUPPORT,
                InterfaceCapability.REAL_TIME_UPDATES,
                InterfaceCapability.CONSCIOUSNESS_MAPPING,
                InterfaceCapability.BIOFIELD_VISUALIZATION
            ])
        
        return capabilities
    
    def adapt_to_neural_profile(self, neural_profile: Dict[str, Any]) -> None:
        """Adapt CLI interface based on neural profile."""
        sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
        experience_level = neural_profile.get('experience_level', 'intermediate')
        
        # Adapt display complexity based on experience level
        if experience_level == 'beginner':
            self.current_display_mode = "simplified"
        elif experience_level in ['advanced', 'expert']:
            self.current_display_mode = "detailed"
        else:
            self.current_display_mode = "normal"
        
        # Adapt sensitivity settings
        if sensitivity_level == 'sensitive':
            self.enable_gentle_mode(True)
            self.config.animation_sensitivity = 1.8
            self.config.comfort_check_interval = 180
        elif sensitivity_level == 'resilient':
            self.enable_gentle_mode(False)
            self.config.animation_sensitivity = 0.6
            
        logging.info(f"CLI adapted for {sensitivity_level} neural profile, {experience_level} experience")
    
    def update_consciousness_state(self, consciousness_state: ConsciousnessState) -> None:
        """Update CLI interface based on consciousness state."""
        
        # Adapt interface complexity based on state
        if consciousness_state == ConsciousnessState.OVERWHELMED:
            self.enable_gentle_mode(True)
            self.current_display_mode = "minimal"
        elif consciousness_state == ConsciousnessState.MEDITATIVE:
            self.current_display_mode = "peaceful"
        elif consciousness_state == ConsciousnessState.FOCUSED:
            self.current_display_mode = "focused"
        else:
            self.current_display_mode = "normal"
        
        # Trigger event for other components
        old_state = getattr(self, '_previous_consciousness_state', 'unknown')
        self.trigger_consciousness_state_change(old_state, consciousness_state.value)
        self._previous_consciousness_state = consciousness_state.value
    
    # ─────────────────────────────────────────────────────────────────────────────────
    # Neural Adaptive Interface Implementation
    # ─────────────────────────────────────────────────────────────────────────────────
    
    def assess_neural_sensitivity(self) -> Dict[str, float]:
        """Assess neural sensitivity through CLI interaction patterns."""
        # This would track user interaction patterns to assess sensitivity
        # For now, return default values
        return {
            'visual_sensitivity': self.config.animation_sensitivity,
            'information_processing_speed': 1.0,
            'interaction_preference': 0.8,
            'comfort_with_complexity': 0.7
        }
    
    def adapt_visual_density(self, density_level: float) -> None:
        """Adapt visual information density."""
        if density_level < 0.3:
            self.current_display_mode = "minimal"
        elif density_level < 0.7:
            self.current_display_mode = "normal"
        else:
            self.current_display_mode = "detailed"
    
    def adapt_interaction_speed(self, speed_preference: str) -> None:
        """Adapt interface interaction speed."""
        self.config.transition_speed = speed_preference
        
        # Adjust comfort check intervals
        if speed_preference == "very_slow":
            self.config.comfort_check_interval = 120
        elif speed_preference == "slow":
            self.config.comfort_check_interval = 180
        elif speed_preference == "fast":
            self.config.comfort_check_interval = 600
    
    def enable_gentle_mode(self, gentle: bool = True) -> None:
        """Enable gentle mode for sensitive users."""
        self.gentle_mode_active = gentle
        self.config.gentle_mode = gentle
        
        if gentle:
            self.current_display_mode = "gentle"
            self.config.animation_sensitivity = 2.0
        
        logging.info(f"Gentle mode {'enabled' if gentle else 'disabled'}")
    
    # ─────────────────────────────────────────────────────────────────────────────────
    # Biofield Intelligence Interface Implementation
    # ─────────────────────────────────────────────────────────────────────────────────
    
    def display_biofield_coherence(self, coherence_data: Dict[str, Any]) -> None:
        """Display biofield coherence in CLI."""
        if self._biofield_display:
            self._biofield_display.show_coherence(coherence_data)
    
    def display_schumann_resonance(self, schumann_data: Dict[str, Any]) -> None:
        """Display Schumann resonance connection."""
        if self._biofield_display:
            self._biofield_display.show_schumann_resonance(schumann_data)
    
    def display_solfeggio_frequencies(self, solfeggio_data: Dict[str, Any]) -> None:
        """Display Solfeggio frequency activity."""
        if self._biofield_display:
            self._biofield_display.show_solfeggio_frequencies(solfeggio_data)
    
    def display_golden_ratio_harmonics(self, golden_ratio_data: Dict[str, Any]) -> None:
        """Display golden ratio harmonic alignment."""
        if self._biofield_display:
            self._biofield_display.show_golden_ratio_harmonics(golden_ratio_data)
    
    # ─────────────────────────────────────────────────────────────────────────────────
    # Safety Protocol Interface Implementation
    # ─────────────────────────────────────────────────────────────────────────────────
    
    def display_safety_status(self, safety_data: Dict[str, Any]) -> None:
        """Display safety protocol status."""
        if self._safety_monitor:
            self._safety_monitor.show_safety_status(safety_data)
    
    def display_neural_load(self, neural_load: float) -> None:
        """Display neural processing load."""
        if self._safety_monitor:
            self._safety_monitor.show_neural_load(neural_load)
    
    def display_comfort_feedback(self, comfort_level: float) -> None:
        """Display comfort level feedback."""
        if self._safety_monitor:
            self._safety_monitor.show_comfort_feedback(comfort_level)
    
    def trigger_emergency_stop(self) -> None:
        """Trigger emergency stop protocol."""
        print("\n🚨 EMERGENCY STOP ACTIVATED 🚨")
        print("Session terminated for safety.")
        
        # Trigger emergency stop in event handlers
        for handler in self.event_handlers:
            try:
                handler.on_emergency_stop()
            except Exception as e:
                logging.error(f"Error in emergency stop handler: {e}")
    
    def show_safety_alert(self, alert_level: str, message: str) -> None:
        """Show safety alert to user."""
        alert_symbols = {
            'info': 'ℹ️',
            'warning': '⚠️',
            'danger': '🚨',
            'critical': '🔥'
        }
        
        symbol = alert_symbols.get(alert_level, '⚠️')
        print(f"\n{symbol} SAFETY ALERT ({alert_level.upper()}): {message}")
    
    # ─────────────────────────────────────────────────────────────────────────────────
    # Session Control Interface Implementation
    # ─────────────────────────────────────────────────────────────────────────────────
    
    def display_session_info(self, session_info: SessionDisplayInfo) -> None:
        """Display current session information."""
        self.session_info = session_info
        
        if self._progress_tracker:
            self._progress_tracker.update_session_info(session_info)
    
    def display_consciousness_journey(self, journey_data: Dict[str, Any]) -> None:
        """Display consciousness journey progress."""
        if self._consciousness_display:
            self._consciousness_display.show_consciousness_journey(journey_data)
    
    def provide_session_controls(self) -> Dict[str, Callable]:
        """Provide session control functions."""
        self.session_controls = {
            'pause': self._pause_session,
            'resume': self._resume_session,
            'stop': self._stop_session,
            'emergency_stop': self._emergency_stop,
            'adjust_intensity': self._adjust_intensity,
            'comfort_feedback': self._provide_comfort_feedback
        }
        
        return self.session_controls
    
    def update_session_progress(self, progress: float) -> None:
        """Update session progress display."""
        if self._progress_tracker:
            self._progress_tracker.update_progress(progress)
    
    # ─────────────────────────────────────────────────────────────────────────────────
    # Internal Helper Methods
    # ─────────────────────────────────────────────────────────────────────────────────
    
    def _initialize_display_components(self) -> None:
        """Initialize CLI display components."""
        # These will be imported from the CLI modules once created
        try:
            # Import display components
            # from ..cli.ui.consciousness_display import ConsciousnessDisplay
            # from ..cli.ui.biofield_display import BiofieldDisplay
            # from ..cli.ui.safety_monitor import SafetyMonitor
            # from ..cli.ui.progress_tracker import ProgressTracker
            
            # self._consciousness_display = ConsciousnessDisplay(self.terminal_adapter)
            # self._biofield_display = BiofieldDisplay(self.terminal_adapter)
            # self._safety_monitor = SafetyMonitor(self.terminal_adapter)
            # self._progress_tracker = ProgressTracker(self.terminal_adapter)
            
            # For now, set to None until CLI modules are created
            pass
            
        except ImportError:
            logging.warning("CLI display components not yet available")
    
    def _pause_session(self) -> bool:
        """Pause current session."""
        print("⏸️  Session paused.")
        return True
    
    def _resume_session(self) -> bool:
        """Resume paused session."""
        print("▶️  Session resumed.")
        return True
    
    def _stop_session(self) -> bool:
        """Stop current session."""
        print("⏹️  Session stopped.")
        return True
    
    def _emergency_stop(self) -> bool:
        """Emergency stop session."""
        self.trigger_emergency_stop()
        return True
    
    def _adjust_intensity(self, adjustment: float) -> bool:
        """Adjust session intensity."""
        print(f"🎚️  Intensity adjusted: {adjustment:+.1f}")
        return True
    
    def _provide_comfort_feedback(self, comfort_level: float) -> bool:
        """Provide comfort feedback."""
        comfort_emoji = "😌" if comfort_level > 0.7 else "😐" if comfort_level > 0.4 else "😓"
        print(f"{comfort_emoji} Comfort level: {comfort_level:.1%}")
        
        # Trigger comfort level change event
        for handler in self.event_handlers:
            try:
                handler.on_comfort_level_change(comfort_level)
            except Exception as e:
                logging.error(f"Error in comfort level change handler: {e}")
        
        return True

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CLI INTERFACE FACTORY FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def create_cli_interface(neural_profile: Dict[str, Any], preferences: Dict[str, Any] = None) -> ConsciousnessCLIInterface:
    """
    Create and configure CLI interface for consciousness work.
    
    Args:
        neural_profile: Neural profile assessment data
        preferences: User interface preferences
        
    Returns:
        Configured ConsciousnessCLIInterface instance
    """
    from .base_interface import create_interface_config
    
    config = create_interface_config(neural_profile, preferences)
    interface = ConsciousnessCLIInterface(config)
    
    if not interface.initialize():
        raise RuntimeError("Failed to initialize CLI consciousness interface")
    
    return interface

def detect_optimal_cli_configuration() -> Dict[str, Any]:
    """
    Detect optimal CLI configuration based on terminal capabilities.
    
    Returns:
        Configuration dictionary optimized for current terminal
    """
    adapter = TerminalConsciousnessAdapter()
    
    config = {
        'supports_color': adapter.capabilities.supports_color,
        'supports_unicode': adapter.capabilities.supports_unicode,
        'supports_animation': adapter.capabilities.supports_biofield_animation,
        'terminal_width': adapter.capabilities.width,
        'terminal_height': adapter.capabilities.height,
        'optimal_width': adapter.capabilities.optimal_consciousness_width,
        'supports_sacred_geometry': adapter.capabilities.supports_sacred_geometry
    }
    
    return config