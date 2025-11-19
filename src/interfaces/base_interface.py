# 🧠 Neural Entrainment System v2.0 - Base Interface Abstractions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Base Interface Abstractions - Foundation patterns for consciousness-aware interfaces.

This module defines the core interface abstractions that ensure all interface implementations
(CLI, Desktop, Web) maintain consistency in consciousness sovereignty principles, biofield 
intelligence integration, and safety protocol adherence.
"""

import abc
import logging
from typing import Dict, Any, List, Optional, Protocol, Union, Callable
from dataclasses import dataclass, field
from enum import Enum
import datetime

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS INTERFACE ENUMS & TYPES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class InterfaceCapability(Enum):
    """Interface capability flags for consciousness-aware feature detection."""
    
    # Visual capabilities
    COLOR_SUPPORT = "color_support"
    UNICODE_SUPPORT = "unicode_support"
    ANIMATION_SUPPORT = "animation_support"
    REAL_TIME_UPDATES = "real_time_updates"
    
    # Consciousness visualization
    CONSCIOUSNESS_MAPPING = "consciousness_mapping"
    BIOFIELD_VISUALIZATION = "biofield_visualization"
    SACRED_GEOMETRY_DISPLAY = "sacred_geometry_display"
    
    # Interaction capabilities
    INTERACTIVE_FORMS = "interactive_forms"
    REAL_TIME_FEEDBACK = "real_time_feedback"
    EMERGENCY_CONTROLS = "emergency_controls"
    ACCESSIBILITY_SUPPORT = "accessibility_support"
    
    # Audio capabilities
    AUDIO_PLAYBACK = "audio_playback"
    VOLUME_CONTROL = "volume_control"
    REAL_TIME_AUDIO_MONITORING = "real_time_audio_monitoring"

class InterfaceMode(Enum):
    """Interface complexity modes based on user experience and neural sensitivity."""
    
    BEGINNER = "beginner"           # Simple, guided interface with safety emphasis
    INTERMEDIATE = "intermediate"   # Balanced feature access with smart defaults
    EXPERT = "expert"              # Full feature access and customization
    ACCESSIBILITY = "accessibility" # Enhanced accessibility with neural sensitivity adaptations

class ConsciousnessState(Enum):
    """Current consciousness states for interface adaptation."""
    
    GROUNDED = "grounded"           # Stable, present state
    FOCUSED = "focused"             # Active, concentrated state  
    RELAXED = "relaxed"             # Calm, receptive state
    MEDITATIVE = "meditative"       # Deep, contemplative state
    TRANSITIONING = "transitioning" # Between states, needs gentle guidance
    OVERWHELMED = "overwhelmed"     # Requires immediate simplification and support

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS INTERFACE PROTOCOLS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@dataclass
class InterfaceConfig:
    """Configuration for consciousness-aware interface adaptation."""
    
    # Neural profile integration
    neural_sensitivity_level: str = "standard"
    experience_level: str = "intermediate"
    current_consciousness_state: ConsciousnessState = ConsciousnessState.GROUNDED
    
    # Interface preferences
    interface_mode: InterfaceMode = InterfaceMode.INTERMEDIATE
    color_preferences: Dict[str, str] = field(default_factory=dict)
    accessibility_needs: List[str] = field(default_factory=list)
    
    # Feature flags
    enabled_capabilities: List[InterfaceCapability] = field(default_factory=list)
    biofield_visualization_enabled: bool = True
    safety_monitoring_level: str = "standard"
    
    # Animation and transition preferences
    animation_sensitivity: float = 1.0  # 0.0-2.0, higher = more sensitivity
    transition_speed: str = "medium"    # very_slow, slow, medium, fast
    
    # Comfort and safety
    comfort_check_interval: int = 300   # seconds
    emergency_stop_enabled: bool = True
    gentle_mode: bool = False

@dataclass 
class SessionDisplayInfo:
    """Information about current session for interface display."""
    
    session_id: Optional[str] = None
    session_name: str = ""
    current_phase: str = ""
    phase_progress: float = 0.0
    total_progress: float = 0.0
    consciousness_target: str = ""
    current_consciousness_state: str = ""
    
    # Biofield information
    biofield_coherence: float = 0.0
    schumann_alignment: float = 0.0
    solfeggio_presence: Dict[str, float] = field(default_factory=dict)
    
    # Safety information
    neural_load: float = 0.0
    safety_rating: str = "safe"
    comfort_level: float = 0.8
    
    # Time information
    elapsed_time: float = 0.0
    remaining_time: float = 0.0
    estimated_completion: Optional[datetime.datetime] = None

class ConsciousnessEventHandler(Protocol):
    """Protocol for handling consciousness-aware interface events."""
    
    def on_consciousness_state_change(self, old_state: str, new_state: str) -> None:
        """Called when user's consciousness state changes."""
        ...
    
    def on_comfort_level_change(self, comfort_level: float) -> None:
        """Called when user comfort level changes."""
        ...
    
    def on_safety_alert(self, alert_level: str, message: str) -> None:
        """Called when safety alert is triggered."""
        ...
    
    def on_emergency_stop(self) -> None:
        """Called when emergency stop is activated."""
        ...

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BASE INTERFACE ABSTRACTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessInterface(abc.ABC):
    """
    Base interface abstraction for consciousness-aware interfaces.
    
    This class defines the core contract that all interface implementations
    must fulfill to ensure consciousness sovereignty and safety.
    """
    
    def __init__(self, config: InterfaceConfig):
        self.config = config
        self.event_handlers: List[ConsciousnessEventHandler] = []
        self.session_info: Optional[SessionDisplayInfo] = None
        self.is_active = False
        
    @abc.abstractmethod
    def initialize(self) -> bool:
        """Initialize the interface and detect capabilities."""
        pass
    
    @abc.abstractmethod
    def shutdown(self) -> None:
        """Gracefully shutdown the interface."""
        pass
    
    @abc.abstractmethod
    def get_capabilities(self) -> List[InterfaceCapability]:
        """Get list of supported interface capabilities."""
        pass
    
    @abc.abstractmethod
    def adapt_to_neural_profile(self, neural_profile: Dict[str, Any]) -> None:
        """Adapt interface based on neural profile assessment."""
        pass
    
    @abc.abstractmethod
    def update_consciousness_state(self, consciousness_state: ConsciousnessState) -> None:
        """Update interface based on current consciousness state."""
        pass
    
    # Event handling
    def add_event_handler(self, handler: ConsciousnessEventHandler) -> None:
        """Add consciousness event handler."""
        self.event_handlers.append(handler)
    
    def remove_event_handler(self, handler: ConsciousnessEventHandler) -> None:
        """Remove consciousness event handler."""
        if handler in self.event_handlers:
            self.event_handlers.remove(handler)
    
    def trigger_consciousness_state_change(self, old_state: str, new_state: str) -> None:
        """Trigger consciousness state change event."""
        for handler in self.event_handlers:
            try:
                handler.on_consciousness_state_change(old_state, new_state)
            except Exception as e:
                logging.error(f"Error in consciousness state change handler: {e}")

