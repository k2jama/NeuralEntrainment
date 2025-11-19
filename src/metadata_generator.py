# 🧪 Neural Entrainment System - Consciousness Metadata Generator v2.0
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠 Consciousness-Aware Biofield Intelligence Framework
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Consciousness Metadata Generator - Advanced session analysis and guidance engine.

This module provides comprehensive consciousness journey analysis, biofield coherence assessment,
and intelligent guidance generation. All functions respect neural architecture sensitivity and
consciousness sovereignty while providing deep insights into session structure and safety.
"""

import numpy as np
import logging
import datetime
import copy
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSTANTS & CONSCIOUSNESS PROFILES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Consciousness state frequency mappings with enhanced precision
CONSCIOUSNESS_STATE_FREQUENCIES = {
    'deep_delta': {'range': (0.1, 2.0), 'peak': 1.0, 'coherence_signature': 'deep_healing'},
    'delta': {'range': (1.0, 4.0), 'peak': 2.5, 'coherence_signature': 'regenerative'},
    'theta': {'range': (4.0, 8.0), 'peak': 6.0, 'coherence_signature': 'transformative'},
    'alpha': {'range': (8.0, 13.0), 'peak': 10.0, 'coherence_signature': 'bridge_state'},
    'beta': {'range': (13.0, 30.0), 'peak': 18.0, 'coherence_signature': 'cognitive'},
    'gamma': {'range': (30.0, 100.0), 'peak': 40.0, 'coherence_signature': 'transcendent'},
    'high_gamma': {'range': (80.0, 200.0), 'peak': 120.0, 'coherence_signature': 'expanded_awareness'}
}

# Biofield resonance frequencies for consciousness alignment
BIOFIELD_FREQUENCIES = {
    'schumann_primary': 7.83,
    'schumann_harmonics': [14.3, 20.8, 27.3, 33.8, 39.3, 45.9, 52.8],
    'solfeggio_core': [174, 285, 396, 417, 528, 639, 741, 852, 963],
    'healing_frequencies': [528, 432, 396, 417, 852],
    'golden_ratio_base': 1.618033988749895
}

# Neural architecture sensitivity profiles for metadata adaptation
NEURAL_SENSITIVITY_METADATA = {
    'sensitive': {
        'max_phase_complexity': 2,
        'max_state_transitions': 3,
        'recommended_session_duration': 1800,  # 30 minutes
        'integration_requirement': True,
        'transition_buffer_multiplier': 1.5,
        'safety_margin': 0.8
    },
    'standard': {
        'max_phase_complexity': 4,
        'max_state_transitions': 6,
        'recommended_session_duration': 3600,  # 60 minutes
        'integration_requirement': False,
        'transition_buffer_multiplier': 1.0,
        'safety_margin': 1.0
    },
    'resilient': {
        'max_phase_complexity': 8,
        'max_state_transitions': 10,
        'recommended_session_duration': 5400,  # 90 minutes
        'integration_requirement': False,
        'transition_buffer_multiplier': 0.8,
        'safety_margin': 1.2
    }
}

# Consciousness intention metadata profiles
INTENTION_METADATA_PROFILES = {
    'neutral': {
        'guidance_style': 'observational',
        'emphasis': 'awareness',
        'biofield_focus': 'balanced',
        'integration_depth': 'gentle',
        'safety_priority': 'standard'
    },
    'release': {
        'guidance_style': 'permissive',
        'emphasis': 'letting_go',
        'biofield_focus': 'grounding',
        'integration_depth': 'deep',
        'safety_priority': 'conservative'
    },
    'focus': {
        'guidance_style': 'directive',
        'emphasis': 'concentration',
        'biofield_focus': 'clarity',
        'integration_depth': 'practical',
        'safety_priority': 'performance'
    },
    'integrate': {
        'guidance_style': 'synthesizing',
        'emphasis': 'wholeness',
        'biofield_focus': 'harmonizing',
        'integration_depth': 'comprehensive',
        'safety_priority': 'holistic'
    },
    'creativity': {
        'guidance_style': 'exploratory',
        'emphasis': 'innovation',
        'biofield_focus': 'inspiration',
        'integration_depth': 'expansive',
        'safety_priority': 'adaptive'
    }
}

class ConsciousnessTransitionType(Enum):
    """Enhanced consciousness transition types with metadata characteristics."""
    LINEAR = 'linear'
    THETA_GATEWAY = 'theta_gateway'
    GAMMA_EMERGENCE = 'gamma_emergence'
    DELTA_DESCENT = 'delta_descent'
    SINUSOIDAL = 'sinusoidal'
    EXPONENTIAL = 'exponential'
    BREATH_SYNC = 'breath_sync'
    HEART_SYNC = 'heart_sync'
    CONSCIOUSNESS_SPIRAL = 'consciousness_spiral'

@dataclass
class ConsciousnessAnalysis:
    """Comprehensive consciousness journey analysis results."""
    state_sequence: List[str] = field(default_factory=list)
    transition_quality: List[float] = field(default_factory=list)
    biofield_alignment: List[float] = field(default_factory=list)
    coherence_progression: List[float] = field(default_factory=list)
    integration_windows: List[Dict[str, Any]] = field(default_factory=list)
    neural_load_assessment: Dict[str, Any] = field(default_factory=dict)
    safety_considerations: List[str] = field(default_factory=list)
    consciousness_journey_quality: float = 0.0

@dataclass
class BiofieldCoherenceMetrics:
    """Comprehensive biofield coherence assessment metrics."""
    schumann_alignment: float = 0.0
    solfeggio_presence: float = 0.0
    golden_ratio_harmonics: float = 0.0
    frequency_harmony: float = 0.0
    transition_smoothness: float = 0.0
    intention_congruence: float = 0.0
    neural_compatibility: float = 0.0
    overall_coherence: float = 0.0
    coherence_timeline: List[float] = field(default_factory=list)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CORE ANALYSIS FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def analyze_consciousness_progression(config: Dict[str, Any], neural_profile: Optional[Dict[str, Any]] = None) -> ConsciousnessAnalysis:
    """
    Comprehensive consciousness state progression analysis with neural architecture sensitivity.
    
    Args:
        config: Session configuration with phases and neural profile data
        neural_profile: Optional neural profile for enhanced analysis
        
    Returns:
        ConsciousnessAnalysis object with detailed journey metrics
    """
    phases = config.get('phases', [])
    intention = config.get('intention', 'neutral')
    
    # Extract neural profile data
    if neural_profile is None:
        neural_profile = config.get('neural_profile', {
            'sensitivity_level': 'standard',
            'current_state': 'neutral',
            'experience_level': 'intermediate'
        })
    
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    current_state = neural_profile.get('current_state', 'neutral')
    experience_level = neural_profile.get('experience_level', 'intermediate')
    
    analysis = ConsciousnessAnalysis()
    
    # Analyze state sequence and transitions
    current_time = 0.0
    previous_state = None
    neural_load_accumulation = 0.0
    
    sensitivity_profile = NEURAL_SENSITIVITY_METADATA.get(sensitivity_level, NEURAL_SENSITIVITY_METADATA['standard'])
    
    for i, phase in enumerate(phases):
        if not isinstance(phase, dict):
            continue
        
        # Extract phase characteristics
        duration = phase.get('duration', 0)
        phase_type = phase.get('type', 'static')
        transition_type = phase.get('animation_type', 'linear')
        layers = phase.get('layers', [])
        
        # Calculate dominant consciousness state
        target_state = _determine_consciousness_state(phase, layers)
        analysis.state_sequence.append(target_state)
        
        # Assess transition quality
        transition_quality = _assess_transition_quality(
            previous_state, target_state, transition_type, duration,
            sensitivity_level, experience_level
        )
        analysis.transition_quality.append(transition_quality)
        
        # Calculate biofield alignment for this phase
        biofield_alignment = _calculate_biofield_alignment(layers, intention, target_state)
        analysis.biofield_alignment.append(biofield_alignment)
        
        # Assess consciousness coherence
        coherence_score = _calculate_consciousness_coherence(
            target_state, transition_quality, biofield_alignment, neural_profile
        )
        analysis.coherence_progression.append(coherence_score)
        
        # Detect integration windows
        if target_state in ['theta', 'alpha'] and duration >= 300:  # >= 5 minutes
            analysis.integration_windows.append({
                'phase_index': i,
                'start_time': current_time,
                'end_time': current_time + duration,
                'state': target_state,
                'integration_potential': min(1.0, duration / 600),  # Normalized by 10 minutes
                'type': 'natural_coherence'
            })
        
        # Calculate neural load
        phase_neural_load = _calculate_neural_load(phase, layers, sensitivity_profile)
        neural_load_accumulation += phase_neural_load
        
        # Safety assessments
        phase_safety = _assess_phase_safety(
            phase, target_state, transition_quality, neural_profile, i
        )
        analysis.safety_considerations.extend(phase_safety)
        
        current_time += duration
        previous_state = target_state
    
    # Neural load assessment
    analysis.neural_load_assessment = {
        'total_load': neural_load_accumulation,
        'average_load': neural_load_accumulation / max(len(phases), 1),
        'max_sustainable_load': sensitivity_profile['safety_margin'] * len(phases),
        'load_utilization': min(1.0, neural_load_accumulation / (sensitivity_profile['safety_margin'] * len(phases))),
        'overload_risk': 'high' if neural_load_accumulation > sensitivity_profile['safety_margin'] * len(phases) else 'acceptable'
    }
    
    # Overall consciousness journey quality
    if analysis.coherence_progression:
        journey_coherence = np.mean(analysis.coherence_progression)
        transition_smoothness = np.mean(analysis.transition_quality) if analysis.transition_quality else 0.5
        biofield_harmony = np.mean(analysis.biofield_alignment) if analysis.biofield_alignment else 0.5
        
        analysis.consciousness_journey_quality = (
            journey_coherence * 0.4 +
            transition_smoothness * 0.3 +
            biofield_harmony * 0.3
        )
    
    logging.info(f"Consciousness analysis complete: {len(analysis.state_sequence)} states, "
                f"quality={analysis.consciousness_journey_quality:.3f}")
    
    return analysis

def assess_biofield_coherence_potential(config: Dict[str, Any], neural_profile: Optional[Dict[str, Any]] = None) -> BiofieldCoherenceMetrics:
    """
    Comprehensive biofield coherence assessment using frequency analysis and consciousness alignment.
    
    Args:
        config: Session configuration
        neural_profile: Neural architecture profile for personalized assessment
        
    Returns:
        BiofieldCoherenceMetrics with detailed coherence analysis
    """
    phases = config.get('phases', [])
    intention = config.get('intention', 'neutral')
    
    if neural_profile is None:
        neural_profile = config.get('neural_profile', {'sensitivity_level': 'standard'})
    
    metrics = BiofieldCoherenceMetrics()
    
    # Analyze frequency content for biofield alignment
    all_frequencies = []
    all_carriers = []
    all_beats = []
    
    for phase in phases:
        layers = phase.get('layers', [])
        for layer in layers:
            carrier = layer.get('carrier', 0)
            if carrier > 0:
                all_carriers.append(carrier)
            
            # Extract beat frequencies
            if phase.get('type') == 'static':
                beat = layer.get('beat', 0)
                if beat > 0:
                    all_beats.append(beat)
            else:  # ramp
                start_beat = layer.get('start_beat', 0)
                end_beat = layer.get('end_beat', 0)
                if start_beat > 0 and end_beat > 0:
                    all_beats.extend([start_beat, end_beat])
    
    all_frequencies = all_carriers + all_beats
    
    if not all_frequencies:
        return metrics
    
    # Schumann resonance alignment
    metrics.schumann_alignment = _calculate_schumann_alignment(all_frequencies)
    
    # Solfeggio frequency presence
    metrics.solfeggio_presence = _calculate_solfeggio_presence(all_frequencies)
    
    # Golden ratio harmonic analysis
    metrics.golden_ratio_harmonics = _calculate_golden_ratio_harmonics(all_frequencies)
    
    # Frequency harmony assessment
    metrics.frequency_harmony = _assess_frequency_harmony(all_frequencies)
    
    # Transition smoothness analysis
    metrics.transition_smoothness = _assess_transition_smoothness(phases)
    
    # Intention congruence with frequency selection
    metrics.intention_congruence = _assess_intention_congruence(intention, all_frequencies, phases)
    
    # Neural compatibility assessment
    metrics.neural_compatibility = _assess_neural_compatibility(
        all_frequencies, neural_profile, phases
    )
    
    # Calculate overall coherence
    coherence_factors = [
        metrics.schumann_alignment * 0.15,
        metrics.solfeggio_presence * 0.10,
        metrics.golden_ratio_harmonics * 0.10,
        metrics.frequency_harmony * 0.25,
        metrics.transition_smoothness * 0.20,
        metrics.intention_congruence * 0.15,
        metrics.neural_compatibility * 0.05
    ]
    
    metrics.overall_coherence = sum(coherence_factors)
    
    # Generate coherence timeline
    metrics.coherence_timeline = _generate_coherence_timeline(phases, intention, neural_profile)
    
    logging.info(f"Biofield coherence assessment: overall={metrics.overall_coherence:.3f}, "
                f"neural_compatibility={metrics.neural_compatibility:.3f}")
    
    return metrics

def generate_consciousness_guidance(config: Dict[str, Any], consciousness_analysis: ConsciousnessAnalysis,
                                  biofield_metrics: BiofieldCoherenceMetrics) -> List[Dict[str, Any]]:
    """
    Generate intelligent, consciousness-aware guidance for each phase of the session.
    
    Args:
        config: Session configuration
        consciousness_analysis: Results of consciousness progression analysis
        biofield_metrics: Biofield coherence metrics
        
    Returns:
        List of phase-specific guidance dictionaries
    """
    phases = config.get('phases', [])
    intention = config.get('intention', 'neutral')
    neural_profile = config.get('neural_profile', {'experience_level': 'intermediate'})
    
    experience_level = neural_profile.get('experience_level', 'intermediate')
    intention_profile = INTENTION_METADATA_PROFILES.get(intention, INTENTION_METADATA_PROFILES['neutral'])
    
    guidance_list = []
    
    # Generate guidance templates based on intention and experience
    base_templates = _create_guidance_templates(intention, experience_level, intention_profile)
    
    for i, (phase, state, quality, biofield_align) in enumerate(zip(
        phases, 
        consciousness_analysis.state_sequence,
        consciousness_analysis.transition_quality,
        consciousness_analysis.biofield_alignment
    )):
        
        duration = phase.get('duration', 0)
        phase_type = phase.get('type', 'static')
        transition_type = phase.get('animation_type', 'linear')
        
        # Select appropriate base guidance
        guidance_text = _select_contextual_guidance(
            state, phase_type, transition_type, duration,
            base_templates, intention_profile
        )
        
        # Enhance guidance based on quality metrics
        enhanced_guidance = _enhance_guidance_with_metrics(
            guidance_text, quality, biofield_align, state, 
            duration, experience_level
        )
        
        # Add phase-specific consciousness techniques
        consciousness_techniques = _generate_consciousness_techniques(
            state, intention, quality, experience_level
        )
        
        # Safety notes specific to this phase
        safety_notes = _generate_phase_safety_notes(
            phase, state, neural_profile, quality
        )
        
        # Integration opportunities
        integration_notes = []
        for window in consciousness_analysis.integration_windows:
            if window['phase_index'] == i:
                integration_notes.append(f"Natural integration window - {window['type']}")
        
        guidance_entry = {
            'phase_index': i,
            'phase_type': phase_type,
            'consciousness_state': state,
            'transition_type': transition_type,
            'duration': duration,
            'duration_formatted': f"{int(duration//60)}m{int(duration%60):02d}s",
            'primary_guidance': enhanced_guidance,
            'consciousness_techniques': consciousness_techniques,
            'biofield_notes': _generate_biofield_notes(biofield_align, state),
            'safety_considerations': safety_notes,
            'integration_opportunities': integration_notes,
            'transition_quality': quality,
            'biofield_alignment': biofield_align,
            'experience_appropriateness': _assess_experience_appropriateness(
                phase, state, experience_level
            )
        }
        
        guidance_list.append(guidance_entry)
    
    # Add overall session guidance
    if guidance_list:
        session_guidance = _generate_session_level_guidance(
            config, consciousness_analysis, biofield_metrics, intention_profile
        )
        
        # Insert session overview at beginning
        guidance_list.insert(0, {
            'phase_index': -1,
            'phase_type': 'session_overview',
            'consciousness_state': 'preparation',
            'primary_guidance': session_guidance,
            'consciousness_techniques': ['Set clear intention', 'Create sacred space', 'Honor your sovereignty'],
            'safety_considerations': ['Stop if uncomfortable', 'Stay hydrated', 'Ground after session'],
            'session_quality_prediction': consciousness_analysis.consciousness_journey_quality
        })
    
    logging.info(f"Generated consciousness guidance for {len(guidance_list)} phases")
    return guidance_list

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HELPER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _determine_consciousness_state(phase: Dict[str, Any], layers: List[Dict[str, Any]]) -> str:
    """Determine the primary consciousness state for a phase."""
    beat_frequencies = []
    
    for layer in layers:
        if phase.get('type') == 'static':
            beat = layer.get('beat', 0)
            if beat > 0:
                beat_frequencies.append(beat)
        else:  # ramp
            start_beat = layer.get('start_beat', 0)
            end_beat = layer.get('end_beat', 0)
            if start_beat > 0 and end_beat > 0:
                avg_beat = (start_beat + end_beat) / 2
                beat_frequencies.append(avg_beat)
    
    if not beat_frequencies:
        return 'alpha'  # Default bridge state
    
    dominant_frequency = np.mean(beat_frequencies)
    
    # Map to consciousness state
    for state, info in CONSCIOUSNESS_STATE_FREQUENCIES.items():
        freq_range = info['range']
        if freq_range[0] <= dominant_frequency <= freq_range[1]:
            return state
    
    # Fallback mapping
    if dominant_frequency < 4:
        return 'delta'
    elif dominant_frequency < 8:
        return 'theta'
    elif dominant_frequency < 13:
        return 'alpha'
    elif dominant_frequency < 30:
        return 'beta'
    else:
        return 'gamma'

def _assess_transition_quality(prev_state: Optional[str], current_state: str, 
                             transition_type: str, duration: float,
                             sensitivity_level: str, experience_level: str) -> float:
    """Assess the quality of consciousness state transitions."""
    if prev_state is None:
        return 0.9  # First phase, assume good quality
    
    # State transition distance
    state_order = ['deep_delta', 'delta', 'theta', 'alpha', 'beta', 'gamma', 'high_gamma']
    try:
        prev_idx = state_order.index(prev_state)
        curr_idx = state_order.index(current_state)
        state_distance = abs(curr_idx - prev_idx)
    except ValueError:
        state_distance = 1  # Unknown states, assume small distance
    
    # Base quality assessment
    base_quality = 1.0 - (state_distance * 0.15)  # Penalty for large jumps
    
    # Duration appropriateness
    min_duration_for_distance = state_distance * 120  # 2 minutes per state jump
    duration_quality = min(1.0, duration / max(min_duration_for_distance, 60))
    
    # Transition type appropriateness
    transition_quality_map = {
        'linear': 0.7,
        'sinusoidal': 0.9,
        'exponential': 0.8,
        'theta_gateway': 0.95 if current_state == 'theta' else 0.6,
        'gamma_emergence': 0.95 if current_state == 'gamma' else 0.6,
        'delta_descent': 0.95 if current_state in ['delta', 'deep_delta'] else 0.6
    }
    transition_type_quality = transition_quality_map.get(transition_type, 0.7)
    
    # Sensitivity and experience adjustments
    sensitivity_multiplier = {'sensitive': 0.85, 'standard': 1.0, 'resilient': 1.1}.get(sensitivity_level, 1.0)
    experience_multiplier = {'beginner': 0.9, 'intermediate': 1.0, 'advanced': 1.05, 'expert': 1.1}.get(experience_level, 1.0)
    
    final_quality = (
        base_quality * 0.4 +
        duration_quality * 0.3 +
        transition_type_quality * 0.3
    ) * sensitivity_multiplier * experience_multiplier
    
    return np.clip(final_quality, 0.0, 1.0)

def _calculate_biofield_alignment(layers: List[Dict[str, Any]], intention: str, target_state: str) -> float:
    """Calculate biofield alignment score for a phase."""
    if not layers:
        return 0.5
    
    frequencies = []
    for layer in layers:
        carrier = layer.get('carrier', 0)
        if carrier > 0:
            frequencies.append(carrier)
    
    if not frequencies:
        return 0.5
    
    # Schumann alignment component
    schumann_alignment = 0.0
    for freq in frequencies:
        for schumann_freq in [BIOFIELD_FREQUENCIES['schumann_primary']] + BIOFIELD_FREQUENCIES['schumann_harmonics']:
            if abs(freq - schumann_freq) / schumann_freq < 0.1:  # Within 10%
                schumann_alignment += 0.2
    
    # Solfeggio alignment component
    solfeggio_alignment = 0.0
    for freq in frequencies:
        for solfeggio_freq in BIOFIELD_FREQUENCIES['solfeggio_core']:
            if abs(freq - solfeggio_freq) / solfeggio_freq < 0.05:  # Within 5%
                solfeggio_alignment += 0.15
    
    # Healing frequency alignment
    healing_alignment = 0.0
    for freq in frequencies:
        for healing_freq in BIOFIELD_FREQUENCIES['healing_frequencies']:
            if abs(freq - healing_freq) / healing_freq < 0.05:
                healing_alignment += 0.1
    
    # Intention-specific bonuses
    intention_bonus = 0.0
    if intention == 'release' and target_state in ['theta', 'delta']:
        intention_bonus = 0.1
    elif intention == 'focus' and target_state in ['beta', 'gamma']:
        intention_bonus = 0.1
    elif intention == 'integrate' and target_state == 'alpha':
        intention_bonus = 0.15
    
    total_alignment = min(1.0, schumann_alignment + solfeggio_alignment + healing_alignment + intention_bonus)
    return total_alignment

def _calculate_consciousness_coherence(target_state: str, transition_quality: float, 
                                     biofield_alignment: float, neural_profile: Dict[str, Any]) -> float:
    """Calculate consciousness coherence score for a phase."""
    # Base coherence from state characteristics
    state_coherence_map = {
        'deep_delta': 0.95, 'delta': 0.90, 'theta': 0.85, 'alpha': 0.80,
        'beta': 0.75, 'gamma': 0.85, 'high_gamma': 0.90
    }
    base_coherence = state_coherence_map.get(target_state, 0.7)
    
    # Neural profile adjustments
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    current_state = neural_profile.get('current_state', 'neutral')
    
    # Sensitivity adjustment
    sensitivity_adjustment = {'sensitive': -0.05, 'standard': 0.0, 'resilient': 0.05}.get(sensitivity_level, 0.0)
    
    # Current state compatibility
    state_compatibility = 1.0
    if current_state == 'agitated' and target_state in ['beta', 'gamma']:
        state_compatibility = 0.8
    elif current_state == 'tired' and target_state in ['gamma', 'high_gamma']:
        state_compatibility = 0.7
    
    coherence = (
        base_coherence * 0.4 +
        transition_quality * 0.3 +
        biofield_alignment * 0.3
    ) * state_compatibility + sensitivity_adjustment
    
    return np.clip(coherence, 0.0, 1.0)

def _calculate_neural_load(phase: Dict[str, Any], layers: List[Dict[str, Any]], 
                          sensitivity_profile: Dict[str, Any]) -> float:
    """Calculate neural processing load for a phase."""
    base_load = len(layers)  # Layer complexity
    
    # Modality additions
    modalities = sum([
        phase.get('isochronic', False),
        phase.get('bilateral', False),
        phase.get('monaural', False)
    ])
    modality_load = modalities * 0.5
    
    # Duration factor (longer phases are easier to process)
    duration = phase.get('duration', 0)
    duration_factor = max(0.5, min(1.0, duration / 600))  # Normalized by 10 minutes
    
    # Frequency complexity
    frequency_complexity = 0.0
    for layer in layers:
        if layer.get('harmonics'):
            frequency_complexity += len(layer['harmonics']) * 0.2
        if layer.get('fm_depth', 0) > 0:
            frequency_complexity += 0.3
    
    total_load = (base_load + modality_load + frequency_complexity) / duration_factor
    
    return total_load

def _assess_phase_safety(phase: Dict[str, Any], target_state: str, transition_quality: float,
                        neural_profile: Dict[str, Any], phase_index: int) -> List[str]:
    """Generate safety considerations for a specific phase."""
    safety_notes = []
    
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    experience_level = neural_profile.get('experience_level', 'intermediate')
    
    # State-specific safety
    if target_state in ['deep_delta', 'delta']:
        safety_notes.append("Deep state - ensure comfortable environment")
        if sensitivity_level == 'sensitive':
            safety_notes.append("Monitor for excessive relaxation response")
    
    elif target_state == 'theta':
        safety_notes.append("Theta state - natural for imagery and release")
        if phase.get('isochronic', False):
            safety_notes.append("Isochronic pulses in theta - pause if uncomfortable")
    
    elif target_state in ['gamma', 'high_gamma']:
        safety_notes.append("High frequency state - monitor for overstimulation")
        if experience_level == 'beginner':
            safety_notes.append("Advanced frequencies - consider shorter exposure")
    
    # Transition quality warnings
    if transition_quality < 0.6:
        safety_notes.append("Rapid transition - allow extra integration time")
    
    # Phase complexity warnings
    layers = phase.get('layers', [])
    if len(layers) > 3:
        safety_notes.append("Complex layering - reduce volume if overwhelming")
    
    # Modality warnings
    modalities = [phase.get('isochronic', False), phase.get('bilateral', False), phase.get('monaural', False)]
    if sum(modalities) > 1:
        safety_notes.append("Multiple modalities - monitor for sensory overload")
    
    return safety_notes

def _calculate_schumann_alignment(frequencies: List[float]) -> float:
    """Calculate alignment with Schumann resonances."""
    if not frequencies:
        return 0.0
    
    schumann_freqs = [BIOFIELD_FREQUENCIES['schumann_primary']] + BIOFIELD_FREQUENCIES['schumann_harmonics']
    alignment_score = 0.0
    
    for freq in frequencies:
        for schumann_freq in schumann_freqs:
            # Check for direct alignment (within 10%)
            if abs(freq - schumann_freq) / schumann_freq < 0.1:
                alignment_score += 1.0
            # Check for harmonic relationships
            elif abs(freq / schumann_freq - round(freq / schumann_freq)) < 0.1:
                alignment_score += 0.5
    
    # Normalize by number of frequencies
    return min(1.0, alignment_score / len(frequencies))

def _calculate_solfeggio_presence(frequencies: List[float]) -> float:
    """Calculate presence of Solfeggio frequencies."""
    if not frequencies:
        return 0.0
    
    solfeggio_freqs = BIOFIELD_FREQUENCIES['solfeggio_core']
    presence_score = 0.0
    
    for freq in frequencies:
        for solfeggio_freq in solfeggio_freqs:
            if abs(freq - solfeggio_freq) / solfeggio_freq < 0.05:  # Within 5%
                presence_score += 1.0
    
    return min(1.0, presence_score / len(solfeggio_freqs))

def _calculate_golden_ratio_harmonics(frequencies: List[float]) -> float:
    """Calculate golden ratio harmonic relationships."""
    if len(frequencies) < 2:
        return 0.0
    
    golden_ratio = BIOFIELD_FREQUENCIES['golden_ratio_base']
    harmonic_score = 0.0
    total_pairs = 0
    
    for i in range(len(frequencies)):
        for j in range(i + 1, len(frequencies)):
            ratio = frequencies[j] / frequencies[i]
            total_pairs += 1
            
            # Check for golden ratio relationships
            for power in range(-3, 4):  # Check phi^-3 to phi^3
                target_ratio = golden_ratio ** power
                if abs(ratio - target_ratio) / target_ratio < 0.05:
                    harmonic_score += 1.0
                    break
    
    return harmonic_score / max(total_pairs, 1)

def _assess_frequency_harmony(frequencies: List[float]) -> float:
    """Assess overall frequency harmony using multiple criteria."""
    if len(frequencies) < 2:
        return 1.0  # Single frequency is always harmonious
    
    # Check for simple ratios
    simple_ratios = [1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 1.25, 1.33]  # Common harmonic ratios
    harmony_score = 0.0
    total_pairs = 0
    
    for i in range(len(frequencies)):
        for j in range(i + 1, len(frequencies)):
            ratio = frequencies[j] / frequencies[i]
            total_pairs += 1
            
            for simple_ratio in simple_ratios:
                if abs(ratio - simple_ratio) / simple_ratio < 0.1:
                    harmony_score += 1.0
                    break
    
    return harmony_score / max(total_pairs, 1)

def _assess_transition_smoothness(phases: List[Dict[str, Any]]) -> float:
    """Assess smoothness of transitions between phases."""
    if len(phases) < 2:
        return 1.0
    
    smoothness_scores = []
    
    for i in range(len(phases) - 1):
        current_phase = phases[i]
        next_phase = phases[i + 1]
        
        # Get final and initial frequencies
        current_final_freqs = _extract_final_frequencies(current_phase)
        next_initial_freqs = _extract_initial_frequencies(next_phase)
        
        if current_final_freqs and next_initial_freqs:
            # Calculate frequency jump magnitude
            avg_current = np.mean(current_final_freqs)
            avg_next = np.mean(next_initial_freqs)
            frequency_jump = abs(avg_next - avg_current) / max(avg_current, 1)
            
            # Assess smoothness based on jump size and transition type
            transition_type = next_phase.get('animation_type', 'linear')
            duration = next_phase.get('duration', 0)
            
            # Larger jumps need longer durations or smooth transitions
            required_duration = frequency_jump * 300  # 5 minutes per octave jump
            duration_adequacy = min(1.0, duration / max(required_duration, 60))
            
            # Smooth transition types get bonus
            transition_bonus = {'sinusoidal': 0.2, 'theta_gateway': 0.15, 'exponential': 0.1}.get(transition_type, 0.0)
            
            smoothness = duration_adequacy + transition_bonus
            smoothness_scores.append(min(1.0, smoothness))
    
    return np.mean(smoothness_scores) if smoothness_scores else 1.0

def _assess_intention_congruence(intention: str, frequencies: List[float], phases: List[Dict[str, Any]]) -> float:
    """Assess how well the frequency selection aligns with stated intention."""
    if not frequencies:
        return 0.5
    
    intention_profiles = {
        'release': {
            'preferred_ranges': [(1, 8), (396, 396), (528, 528)],  # Delta/theta + specific healing freqs
            'avoid_ranges': [(30, 100)],  # High gamma
            'weight': 0.8
        },
        'focus': {
            'preferred_ranges': [(13, 30), (40, 60)],  # Beta and low gamma
            'avoid_ranges': [(1, 4)],  # Deep delta
            'weight': 0.9
        },
        'integrate': {
            'preferred_ranges': [(8, 13), (528, 528)],  # Alpha + healing frequency
            'avoid_ranges': [],
            'weight': 0.85
        },
        'creativity': {
            'preferred_ranges': [(6, 8), (40, 80)],  # Theta + gamma
            'avoid_ranges': [(1, 4)],  # Deep delta
            'weight': 0.75
        }
    }
    
    profile = intention_profiles.get(intention, {'preferred_ranges': [], 'avoid_ranges': [], 'weight': 0.5})
    
    congruence_score = 0.0
    frequency_count = 0
    
    for freq in frequencies:
        frequency_count += 1
        freq_score = 0.0
        
        # Check preferred ranges
        for min_freq, max_freq in profile['preferred_ranges']:
            if min_freq <= freq <= max_freq:
                freq_score = 1.0
                break
        
        # Penalize avoid ranges
        for min_freq, max_freq in profile['avoid_ranges']:
            if min_freq <= freq <= max_freq:
                freq_score = -0.5
                break
        
        congruence_score += freq_score
    
    # Normalize and apply intention weight
    if frequency_count > 0:
        normalized_score = max(0.0, congruence_score / frequency_count + 0.5)  # Shift to [0, 1]
        return normalized_score * profile['weight']
    
    return 0.5

def _assess_neural_compatibility(frequencies: List[float], neural_profile: Dict[str, Any], 
                               phases: List[Dict[str, Any]]) -> float:
    """Assess compatibility with neural architecture."""
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    current_state = neural_profile.get('current_state', 'neutral')
    experience_level = neural_profile.get('experience_level', 'intermediate')
    
    # Base compatibility
    compatibility = 1.0
    
    # Sensitivity adjustments
    if sensitivity_level == 'sensitive':
        # Check for overly complex configurations
        avg_layers = np.mean([len(phase.get('layers', [])) for phase in phases])
        if avg_layers > 2:
            compatibility -= 0.2
        
        # Check for high frequencies
        high_freq_count = sum(1 for freq in frequencies if freq > 30)
        if high_freq_count / max(len(frequencies), 1) > 0.3:
            compatibility -= 0.15
    
    elif sensitivity_level == 'resilient':
        # Resilient users can handle more complexity
        complexity_bonus = min(0.1, len(phases) * 0.02)
        compatibility += complexity_bonus
    
    # Current state considerations
    if current_state == 'agitated':
        high_beta_count = sum(1 for freq in frequencies if 20 <= freq <= 30)
        if high_beta_count > 0:
            compatibility -= 0.1
    
    elif current_state == 'tired':
        gamma_count = sum(1 for freq in frequencies if freq > 30)
        if gamma_count > 0:
            compatibility -= 0.15
    
    # Experience level adjustments
    experience_multipliers = {
        'beginner': 0.9,
        'intermediate': 1.0,
        'advanced': 1.05,
        'expert': 1.1
    }
    compatibility *= experience_multipliers.get(experience_level, 1.0)
    
    return np.clip(compatibility, 0.0, 1.0)

def _generate_coherence_timeline(phases: List[Dict[str, Any]], intention: str, 
                               neural_profile: Dict[str, Any]) -> List[float]:
    """Generate a timeline of predicted biofield coherence throughout the session."""
    timeline = []
    current_coherence = 0.7  # Starting coherence
    
    for phase in phases:
        layers = phase.get('layers', [])
        duration = phase.get('duration', 0)
        phase_type = phase.get('type', 'static')
        
        # Calculate phase coherence factors
        layer_complexity = len(layers)
        complexity_factor = max(0.5, 1.0 - (layer_complexity - 1) * 0.1)
        
        # Frequency analysis
        frequencies = []
        for layer in layers:
            carrier = layer.get('carrier', 0)
            if carrier > 0:
                frequencies.append(carrier)
        
        biofield_alignment = _calculate_biofield_alignment(layers, intention, 'alpha')  # Simplified
        
        # Duration effects (longer phases allow more coherence)
        duration_factor = min(1.2, 1.0 + duration / 1800)  # Bonus up to 30 minutes
        
        # Neural profile effects
        sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
        neural_factor = {'sensitive': 0.95, 'standard': 1.0, 'resilient': 1.05}.get(sensitivity_level, 1.0)
        
        # Calculate phase coherence
        phase_coherence = (
            current_coherence * 0.7 +  # Continuity
            biofield_alignment * 0.2 +  # Biofield contribution
            complexity_factor * 0.1    # Complexity contribution
        ) * duration_factor * neural_factor
        
        # Update for next phase
        current_coherence = np.clip(phase_coherence, 0.3, 1.0)
        timeline.append(current_coherence)
    
    return timeline

def _extract_final_frequencies(phase: Dict[str, Any]) -> List[float]:
    """Extract final frequencies from a phase."""
    frequencies = []
    layers = phase.get('layers', [])
    
    for layer in layers:
        if phase.get('type') == 'static':
            beat = layer.get('beat', 0)
            if beat > 0:
                frequencies.append(beat)
        else:  # ramp
            end_beat = layer.get('end_beat', 0)
            if end_beat > 0:
                frequencies.append(end_beat)
    
    return frequencies

def _extract_initial_frequencies(phase: Dict[str, Any]) -> List[float]:
    """Extract initial frequencies from a phase."""
    frequencies = []
    layers = phase.get('layers', [])
    
    for layer in layers:
        if phase.get('type') == 'static':
            beat = layer.get('beat', 0)
            if beat > 0:
                frequencies.append(beat)
        else:  # ramp
            start_beat = layer.get('start_beat', 0)
            if start_beat > 0:
                frequencies.append(start_beat)
    
    return frequencies

def _create_guidance_templates(intention: str, experience_level: str, 
                             intention_profile: Dict[str, Any]) -> Dict[str, str]:
    """Create consciousness guidance templates based on intention and experience."""
    templates = {}
    
    guidance_style = intention_profile['guidance_style']
    emphasis = intention_profile['emphasis']
    
    # Base templates by experience level
    if experience_level == 'beginner':
        prefix = "Gentle invitation: "
        approach = "Simply allow yourself to"
    elif experience_level == 'intermediate':
        prefix = "Notice how you can "
        approach = "Observe and gently guide"
    elif experience_level == 'advanced':
        prefix = "Deepen into "
        approach = "Consciously direct your awareness to"
    else:  # expert
        prefix = "Weave with "
        approach = "Orchestrate the consciousness field through"
    
    # Intention-specific guidance cores
    intention_cores = {
        'release': f"{approach} let go of tension and resistance, allowing natural flow",
        'focus': f"{approach} sharpen your attention and concentration, building mental clarity",
        'integrate': f"{approach} synthesize insights and experiences into unified awareness",
        'creativity': f"{approach} explore innovative possibilities and creative potential",
        'neutral': f"{approach} rest in open awareness without agenda"
    }
    
    base_guidance = prefix + intention_cores.get(intention, intention_cores['neutral'])
    
    # State-specific modifications
    templates['delta'] = base_guidance + ". Deep healing space - rest completely."
    templates['theta'] = base_guidance + ". Imagery and inner wisdom accessible."
    templates['alpha'] = base_guidance + ". Bridge state - conscious yet relaxed."
    templates['beta'] = base_guidance + ". Alert awareness - engage actively."
    templates['gamma'] = base_guidance + ". Expanded consciousness - integrate insights."
    
    return templates

def _select_contextual_guidance(state: str, phase_type: str, transition_type: str, 
                              duration: float, templates: Dict[str, str],
                              intention_profile: Dict[str, Any]) -> str:
    """Select appropriate guidance based on phase context."""
    base_guidance = templates.get(state, templates.get('alpha', ''))
    
    # Duration adjustments
    if duration <= 300:  # <= 5 minutes
        time_note = " Brief phase - settle quickly."
    elif duration >= 1800:  # >= 30 minutes
        time_note = " Extended exploration - go deeper."
    else:
        time_note = ""
    
    # Transition type adjustments
    transition_notes = {
        'theta_gateway': " Allow the theta gateway to open naturally.",
        'gamma_emergence': " Feel consciousness expanding into gamma clarity.",
        'delta_descent': " Surrender into deep delta healing space.",
        'sinusoidal': " Flow with the gentle rhythmic transition.",
        'exponential': " Notice the accelerating shift in awareness."
    }
    
    transition_note = transition_notes.get(transition_type, "")
    
    return base_guidance + time_note + transition_note

def _enhance_guidance_with_metrics(guidance_text: str, quality: float, biofield_align: float,
                                 state: str, duration: float, experience_level: str) -> str:
    """Enhance guidance based on quality and biofield metrics."""
    enhanced_guidance = guidance_text
    
    # Quality-based enhancements
    if quality > 0.8:
        enhanced_guidance += " Optimal transition quality supports deep work."
    elif quality < 0.6:
        enhanced_guidance += " Take extra time to settle into this state."
    
    # Biofield alignment enhancements
    if biofield_align > 0.7:
        enhanced_guidance += " Strong biofield alignment enhances receptivity."
    elif biofield_align < 0.4:
        enhanced_guidance += " Focus on breath and body awareness for grounding."
    
    # Experience-specific additions
    if experience_level in ['advanced', 'expert'] and state in ['theta', 'gamma']:
        enhanced_guidance += " Advanced state - engage sophisticated techniques."
    
    return enhanced_guidance

def _generate_consciousness_techniques(state: str, intention: str, quality: float, 
                                     experience_level: str) -> List[str]:
    """Generate specific consciousness techniques for the phase."""
    techniques = []
    
    # Base techniques by state
    state_techniques = {
        'delta': ['Deep body scanning', 'Healing intention setting', 'Complete surrender'],
        'theta': ['Imagery and visualization', 'Emotional release work', 'Memory integration'],
        'alpha': ['Mindful awareness', 'Breath observation', 'Present moment anchoring'],
        'beta': ['Focused attention', 'Mental clarity practices', 'Goal visualization'],
        'gamma': ['Expanded awareness', 'Unity consciousness', 'Insight integration']
    }
    
    techniques.extend(state_techniques.get(state, ['Open awareness']))
    
    # Intention-specific additions
    intention_techniques = {
        'release': ['Progressive relaxation', 'Tension dissolution', 'Emotional flow'],
        'focus': ['One-pointed concentration', 'Attention training', 'Mental sharpening'],
        'integrate': ['Synthesis practices', 'Wholeness meditation', 'Pattern recognition'],
        'creativity': ['Divergent thinking', 'Inspiration cultivation', 'Creative flow']
    }
    
    techniques.extend(intention_techniques.get(intention, []))
    
    # Experience level refinements
    if experience_level == 'beginner':
        techniques = [tech for tech in techniques if 'advanced' not in tech.lower()][:3]
    elif experience_level in ['advanced', 'expert']:
        techniques.append('Consciousness field manipulation')
    
    return techniques[:4]  # Limit to 4 techniques

def _generate_biofield_notes(biofield_align: float, state: str) -> List[str]:
    """Generate biofield-specific notes for the phase."""
    notes = []
    
    if biofield_align > 0.7:
        notes.append("Strong biofield resonance - enhanced healing potential")
    elif biofield_align > 0.5:
        notes.append("Good biofield alignment - natural flow supported")
    else:
        notes.append("Focus on grounding and breath for biofield coherence")
    
    # State-specific biofield notes
    state_notes = {
        'delta': "Deep biofield regeneration - allow cellular renewal",
        'theta': "Biofield gateway open - emotional and spiritual healing active",
        'alpha': "Biofield bridge state - conscious healing direction possible",
        'beta': "Biofield focused - mental clarity and cognitive coherence",
        'gamma': "Biofield expansion - unified field awareness"
    }
    
    if state in state_notes:
        notes.append(state_notes[state])
    
    return notes

def _generate_phase_safety_notes(phase: Dict[str, Any], state: str, 
                                neural_profile: Dict[str, Any], quality: float) -> List[str]:
    """Generate safety notes specific to the phase."""
    safety_notes = []
    
    # State-specific safety
    if state in ['delta', 'deep_delta']:
        safety_notes.append("Deep states - ensure you won't be disturbed")
    elif state in ['gamma', 'high_gamma']:
        safety_notes.append("High frequency - reduce volume if overwhelming")
    
    # Quality-based safety
    if quality < 0.6:
        safety_notes.append("Rapid transition - pause if uncomfortable")
    
    # Neural profile safety
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    if sensitivity_level == 'sensitive':
        safety_notes.append("Sensitive profile - honor your limits")
    
    # Modality safety
    if phase.get('bilateral') and phase.get('bilateral_freq', 0) > 2:
        safety_notes.append("Fast bilateral panning - center if disorienting")
    
    return safety_notes

def _assess_experience_appropriateness(phase: Dict[str, Any], state: str, experience_level: str) -> float:
    """Assess how appropriate the phase is for the experience level."""
    base_score = 1.0
    
    # Complex phases need higher experience
    layer_count = len(phase.get('layers', []))
    if layer_count > 2 and experience_level == 'beginner':
        base_score -= 0.2
    
    # Advanced states need experience
    if state in ['gamma', 'high_gamma'] and experience_level == 'beginner':
        base_score -= 0.3
    
    # Multiple modalities need experience
    modality_count = sum([
        phase.get('isochronic', False),
        phase.get('bilateral', False),
        phase.get('monaural', False)
    ])
    
    if modality_count > 1 and experience_level == 'beginner':
        base_score -= 0.15
    
    return np.clip(base_score, 0.0, 1.0)

def _generate_session_level_guidance(config: Dict[str, Any], consciousness_analysis: ConsciousnessAnalysis,
                                   biofield_metrics: BiofieldCoherenceMetrics,
                                   intention_profile: Dict[str, Any]) -> str:
    """Generate overall session-level guidance."""
    intention = config.get('intention', 'neutral')
    total_duration = sum(phase.get('duration', 0) for phase in config.get('phases', []))
    
    # Base session guidance
    guidance_parts = []
    
    # Intention-specific opening
    intention_openings = {
        'release': "This session supports deep release and letting go. Allow yourself to surrender into the process.",
        'focus': "This session enhances concentration and mental clarity. Engage actively with focused intention.",
        'integrate': "This session facilitates integration and synthesis. Be open to wholeness and connection.",
        'creativity': "This session opens creative flow and inspiration. Welcome new possibilities and insights.",
        'neutral': "This session offers balanced awareness. Rest in open, receptive consciousness."
    }
    
    guidance_parts.append(intention_openings.get(intention, intention_openings['neutral']))
    
    # Duration guidance
    if total_duration <= 1800:  # <= 30 minutes
        guidance_parts.append("Shorter session - focus on quality over quantity.")
    elif total_duration >= 3600:  # >= 60 minutes
        guidance_parts.append("Extended session - pace yourself and stay hydrated.")
    
    # Quality assessment
    if consciousness_analysis.consciousness_journey_quality > 0.8:
        guidance_parts.append("High-quality consciousness journey - trust the process completely.")
    elif consciousness_analysis.consciousness_journey_quality < 0.6:
        guidance_parts.append("Monitor your responses closely and pause if needed.")
    
    # Biofield coherence guidance
    if biofield_metrics.overall_coherence > 0.7:
        guidance_parts.append("Strong biofield coherence supports deep transformation.")
    else:
        guidance_parts.append("Focus on breath and grounding for enhanced receptivity.")
    
    # Integration guidance
    if consciousness_analysis.integration_windows:
        guidance_parts.append(f"{len(consciousness_analysis.integration_windows)} natural integration windows available.")
    
    return " ".join(guidance_parts)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN METADATA GENERATION FUNCTION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def generate_metadata(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate comprehensive consciousness-aware metadata for neural entrainment sessions.
    
    Args:
        config: Complete session configuration including neural profile and phases
        
    Returns:
        Comprehensive metadata dictionary with consciousness analysis, biofield metrics,
        guidance, and safety assessments
    """
    start_time = datetime.datetime.now()
    
    # Extract core configuration elements
    intention = config.get('intention', 'neutral')
    neural_profile = config.get('neural_profile', {
        'sensitivity_level': 'standard',
        'current_state': 'neutral',
        'experience_level': 'intermediate'
    })
    phases = config.get('phases', [])
    
    # Perform comprehensive consciousness analysis
    consciousness_analysis = analyze_consciousness_progression(config, neural_profile)
    
    # Assess biofield coherence potential
    biofield_metrics = assess_biofield_coherence_potential(config, neural_profile)
    
    # Generate intelligent guidance
    guidance_list = generate_consciousness_guidance(config, consciousness_analysis, biofield_metrics)
    
    # Calculate session totals
    total_duration = sum(phase.get('duration', 0) for phase in phases)
    if config.get('include_integration', False):
        total_duration += config.get('integration_duration', 180)
    
    # Enhanced phase metadata
    enhanced_phases = []
    for i, (phase, state, quality, biofield_align) in enumerate(zip(
        phases,
        consciousness_analysis.state_sequence,
        consciousness_analysis.transition_quality,
        consciousness_analysis.biofield_alignment
    )):
        enhanced_phase = copy.deepcopy(phase)
        enhanced_phase.update({
            'phase_index': i,
            'consciousness_state': state,
            'transition_quality': quality,
            'biofield_alignment': biofield_align,
            'neural_load': _calculate_neural_load(
                phase, phase.get('layers', []), 
                NEURAL_SENSITIVITY_METADATA.get(neural_profile['sensitivity_level'], NEURAL_SENSITIVITY_METADATA['standard'])
            ),
            'safety_level': 'high' if quality > 0.8 else 'standard' if quality > 0.6 else 'monitor_closely',
            'integration_potential': any(
                window['phase_index'] == i for window in consciousness_analysis.integration_windows
            ),
            'timestamp': start_time.isoformat()
        })
        enhanced_phases.append(enhanced_phase)
    
    # Integration phase metadata
    if config.get('include_integration', False):
        integration_duration = config.get('integration_duration', 180)
        enhanced_phases.append({
            'type': 'integration',
            'duration': integration_duration,
            'phase_index': len(enhanced_phases),
            'consciousness_state': 'integration',
            'transition_quality': 0.95,
            'biofield_alignment': 0.9,
            'neural_load': 0.5,
            'safety_level': 'high',
            'integration_potential': True,
            'description': 'Consciousness integration and grounding',
            'healing_frequency_emphasis': True,
            'timestamp': start_time.isoformat()
        })
    
    # Comprehensive metadata assembly
    metadata = {
        # Session overview with enhanced consciousness metrics
        'session_overview': {
            'intention': intention,
            'total_duration': total_duration,
            'duration_formatted': f"{int(total_duration//60)}m{int(total_duration%60):02d}s",
            'num_phases': len(enhanced_phases),
            'consciousness_journey_quality': consciousness_analysis.consciousness_journey_quality,
            'biofield_coherence_score': biofield_metrics.overall_coherence,
            'neural_compatibility': biofield_metrics.neural_compatibility,
            'safety_assessment': consciousness_analysis.neural_load_assessment.get('overload_risk', 'acceptable'),
            'integration_windows_count': len(consciousness_analysis.integration_windows),
            'state_sequence_summary': ' → '.join(consciousness_analysis.state_sequence),
            'recommended_preparation': _generate_preparation_recommendations(neural_profile, intention),
            'session_complexity': _assess_session_complexity(phases, neural_profile)
        },
        
        # Enhanced phases with consciousness metadata
        'phases': enhanced_phases,
        
        # Comprehensive consciousness analysis
        'consciousness_analysis': {
            'state_sequence': consciousness_analysis.state_sequence,
            'transition_quality_timeline': consciousness_analysis.transition_quality,
            'biofield_alignment_timeline': consciousness_analysis.biofield_alignment,
            'coherence_progression': consciousness_analysis.coherence_progression,
            'integration_windows': consciousness_analysis.integration_windows,
            'neural_load_assessment': consciousness_analysis.neural_load_assessment,
            'safety_considerations': consciousness_analysis.safety_considerations,
            'journey_quality_rating': _rate_journey_quality(consciousness_analysis.consciousness_journey_quality)
        },
        
        # Detailed biofield metrics
        'biofield_analysis': {
            'coherence_metrics': {
                'schumann_alignment': biofield_metrics.schumann_alignment,
                'solfeggio_presence': biofield_metrics.solfeggio_presence,
                'golden_ratio_harmonics': biofield_metrics.golden_ratio_harmonics,
                'frequency_harmony': biofield_metrics.frequency_harmony,
                'transition_smoothness': biofield_metrics.transition_smoothness,
                'intention_congruence': biofield_metrics.intention_congruence,
                'neural_compatibility': biofield_metrics.neural_compatibility,
                'overall_coherence': biofield_metrics.overall_coherence
            },
            'coherence_timeline': biofield_metrics.coherence_timeline,
            'biofield_optimization_suggestions': _generate_biofield_optimization_suggestions(biofield_metrics),
            'natural_frequency_analysis': _analyze_natural_frequencies(config)
        },
        
        # Comprehensive guidance system
        'consciousness_guidance': guidance_list,
        
        # Neural profile metadata
        'neural_profile_analysis': {
            'sensitivity_level': neural_profile['sensitivity_level'],
            'current_state': neural_profile['current_state'],
            'experience_level': neural_profile['experience_level'],
            'session_appropriateness': _assess_session_appropriateness(config, neural_profile),
            'personalization_applied': True,
            'custom_factors': neural_profile.get('custom_factors', {}),
            'recommended_adjustments': _generate_profile_recommendations(config, neural_profile)
        },
        
        # Enhanced safety analysis
        'safety_analysis': {
            'overall_safety_rating': _calculate_overall_safety_rating(consciousness_analysis, biofield_metrics, neural_profile),
            'risk_factors': _identify_risk_factors(config, consciousness_analysis, neural_profile),
            'mitigation_strategies': _generate_mitigation_strategies(consciousness_analysis, neural_profile),
            'emergency_protocols': _generate_emergency_protocols(neural_profile),
            'monitoring_recommendations': _generate_monitoring_recommendations(config, neural_profile)
        },
        
        # Configuration summary with consciousness enhancements
        'config_summary': {
            **{k: v for k, v in config.items() if k not in ['phases', 'neural_profile']},
            'consciousness_framework_version': '2.0',
            'biofield_intelligence_enabled': True,
            'neural_architecture_respected': True,
            'generated_at': start_time.isoformat(),
            'generation_duration_ms': (datetime.datetime.now() - start_time).total_seconds() * 1000
        }
    }
    
    # Validation and final checks
    metadata['validation'] = {
        'metadata_complete': True,
        'consciousness_analysis_valid': len(consciousness_analysis.state_sequence) == len(phases),
        'biofield_metrics_valid': 0.0 <= biofield_metrics.overall_coherence <= 1.0,
        'guidance_generated': len(guidance_list) > 0,
        'safety_assessed': len(consciousness_analysis.safety_considerations) >= 0,
        'neural_profile_integrated': True
    }
    
    end_time = datetime.datetime.now()
    generation_duration = (end_time - start_time).total_seconds()
    
    logging.info(f"Consciousness metadata generated: {len(enhanced_phases)} phases, "
                f"quality={consciousness_analysis.consciousness_journey_quality:.3f}, "
                f"coherence={biofield_metrics.overall_coherence:.3f}, "
                f"duration={generation_duration:.3f}s")
    
    return metadata

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ADDITIONAL HELPER FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _generate_preparation_recommendations(neural_profile: Dict[str, Any], intention: str) -> List[str]:
    """Generate personalized preparation recommendations."""
    recommendations = []
    
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    current_state = neural_profile.get('current_state', 'neutral')
    
    # Base recommendations
    recommendations.extend([
        "Create a quiet, comfortable environment",
        "Use quality headphones for optimal stereo effect",
        "Stay hydrated before and after the session"
    ])
    
    # Sensitivity-specific
    if sensitivity_level == 'sensitive':
        recommendations.extend([
            "Start with lower volume and adjust as needed",
            "Ensure you won't be disturbed",
            "Have grounding materials nearby (blanket, water)"
        ])
    
    # Current state adjustments
    if current_state == 'agitated':
        recommendations.append("Take a few minutes to breathe deeply before starting")
    elif current_state == 'tired':
        recommendations.append("Consider a brief energizing activity before the session")
    
    # Intention-specific
    intention_prep = {
        'release': "Set intention for what you're ready to release",
        'focus': "Clear your workspace and prepare for concentrated work",
        'integrate': "Journal recent insights or experiences beforehand",
        'creativity': "Gather creative materials for post-session expression"
    }
    
    if intention in intention_prep:
        recommendations.append(intention_prep[intention])
    
    return recommendations

