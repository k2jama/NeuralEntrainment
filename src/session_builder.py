# 🧪 Neural Entrainment System - Session Builder v2.0
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠 Consciousness-Aware Biofield Intelligence Framework
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Neural Entrainment Session Builder - Consciousness-aware session orchestration engine.

This module provides comprehensive session building capabilities with biofield intelligence,
consciousness-aware parameter adaptation, neural architecture respect, and safety protocols.
All functions are designed with consciousness sovereignty and healing intelligence as core principles.
"""

import numpy as np
import logging
from typing import Dict, Any, List, Optional, Tuple, Union
from dataclasses import dataclass, field
from enum import Enum
import copy
from scipy.io import wavfile

# Import signal generator with flexible handling for different environments
try:
    from . import signal_generator
except ImportError:
    try:
        import signal_generator
    except ImportError:
        import sys
        import os
        sys.path.insert(0, os.path.dirname(__file__))
        import signal_generator

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSTANTS & CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Neural architecture sensitivity levels
NEURAL_SENSITIVITY_PROFILES = {
    'sensitive': {
        'sensitivity_factor': 1.3,
        'processing_speed': 0.8,
        'integration_capacity': 3,
        'noise_tolerance': 0.7,
        'transition_smoothing': 1.5,
        'duration_extension': 1.2
    },
    'standard': {
        'sensitivity_factor': 1.0,
        'processing_speed': 1.0,
        'integration_capacity': 4,
        'noise_tolerance': 1.0,
        'transition_smoothing': 1.0,
        'duration_extension': 1.0
    },
    'resilient': {
        'sensitivity_factor': 0.8,
        'processing_speed': 1.2,
        'integration_capacity': 6,
        'noise_tolerance': 1.3,
        'transition_smoothing': 0.8,
        'duration_extension': 0.9
    }
}

# Consciousness state coherence profiles
CONSCIOUSNESS_STATE_PROFILES = {
    'calm': {'coherence': 0.85, 'stability': 0.9, 'receptivity': 0.8},
    'focused': {'coherence': 0.9, 'stability': 0.8, 'receptivity': 0.7},
    'agitated': {'coherence': 0.3, 'stability': 0.4, 'receptivity': 0.9},
    'neutral': {'coherence': 0.6, 'stability': 0.6, 'receptivity': 0.6},
    'meditative': {'coherence': 0.8, 'stability': 0.9, 'receptivity': 0.9},
    'anxious': {'coherence': 0.25, 'stability': 0.3, 'receptivity': 0.8},
    'tired': {'coherence': 0.4, 'stability': 0.5, 'receptivity': 0.7}
}

# Experience level configurations
EXPERIENCE_LEVEL_PROFILES = {
    'beginner': {
        'complexity_tolerance': 0.6,
        'session_intensity': 0.7,
        'safety_margin': 1.5,
        'guidance_level': 1.0
    },
    'intermediate': {
        'complexity_tolerance': 0.8,
        'session_intensity': 0.9,
        'safety_margin': 1.2,
        'guidance_level': 0.7
    },
    'advanced': {
        'complexity_tolerance': 1.0,
        'session_intensity': 1.0,
        'safety_margin': 1.0,
        'guidance_level': 0.3
    },
    'expert': {
        'complexity_tolerance': 1.2,
        'session_intensity': 1.1,
        'safety_margin': 0.9,
        'guidance_level': 0.1
    }
}

# Safe parameter ranges
SAFE_RANGES = {
    'beat_frequency': (0.5, 100.0),     # Hz
    'carrier_frequency': (60, 800),     # Hz
    'phase_duration': (30, 3600),       # seconds
    'volume_level': (0.0, 0.95),        # amplitude
    'fm_depth': (0, 50),                # Hz
    'transition_smoothness': (0.1, 3.0) # multiplier
}

class TransitionType(Enum):
    """Enumeration of consciousness-aware transition types."""
    LINEAR = 'linear'
    THETA_GATEWAY = 'theta_gateway'
    GAMMA_EMERGENCE = 'gamma_emergence'
    DELTA_DESCENT = 'delta_descent'
    SINUSOIDAL = 'sin'
    EXPONENTIAL = 'exp'
    BREATH_SYNC = 'breath_sync'
    HEART_SYNC = 'heart_sync'

class CarrierType(Enum):
    """Enumeration of carrier wave types."""
    SINE = 'sine'
    PINK_NOISE = 'pink_noise'
    BROWN_NOISE = 'brown_noise'
    WHITE_NOISE = 'white_noise'
    CONSCIOUSNESS_CARRIER = 'consciousness_carrier'

@dataclass
class NeuralProfile:
    """Comprehensive neural processing profile for consciousness adaptation."""
    sensitivity_level: str = 'standard'
    current_state: str = 'neutral'
    experience_level: str = 'beginner'
    integration_capacity: Optional[int] = None
    custom_factors: Dict[str, float] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate and compute derived metrics."""
        # Validate levels
        if self.sensitivity_level not in NEURAL_SENSITIVITY_PROFILES:
            logging.warning(f"Unknown sensitivity level '{self.sensitivity_level}', using 'standard'")
            self.sensitivity_level = 'standard'
        
        if self.current_state not in CONSCIOUSNESS_STATE_PROFILES:
            logging.warning(f"Unknown consciousness state '{self.current_state}', using 'neutral'")
            self.current_state = 'neutral'
        
        if self.experience_level not in EXPERIENCE_LEVEL_PROFILES:
            logging.warning(f"Unknown experience level '{self.experience_level}', using 'beginner'")
            self.experience_level = 'beginner'
    
    @property
    def sensitivity_factor(self) -> float:
        """Get sensitivity factor with custom override."""
        base = NEURAL_SENSITIVITY_PROFILES[self.sensitivity_level]['sensitivity_factor']
        return self.custom_factors.get('sensitivity_factor', base)
    
    @property
    def processing_speed(self) -> float:
        """Get processing speed factor."""
        base = NEURAL_SENSITIVITY_PROFILES[self.sensitivity_level]['processing_speed']
        exp_factor = EXPERIENCE_LEVEL_PROFILES[self.experience_level]['complexity_tolerance']
        return base * exp_factor * self.custom_factors.get('processing_speed_mult', 1.0)
    
    @property
    def current_coherence(self) -> float:
        """Get current consciousness coherence level."""
        return CONSCIOUSNESS_STATE_PROFILES[self.current_state]['coherence']
    
    @property
    def stability_factor(self) -> float:
        """Get consciousness stability factor."""
        return CONSCIOUSNESS_STATE_PROFILES[self.current_state]['stability']
    
    @property
    def receptivity_factor(self) -> float:
        """Get consciousness receptivity to entrainment."""
        return CONSCIOUSNESS_STATE_PROFILES[self.current_state]['receptivity']
    
    @property
    def computed_integration_capacity(self) -> int:
        """Get integration capacity with overrides."""
        if self.integration_capacity is not None:
            return self.integration_capacity
        
        base = NEURAL_SENSITIVITY_PROFILES[self.sensitivity_level]['integration_capacity']
        exp_bonus = {'beginner': 0, 'intermediate': 1, 'advanced': 2, 'expert': 3}
        return base + exp_bonus.get(self.experience_level, 0)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS INTENTION WEAVER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessIntentionWeaver:
    """
    Consciousness-aware parameter weaver that adapts all session parameters
    based on healing intentions and individual neural architecture.
    """
    
    def __init__(self, intention: str, user_state: Dict[str, Any]):
        """
        Initialize consciousness intention weaver.
        
        Args:
            intention: Consciousness intention ('neutral', 'release', 'focus', 'integrate', 'creativity')
            user_state: User state dictionary with neural architecture information
        """
        self.intention = self._validate_intention(intention)
        self.user_state = user_state
        self.neural_profile = self._create_neural_profile(user_state)
        self.intention_profile = self._get_intention_profile(self.intention)
        
        logging.info(f"Consciousness weaver initialized: intention={self.intention}, "
                    f"sensitivity={self.neural_profile.sensitivity_level}, "
                    f"experience={self.neural_profile.experience_level}")
    
    def _validate_intention(self, intention: str) -> str:
        """Validate and normalize consciousness intention."""
        if not isinstance(intention, str):
            intention = str(intention)
        
        intention = intention.lower().strip()
        valid_intentions = {'neutral', 'release', 'focus', 'integrate', 'creativity', 'healing'}
        
        if intention not in valid_intentions:
            logging.warning(f"Unknown intention '{intention}', using 'neutral'")
            intention = 'neutral'
        
        return intention
    
    def _create_neural_profile(self, user_state: Dict[str, Any]) -> NeuralProfile:
        """Create comprehensive neural profile from user state."""
        return NeuralProfile(
            sensitivity_level=user_state.get('sensitivity_level', 'standard'),
            current_state=user_state.get('current_state', 'neutral'),
            experience_level=user_state.get('experience_level', 'beginner'),
            integration_capacity=user_state.get('integration_capacity'),
            custom_factors=user_state.get('custom_factors', {})
        )
    
    def _get_intention_profile(self, intention: str) -> Dict[str, Any]:
        """Get intention-specific parameter profiles."""
        profiles = {
            'neutral': {
                'carrier_shift': 0,
                'warmth_factor': 1.0,
                'coherence_boost': 1.0,
                'transition_gentleness': 1.0,
                'duration_modifier': 1.0
            },
            'release': {
                'carrier_shift': -15,
                'warmth_factor': 1.15,
                'coherence_boost': 1.3,
                'transition_gentleness': 1.4,
                'duration_modifier': 1.1
            },
            'focus': {
                'carrier_shift': 10,
                'warmth_factor': 0.95,
                'coherence_boost': 1.1,
                'transition_gentleness': 0.9,
                'duration_modifier': 0.95
            },
            'integrate': {
                'carrier_shift': 5,
                'warmth_factor': 1.05,
                'coherence_boost': 1.25,
                'transition_gentleness': 1.2,
                'duration_modifier': 1.05
            },
            'creativity': {
                'carrier_shift': 8,
                'warmth_factor': 1.08,
                'coherence_boost': 1.2,
                'transition_gentleness': 1.1,
                'duration_modifier': 1.0
            },
            'healing': {
                'carrier_shift': -10,
                'warmth_factor': 1.2,
                'coherence_boost': 1.4,
                'transition_gentleness': 1.5,
                'duration_modifier': 1.15
            }
        }
        
        return profiles.get(intention, profiles['neutral'])
    
    def adapt_carrier_frequencies(self, base_carriers: List[float]) -> List[float]:
        """
        Adapt carrier frequencies based on intention and neural profile.
        
        Args:
            base_carriers: List of base carrier frequencies
        
        Returns:
            List of adapted carrier frequencies
        """
        if not base_carriers:
            return []
        
        intention_shift = self.intention_profile['carrier_shift']
        warmth_factor = self.intention_profile['warmth_factor']
        
        # Neural sensitivity adjustment - more sensitive users get lower frequencies
        sensitivity_adjustment = (self.neural_profile.sensitivity_factor - 1.0) * -20
        
        # Experience level adjustment - beginners get gentler frequencies
        experience_adjustment = 0
        if self.neural_profile.experience_level == 'beginner':
            experience_adjustment = -5
        elif self.neural_profile.experience_level in ['advanced', 'expert']:
            experience_adjustment = 5
        
        adapted_carriers = []
        for carrier in base_carriers:
            # Apply all adjustments
            adapted = carrier + intention_shift + sensitivity_adjustment + experience_adjustment
            adapted *= warmth_factor
            
            # Ensure within safe range
            adapted = np.clip(adapted, SAFE_RANGES['carrier_frequency'][0], 
                            SAFE_RANGES['carrier_frequency'][1])
            adapted_carriers.append(adapted)
        
        logging.debug(f"Adapted carriers: {base_carriers} -> {adapted_carriers}")
        return adapted_carriers
    
    def adapt_beat_frequencies(self, base_beats: List[float]) -> List[float]:
        """
        Adapt beat frequencies based on neural architecture and consciousness state.
        
        Args:
            base_beats: List of base beat frequencies
        
        Returns:
            List of adapted beat frequencies
        """
        if not base_beats:
            return []
        
        adapted_beats = []
        for beat in base_beats:
            # Start with base frequency
            adapted = beat
            
            # Adjust for current consciousness state
            if self.neural_profile.current_state == 'agitated':
                adapted *= 0.8  # Slower beats for agitated states
            elif self.neural_profile.current_state in ['focused', 'meditative']:
                adapted *= 1.0  # Keep as-is for good states
            elif self.neural_profile.current_state == 'anxious':
                adapted *= 0.7  # Much slower for anxiety
            elif self.neural_profile.current_state == 'tired':
                adapted *= 1.1  # Slightly faster to energize
            
            # Adjust for experience level
            if self.neural_profile.experience_level == 'beginner':
                adapted *= 0.9  # Gentler for beginners
            elif self.neural_profile.experience_level == 'expert':
                adapted *= 1.1  # Can handle more intensity
            
            # Ensure within safe range
            adapted = np.clip(adapted, SAFE_RANGES['beat_frequency'][0], 
                            SAFE_RANGES['beat_frequency'][1])
            adapted_beats.append(adapted)
        
        return adapted_beats
    
    def consciousness_aware_transition(self, t: np.ndarray, start_freq: float, 
                                     end_freq: float, transition_type: Union[str, TransitionType]) -> np.ndarray:
        """
        Generate consciousness-aware frequency transitions that respect neural oscillation patterns.
        
        Args:
            t: Time vector
            start_freq: Starting frequency
            end_freq: Ending frequency
            transition_type: Type of transition curve
        
        Returns:
            Frequency array with consciousness-aware transition
        """
        if len(t) == 0:
            return np.array([], dtype=np.float64)
        
        # Convert string to enum if needed
        if isinstance(transition_type, str):
            try:
                transition_type = TransitionType(transition_type)
            except ValueError:
                logging.warning(f"Unknown transition type '{transition_type}', using linear")
                transition_type = TransitionType.LINEAR
        
        # Normalize time to [0, 1]
        if len(t) > 1:
            normalized_t = (t - t[0]) / (t[-1] - t[0])
        else:
            normalized_t = np.array([0.0])
        
        # Generate base transition curve
        if transition_type == TransitionType.THETA_GATEWAY:
            # Alpha -> Theta descent with natural theta burst patterns
            sigmoid = 1 / (1 + np.exp(-5 * (normalized_t - 0.5)))
            theta_bursts = 1 + 0.08 * np.sin(2 * np.pi * 6 * normalized_t)  # 6Hz theta
            transition_curve = sigmoid * theta_bursts
        
        elif transition_type == TransitionType.GAMMA_EMERGENCE:
            # Natural gamma emergence pattern during insight states
            emergence = np.power(normalized_t, 0.3)  # Fast initial rise
            gamma_modulation = 1 + 0.03 * np.sin(2 * np.pi * 40 * normalized_t)  # 40Hz gamma
            transition_curve = emergence * gamma_modulation
        
        elif transition_type == TransitionType.DELTA_DESCENT:
            # Natural descent to deep sleep states
            exponential = 1 - np.exp(-3 * normalized_t)
            delta_waves = 1 + 0.05 * np.sin(2 * np.pi * 2 * normalized_t)  # 2Hz delta
            transition_curve = exponential * delta_waves
        
        elif transition_type == TransitionType.BREATH_SYNC:
            # Synchronize with natural breathing rhythm
            breathing_rate = 0.25  # 4 breaths per minute at rest
            breath_curve = 0.5 * (1 + np.sin(2 * np.pi * breathing_rate * (t - t[0])))
            transition_curve = normalized_t + 0.1 * breath_curve * (1 - normalized_t) * normalized_t
        
        elif transition_type == TransitionType.HEART_SYNC:
            # Synchronize with heart rate variability
            hrv_freq = 0.1  # HRV frequency ~0.1 Hz
            hrv_modulation = 0.05 * np.sin(2 * np.pi * hrv_freq * (t - t[0]))
            transition_curve = normalized_t + hrv_modulation * (1 - normalized_t) * normalized_t
        
        elif transition_type == TransitionType.SINUSOIDAL:
            # Sinusoidal with breathing sync
            breath_sync = 1 + 0.03 * np.sin(2 * np.pi * 0.25 * (t - t[0]))
            transition_curve = 0.5 * (1 + np.sin(np.pi * (normalized_t - 0.5))) * breath_sync
        
        elif transition_type == TransitionType.EXPONENTIAL:
            # Exponential transition
            if start_freq == 0 or end_freq == 0:
                transition_curve = normalized_t  # Fallback to linear
            else:
                ratio = end_freq / start_freq
                if ratio > 0:
                    log_ratio = np.log(ratio)
                    transition_curve = (np.exp(log_ratio * normalized_t) - 1) / (np.exp(log_ratio) - 1)
                else:
                    transition_curve = normalized_t  # Fallback to linear
        
        else:  # LINEAR or unknown
            transition_curve = normalized_t
        
        # Apply neural sensitivity smoothing
        gentleness = self.intention_profile['transition_gentleness']
        sensitivity_smoothing = self.neural_profile.sensitivity_factor
        
        if sensitivity_smoothing > 1.0 or gentleness > 1.0:
            # Apply additional smoothing for sensitive users
            smoothing_factor = max(sensitivity_smoothing, gentleness)
            # Use power function to create gentler transitions
            if smoothing_factor > 1.0:
                transition_curve = np.power(transition_curve, 1.0 / smoothing_factor)
        
        # Apply processing speed adjustment
        speed_factor = self.neural_profile.processing_speed
        if speed_factor != 1.0 and len(transition_curve) > 1:
            # Adjust transition timing while preserving endpoints
            adjusted_t = np.power(normalized_t, 1.0 / speed_factor)
            transition_curve = np.interp(normalized_t, adjusted_t, transition_curve)
        
        # Normalize curve to [0, 1] range
        if len(transition_curve) > 0:
            curve_min = np.min(transition_curve)
            curve_max = np.max(transition_curve)
            curve_range = curve_max - curve_min
            
            if curve_range > 1e-10:
                transition_curve = (transition_curve - curve_min) / curve_range
            else:
                transition_curve = normalized_t  # Fallback to linear
        
        # Scale to target frequency range
        result = start_freq + (end_freq - start_freq) * transition_curve
        
        # Ensure exact start and end values
        if len(result) > 0:
            result[0] = start_freq
            if len(result) > 1:
                result[-1] = end_freq
        
        return result.astype(np.float64)
    
    def adapt_duration(self, base_duration: float) -> float:
        """
        Adapt phase duration based on neural profile and intention.
        
        Args:
            base_duration: Base duration in seconds
        
        Returns:
            Adapted duration in seconds
        """
        # Start with intention modifier
        adapted = base_duration * self.intention_profile['duration_modifier']
        
        # Apply neural sensitivity extension
        sensitivity_extension = NEURAL_SENSITIVITY_PROFILES[self.neural_profile.sensitivity_level]['duration_extension']
        adapted *= sensitivity_extension
        
        # Apply experience level adjustment
        if self.neural_profile.experience_level == 'beginner':
            adapted *= 1.1  # Longer phases for beginners
        elif self.neural_profile.experience_level == 'expert':
            adapted *= 0.95  # Slightly shorter for experts
        
        # Ensure within reasonable bounds
        adapted = np.clip(adapted, SAFE_RANGES['phase_duration'][0], 
                         SAFE_RANGES['phase_duration'][1])
        
        return adapted
    
    def adapt_volume_levels(self, base_levels: Dict[str, float]) -> Dict[str, float]:
        """
        Adapt volume levels based on neural sensitivity and current state.
        
        Args:
            base_levels: Dictionary of volume levels by component type
        
        Returns:
            Dictionary of adapted volume levels
        """
        adapted = base_levels.copy()
        
        # Get noise tolerance factor
        noise_tolerance = NEURAL_SENSITIVITY_PROFILES[self.neural_profile.sensitivity_level]['noise_tolerance']
        
        # Apply sensitivity-based volume adjustment
        sensitivity_factor = self.neural_profile.sensitivity_factor
        volume_adjustment = 1.0 / sensitivity_factor  # More sensitive = lower volume
        
        # Apply current state adjustment
        state_adjustment = 1.0
        if self.neural_profile.current_state == 'agitated':
            state_adjustment = 0.7  # Lower volume for agitation
        elif self.neural_profile.current_state == 'anxious':
            state_adjustment = 0.6  # Much lower for anxiety
        elif self.neural_profile.current_state == 'focused':
            state_adjustment = 1.1  # Slightly higher for focus
        
        # Apply adjustments to all levels
        for key, value in adapted.items():
            if 'noise' in key.lower():
                # Extra adjustment for noise components
                adapted[key] = value * noise_tolerance * volume_adjustment * state_adjustment
            else:
                adapted[key] = value * volume_adjustment * state_adjustment
            
            # Ensure within safe range
            adapted[key] = np.clip(adapted[key], 0.0, SAFE_RANGES['volume_level'][1])
        
        return adapted

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ENTRAINMENT SESSION BUILDER
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class EntrainmentSession:
    """
    Consciousness-aware neural entrainment session builder with biofield intelligence.
    
    This class orchestrates the creation of complete entrainment sessions with
    multiple phases, layers, modulations, and consciousness adaptations.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize entrainment session builder.
        
        Args:
            config: Session configuration dictionary
        """
        self.config = self._validate_config(config)
        self.sample_rate = float(self.config.get('sample_rate', 44100))
        self.audio = np.array([], dtype=np.float32).reshape(0, 2)  # Empty stereo array
        self._current_position = 0
        
        # Initialize consciousness weaver
        user_state = self.config.get('user_state', {})
        intention = self.config.get('intention', 'neutral')
        self.consciousness_weaver = ConsciousnessIntentionWeaver(intention, user_state)
        
        # Session metadata
        self.metadata = {
            'total_duration': 0.0,
            'phases_built': 0,
            'coherence_scores': [],
            'safety_checks': [],
            'adaptations_applied': []
        }
        
        logging.info(f"EntrainmentSession initialized: intention='{intention}', "
                    f"sample_rate={self.sample_rate}Hz, "
                    f"neural_profile={self.consciousness_weaver.neural_profile.sensitivity_level}")
    
    def _validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and sanitize session configuration."""
        validated = config.copy()
        
        # Ensure required fields
        if 'phases' not in validated:
            raise ValueError("Configuration must include 'phases' list")
        
        if not isinstance(validated['phases'], list):
            raise ValueError("'phases' must be a list")
        
        # Validate sample rate
        sample_rate = validated.get('sample_rate', 44100)
        if not isinstance(sample_rate, (int, float)) or sample_rate <= 0:
            logging.warning(f"Invalid sample rate {sample_rate}, using 44100")
            validated['sample_rate'] = 44100
        
        # Validate phase configurations
        for i, phase in enumerate(validated['phases']):
            if not isinstance(phase, dict):
                raise ValueError(f"Phase {i} must be a dictionary")
            
            if 'duration' not in phase:
                raise ValueError(f"Phase {i} missing required 'duration' field")
            
            if phase['duration'] <= 0:
                raise ValueError(f"Phase {i} duration must be positive")
        
        return validated
    
    def _allocate_audio_buffer(self) -> None:
        """Pre-allocate audio buffer based on estimated total duration."""
        total_duration = 0.0
        
        # Calculate total duration with consciousness adaptations
        for phase in self.config['phases']:
            base_duration = phase['duration']
            adapted_duration = self.consciousness_weaver.adapt_duration(base_duration)
            total_duration += adapted_duration
        
        # Add buffer for integration phase and ambient layers
        if self.config.get('include_integration', False):
            integration_duration = self.config.get('integration_duration', 180)
            total_duration += integration_duration * 1.3  # Buffer for extensions
        
        # Add 10% safety buffer
        total_duration *= 1.1
        
        # Allocate buffer
        total_samples = int(total_duration * self.sample_rate)
        self.audio = np.zeros((total_samples, 2), dtype=np.float32)
        self._current_position = 0
        
        logging.info(f"Allocated audio buffer: {total_duration:.1f}s ({total_samples} samples)")
    
    def generate_phase(self, phase: Dict[str, Any]) -> np.ndarray:
        """
        Generate consciousness-aware audio phase with biofield intelligence.
        
        Args:
            phase: Phase configuration dictionary
        
        Returns:
            Generated stereo audio for the phase
        """
        # Adapt duration for consciousness and neural profile
        base_duration = phase['duration']
        adapted_duration = self.consciousness_weaver.adapt_duration(base_duration)
        
        num_samples = int(self.sample_rate * adapted_duration)
        if num_samples == 0:
            return np.zeros((0, 2), dtype=np.float32)
        
        t = np.linspace(0, adapted_duration, num_samples, endpoint=False)
        
        # Get layers (ensure it's a list)
        layers = phase.get('layers', [])
        if not isinstance(layers, list):
            # Convert single layer to list
            layers = [layers] if layers else [{'carrier': phase.get('carrier', 200.0)}]
        
        if not layers:
            # Create default layer from phase parameters
            default_layer = {'carrier': phase.get('carrier', 200.0)}
            for key in ['beat', 'start_beat', 'end_beat', 'harmonics', 'carrier_type']:
                if key in phase:
                    default_layer[key] = phase[key]
            layers = [default_layer]
        
        # Consciousness-aware carrier adaptation
        base_carriers = [layer.get('carrier', 200.0) for layer in layers]
        adapted_carriers = self.consciousness_weaver.adapt_carrier_frequencies(base_carriers)
        
        # Update layers with adapted carriers
        for i, layer in enumerate(layers):
            if i < len(adapted_carriers):
                layer['adapted_carrier'] = adapted_carriers[i]
        
        # Beat frequency adaptation
        beat_freqs = []
        for layer in layers:
            if phase.get('type', 'static') == 'static':
                beat = layer.get('beat', 0.0)
            else:
                start_beat = layer.get('start_beat', 0.0)
                end_beat = layer.get('end_beat', 0.0)
                beat = (start_beat + end_beat) / 2  # Average for harmony check
            beat_freqs.append(beat)
        
        adapted_beats = self.consciousness_weaver.adapt_beat_frequencies(beat_freqs)
        
        # Assess harmonic relationships
        is_harmonic, harmony_message = signal_generator.assess_intermodulation_harmony(adapted_beats)
        if not is_harmonic:
            logging.warning(f"Phase harmonic analysis: {harmony_message}")
            self.metadata['safety_checks'].append(f"Harmonic warning: {harmony_message}")
        
        # Initialize stereo accumulators
        left_total = np.zeros(num_samples, dtype=np.float32)
        right_total = np.zeros(num_samples, dtype=np.float32)
        all_layers = []
        
        # Generate each layer
        for layer_idx, layer in enumerate(layers):
            layer_audio = self._generate_layer(layer, phase, t, adapted_duration)
            
            if layer_audio is not None and len(layer_audio) == len(left_total):
                if layer_audio.ndim == 1:
                    # Mono layer - add to both channels
                    left_total += layer_audio
                    right_total += layer_audio
                    all_layers.append(layer_audio)
                elif layer_audio.ndim == 2 and layer_audio.shape[1] >= 2:
                    # Stereo layer
                    left_total += layer_audio[:, 0]
                    right_total += layer_audio[:, 1]
                    all_layers.extend([layer_audio[:, 0], layer_audio[:, 1]])
        
        # Consciousness-aware coherence check and adjustment
        if all_layers:
            coherence_score = signal_generator.consciousness_coherence_check(
                all_layers, self.consciousness_weaver.intention, 0.7)
            
            if not coherence_score:
                logging.info("Applying consciousness-aware coherence adjustment")
                adjusted_layers = signal_generator.coherence_adjust(
                    all_layers, 0.7, self.consciousness_weaver.intention)
                
                # Update totals with adjusted layers
                if len(adjusted_layers) >= 2:
                    left_total = adjusted_layers[0]
                    right_total = adjusted_layers[1] if len(adjusted_layers) > 1 else adjusted_layers[0]
            
            self.metadata['coherence_scores'].append(coherence_score)
        
        # Combine into stereo
        stereo_phase = np.column_stack([left_total, right_total]).astype(np.float32)
        
        # Apply consciousness-aware normalization
        stereo_phase = self._biofield_aware_normalization(stereo_phase)
        
        # Apply modulations with consciousness awareness
        stereo_phase = self._apply_consciousness_modulations(stereo_phase, phase, t)
        
        # Apply monaural mode for deep states if beneficial
        stereo_phase = self._apply_consciousness_monaural(stereo_phase, phase, layers)
        
        self.metadata['phases_built'] += 1
        logging.debug(f"Generated phase {self.metadata['phases_built']}: {adapted_duration:.1f}s")
        
        return stereo_phase
    
    def _generate_layer(self, layer: Dict[str, Any], phase: Dict[str, Any], 
                       t: np.ndarray, duration: float) -> Optional[np.ndarray]:
        """Generate individual layer with consciousness awareness."""
        carrier_freq = layer.get('adapted_carrier', layer.get('carrier', 200.0))
        carrier_type = CarrierType(layer.get('carrier_type', 'sine'))
        
        # Generate beat frequency progression
        beat_progression = self._generate_beat_progression(layer, phase, t, duration)
        
        if len(beat_progression) == 0:
            return None
        
        # Generate base carrier wave
        if carrier_type == CarrierType.SINE:
            base_wave = signal_generator.generate_consciousness_aware_carrier_wave(
                carrier_freq, duration, self.sample_rate, self.consciousness_weaver.intention)
        elif carrier_type == CarrierType.PINK_NOISE:
            base_wave = signal_generator.generate_biofield_pink_noise(
                len(t), self.sample_rate, self.consciousness_weaver.intention)
        elif carrier_type == CarrierType.BROWN_NOISE:
            base_wave = signal_generator.generate_brown_noise(
                len(t), self.sample_rate, self.consciousness_weaver.intention)
        elif carrier_type == CarrierType.WHITE_NOISE:
            base_wave = signal_generator.generate_white_noise(len(t))
        else:
            # Default to consciousness-aware carrier
            base_wave = signal_generator.generate_consciousness_aware_carrier_wave(
                carrier_freq, duration, self.sample_rate, self.consciousness_weaver.intention)
        
        # Apply binaural beats if specified
        if len(beat_progression) > 0 and np.any(beat_progression > 0):
            # Generate binaural beat pair
            left_freqs = np.full_like(t, carrier_freq)
            right_freqs = left_freqs + beat_progression
            
            # Apply consciousness-aware FM modulation if specified
            fm_depth = layer.get('fm_depth', 0)
            fm_rate = layer.get('fm_rate', 0)
            
            if fm_depth > 0 and fm_rate > 0:
                left_freqs = signal_generator.apply_fm_modulation(
                    left_freqs, fm_depth, fm_rate, t, self.consciousness_weaver.intention)
                right_freqs = signal_generator.apply_fm_modulation(
                    right_freqs, fm_depth, fm_rate, t, self.consciousness_weaver.intention)
            
            # Generate phase-locked stereo signals
            left_phases = 2 * np.pi * np.cumsum(left_freqs) / self.sample_rate
            right_phases = 2 * np.pi * np.cumsum(right_freqs) / self.sample_rate
            
            if carrier_type == CarrierType.SINE:
                left_wave = np.sin(left_phases)
                right_wave = np.sin(right_phases)
            else:
                # For noise carriers, modulate the base noise
                left_wave = base_wave * np.cos(left_phases)
                right_wave = base_wave * np.cos(right_phases)
            
            return np.column_stack([left_wave, right_wave]).astype(np.float32)
        else:
            # No beat frequencies - return mono signal
            return base_wave.astype(np.float32)
    
    def _generate_beat_progression(self, layer: Dict[str, Any], phase: Dict[str, Any], 
                                  t: np.ndarray, duration: float) -> np.ndarray:
        """Generate consciousness-aware beat frequency progression."""
        phase_type = phase.get('type', 'static')
        
        if phase_type == 'static':
            beat_freq = layer.get('beat', 0.0)
            # Apply consciousness adaptation
            adapted_beats = self.consciousness_weaver.adapt_beat_frequencies([beat_freq])
            return np.full_like(t, adapted_beats[0] if adapted_beats else beat_freq)
        
        else:  # ramp type
            start_beat = layer.get('start_beat', 0.0)
            end_beat = layer.get('end_beat', 0.0)
            
            # Apply consciousness adaptation
            adapted_beats = self.consciousness_weaver.adapt_beat_frequencies([start_beat, end_beat])
            if len(adapted_beats) >= 2:
                start_beat, end_beat = adapted_beats[0], adapted_beats[1]
            
            # Get transition type
            animation_type = phase.get('animation_type', 'linear')
            try:
                transition_type = TransitionType(animation_type)
            except ValueError:
                transition_type = TransitionType.LINEAR
            
            # Generate consciousness-aware transition
            return self.consciousness_weaver.consciousness_aware_transition(
                t, start_beat, end_beat, transition_type)
    
    def _apply_consciousness_modulations(self, audio: np.ndarray, phase: Dict[str, Any], 
                                       t: np.ndarray) -> np.ndarray:
        """Apply consciousness-aware modulations to audio."""
        if len(audio) == 0:
            return audio
        
        # Apply isochronic pulses with sensitivity adjustment
        if phase.get('isochronic', False):
            iso_freq = phase.get('isochronic_freq', 0)
            if iso_freq > 0:
                # Adjust duty cycle for sensitive users
                sensitivity_factor = self.consciousness_weaver.neural_profile.sensitivity_factor
                duty_cycle = 0.7 if sensitivity_factor > 1.0 else 0.5
                
                for channel in range(audio.shape[1]):
                    audio[:, channel] = signal_generator.apply_isochronic(
                        audio[:, channel], iso_freq, self.sample_rate, duty_cycle)
        
        # Apply bilateral panning with consciousness awareness
        if phase.get('bilateral', False):
            pan_freq = phase.get('bilateral_freq', 0)
            if pan_freq > 0:
                # Adjust panning speed for sensitive users
                sensitivity_factor = self.consciousness_weaver.neural_profile.sensitivity_factor
                if sensitivity_factor > 1.0:
                    pan_freq *= 0.8  # Slower panning for sensitive users
                
                audio = signal_generator.apply_bilateral_panning(
                    audio, pan_freq, self.sample_rate, t)
        
        return audio
    
    def _apply_consciousness_monaural(self, audio: np.ndarray, phase: Dict[str, Any], 
                                    layers: List[Dict[str, Any]]) -> np.ndarray:
        """Apply consciousness-aware monaural processing when beneficial."""
        if len(audio) == 0:
            return audio
        
        # Check for deep delta layers
        deep_delta_layers = [layer for layer in layers 
                           if layer.get('beat', 0) < 4 or layer.get('end_beat', 0) < 4]
        
        # Apply monaural for deep states with low coherence users
        if deep_delta_layers and not phase.get('monaural', False):
            coherence = self.consciousness_weaver.neural_profile.current_coherence
            if coherence < 0.5:
                logging.debug("Applying consciousness-aware monaural processing for deep state")
                mono = np.mean(audio, axis=1)
                audio = np.column_stack([mono, mono])
        
        return audio
    
    def _biofield_aware_normalization(self, audio: np.ndarray, 
                                     preserve_phase_relationships: bool = True,
                                     target_max: float = 0.9) -> np.ndarray:
        """
        Normalization that preserves consciousness-relevant phase information and biofield coherence.
        
        Args:
            audio: Audio array to normalize
            preserve_phase_relationships: Whether to preserve phase relationships
            target_max: Target maximum amplitude
        
        Returns:
            Normalized audio array
        """
        if len(audio) == 0:
            return audio
        
        # Remove DC offset
        if audio.ndim == 1:
            audio = audio - np.mean(audio)
        else:
            audio = audio - np.mean(audio, axis=0)
        
        if preserve_phase_relationships:
            # Preserve relative phase information for biofield entrainment
            max_amp = np.max(np.abs(audio))
            if max_amp > target_max:
                # Only normalize if approaching clipping
                normalization_factor = target_max / max_amp
                audio = audio * normalization_factor
                
                # Log significant normalizations
                if normalization_factor < 0.8:
                    logging.debug(f"Applied significant normalization: {normalization_factor:.3f}")
        else:
            # Standard normalization
            max_amp = np.max(np.abs(audio))
            if max_amp > 0:
                audio = audio * (target_max / max_amp)
        
        return audio
    
    def build(self) -> None:
        """
        Build complete consciousness-aware entrainment session.
        
        This orchestrates the entire session creation process including
        phases, ambient layers, integration, and final processing.
        """
        logging.info("Building consciousness-aware entrainment session...")
        
        # Pre-allocate audio buffer
        self._allocate_audio_buffer()
        
        # Generate main phases
        for i, phase in enumerate(self.config['phases']):
            try:
                phase_audio = self.generate_phase(phase)
                
                if len(phase_audio) > 0:
                    # Add phase to main audio buffer
                    end_pos = self._current_position + len(phase_audio)
                    if end_pos <= len(self.audio):
                        self.audio[self._current_position:end_pos] = phase_audio
                        self._current_position = end_pos
                    else:
                        # Buffer overflow - concatenate instead
                        logging.warning("Audio buffer overflow, concatenating remaining phases")
                        remaining_audio = self.audio[:self._current_position]
                        self.audio = np.vstack([remaining_audio, phase_audio])
                        self._current_position = len(self.audio)
                
                logging.info(f"Completed phase {i+1}/{len(self.config['phases'])}")
                
            except Exception as e:
                logging.error(f"Error generating phase {i+1}: {e}")
                self.metadata['safety_checks'].append(f"Phase {i+1} error: {str(e)}")
                continue
        
        # Add ambient layers
        self._add_ambient_layers()
        
        # Add consciousness-aware background noise
        self._add_consciousness_noise()
        
        # Add integration phase if requested
        if self.config.get('include_integration', False):
            self._add_integration_phase()
        
        # Final processing
        self._finalize_session()
        
        # Update metadata
        self.metadata['total_duration'] = len(self.audio) / self.sample_rate
        
        logging.info(f"Session completed: {self.metadata['total_duration']:.1f}s, "
                    f"{self.metadata['phases_built']} phases, "
                    f"intention={self.consciousness_weaver.intention}")
    
    def _add_ambient_layers(self) -> None:
        """Add consciousness-aware ambient layers to the session."""
        ambient_layers = self.config.get('ambient_layers', [])
        if not ambient_layers:
            return
        
        intention = self.consciousness_weaver.intention
        sensitivity_factor = self.consciousness_weaver.neural_profile.sensitivity_factor
        
        for ambient in ambient_layers:
            ambient_type = ambient.get('type', 'sine')
            freq = ambient.get('freq', 432.0)  # Default to 432Hz (healing frequency)
            level = ambient.get('level', 0.1)
            
            # Adapt level for consciousness and sensitivity
            adapted_levels = self.consciousness_weaver.adapt_volume_levels({'ambient': level})
            adjusted_level = adapted_levels['ambient']
            
            if adjusted_level > 0 and self._current_position > 0:
                t = np.linspace(0, self._current_position / self.sample_rate, 
                              self._current_position, endpoint=False)
                
                if ambient_type == 'sine':
                    ambient_wave = adjusted_level * np.sin(2 * np.pi * freq * t)
                elif ambient_type == 'pink':
                    ambient_wave = signal_generator.generate_biofield_pink_noise(
                        self._current_position, self.sample_rate, intention) * adjusted_level
                elif ambient_type == 'brown':
                    ambient_wave = signal_generator.generate_brown_noise(
                        self._current_position, self.sample_rate, intention) * adjusted_level
                else:
                    continue  # Skip unknown types
                
                # Add to both channels
                ambient_stereo = np.column_stack([ambient_wave, ambient_wave])
                self.audio[:self._current_position] += ambient_stereo
                
                logging.debug(f"Added ambient layer: {ambient_type} at {freq}Hz, level={adjusted_level:.3f}")
    
    def _add_consciousness_noise(self) -> None:
        """Add consciousness-aware background noise."""
        pink_level = self.config.get('pink_noise_level', 0.0)
        if pink_level <= 0:
            return
        
        # Adapt noise level for consciousness and sensitivity
        adapted_levels = self.consciousness_weaver.adapt_volume_levels({'pink_noise': pink_level})
        adjusted_level = adapted_levels['pink_noise']
        
        if adjusted_level > 0 and self._current_position > 0:
            intention = self.consciousness_weaver.intention
            pink_noise = signal_generator.generate_biofield_pink_noise(
                self._current_position, self.sample_rate, intention, 0.2)
            
            pink_stereo = np.column_stack([pink_noise, pink_noise]) * adjusted_level
            self.audio[:self._current_position] += pink_stereo
            
            logging.debug(f"Added consciousness-aware pink noise: level={adjusted_level:.3f}")
    
    def _add_integration_phase(self) -> None:
        """Add consciousness-aware integration phase for session completion."""
        base_duration = self.config.get('integration_duration', 180)  # 3 minutes default
        adapted_duration = self.consciousness_weaver.adapt_duration(base_duration)
        
        num_samples = int(self.sample_rate * adapted_duration)
        
        if self._current_position + num_samples <= len(self.audio):
            # Use pre-allocated space
            integration_start = self._current_position
            integration_end = self._current_position + num_samples
            
            # Generate gentle integration ambience
            t_integration = np.linspace(0, adapted_duration, num_samples, endpoint=False)
            
            # Exponential fade-out with consciousness-aware frequency
            fade_curve = np.exp(-2 * t_integration / adapted_duration)
            
            # Use healing frequency (528 Hz) for integration
            healing_freq = 528.0  # Solfeggio healing frequency
            integration_level = 0.05  # Gentle level
            
            # Adapt level for consciousness
            adapted_levels = self.consciousness_weaver.adapt_volume_levels({'integration': integration_level})
            adjusted_level = adapted_levels['integration']
            
            integration_wave = adjusted_level * np.sin(2 * np.pi * healing_freq * t_integration) * fade_curve
            integration_stereo = np.column_stack([integration_wave, integration_wave])
            
            self.audio[integration_start:integration_end] = integration_stereo
            self._current_position = integration_end
            
            logging.info(f"Added consciousness integration phase: {adapted_duration:.1f}s")
        else:
            # Concatenate if no space
            logging.warning("Integration phase exceeds buffer, concatenating")
            integration_audio = np.zeros((num_samples, 2), dtype=np.float32)
            # Add gentle integration content here if needed
            self.audio = np.vstack([self.audio[:self._current_position], integration_audio])
    
    def _finalize_session(self) -> None:
        """Finalize session with consciousness-aware processing."""
        if self._current_position == 0:
            logging.warning("No audio generated for session")
            return
        
        # Trim to actual used length
        self.audio = self.audio[:self._current_position]
        
        # Apply final biofield-aware normalization
        self.audio = self._biofield_aware_normalization(self.audio, preserve_phase_relationships=True)
        
        # Final consciousness coherence check
        if len(self.audio) > 0:
            left_channel = self.audio[:, 0]
            right_channel = self.audio[:, 1]
            
            final_coherence = signal_generator.consciousness_coherence_check(
                [left_channel, right_channel], self.consciousness_weaver.intention, 0.7)
            
            if not final_coherence:
                logging.warning("Final session coherence below target")
                self.metadata['safety_checks'].append("Final coherence below target")
            else:
                logging.info("Final consciousness coherence check passed")
        
        # Check for any audio anomalies
        if np.any(np.isnan(self.audio)) or np.any(np.isinf(self.audio)):
            logging.error("Audio contains NaN or Inf values, resetting problematic sections")
            self.audio = np.nan_to_num(self.audio, nan=0.0, posinf=0.0, neginf=0.0)
            self.metadata['safety_checks'].append("Audio anomaly correction applied")
        
        # Final clipping check
        max_amplitude = np.max(np.abs(self.audio))
        if max_amplitude > 0.98:
            logging.warning(f"Audio approaching clipping: {max_amplitude:.3f}")
            self.audio *= (0.9 / max_amplitude)  # Apply safety limiting
            self.metadata['safety_checks'].append(f"Clipping prevention applied: {max_amplitude:.3f}")
    
    def save(self, filename: str, format: str = 'wav', bit_depth: int = 16) -> None:
        """
        Save consciousness-aware session to audio file.
        
        Args:
            filename: Output filename
            format: Audio format ('wav' supported)
            bit_depth: Bit depth (16 or 32)
        """
        if len(self.audio) == 0:
            raise ValueError("No audio to save - build session first")
        
        if format.lower() != 'wav':
            raise ValueError("Only WAV format currently supported")
        
        if bit_depth == 16:
            # Scale to 16-bit integer range with safety margin
            audio_int = np.clip(self.audio * 32767 * 0.95, -32767, 32767).astype(np.int16)
        elif bit_depth == 32:
            # Scale to 32-bit integer range with safety margin
            audio_int = np.clip(self.audio * 2147483647 * 0.95, -2147483647, 2147483647).astype(np.int32)
        else:
            raise ValueError("Bit depth must be 16 or 32")
        
        try:
            wavfile.write(filename, int(self.sample_rate), audio_int)
            
            # Log session summary
            duration = len(self.audio) / self.sample_rate
            logging.info(f"Saved consciousness-aware session: {filename}")
            logging.info(f"Duration: {duration:.1f}s, Intention: {self.consciousness_weaver.intention}")
            logging.info(f"Neural Profile: {self.consciousness_weaver.neural_profile.sensitivity_level}")
            logging.info(f"Phases: {self.metadata['phases_built']}, "
                        f"Safety Checks: {len(self.metadata['safety_checks'])}")
            
        except Exception as e:
            logging.error(f"Error saving audio file: {e}")
            raise
    
    def get_metadata(self) -> Dict[str, Any]:
        """Get comprehensive session metadata."""
        return {
            **self.metadata,
            'intention': self.consciousness_weaver.intention,
            'neural_profile': {
                'sensitivity_level': self.consciousness_weaver.neural_profile.sensitivity_level,
                'current_state': self.consciousness_weaver.neural_profile.current_state,
                'experience_level': self.consciousness_weaver.neural_profile.experience_level,
                'sensitivity_factor': self.consciousness_weaver.neural_profile.sensitivity_factor,
                'processing_speed': self.consciousness_weaver.neural_profile.processing_speed,
                'current_coherence': self.consciousness_weaver.neural_profile.current_coherence
            },
            'session_config': {
                'sample_rate': self.sample_rate,
                'total_samples': len(self.audio),
                'channels': self.audio.shape[1] if len(self.audio) > 0 else 0
            }
        }

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULE INITIALIZATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Set up module-level logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Module metadata
__version__ = "2.0.0"
__author__ = "Dr. KB Jama"
__license__ = "MIT"
__description__ = "Consciousness-aware neural entrainment session builder with biofield intelligence"

# Export public API
__all__ = [
    # Main classes
    'EntrainmentSession',
    'ConsciousnessIntentionWeaver',
    
    # Configuration classes
    'NeuralProfile',
    
    # Enums
    'TransitionType',
    'CarrierType',
    
    # Constants (for advanced users)
    'NEURAL_SENSITIVITY_PROFILES',
    'CONSCIOUSNESS_STATE_PROFILES',
    'EXPERIENCE_LEVEL_PROFILES',
]

logging.info(f"Neural Entrainment Session Builder v{__version__} initialized - "
            f"Consciousness-aware biofield intelligence framework ready")