class NeuralAdaptiveInterface(abc.ABC):
    """Interface that adapts to neural sensitivity and processing preferences."""
    
    @abc.abstractmethod
    def assess_neural_sensitivity(self) -> Dict[str, float]:
        """Assess user's neural sensitivity through interface interaction."""
        pass
    
    @abc.abstractmethod
    def adapt_visual_density(self, density_level: float) -> None:
        """Adapt visual information density based on neural capacity."""
        pass
    
    @abc.abstractmethod
    def adapt_interaction_speed(self, speed_preference: str) -> None:
        """Adapt interface interaction speed to user preference."""
        pass
    
    @abc.abstractmethod
    def enable_gentle_mode(self, gentle: bool = True) -> None:
        """Enable gentle mode for sensitive users."""
        pass

class BiofieldIntelligenceInterface(abc.ABC):
    """Interface for biofield intelligence visualization and control."""
    
    @abc.abstractmethod
    def display_biofield_coherence(self, coherence_data: Dict[str, Any]) -> None:
        """Display biofield coherence information."""
        pass
    
    @abc.abstractmethod
    def display_schumann_resonance(self, schumann_data: Dict[str, Any]) -> None:
        """Display Schumann resonance connection status."""
        pass
    
    @abc.abstractmethod
    def display_solfeggio_frequencies(self, solfeggio_data: Dict[str, Any]) -> None:
        """Display Solfeggio frequency presence and activity."""
        pass
    
    @abc.abstractmethod
    def display_golden_ratio_harmonics(self, golden_ratio_data: Dict[str, Any]) -> None:
        """Display golden ratio harmonic alignment."""
        pass