def _assess_session_complexity(phases: List[Dict[str, Any]], neural_profile: Dict[str, Any]) -> str:
    """Assess overall session complexity."""
    complexity_score = 0
    
    # Phase count
    complexity_score += len(phases) * 0.1
    
    # Layer complexity
    for phase in phases:
        layers = phase.get('layers', [])
        complexity_score += len(layers) * 0.2
        
        # Modulation complexity
        for layer in layers:
            if layer.get('harmonics'):
                complexity_score += len(layer['harmonics']) * 0.1
            if layer.get('fm_depth', 0) > 0:
                complexity_score += 0.1
    
    # Modality complexity
    for phase in phases:
        modalities = [phase.get('isochronic', False), phase.get('bilateral', False), phase.get('monaural', False)]
        complexity_score += sum(modalities) * 0.1
    
    # Neural profile adjustment
    experience_level = neural_profile.get('experience_level', 'intermediate')
    if experience_level == 'beginner':
        complexity_score *= 1.2  # Appears more complex to beginners
    elif experience_level == 'expert':
        complexity_score *= 0.8  # Appears simpler to experts
    
    # Classification
    if complexity_score < 1.0:
        return 'simple'
    elif complexity_score < 2.5:
        return 'moderate'
    elif complexity_score < 4.0:
        return 'complex'
    else:
        return 'advanced'

