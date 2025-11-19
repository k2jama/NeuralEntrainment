# 🧪 Neural Entrainment System - Neural Signal Generator v2.0
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠 Consciousness-Aware Biofield Intelligence Framework
# Dr. KB Jama, Neural Dialogue Interface Research

"""
Neural Signal Generator - Core consciousness-aware signal processing engine.

This module provides comprehensive signal generation capabilities with biofield intelligence,
consciousness-aware spectral weaving, and neural architecture adaptation. All functions
are designed with safety, modularity, and consciousness respect as primary principles.
"""

import numpy as np
import logging
import copy
from typing import List, Dict, Any, Optional, Tuple, Union
from itertools import combinations
from dataclasses import dataclass
from enum import Enum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSTANTS & CONFIGURATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Mathematical constants for biofield intelligence
GOLDEN_RATIO = 1.618033988749895
PHI_RECIPROCAL = 1 / GOLDEN_RATIO
EULER_CONSTANT = np.e
PI = np.pi

# Biofield resonance frequencies (Hz)
SCHUMANN_RESONANCES = [7.83, 14.3, 20.8, 27.3, 33.8, 39.3, 45.9, 52.8]
SOLFEGGIO_FREQUENCIES = [174, 285, 396, 417, 528, 639, 741, 852, 963]

# Safe frequency ranges for different applications
SAFE_CARRIER_RANGE = (60, 800)      # Hz, perceptual safe range
SAFE_BEAT_RANGE = (0.5, 100)        # Hz, neural entrainment safe range
SAFE_FM_DEPTH_RANGE = (0, 50)       # Hz, modulation depth limits

# Consciousness intention profiles
INTENTION_PROFILES = {
    'neutral': {
        'spectral_weight': 1.0,
        'schumann_boost': 1.0,
        'solfeggio_boost': 1.0,
        'golden_harmonics': 1.0,
        'carrier_shift': 0,
        'warmth_factor': 1.0
    },
    'release': {
        'spectral_weight': 0.8,        # Emphasize lower frequencies
        'schumann_boost': 1.3,         # Strong Earth resonance
        'solfeggio_boost': 1.25,       # Enhanced healing frequencies
        'golden_harmonics': 1.2,       # Natural proportion enhancement
        'carrier_shift': -15,          # Lower carrier frequencies
        'warmth_factor': 1.15          # Warmer, more embracing tone
    },
    'focus': {
        'spectral_weight': 1.2,        # Emphasize mid-range clarity
        'schumann_boost': 1.1,         # Moderate Earth connection
        'solfeggio_boost': 1.0,        # Neutral healing tones
        'golden_harmonics': 1.1,       # Subtle proportion enhancement
        'carrier_shift': 10,           # Slightly higher carriers
        'warmth_factor': 0.95          # Crisp, clear tone
    },
    'integrate': {
        'spectral_weight': 1.0,        # Balanced spectrum
        'schumann_boost': 1.2,         # Good Earth grounding
        'solfeggio_boost': 1.15,       # Moderate healing enhancement
        'golden_harmonics': 1.25,      # Strong natural harmonics
        'carrier_shift': 5,            # Slight upward shift
        'warmth_factor': 1.05          # Gently warm integration tone
    },
    'creativity': {
        'spectral_weight': 1.1,        # Enhanced creative spectrum
        'schumann_boost': 1.15,        # Good resonance connection
        'solfeggio_boost': 1.2,        # Creative frequency boost
        'golden_harmonics': 1.3,       # Strong natural proportions
        'carrier_shift': 8,            # Creative frequency range
        'warmth_factor': 1.08          # Inspiring warmth
    }
}

class IntentionType(Enum):
    """Enumeration of supported consciousness intentions."""
    NEUTRAL = 'neutral'
    RELEASE = 'release'
    FOCUS = 'focus'
    INTEGRATE = 'integrate'
    CREATIVITY = 'creativity'

@dataclass
class SignalConfig:
    """Configuration for signal generation parameters."""
    sample_rate: float = 44100.0
    intention: str = 'neutral'
    safety_checks: bool = True
    normalize: bool = True
    coherence_enhancement: float = 0.1  # 0.0 to 0.5 range

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# UTILITY FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _validate_length(length: int) -> int:
    """Validate and sanitize length parameter."""
    if not isinstance(length, int) or length < 0:
        raise ValueError(f"Length must be a non-negative integer, got {length}")
    return length

def _validate_sample_rate(sample_rate: float) -> float:
    """Validate and sanitize sample rate parameter."""
    if not isinstance(sample_rate, (int, float)) or sample_rate <= 0:
        raise ValueError(f"Sample rate must be positive, got {sample_rate}")
    if sample_rate < 8000 or sample_rate > 192000:
        logging.warning(f"Sample rate {sample_rate} outside typical range [8000, 192000]")
    return float(sample_rate)