class SafetyProtocolInterface(abc.ABC):
    """Interface for safety protocol monitoring and control."""
    
    @abc.abstractmethod
    def display_safety_status(self, safety_data: Dict[str, Any]) -> None:
        """Display current safety protocol status."""
        pass
    
    @abc.abstractmethod
    def display_neural_load(self, neural_load: float) -> None:
        """Display current neural processing load."""
        pass
    
    @abc.abstractmethod
    def display_comfort_feedback(self, comfort_level: float) -> None:
        """Display user comfort level feedback."""
        pass
    
    @abc.abstractmethod
    def trigger_emergency_stop(self) -> None:
        """Trigger emergency stop protocol."""
        pass
    
    @abc.abstractmethod
    def show_safety_alert(self, alert_level: str, message: str) -> None:
        """Show safety alert to user."""
        pass

class SessionControlInterface(abc.ABC):
    """Interface for session control and monitoring."""
    
    @abc.abstractmethod
    def display_session_info(self, session_info: SessionDisplayInfo) -> None:
        """Display current session information."""
        pass
    
    @abc.abstractmethod
    def display_consciousness_journey(self, journey_data: Dict[str, Any]) -> None:
        """Display consciousness journey progress."""
        pass
    
    @abc.abstractmethod
    def provide_session_controls(self) -> Dict[str, Callable]:
        """Provide session control functions (pause, stop, adjust, etc.)."""
        pass
    
    @abc.abstractmethod
    def update_session_progress(self, progress: float) -> None:
        """Update session progress display."""
        pass

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# UTILITY FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def create_interface_config(
    neural_profile: Dict[str, Any],
    preferences: Dict[str, Any] = None
) -> InterfaceConfig:
    """
    Create interface configuration from neural profile and user preferences.
    
    Args:
        neural_profile: Neural profile data from assessment
        preferences: User interface preferences
        
    Returns:
        Configured InterfaceConfig instance
    """
    preferences = preferences or {}
    
    # Map neural sensitivity to interface configuration
    sensitivity_mapping = {
        'sensitive': {
            'animation_sensitivity': 1.8,
            'transition_speed': 'slow',
            'gentle_mode': True,
            'comfort_check_interval': 180
        },
        'standard': {
            'animation_sensitivity': 1.0,
            'transition_speed': 'medium',
            'gentle_mode': False,
            'comfort_check_interval': 300
        },
        'resilient': {
            'animation_sensitivity': 0.6,
            'transition_speed': 'fast',
            'gentle_mode': False,
            'comfort_check_interval': 600
        }
    }
    
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    sensitivity_config = sensitivity_mapping.get(sensitivity_level, sensitivity_mapping['standard'])
    
    # Map experience level to interface mode
    experience_mapping = {
        'beginner': InterfaceMode.BEGINNER,
        'intermediate': InterfaceMode.INTERMEDIATE,
        'advanced': InterfaceMode.EXPERT,
        'expert': InterfaceMode.EXPERT
    }
    
    experience_level = neural_profile.get('experience_level', 'intermediate')
    interface_mode = experience_mapping.get(experience_level, InterfaceMode.INTERMEDIATE)
    
    # Create configuration
    config = InterfaceConfig(
        neural_sensitivity_level=sensitivity_level,
        experience_level=experience_level,
        interface_mode=interface_mode,
        animation_sensitivity=sensitivity_config['animation_sensitivity'],
        transition_speed=sensitivity_config['transition_speed'],
        gentle_mode=sensitivity_config['gentle_mode'],
        comfort_check_interval=sensitivity_config['comfort_check_interval']
    )
    
    # Apply user preferences
    for key, value in preferences.items():
        if hasattr(config, key):
            setattr(config, key, value)
    
    return config

def validate_interface_compatibility(
    interface: ConsciousnessInterface,
    required_capabilities: List[InterfaceCapability]
) -> bool:
    """
    Validate that an interface supports required capabilities.
    
    Args:
        interface: Interface instance to validate
        required_capabilities: List of required capabilities
        
    Returns:
        True if interface supports all required capabilities
    """
    supported_capabilities = interface.get_capabilities()
    
    for capability in required_capabilities:
        if capability not in supported_capabilities:
            logging.warning(f"Interface missing required capability: {capability}")
            return False
    
    return True

def adapt_interface_for_consciousness_state(
    interface: ConsciousnessInterface,
    consciousness_state: ConsciousnessState
) -> None:
    """
    Adapt interface based on current consciousness state.
    
    Args:
        interface: Interface to adapt
        consciousness_state: Current consciousness state
    """
    try:
        interface.update_consciousness_state(consciousness_state)
        logging.info(f"Interface adapted for consciousness state: {consciousness_state.value}")
    except Exception as e:
        logging.error(f"Error adapting interface for consciousness state: {e}")