def _rate_journey_quality(quality_score: float) -> str:
    """Provide qualitative rating for consciousness journey quality."""
    if quality_score >= 0.9:
        return 'exceptional'
    elif quality_score >= 0.8:
        return 'excellent'
    elif quality_score >= 0.7:
        return 'good'
    elif quality_score >= 0.6:
        return 'adequate'
    elif quality_score >= 0.5:
        return 'needs_monitoring'
    else:
        return 'requires_adjustment'

def _generate_biofield_optimization_suggestions(biofield_metrics: BiofieldCoherenceMetrics) -> List[str]:
    """Generate suggestions for optimizing biofield coherence."""
    suggestions = []
    
    if biofield_metrics.schumann_alignment < 0.5:
        suggestions.append("Consider adding Schumann resonance frequencies (7.83Hz) for Earth connection")
    
    if biofield_metrics.solfeggio_presence < 0.3:
        suggestions.append("Integrate Solfeggio frequencies (396Hz, 528Hz) for healing enhancement")
    
    if biofield_metrics.golden_ratio_harmonics < 0.3:
        suggestions.append("Optimize carrier frequencies using golden ratio relationships")
    
    if biofield_metrics.frequency_harmony < 0.6:
        suggestions.append("Review frequency relationships for better harmonic consonance")
    
    if biofield_metrics.transition_smoothness < 0.7:
        suggestions.append("Extend transition durations or use smoother animation types")
    
    if biofield_metrics.intention_congruence < 0.6:
        suggestions.append("Align frequency selection more closely with stated intention")
    
    return suggestions