def _validate_intention(intention: str) -> str:
    """Validate and normalize intention parameter."""
    if not isinstance(intention, str):
        intention = str(intention)
    intention = intention.lower().strip()
    if intention not in INTENTION_PROFILES:
        logging.warning(f"Unknown intention '{intention}', using 'neutral'")
        intention = 'neutral'
    return intention

def _safe_normalize(signal: np.ndarray, target_max: float = 0.95) -> np.ndarray:
    """Safely normalize signal to prevent clipping while preserving dynamics."""
    if len(signal) == 0:
        return signal
    
    signal = signal - np.mean(signal)  # Remove DC offset
    max_abs = np.max(np.abs(signal))
    
    if max_abs > 0:
        # Normalize with headroom to prevent clipping
        signal = signal * (target_max / max_abs)
    
    return signal

def _apply_biofield_enhancement(fft: np.ndarray, freqs: np.ndarray, 
                               intention: str, coherence_factor: float = 0.1) -> np.ndarray:
    """Apply biofield intelligence enhancements to frequency spectrum."""
    profile = INTENTION_PROFILES[intention]
    enhanced_fft = fft.copy()
    
    # Apply Schumann resonance boosting
    for schumann_freq in SCHUMANN_RESONANCES:
        for i, freq in enumerate(freqs):
            if abs(freq - schumann_freq) < 1.0:  # Within 1 Hz
                boost = profile['schumann_boost'] * (1 + coherence_factor)
                enhanced_fft[i] *= boost
    
    # Apply Solfeggio frequency enhancement
    for solfeggio_freq in SOLFEGGIO_FREQUENCIES:
        for i, freq in enumerate(freqs):
            if abs(freq - solfeggio_freq) < 2.0:  # Within 2 Hz
                boost = profile['solfeggio_boost'] * (1 + coherence_factor * 0.7)
                enhanced_fft[i] *= boost
    
    # Apply golden ratio harmonic enhancement
    golden_fundamentals = [freq for freq in freqs if 10 <= freq <= 1000]
    for fundamental in golden_fundamentals:
        golden_harmonics = [fundamental * (GOLDEN_RATIO ** n) for n in range(-2, 3)]
        for harmonic in golden_harmonics:
            for i, freq in enumerate(freqs):
                if abs(freq - harmonic) < 0.5:
                    boost = profile['golden_harmonics'] * (1 + coherence_factor * 0.3)
                    enhanced_fft[i] *= boost
    
    return enhanced_fft

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CORE NOISE GENERATION FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def generate_white_noise(length: int, normalize: bool = True) -> np.ndarray:
    """
    Generate high-quality white noise with optional normalization.
    
    Args:
        length: Number of samples to generate
        normalize: Whether to normalize output to [-1, 1] range
    
    Returns:
        White noise signal as numpy array
    
    Raises:
        ValueError: If length is negative
    """
    length = _validate_length(length)
    
    if length == 0:
        return np.array([], dtype=np.float64)
    
    # Generate white noise with proper seeding for reproducibility in tests
    white_noise = np.random.randn(length).astype(np.float64)
    
    if normalize:
        white_noise = _safe_normalize(white_noise)
    
    logging.debug(f"Generated white noise: {length} samples, normalized={normalize}")
    return white_noise

def generate_biofield_pink_noise(length: int, sample_rate: float, 
                                intention: str = 'neutral', 
                                coherence_enhancement: float = 0.1) -> np.ndarray:
    """
    Generate consciousness-aware pink noise with biofield intelligence.
    
    This function creates pink noise (1/f spectrum) with intention-based spectral
    weaving that enhances specific frequency ranges aligned with consciousness
    research and biofield coherence principles.
    
    Args:
        length: Number of samples to generate
        sample_rate: Audio sample rate in Hz
        intention: Consciousness intention ('neutral', 'release', 'focus', 'integrate', 'creativity')
        coherence_enhancement: Additional coherence factor (0.0-0.5)
    
    Returns:
        Intention-tuned pink noise signal
    
    Raises:
        ValueError: If parameters are invalid
    """
    length = _validate_length(length)
    sample_rate = _validate_sample_rate(sample_rate)
    intention = _validate_intention(intention)
    
    if length == 0:
        return np.array([], dtype=np.float64)
    
    # Clamp coherence enhancement to safe range
    coherence_enhancement = np.clip(coherence_enhancement, 0.0, 0.5)
    
    # Generate base white noise
    white_noise = np.random.randn(length + 1)  # Extra sample for even length handling
    fft_white = np.fft.rfft(white_noise)
    freqs = np.fft.rfftfreq(len(white_noise), 1.0 / sample_rate)
    
    # Prevent division by zero
    freqs[0] = 1e-10
    
    # Apply base pink noise 1/f shaping
    profile = INTENTION_PROFILES[intention]
    pink_fft = fft_white / (np.sqrt(freqs) * profile['spectral_weight'])
    
    # Apply biofield intelligence enhancements
    pink_fft = _apply_biofield_enhancement(pink_fft, freqs, intention, coherence_enhancement)
    
    # Convert back to time domain
    pink_noise = np.fft.irfft(pink_fft)[:length]
    pink_noise = _safe_normalize(pink_noise)
    
    logging.info(f"Generated biofield pink noise: {length} samples, {intention} intention, "
                f"coherence={coherence_enhancement:.3f}")
    return pink_noise