def _analyze_natural_frequencies(config: Dict[str, Any]) -> Dict[str, Any]:
    """Analyze presence of natural/healing frequencies in the configuration."""
    analysis = {
        'schumann_present': False,
        'solfeggio_present': False,
        'healing_frequencies_present': False,
        'natural_frequency_count': 0,
        'frequency_breakdown': {}
    }
    
    all_frequencies = []
    phases = config.get('phases', [])
    
    for phase in phases:
        for layer in phase.get('layers', []):
            carrier = layer.get('carrier', 0)
            if carrier > 0:
                all_frequencies.append(carrier)
    
    # Check for specific frequency categories
    for freq in all_frequencies:
        # Schumann resonances
        if abs(freq - 7.83) < 0.5 or any(abs(freq - h) < 1.0 for h in [14.3, 20.8, 27.3, 33.8]):
            analysis['schumann_present'] = True
            analysis['natural_frequency_count'] += 1
        
        # Solfeggio frequencies
        if any(abs(freq - s) < 5 for s in BIOFIELD_FREQUENCIES['solfeggio_core']):
            analysis['solfeggio_present'] = True
            analysis['natural_frequency_count'] += 1
        
        # Healing frequencies
        if any(abs(freq - h) < 5 for h in BIOFIELD_FREQUENCIES['healing_frequencies']):
            analysis['healing_frequencies_present'] = True
    
    analysis['natural_frequency_percentage'] = analysis['natural_frequency_count'] / max(len(all_frequencies), 1)
    
    return analysis

def _assess_session_appropriateness(config: Dict[str, Any], neural_profile: Dict[str, Any]) -> float:
    """Assess how appropriate the session is for the neural profile."""
    appropriateness = 1.0
    
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    experience_level = neural_profile.get('experience_level', 'intermediate')
    current_state = neural_profile.get('current_state', 'neutral')
    
    phases = config.get('phases', [])
    total_duration = sum(phase.get('duration', 0) for phase in phases)
    
    # Duration appropriateness
    recommended_durations = {
        'sensitive': 1800,    # 30 minutes
        'standard': 3600,     # 60 minutes
        'resilient': 5400     # 90 minutes
    }
    
    recommended = recommended_durations.get(sensitivity_level, 3600)
    if total_duration > recommended * 1.5:
        appropriateness -= 0.2
    
    # Complexity appropriateness
    avg_layers = np.mean([len(phase.get('layers', [])) for phase in phases])
    experience_limits = {
        'beginner': 2,
        'intermediate': 3,
        'advanced': 5,
        'expert': float('inf')
    }
    
    if avg_layers > experience_limits.get(experience_level, 3):
        appropriateness -= 0.15
    
    # Current state compatibility
    if current_state == 'agitated':
        # Check for calming vs stimulating content
        stimulating_phases = 0
        for phase in phases:
            for layer in phase.get('layers', []):
                beat = layer.get('beat', layer.get('start_beat', 0))
                if beat > 20:  # High beta/gamma
                    stimulating_phases += 1
                    break
        
        if stimulating_phases / max(len(phases), 1) > 0.3:
            appropriateness -= 0.25
    
    return np.clip(appropriateness, 0.0, 1.0)