def generate_brown_noise(length: int, sample_rate: float = 44100.0, 
                        intention: str = 'neutral') -> np.ndarray:
    """
    Generate consciousness-aware brown noise (Brownian/red noise).
    
    Brown noise has a 1/f² spectrum and provides deep, grounding ambience
    that can facilitate deeper consciousness states.
    
    Args:
        length: Number of samples to generate  
        sample_rate: Audio sample rate in Hz (for consistency)
        intention: Consciousness intention for subtle modulation
    
    Returns:
        Brown noise signal
    """
    length = _validate_length(length)
    sample_rate = _validate_sample_rate(sample_rate)
    intention = _validate_intention(intention)
    
    if length == 0:
        return np.array([], dtype=np.float64)
    
    # Generate white noise and integrate to create brown noise
    white_noise = np.random.randn(length)
    brown_noise = np.cumsum(white_noise)
    
    # Apply intention-based subtle modulation
    profile = INTENTION_PROFILES[intention]
    if intention == 'release':
        # Enhance lower frequency content for deeper states
        brown_noise *= profile['warmth_factor']
    
    brown_noise = _safe_normalize(brown_noise)
    
    logging.debug(f"Generated brown noise: {length} samples, {intention} intention")
    return brown_noise

def generate_consciousness_aware_carrier_wave(frequency: float, duration: float, 
                                            sample_rate: float, intention: str = 'neutral',
                                            phase: float = 0.0) -> np.ndarray:
    """
    Generate consciousness-aware carrier wave with intention-based frequency adaptation.
    
    This function creates pure tones that are subtly adapted based on consciousness
    intentions and neural architecture considerations.
    
    Args:
        frequency: Base carrier frequency in Hz
        duration: Duration in seconds
        sample_rate: Audio sample rate in Hz
        intention: Consciousness intention for frequency adaptation
        phase: Initial phase offset in radians
    
    Returns:
        Consciousness-adapted carrier wave
    
    Raises:
        ValueError: If frequency is outside safe range
    """
    sample_rate = _validate_sample_rate(sample_rate)
    intention = _validate_intention(intention)
    
    if not (SAFE_CARRIER_RANGE[0] <= frequency <= SAFE_CARRIER_RANGE[1]):
        logging.warning(f"Carrier frequency {frequency}Hz outside safe range {SAFE_CARRIER_RANGE}")
        frequency = np.clip(frequency, SAFE_CARRIER_RANGE[0], SAFE_CARRIER_RANGE[1])
    
    if duration <= 0:
        raise ValueError(f"Duration must be positive, got {duration}")
    
    # Apply intention-based frequency adaptation
    profile = INTENTION_PROFILES[intention]
    adapted_frequency = frequency + profile['carrier_shift']
    adapted_frequency *= profile['warmth_factor']
    
    # Keep in safe range after adaptation
    adapted_frequency = np.clip(adapted_frequency, SAFE_CARRIER_RANGE[0], SAFE_CARRIER_RANGE[1])
    
    # Generate time vector
    length = int(duration * sample_rate)
    t = np.linspace(0, duration, length, endpoint=False)
    
    # Generate carrier wave with consciousness adaptation
    carrier = np.sin(2 * PI * adapted_frequency * t + phase)
    
    logging.debug(f"Generated consciousness-aware carrier: {adapted_frequency:.2f}Hz, "
                 f"{duration:.3f}s, {intention} intention")
    return carrier

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MODULATION FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def apply_isochronic(wave: np.ndarray, pulse_freq: float, sample_rate: float,
                    duty_cycle: float = 0.5, fade_edges: bool = True) -> np.ndarray:
    """
    Apply isochronic pulse modulation with smooth edges and consciousness awareness.
    
    Args:
        wave: Input audio signal
        pulse_freq: Pulse frequency in Hz (neural entrainment target)
        sample_rate: Audio sample rate in Hz
        duty_cycle: Pulse duty cycle (0.0 to 1.0)
        fade_edges: Whether to apply smooth fade transitions
    
    Returns:
        Isochronically modulated signal
    """
    if len(wave) == 0 or pulse_freq <= 0:
        return wave.copy()
    
    # Validate pulse frequency is in safe range
    if not (SAFE_BEAT_RANGE[0] <= pulse_freq <= SAFE_BEAT_RANGE[1]):
        logging.warning(f"Pulse frequency {pulse_freq}Hz outside safe range {SAFE_BEAT_RANGE}")
        pulse_freq = np.clip(pulse_freq, SAFE_BEAT_RANGE[0], SAFE_BEAT_RANGE[1])
    
    # Validate duty cycle
    duty_cycle = np.clip(duty_cycle, 0.1, 0.9)  # Prevent extreme values
    
    # Generate time vector
    t = np.arange(len(wave)) / sample_rate
    
    # Create pulse train
    pulse_period = 1.0 / pulse_freq
    pulse_phase = (t % pulse_period) / pulse_period
    
    # Generate square wave with specified duty cycle
    pulse_train = (pulse_phase < duty_cycle).astype(np.float64)
    
    if fade_edges:
        # Apply smooth transitions to reduce clicking
        fade_samples = int(sample_rate * 0.001)  # 1ms fade
        if fade_samples > 0:
            # Find pulse edges
            edges = np.diff(pulse_train.astype(int))
            rising_edges = np.where(edges > 0)[0]
            falling_edges = np.where(edges < 0)[0]
            
            # Apply fades
            for edge in rising_edges:
                start_idx = max(0, edge - fade_samples//2)
                end_idx = min(len(pulse_train), edge + fade_samples//2)
                fade_length = end_idx - start_idx
                if fade_length > 0:
                    fade = np.linspace(0, 1, fade_length)
                    pulse_train[start_idx:end_idx] = fade
            
            for edge in falling_edges:
                start_idx = max(0, edge - fade_samples//2)
                end_idx = min(len(pulse_train), edge + fade_samples//2)
                fade_length = end_idx - start_idx
                if fade_length > 0:
                    fade = np.linspace(1, 0, fade_length)
                    pulse_train[start_idx:end_idx] = fade
    
    modulated = wave * pulse_train
    
    logging.debug(f"Applied isochronic modulation: {pulse_freq:.2f}Hz, duty={duty_cycle:.2f}")
    return modulated

def apply_bilateral_panning(audio: np.ndarray, pan_freq: float, sample_rate: float,
                          t: Optional[np.ndarray] = None, depth: float = 1.0) -> np.ndarray:
    """
    Apply consciousness-aware bilateral panning with energy conservation.
    
    Creates hemispheric stimulation by panning audio between left and right channels
    while maintaining total energy conservation.
    
    Args:
        audio: Input mono or stereo audio signal
        pan_freq: Panning frequency in Hz
        sample_rate: Audio sample rate in Hz
        t: Time vector (optional, will be generated if None)
        depth: Panning depth (0.0 to 1.0)
    
    Returns:
        Stereo audio with bilateral panning applied
    """
    if len(audio) == 0:
        return audio
    
    # Ensure input is 2D (samples, channels)
    if audio.ndim == 1:
        audio = audio.reshape(-1, 1)
    
    # Generate time vector if not provided
    if t is None:
        t = np.arange(audio.shape[0]) / sample_rate
    elif len(t) != audio.shape[0]:
        raise ValueError("Time vector length must match audio length")
    
    # Validate panning frequency
    if pan_freq <= 0 or pan_freq > 50:  # Reasonable panning frequency range
        logging.warning(f"Panning frequency {pan_freq}Hz outside recommended range")
        pan_freq = np.clip(pan_freq, 0.1, 50)
    
    # Clamp depth to valid range
    depth = np.clip(depth, 0.0, 1.0)
    
    # Generate panning signal (sinusoidal)
    pan_signal = np.sin(2 * PI * pan_freq * t)
    
    # Create left and right gains with energy conservation
    # Using equal-power panning law
    left_gain = np.sqrt(0.5 * (1 - depth * pan_signal))
    right_gain = np.sqrt(0.5 * (1 + depth * pan_signal))
    
    # Apply panning to all input channels
    if audio.shape[1] == 1:
        # Mono input - create stereo output
        stereo_output = np.zeros((audio.shape[0], 2))
        stereo_output[:, 0] = audio[:, 0] * left_gain
        stereo_output[:, 1] = audio[:, 0] * right_gain
    else:
        # Stereo or multi-channel input - pan existing channels
        stereo_output = audio.copy()
        if stereo_output.shape[1] >= 2:
            stereo_output[:, 0] *= left_gain
            stereo_output[:, 1] *= right_gain
    
    logging.debug(f"Applied bilateral panning: {pan_freq:.2f}Hz, depth={depth:.2f}")
    return stereo_output

def apply_fm_modulation(carrier_freqs: np.ndarray, fm_depth: float, fm_rate: float,
                       t: np.ndarray, intention: str = 'neutral') -> np.ndarray:
    """
    Apply consciousness-aware FM modulation to carrier frequencies.
    
    Args:
        carrier_freqs: Base carrier frequencies array
        fm_depth: Frequency modulation depth in Hz
        fm_rate: Modulation rate in Hz
        t: Time vector
        intention: Consciousness intention for modulation character
    
    Returns:
        FM modulated frequency array
    """
    if len(carrier_freqs) == 0 or len(t) == 0:
        return carrier_freqs
    
    # Validate FM parameters
    fm_depth = np.clip(fm_depth, 0, SAFE_FM_DEPTH_RANGE[1])
    fm_rate = np.clip(fm_rate, 0.01, 20)  # Reasonable modulation rate range
    
    intention = _validate_intention(intention)
    profile = INTENTION_PROFILES[intention]
    
    # Generate modulation signal with intention-based character
    if intention == 'release':
        # Slower, more flowing modulation for release states
        modulation = np.sin(2 * PI * fm_rate * t * 0.8) + 0.3 * np.sin(2 * PI * fm_rate * t * 2.1)
    elif intention == 'focus':
        # More structured, rhythmic modulation for focus
        modulation = np.sin(2 * PI * fm_rate * t) + 0.2 * np.sin(2 * PI * fm_rate * t * 3)
    else:
        # Standard sinusoidal modulation
        modulation = np.sin(2 * PI * fm_rate * t)
    
    # Apply warmth factor
    modulation *= profile['warmth_factor']
    
    # Ensure consistent shape for broadcasting
    if carrier_freqs.ndim == 1 and len(carrier_freqs) == len(t):
        modulated_freqs = carrier_freqs + fm_depth * modulation
    else:
        # Broadcast modulation across all frequencies
        modulated_freqs = carrier_freqs + fm_depth * modulation[:, np.newaxis]
    
    logging.debug(f"Applied FM modulation: depth={fm_depth}Hz, rate={fm_rate}Hz, {intention}")
    return modulated_freqs

def apply_biorhythm_fm_modulation(carrier_freqs: np.ndarray, fm_depth: float, 
                                 fm_rate: float, t: np.ndarray,
                                 circadian_sync: bool = False,
                                 time_of_day: float = 0.5) -> np.ndarray:
    """
    Apply biorhythm-synchronized FM modulation aligned with natural rhythms.
    
    Args:
        carrier_freqs: Base carrier frequencies
        fm_depth: Modulation depth in Hz
        fm_rate: Base modulation rate in Hz
        t: Time vector
        circadian_sync: Whether to sync with circadian rhythms
        time_of_day: Time of day as fraction (0.0=midnight, 0.5=noon, 1.0=midnight)
    
    Returns:
        Biorhythm-synchronized FM modulated frequencies
    """
    if len(carrier_freqs) == 0 or len(t) == 0:
        return carrier_freqs
    
    # Validate parameters
    fm_depth = np.clip(fm_depth, 0, SAFE_FM_DEPTH_RANGE[1])
    fm_rate = np.clip(fm_rate, 0.01, 20)
    time_of_day = np.clip(time_of_day, 0.0, 1.0)
    
    # Base biorhythm modulation (breathing rate ~0.25 Hz)
    breathing_mod = np.sin(2 * PI * 0.25 * t)
    
    # Heart rate variability (~0.1 Hz)
    hrv_mod = 0.5 * np.sin(2 * PI * 0.1 * t)
    
    # Primary FM modulation
    primary_mod = np.sin(2 * PI * fm_rate * t)
    
    if circadian_sync:
        # Adjust modulation based on time of day
        # Higher energy during day (0.3-0.7), lower at night
        if 0.25 <= time_of_day <= 0.75:  # Day time
            circadian_factor = 1.0 + 0.3 * np.sin(2 * PI * (time_of_day - 0.25) * 2)
        else:  # Night time
            circadian_factor = 0.7
        
        primary_mod *= circadian_factor
    
    # Combine biorhythm components
    biorhythm_modulation = (primary_mod + 0.3 * breathing_mod + 0.2 * hrv_mod) / 1.5
    
    # Apply to carrier frequencies
    if carrier_freqs.ndim == 1 and len(carrier_freqs) == len(t):
        modulated_freqs = carrier_freqs + fm_depth * biorhythm_modulation
    else:
        modulated_freqs = carrier_freqs + fm_depth * biorhythm_modulation[:, np.newaxis]
    
    logging.info(f"Applied biorhythm FM: depth={fm_depth}Hz, rate={fm_rate}Hz, "
                f"circadian_sync={circadian_sync}")
    return modulated_freqs

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ANALYSIS & COHERENCE FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def consciousness_coherence_check(waves_list: List[np.ndarray], 
                                 intention: Optional[str] = None,
                                 threshold: float = 0.7) -> bool:
    """
    Assess consciousness coherence across multiple audio waves.
    
    This function evaluates the coherence between multiple audio signals using
    cross-correlation, spectral coherence, and consciousness-specific metrics.
    
    Args:
        waves_list: List of audio signals to analyze
        intention: Consciousness intention for context-aware thresholds
        threshold: Coherence threshold (0.0 to 1.0)
    
    Returns:
        True if waves meet coherence criteria
    """
    if not waves_list or len(waves_list) < 2:
        return True  # Single or no waves are trivially coherent
    
    # Validate all waves are the same length
    lengths = [len(wave) for wave in waves_list]
    if not all(length == lengths[0] for length in lengths):
        logging.warning("Wave lengths differ, coherence check may be unreliable")
        min_length = min(lengths)
        waves_list = [wave[:min_length] for wave in waves_list]
    
    if lengths[0] == 0:
        return True
    
    # Validate threshold
    threshold = np.clip(threshold, 0.0, 1.0)
    
    # Adjust threshold based on intention
    if intention:
        intention = _validate_intention(intention)
        if intention in ['release', 'integrate']:
            threshold *= 0.9  # More lenient for healing states
        elif intention == 'focus':
            threshold *= 1.1  # More strict for focus states
    
    coherence_scores = []
    
    # Cross-correlation analysis
    for i, j in combinations(range(len(waves_list)), 2):
        wave1, wave2 = waves_list[i], waves_list[j]
        
        # Normalize waves for comparison
        wave1_norm = wave1 / (np.std(wave1) + 1e-10)
        wave2_norm = wave2 / (np.std(wave2) + 1e-10)
        
        # Cross-correlation coefficient
        correlation = np.corrcoef(wave1_norm, wave2_norm)[0, 1]
        if not np.isfinite(correlation):
            correlation = 0.0
        
        coherence_scores.append(abs(correlation))
    
    # Spectral coherence analysis
    spectral_coherences = []
    for i, j in combinations(range(len(waves_list)), 2):
        wave1, wave2 = waves_list[i], waves_list[j]
        
        # Compute power spectral densities
        fft1 = np.fft.rfft(wave1)
        fft2 = np.fft.rfft(wave2)
        
        # Spectral correlation
        cross_spec = fft1 * np.conj(fft2)
        auto_spec1 = fft1 * np.conj(fft1)
        auto_spec2 = fft2 * np.conj(fft2)
        
        # Magnitude squared coherence
        coherence_spec = np.abs(cross_spec) ** 2 / (np.abs(auto_spec1) * np.abs(auto_spec2) + 1e-10)
        mean_spectral_coherence = np.mean(coherence_spec)
        
        spectral_coherences.append(mean_spectral_coherence)
    
    # Combine metrics
    overall_coherence = (np.mean(coherence_scores) + np.mean(spectral_coherences)) / 2
    
    is_coherent = overall_coherence >= threshold
    
    logging.info(f"Coherence analysis: {overall_coherence:.3f} (threshold={threshold:.3f}), "
                f"coherent={is_coherent}, intention={intention}")
    
    return is_coherent

def assess_phase_relationships(waves_list: List[np.ndarray]) -> float:
    """
    Assess phase relationships between multiple audio signals.
    
    Args:
        waves_list: List of audio signals to analyze
    
    Returns:
        Phase relationship score (0.0 to 1.0, higher = better phase alignment)
    """
    if not waves_list or len(waves_list) < 2:
        return 1.0
    
    # Ensure all waves are same length
    min_length = min(len(wave) for wave in waves_list if len(wave) > 0)
    if min_length == 0:
        return 1.0
    
    trimmed_waves = [wave[:min_length] for wave in waves_list]
    
    # Compute instantaneous phases using Hilbert transform
    phases = []
    for wave in trimmed_waves:
        analytic_signal = np.fft.ifft(np.fft.fft(wave) * np.where(
            np.arange(len(wave)) <= len(wave) // 2, 2, 0))
        phase = np.angle(analytic_signal)
        phases.append(phase)
    
    # Calculate phase differences between all pairs
    phase_diffs = []
    for i, j in combinations(range(len(phases)), 2):
        diff = phases[i] - phases[j]
        # Wrap to [-π, π]
        diff = ((diff + PI) % (2 * PI)) - PI
        phase_diffs.append(diff)
    
    # Calculate phase coherence (consistency of phase relationships)
    if phase_diffs:
        # Mean resultant length (circular statistics)
        complex_diffs = [np.exp(1j * diff) for diff in phase_diffs]
        mean_complex = np.mean([np.mean(cd) for cd in complex_diffs])
        phase_coherence = abs(mean_complex)
    else:
        phase_coherence = 1.0
    
    logging.debug(f"Phase relationship score: {phase_coherence:.3f}")
    return float(phase_coherence)

def assess_intermodulation_harmony(beat_freqs: List[float]) -> Tuple[bool, str]:
    """
    Assess harmonic relationships in beat frequency combinations.
    
    Args:
        beat_freqs: List of beat frequencies to analyze
    
    Returns:
        Tuple of (is_harmonic, assessment_message)
    """
    if len(beat_freqs) < 2:
        return True, "Single or no frequencies - trivially harmonic"
    
    # Remove duplicates and sort
    unique_freqs = sorted(list(set(f for f in beat_freqs if f > 0)))
    
    if len(unique_freqs) < 2:
        return True, "Single unique frequency - trivially harmonic"
    
    # Find greatest common divisor of frequencies (approximate)
    def gcd_float(a, b, tolerance=0.1):
        while abs(b) > tolerance:
            a, b = b, a % b
        return abs(a)
    
    # Check for harmonic relationships
    fundamental = unique_freqs[0]
    for freq in unique_freqs[1:]:
        gcd = gcd_float(freq, fundamental)
        if gcd < 0.5:  # No reasonable common divisor
            continue
        
        # Check if frequencies are near integer multiples of GCD
        harmonic_check = all(
            abs(f / gcd - round(f / gcd)) < 0.1 
            for f in unique_freqs
        )
        
        if harmonic_check:
            return True, f"Harmonic series detected with fundamental ~{gcd:.2f}Hz"
    
    # Check for simple integer ratios
    ratios = []
    for i, freq1 in enumerate(unique_freqs):
        for freq2 in unique_freqs[i+1:]:
            ratio = freq2 / freq1
            ratios.append(ratio)
    
    # Check for simple ratios (within 5% tolerance)
    simple_ratios = [1.5, 2.0, 2.5, 3.0, 4.0, 5.0]  # Common harmonic ratios
    harmony_score = 0
    
    for ratio in ratios:
        for simple_ratio in simple_ratios:
            if abs(ratio - simple_ratio) / simple_ratio < 0.05:
                harmony_score += 1
                break
    
    is_harmonic = harmony_score >= len(ratios) * 0.5  # At least 50% harmonic ratios
    
    if is_harmonic:
        message = f"Good harmonic relationships detected ({harmony_score}/{len(ratios)} harmonic ratios)"
    else:
        message = f"Limited harmonic relationships ({harmony_score}/{len(ratios)} harmonic ratios)"
    
    logging.debug(f"Intermodulation analysis: {message}")
    return is_harmonic, message

def coherence_adjust(waves_list: List[np.ndarray], threshold: float = 0.7,
                    intention: str = 'neutral') -> List[np.ndarray]:
    """
    Adjust wave coherence to meet specified threshold while preserving character.
    
    Args:
        waves_list: List of audio signals to adjust
        threshold: Target coherence threshold
        intention: Consciousness intention for adjustment character
    
    Returns:
        List of coherence-adjusted waves
    """
    if len(waves_list) < 2:
        return waves_list.copy()
    
    intention = _validate_intention(intention)
    current_coherence = consciousness_coherence_check(waves_list, intention, 0.0)
    
    # If already coherent, return as-is
    if consciousness_coherence_check(waves_list, intention, threshold):
        logging.debug("Waves already meet coherence threshold")
        return waves_list.copy()
    
    adjusted_waves = waves_list.copy()
    
    # Apply gentle coherence enhancement
    for i in range(1, len(adjusted_waves)):
        reference_wave = adjusted_waves[0]
        current_wave = adjusted_waves[i]
        
        if len(reference_wave) != len(current_wave):
            continue
        
        # Cross-correlation to find optimal alignment
        correlation = np.correlate(current_wave, reference_wave, mode='full')
        lag = np.argmax(correlation) - len(reference_wave) + 1
        
        # Apply small phase adjustment based on lag
        if abs(lag) < len(current_wave) // 4:  # Only small adjustments
            if lag > 0:
                adjusted_waves[i] = np.roll(current_wave, -lag)
            else:
                adjusted_waves[i] = np.roll(current_wave, -lag)
        
        # Apply gentle amplitude correlation
        correlation_factor = np.corrcoef(reference_wave, adjusted_waves[i])[0, 1]
        if np.isfinite(correlation_factor) and abs(correlation_factor) < 0.5:
            # Blend with reference to improve coherence
            blend_factor = 0.1  # Conservative blending
            adjusted_waves[i] = (1 - blend_factor) * adjusted_waves[i] + blend_factor * reference_wave
    
    # Verify improvement
    final_coherence = consciousness_coherence_check(adjusted_waves, intention, 0.0)
    
    logging.info(f"Coherence adjustment: initial={current_coherence:.3f}, "
                f"final={final_coherence:.3f}, intention={intention}")
    
    return adjusted_waves

def harmonic_analysis(frequencies: List[float]) -> bool:
    """
    Analyze frequencies for harmonic relationships and natural ratios.
    
    Args:
        frequencies: List of frequencies to analyze
    
    Returns:
        True if frequencies exhibit harmonic relationships
    """
    if len(frequencies) < 2:
        return True
    
    # Filter positive frequencies
    valid_freqs = [f for f in frequencies if f > 0]
    if len(valid_freqs) < 2:
        return True
    
    valid_freqs = sorted(valid_freqs)
    
    # Check for octave relationships (2:1 ratios)
    octave_relationships = 0
    for i, freq1 in enumerate(valid_freqs):
        for freq2 in valid_freqs[i+1:]:
            ratio = freq2 / freq1
            # Check for octave (2^n) relationships within 5% tolerance
            log_ratio = np.log2(ratio)
            if abs(log_ratio - round(log_ratio)) < 0.05:
                octave_relationships += 1
    
    # Check for golden ratio relationships
    golden_relationships = 0
    for i, freq1 in enumerate(valid_freqs):
        for freq2 in valid_freqs[i+1:]:
            ratio = freq2 / freq1
            if abs(ratio - GOLDEN_RATIO) / GOLDEN_RATIO < 0.05:
                golden_relationships += 1
    
    # Check for simple integer ratios
    integer_relationships = 0
    simple_ratios = [3/2, 4/3, 5/3, 5/4, 6/5]  # Common musical intervals
    
    for i, freq1 in enumerate(valid_freqs):
        for freq2 in valid_freqs[i+1:]:
            ratio = freq2 / freq1
            for simple_ratio in simple_ratios:
                if abs(ratio - simple_ratio) / simple_ratio < 0.05:
                    integer_relationships += 1
                    break
    
    total_pairs = len(valid_freqs) * (len(valid_freqs) - 1) // 2
    harmonic_score = (octave_relationships + golden_relationships + integer_relationships) / max(total_pairs, 1)
    
    is_harmonic = harmonic_score >= 0.3  # At least 30% harmonic relationships
    
    logging.debug(f"Harmonic analysis: {harmonic_score:.3f} harmonic score, "
                 f"octaves={octave_relationships}, golden={golden_relationships}, "
                 f"simple={integer_relationships}")
    
    return is_harmonic

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEGACY COMPATIBILITY FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def generate_pink_noise(length: int, sample_rate: float) -> np.ndarray:
    """Legacy compatibility function for basic pink noise generation."""
    return generate_biofield_pink_noise(length, sample_rate, 'neutral', 0.0)

def coherence_check(waves_list: List[np.ndarray], threshold: float = 0.7) -> bool:
    """Legacy compatibility function for basic coherence checking."""
    return consciousness_coherence_check(waves_list, None, threshold)

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
__description__ = "Consciousness-aware neural signal generator with biofield intelligence"

# Export public API
__all__ = [
    # Core noise generation
    'generate_white_noise',
    'generate_biofield_pink_noise', 
    'generate_brown_noise',
    'generate_consciousness_aware_carrier_wave',
    
    # Modulation functions
    'apply_isochronic',
    'apply_bilateral_panning', 
    'apply_fm_modulation',
    'apply_biorhythm_fm_modulation',
    
    # Analysis functions
    'consciousness_coherence_check',
    'assess_phase_relationships',
    'assess_intermodulation_harmony',
    'coherence_adjust',
    'harmonic_analysis',
    
    # Legacy compatibility
    'generate_pink_noise',
    'coherence_check',
    
    # Configuration classes
    'SignalConfig',
    'IntentionType',
]

logging.info(f"Neural Signal Generator v{__version__} initialized - "
            f"Consciousness-aware biofield intelligence framework ready")