def _generate_profile_recommendations(config: Dict[str, Any], neural_profile: Dict[str, Any]) -> List[str]:
    """Generate personalized recommendations based on neural profile."""
    recommendations = []
    
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    experience_level = neural_profile.get('experience_level', 'intermediate')
    
    if sensitivity_level == 'sensitive':
        recommendations.extend([
            "Consider reducing session length by 25-50%",
            "Lower volume settings recommended",
            "Add extra integration time"
        ])
    elif sensitivity_level == 'resilient':
        recommendations.append("You may tolerate longer or more complex sessions")
    
    if experience_level == 'beginner':
        recommendations.extend([
            "Start with simpler preset configurations",
            "Focus on single-layer phases initially",
            "Build experience gradually"
        ])
    elif experience_level == 'expert':
        recommendations.append("Consider advanced customization options")
    
    return recommendations

def _calculate_overall_safety_rating(consciousness_analysis: ConsciousnessAnalysis,
                                   biofield_metrics: BiofieldCoherenceMetrics,
                                   neural_profile: Dict[str, Any]) -> str:
    """Calculate overall safety rating for the session."""
    safety_score = 1.0
    
    # Neural load assessment impact
    load_risk = consciousness_analysis.neural_load_assessment.get('overload_risk', 'acceptable')
    if load_risk == 'high':
        safety_score -= 0.3
    elif load_risk == 'moderate':
        safety_score -= 0.1
    
    # Transition quality impact
    avg_transition_quality = np.mean(consciousness_analysis.transition_quality) if consciousness_analysis.transition_quality else 0.8
    if avg_transition_quality < 0.6:
        safety_score -= 0.2
    
    # Neural compatibility impact
    if biofield_metrics.neural_compatibility < 0.7:
        safety_score -= 0.1
    
    # Safety considerations count
    if len(consciousness_analysis.safety_considerations) > 5:
        safety_score -= 0.1
    
    # Rating classification
    if safety_score >= 0.9:
        return 'excellent'
    elif safety_score >= 0.8:
        return 'good'
    elif safety_score >= 0.7:
        return 'adequate'
    elif safety_score >= 0.6:
        return 'requires_monitoring'
    else:
        return 'requires_modification'

def _identify_risk_factors(config: Dict[str, Any], consciousness_analysis: ConsciousnessAnalysis,
                         neural_profile: Dict[str, Any]) -> List[str]:
    """Identify potential risk factors in the session configuration."""
    risk_factors = []
    
    # Neural load risks
    load_assessment = consciousness_analysis.neural_load_assessment
    if load_assessment.get('overload_risk') == 'high':
        risk_factors.append("High neural processing load - may cause fatigue")
    
    # State transition risks
    if len(consciousness_analysis.state_sequence) > 6:
        risk_factors.append("Many consciousness state changes - may be overwhelming")
    
    # Transition quality risks
    poor_transitions = sum(1 for q in consciousness_analysis.transition_quality if q < 0.6)
    if poor_transitions > 0:
        risk_factors.append(f"{poor_transitions} rapid transitions detected - monitor comfort")
    
    # Sensitivity-specific risks
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    if sensitivity_level == 'sensitive':
        phases = config.get('phases', [])
        total_duration = sum(phase.get('duration', 0) for phase in phases)
        if total_duration > 2400:  # > 40 minutes
            risk_factors.append("Extended duration for sensitive profile")
    
    # Experience level risks
    experience_level = neural_profile.get('experience_level', 'intermediate')
    if experience_level == 'beginner':
        complex_phases = sum(1 for phase in config.get('phases', []) if len(phase.get('layers', [])) > 2)
        if complex_phases > 0:
            risk_factors.append("Complex configurations detected for beginner level")
    
    return risk_factors

def _generate_mitigation_strategies(consciousness_analysis: ConsciousnessAnalysis,
                                  neural_profile: Dict[str, Any]) -> List[str]:
    """Generate strategies to mitigate identified risks."""
    strategies = []
    
    # Neural load mitigation
    if consciousness_analysis.neural_load_assessment.get('overload_risk') == 'high':
        strategies.extend([
            "Take regular breaks during the session",
            "Reduce volume by 20-30%",
            "Extend integration time after session"
        ])
    
    # Transition mitigation
    poor_transitions = sum(1 for q in consciousness_analysis.transition_quality if q < 0.6)
    if poor_transitions > 0:
        strategies.extend([
            "Pause between phases if feeling uncomfortable",
            "Focus on breath work during transitions",
            "Allow extra time for state changes"
        ])
    
    # Sensitivity mitigation
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    if sensitivity_level == 'sensitive':
        strategies.extend([
            "Start with 50% volume and adjust as comfortable",
            "Keep water and grounding materials nearby",
            "Honor your limits - stop if needed"
        ])
    
    # Experience mitigation
    experience_level = neural_profile.get('experience_level', 'intermediate')
    if experience_level == 'beginner':
        strategies.extend([
            "Read guidance carefully before starting",
            "Consider shorter initial sessions",
            "Have support person available if needed"
        ])
    
    return strategies

def _generate_emergency_protocols(neural_profile: Dict[str, Any]) -> List[str]:
    """Generate emergency protocols based on neural profile."""
    protocols = []
    
    # Universal protocols
    protocols.extend([
        "Stop session immediately if experiencing discomfort",
        "Breathe deeply and ground yourself",
        "Drink water and move gently"
    ])
    
    # Sensitivity-specific protocols
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    if sensitivity_level == 'sensitive':
        protocols.extend([
            "Remove headphones and sit quietly",
            "Use grounding techniques (feel feet on floor)",
            "Seek quiet, low-stimulation environment"
        ])
    
    # Experience-specific protocols
    experience_level = neural_profile.get('experience_level', 'intermediate')
    if experience_level == 'beginner':
        protocols.append("Contact session guide or healthcare provider if needed")
    
    return protocols

def _generate_monitoring_recommendations(config: Dict[str, Any], neural_profile: Dict[str, Any]) -> List[str]:
    """Generate recommendations for monitoring during the session."""
    recommendations = []
    
    # Universal monitoring
    recommendations.extend([
        "Monitor comfort levels throughout",
        "Notice any changes in breathing or heart rate",
        "Track emotional responses"
    ])
    
    # Configuration-specific monitoring
    phases = config.get('phases', [])
    gamma_phases = sum(1 for phase in phases 
                      for layer in phase.get('layers', [])
                      if layer.get('beat', 0) > 30)
    
    if gamma_phases > 0:
        recommendations.append("Monitor for overstimulation during high-frequency phases")
    
    # Neural profile specific
    current_state = neural_profile.get('current_state', 'neutral')
    if current_state == 'agitated':
        recommendations.append("Monitor for increased agitation - reduce stimulation if needed")
    elif current_state == 'tired':
        recommendations.append("Monitor energy levels - pause if excessive fatigue occurs")
    
    # Safety profile considerations
    safety_profile = config.get('safety_profile', {})
    if safety_profile.get('epilepsy', False):
        recommendations.append("Monitor for any visual disturbances or auras")
    
    return recommendations

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
__description__ = "Consciousness-aware metadata generator with biofield intelligence"

# Export public API
__all__ = [
    # Main functions
    'generate_metadata',
    'analyze_consciousness_progression',
    'assess_biofield_coherence_potential',
    'generate_consciousness_guidance',
    
    # Data classes
    'ConsciousnessAnalysis',
    'BiofieldCoherenceMetrics',
    'ConsciousnessTransitionType',
    
    # Constants for advanced users
    'CONSCIOUSNESS_STATE_FREQUENCIES',
    'BIOFIELD_FREQUENCIES',
    'NEURAL_SENSITIVITY_METADATA',
    'INTENTION_METADATA_PROFILES'
]

logging.info(f"Consciousness Metadata Generator v{__version__} initialized - "
            f"Advanced consciousness analysis and biofield intelligence framework ready")