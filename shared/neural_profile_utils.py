#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Neural Profile Utils
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Neural Profile Utilities - Processing and management for neural profiles.

This module provides comprehensive utilities for neural profile creation, validation,
compatibility checking, and personalization within the Neural Entrainment System.
All profile operations ensure consciousness-aware optimization and safety compliance.
"""

import json
import hashlib
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple, Optional, Union
from dataclasses import dataclass, field, asdict
from enum import Enum
import logging

# Import shared constants
from .consciousness_constants import (
    CONSCIOUSNESS_STATES, 
    BRAINWAVE_FREQUENCIES,
    ExperienceLevel
)
from .biofield_constants import (
    BIOFIELD_COHERENCE_LEVELS,
    calculate_biofield_coherence
)
from .safety_constants import (
    NEURAL_LOAD_LIMITS,
    check_safety_compliance
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# NEURAL PROFILE DATA STRUCTURES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ProfileType(Enum):
    """Types of neural profiles."""
    BEGINNER = "beginner"
    PERSONALIZED = "personalized"
    THERAPEUTIC = "therapeutic"
    ADVANCED = "advanced"
    RESEARCH = "research"

class SensitivityLevel(Enum):
    """Neural sensitivity levels."""
    VERY_LOW = "very_low"
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    VERY_HIGH = "very_high"

@dataclass
class BrainwavePreference:
    """Individual brainwave frequency preferences."""
    frequency_range: str
    preferred_intensity: float
    tolerance_range: Tuple[float, float]
    response_quality: str  # "excellent", "good", "moderate", "poor"
    notes: str = ""

@dataclass
class ConsciousnessPreference:
    """Consciousness state preferences and responses."""
    state_name: str
    affinity_level: float  # 0.0-1.0
    optimal_duration_minutes: int
    preparation_time_needed: int
    integration_time_needed: int
    response_notes: str = ""

@dataclass
class BiofieldProfile:
    """Biofield intelligence profile."""
    schumann_resonance_sensitivity: float
    solfeggio_responsiveness: Dict[str, float]
    golden_ratio_harmony_level: float
    coherence_baseline: float
    field_stability: str  # "stable", "variable", "sensitive"
    optimal_coherence_range: Tuple[float, float]

@dataclass
class SafetyProfile:
    """Safety profile and contraindications."""
    experience_level: str
    health_conditions: List[str]
    medications: List[str]
    contraindications: List[str]
    comfort_preferences: Dict[str, Any]
    emergency_contacts: List[Dict[str, str]]
    special_considerations: List[str]

@dataclass
class SessionHistory:
    """Session history tracking."""
    total_sessions: int
    total_hours: float
    favorite_states: List[str]
    challenging_states: List[str]
    average_comfort_level: float
    progress_metrics: Dict[str, float]
    recent_session_outcomes: List[Dict[str, Any]]

@dataclass
class NeuralProfile:
    """
    Comprehensive neural profile for personalized consciousness exploration.
    
    This profile contains all necessary information for safe, effective, and
    personalized neural entrainment sessions.
    """
    # Basic Information
    profile_id: str
    name: str
    profile_type: ProfileType
    created_date: datetime
    last_updated: datetime
    version: str = "2.0.0"
    
    # Neural Characteristics
    dominant_brainwave_pattern: str
    brainwave_preferences: Dict[str, BrainwavePreference] = field(default_factory=dict)
    neural_sensitivity: SensitivityLevel = SensitivityLevel.MODERATE
    consciousness_preferences: Dict[str, ConsciousnessPreference] = field(default_factory=dict)
    
    # Biofield Profile
    biofield_profile: BiofieldProfile = field(default_factory=lambda: BiofieldProfile(
        schumann_resonance_sensitivity=0.5,
        solfeggio_responsiveness={},
        golden_ratio_harmony_level=0.5,
        coherence_baseline=0.5,
        field_stability="stable",
        optimal_coherence_range=(0.4, 0.8)
    ))
    
    # Safety and Health
    safety_profile: SafetyProfile = field(default_factory=lambda: SafetyProfile(
        experience_level="beginner",
        health_conditions=[],
        medications=[],
        contraindications=[],
        comfort_preferences={},
        emergency_contacts=[],
        special_considerations=[]
    ))
    
    # Session History and Progress
    session_history: SessionHistory = field(default_factory=lambda: SessionHistory(
        total_sessions=0,
        total_hours=0.0,
        favorite_states=[],
        challenging_states=[],
        average_comfort_level=0.8,
        progress_metrics={},
        recent_session_outcomes=[]
    ))
    
    # Personalization Settings
    preferred_session_duration: int = 30
    optimal_time_of_day: str = "evening"
    environmental_preferences: Dict[str, Any] = field(default_factory=dict)
    integration_preferences: Dict[str, Any] = field(default_factory=dict)
    
    # Advanced Settings
    custom_frequency_mappings: Dict[str, float] = field(default_factory=dict)
    advanced_parameters: Dict[str, Any] = field(default_factory=dict)
    research_participation: bool = False
    data_sharing_consent: Dict[str, bool] = field(default_factory=dict)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROFILE CREATION AND MANAGEMENT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def create_default_profile(name: str, experience_level: str = "beginner") -> NeuralProfile:
    """
    Create a default neural profile for new users.
    
    Args:
        name: User's name
        experience_level: Experience level (beginner, intermediate, advanced, expert)
        
    Returns:
        Default NeuralProfile configured for safety and gradual progression
    """
    profile_id = generate_profile_id(name)
    current_time = datetime.now()
    
    # Create default brainwave preferences
    brainwave_prefs = {}
    for freq_name, freq_info in BRAINWAVE_FREQUENCIES.items():
        if freq_name in ['alpha', 'theta', 'low_beta']:  # Safe starting frequencies
            brainwave_prefs[freq_name] = BrainwavePreference(
                frequency_range=freq_name,
                preferred_intensity=0.3,  # Conservative starting intensity
                tolerance_range=(0.1, 0.5),
                response_quality="moderate",
                notes="Default setting - to be personalized through use"
            )
    
    # Create default consciousness preferences
    consciousness_prefs = {}
    safe_states = ['neutral', 'deep_relaxation', 'meditative_awareness']
    for state_name in safe_states:
        consciousness_prefs[state_name] = ConsciousnessPreference(
            state_name=state_name,
            affinity_level=0.7,
            optimal_duration_minutes=15,
            preparation_time_needed=5,
            integration_time_needed=10,
            response_notes="Default setting"
        )
    
    # Create default biofield profile
    biofield_prof = BiofieldProfile(
        schumann_resonance_sensitivity=0.5,
        solfeggio_responsiveness={
            '396_hz': 0.5,
            '528_hz': 0.6,  # Slightly higher for healing frequency
            '852_hz': 0.4
        },
        golden_ratio_harmony_level=0.5,
        coherence_baseline=0.5,
        field_stability="stable",
        optimal_coherence_range=(0.4, 0.7)
    )
    
    # Create safety profile
    safety_prof = SafetyProfile(
        experience_level=experience_level,
        health_conditions=[],
        medications=[],
        contraindications=[],
        comfort_preferences={
            'preferred_volume': 0.6,
            'visual_sensitivity': 'moderate',
            'break_frequency': 15
        },
        emergency_contacts=[],
        special_considerations=[]
    )
    
    # Create session history
    session_hist = SessionHistory(
        total_sessions=0,
        total_hours=0.0,
        favorite_states=[],
        challenging_states=[],
        average_comfort_level=0.8,
        progress_metrics={
            'comfort_trend': 0.0,
            'effectiveness_rating': 0.0,
            'session_completion_rate': 0.0
        },
        recent_session_outcomes=[]
    )
    
    return NeuralProfile(
        profile_id=profile_id,
        name=name,
        profile_type=ProfileType.BEGINNER,
        created_date=current_time,
        last_updated=current_time,
        dominant_brainwave_pattern="alpha",
        brainwave_preferences=brainwave_prefs,
        neural_sensitivity=SensitivityLevel.MODERATE,
        consciousness_preferences=consciousness_prefs,
        biofield_profile=biofield_prof,
        safety_profile=safety_prof,
        session_history=session_hist,
        preferred_session_duration=20,  # Conservative starting duration
        optimal_time_of_day="evening",
        environmental_preferences={
            'ambient_lighting': 'dim',
            'background_sounds': 'minimal',
            'temperature_preference': 'comfortable'
        },
        integration_preferences={
            'journaling': True,
            'meditation': True,
            'rest_time': True
        }
    )

def validate_neural_profile(profile: NeuralProfile) -> Dict[str, Any]:
    """
    Comprehensive validation of a neural profile.
    
    Args:
        profile: NeuralProfile to validate
        
    Returns:
        Validation report with errors, warnings, and recommendations
    """
    validation_report = {
        'is_valid': True,
        'errors': [],
        'warnings': [],
        'recommendations': [],
        'safety_concerns': []
    }
    
    # Validate basic information
    if not profile.profile_id or not profile.name:
        validation_report['errors'].append("Missing required profile identification")
        validation_report['is_valid'] = False
    
    # Validate brainwave preferences
    for freq_name, pref in profile.brainwave_preferences.items():
        if freq_name not in BRAINWAVE_FREQUENCIES:
            validation_report['warnings'].append(f"Unknown brainwave frequency: {freq_name}")
        
        if not (0.0 <= pref.preferred_intensity <= 1.0):
            validation_report['errors'].append(f"Invalid intensity for {freq_name}: {pref.preferred_intensity}")
            validation_report['is_valid'] = False
    
    # Validate consciousness preferences
    for state_name, pref in profile.consciousness_preferences.items():
        if state_name not in CONSCIOUSNESS_STATES:
            validation_report['warnings'].append(f"Unknown consciousness state: {state_name}")
        
        if pref.optimal_duration_minutes < 1 or pref.optimal_duration_minutes > 120:
            validation_report['warnings'].append(f"Unusual duration for {state_name}: {pref.optimal_duration_minutes}min")
    
    # Validate biofield profile
    biofield = profile.biofield_profile
    if not (0.0 <= biofield.coherence_baseline <= 1.0):
        validation_report['errors'].append(f"Invalid coherence baseline: {biofield.coherence_baseline}")
        validation_report['is_valid'] = False
    
    # Validate safety profile
    safety = profile.safety_profile
    if safety.experience_level not in ['beginner', 'intermediate', 'advanced', 'expert']:
        validation_report['errors'].append(f"Invalid experience level: {safety.experience_level}")
        validation_report['is_valid'] = False
    
    # Check for safety concerns based on neural load limits
    neural_limits = NEURAL_LOAD_LIMITS.get(safety.experience_level)
    if neural_limits:
        if profile.preferred_session_duration > neural_limits.max_session_duration_minutes:
            validation_report['safety_concerns'].append(
                f"Preferred duration ({profile.preferred_session_duration}min) exceeds "
                f"safe limit for {safety.experience_level} ({neural_limits.max_session_duration_minutes}min)"
            )
    
    # Check for contraindications
    from .safety_constants import CONTRAINDICATIONS
    for condition in safety.health_conditions:
        if condition in CONTRAINDICATIONS['absolute']:
            validation_report['safety_concerns'].append(f"Absolute contraindication: {condition}")
        elif condition in CONTRAINDICATIONS['relative']:
            validation_report['warnings'].append(f"Relative contraindication: {condition}")
    
    # Provide recommendations
    if len(profile.brainwave_preferences) < 3:
        validation_report['recommendations'].append("Consider exploring more brainwave frequencies")
    
    if len(profile.consciousness_preferences) < 2:
        validation_report['recommendations'].append("Consider exploring additional consciousness states")
    
    if profile.session_history.total_sessions > 10 and profile.profile_type == ProfileType.BEGINNER:
        validation_report['recommendations'].append("Consider upgrading to personalized profile type")
    
    return validation_report

def calculate_profile_compatibility(profile1: NeuralProfile, 
                                  profile2: NeuralProfile) -> Dict[str, float]:
    """
    Calculate compatibility between two neural profiles.
    
    Args:
        profile1: First neural profile
        profile2: Second neural profile
        
    Returns:
        Compatibility scores for different aspects
    """
    compatibility = {
        'overall': 0.0,
        'brainwave_preferences': 0.0,
        'consciousness_states': 0.0,
        'biofield_resonance': 0.0,
        'session_preferences': 0.0,
        'safety_compatibility': 0.0
    }
    
    # Compare brainwave preferences
    common_frequencies = set(profile1.brainwave_preferences.keys()) & set(profile2.brainwave_preferences.keys())
    if common_frequencies:
        brainwave_sim = 0.0
        for freq in common_frequencies:
            pref1 = profile1.brainwave_preferences[freq]
            pref2 = profile2.brainwave_preferences[freq]
            intensity_diff = abs(pref1.preferred_intensity - pref2.preferred_intensity)
            brainwave_sim += 1.0 - intensity_diff
        compatibility['brainwave_preferences'] = brainwave_sim / len(common_frequencies)
    
    # Compare consciousness state preferences
    common_states = set(profile1.consciousness_preferences.keys()) & set(profile2.consciousness_preferences.keys())
    if common_states:
        consciousness_sim = 0.0
        for state in common_states:
            pref1 = profile1.consciousness_preferences[state]
            pref2 = profile2.consciousness_preferences[state]
            affinity_diff = abs(pref1.affinity_level - pref2.affinity_level)
            consciousness_sim += 1.0 - affinity_diff
        compatibility['consciousness_states'] = consciousness_sim / len(common_states)
    
    # Compare biofield profiles
    bio1 = profile1.biofield_profile
    bio2 = profile2.biofield_profile
    
    coherence_sim = 1.0 - abs(bio1.coherence_baseline - bio2.coherence_baseline)
    schumann_sim = 1.0 - abs(bio1.schumann_resonance_sensitivity - bio2.schumann_resonance_sensitivity)
    golden_sim = 1.0 - abs(bio1.golden_ratio_harmony_level - bio2.golden_ratio_harmony_level)
    
    compatibility['biofield_resonance'] = (coherence_sim + schumann_sim + golden_sim) / 3
    
    # Compare session preferences
    duration_sim = 1.0 - min(1.0, abs(profile1.preferred_session_duration - profile2.preferred_session_duration) / 60)
    time_sim = 1.0 if profile1.optimal_time_of_day == profile2.optimal_time_of_day else 0.5
    
    compatibility['session_preferences'] = (duration_sim + time_sim) / 2
    
    # Compare safety compatibility
    safety1 = profile1.safety_profile
    safety2 = profile2.safety_profile
    
    experience_levels = ['beginner', 'intermediate', 'advanced', 'expert']
    level1_idx = experience_levels.index(safety1.experience_level) if safety1.experience_level in experience_levels else 0
    level2_idx = experience_levels.index(safety2.experience_level) if safety2.experience_level in experience_levels else 0
    
    level_diff = abs(level1_idx - level2_idx) / len(experience_levels)
    safety_sim = 1.0 - level_diff
    
    # Consider contraindications
    common_conditions = set(safety1.health_conditions) & set(safety2.health_conditions)
    if common_conditions:
        safety_sim *= 0.8  # Reduce compatibility if common health concerns
    
    compatibility['safety_compatibility'] = safety_sim
    
    # Calculate overall compatibility
    compatibility['overall'] = (
        compatibility['brainwave_preferences'] * 0.25 +
        compatibility['consciousness_states'] * 0.25 +
        compatibility['biofield_resonance'] * 0.2 +
        compatibility['session_preferences'] * 0.15 +
        compatibility['safety_compatibility'] * 0.15
    )
    
    return compatibility

def update_profile_from_session(profile: NeuralProfile, 
                               session_data: Dict[str, Any]) -> NeuralProfile:
    """
    Update neural profile based on session outcomes.
    
    Args:
        profile: Neural profile to update
        session_data: Session outcome data
        
    Returns:
        Updated neural profile
    """
    updated_profile = profile
    
    # Update session history
    updated_profile.session_history.total_sessions += 1
    updated_profile.session_history.total_hours += session_data.get('duration_hours', 0.0)
    
    # Update consciousness state preferences
    states_used = session_data.get('consciousness_states', [])
    comfort_levels = session_data.get('state_comfort_levels', {})
    
    for state in states_used:
        if state in updated_profile.consciousness_preferences:
            pref = updated_profile.consciousness_preferences[state]
            state_comfort = comfort_levels.get(state, 0.8)
            
            # Adjust affinity based on comfort
            if state_comfort > 0.8:
                pref.affinity_level = min(1.0, pref.affinity_level + 0.05)
                if state not in updated_profile.session_history.favorite_states:
                    if len(updated_profile.session_history.favorite_states) < 5:
                        updated_profile.session_history.favorite_states.append(state)
            elif state_comfort < 0.4:
                pref.affinity_level = max(0.0, pref.affinity_level - 0.05)
                if state not in updated_profile.session_history.challenging_states:
                    if len(updated_profile.session_history.challenging_states) < 5:
                        updated_profile.session_history.challenging_states.append(state)
    
    # Update brainwave preferences
    frequencies_used = session_data.get('frequencies_used', {})
    for freq_name, usage_data in frequencies_used.items():
        if freq_name in updated_profile.brainwave_preferences:
            pref = updated_profile.brainwave_preferences[freq_name]
            effectiveness = usage_data.get('effectiveness', 0.5)
            
            # Adjust preferred intensity based on effectiveness
            if effectiveness > 0.8:
                # Slightly increase intensity if very effective
                pref.preferred_intensity = min(1.0, pref.preferred_intensity + 0.02)
            elif effectiveness < 0.3:
                # Decrease intensity if not effective
                pref.preferred_intensity = max(0.1, pref.preferred_intensity - 0.02)
    
    # Update biofield profile
    session_coherence = session_data.get('average_coherence', profile.biofield_profile.coherence_baseline)
    coherence_trend = session_coherence - profile.biofield_profile.coherence_baseline
    
    # Adjust baseline coherence gradually
    if coherence_trend > 0.1:
        updated_profile.biofield_profile.coherence_baseline += 0.02
    elif coherence_trend < -0.1:
        updated_profile.biofield_profile.coherence_baseline = max(0.0, 
            updated_profile.biofield_profile.coherence_baseline - 0.02)
    
    # Update average comfort level
    session_comfort = session_data.get('overall_comfort', 0.8)
    total_sessions = updated_profile.session_history.total_sessions
    current_avg = updated_profile.session_history.average_comfort_level
    
    # Weighted average with more weight on recent sessions
    weight = min(1.0, 1.0 / total_sessions)
    updated_profile.session_history.average_comfort_level = (
        current_avg * (1 - weight) + session_comfort * weight
    )
    
    # Add to recent session outcomes (keep last 10)
    session_outcome = {
        'date': datetime.now().isoformat(),
        'duration_minutes': session_data.get('duration_minutes', 0),
        'comfort_level': session_comfort,
        'effectiveness': session_data.get('effectiveness', 0.5),
        'states_explored': states_used,
        'notes': session_data.get('notes', '')
    }
    
    updated_profile.session_history.recent_session_outcomes.append(session_outcome)
    if len(updated_profile.session_history.recent_session_outcomes) > 10:
        updated_profile.session_history.recent_session_outcomes = (
            updated_profile.session_history.recent_session_outcomes[-10:]
        )
    
    # Update profile metadata
    updated_profile.last_updated = datetime.now()
    
    # Consider profile type upgrade
    if (updated_profile.profile_type == ProfileType.BEGINNER and 
        updated_profile.session_history.total_sessions >= 10):
        updated_profile.profile_type = ProfileType.PERSONALIZED
    
    return updated_profile

def optimize_profile_for_intention(profile: NeuralProfile, 
                                 intention: str) -> Dict[str, Any]:
    """
    Optimize profile settings for a specific intention.
    
    Args:
        profile: Neural profile to optimize
        intention: Session intention (healing, creativity, meditation, etc.)
        
    Returns:
        Optimized session parameters
    """
    base_settings = {
        'duration_minutes': profile.preferred_session_duration,
        'intensity_level': 0.5,
        'consciousness_journey': [],
        'biofield_configuration': {},
        'safety_parameters': {}
    }
    
    intention_optimizations = {
        'healing': {
            'preferred_states': ['healing_trance', 'deep_relaxation'],
            'frequency_focus': 'delta',
            'biofield_emphasis': 'solfeggio_528',
            'intensity_modifier': 0.8,
            'duration_modifier': 1.2
        },
        
        'creativity': {
            'preferred_states': ['creative_flow', 'theta_exploration'],
            'frequency_focus': 'theta',
            'biofield_emphasis': 'golden_ratio_2',
            'intensity_modifier': 0.9,
            'duration_modifier': 1.0
        },
        
        'meditation': {
            'preferred_states': ['meditative_awareness', 'deep_relaxation'],
            'frequency_focus': 'alpha',
            'biofield_emphasis': 'schumann_resonance',
            'intensity_modifier': 0.7,
            'duration_modifier': 1.1
        },
        
        'transcendence': {
            'preferred_states': ['gamma_awakening', 'transcendent_unity'],
            'frequency_focus': 'gamma',
            'biofield_emphasis': 'solfeggio_963',
            'intensity_modifier': 0.6,  # Conservative for safety
            'duration_modifier': 0.8
        },
        
        'learning': {
            'preferred_states': ['learning_state', 'focused_attention'],
            'frequency_focus': 'low_beta',
            'biofield_emphasis': 'golden_ratio_1',
            'intensity_modifier': 0.8,
            'duration_modifier': 0.9
        }
    }
    
    optimization = intention_optimizations.get(intention, intention_optimizations['meditation'])
    
    # Build consciousness journey
    preferred_states = optimization['preferred_states']
    available_states = [state for state in preferred_states 
                       if state in profile.consciousness_preferences]
    
    if available_states:
        base_settings['consciousness_journey'] = ['neutral'] + available_states + ['neutral']
    else:
        # Fallback to safe states
        base_settings['consciousness_journey'] = ['neutral', 'deep_relaxation', 'neutral']
    
    # Set intensity based on profile and intention
    base_intensity = 0.5
    if optimization['frequency_focus'] in profile.brainwave_preferences:
        pref = profile.brainwave_preferences[optimization['frequency_focus']]
        base_intensity = pref.preferred_intensity
    
    base_settings['intensity_level'] = base_intensity * optimization['intensity_modifier']
    
    # Adjust duration
    base_settings['duration_minutes'] = int(
        profile.preferred_session_duration * optimization['duration_modifier']
    )
    
    # Configure biofield settings
    base_settings['biofield_configuration'] = {
        'primary_focus': optimization['biofield_emphasis'],
        'coherence_target': profile.biofield_profile.optimal_coherence_range[1],
        'stability_preference': profile.biofield_profile.field_stability
    }
    
    # Safety parameters
    neural_limits = NEURAL_LOAD_LIMITS.get(profile.safety_profile.experience_level)
    if neural_limits:
        base_settings['safety_parameters'] = {
            'max_duration': neural_limits.max_session_duration_minutes,
            'max_intensity': neural_limits.max_frequency_intensity,
            'max_neural_load': neural_limits.max_neural_load,
            'break_frequency': neural_limits.recommended_break_frequency_minutes
        }
    
    return base_settings

def export_profile(profile: NeuralProfile, include_sensitive_data: bool = False) -> Dict[str, Any]:
    """
    Export neural profile to dictionary format.
    
    Args:
        profile: Neural profile to export
        include_sensitive_data: Whether to include sensitive health/personal data
        
    Returns:
        Profile data as dictionary
    """
    profile_dict = asdict(profile)
    
    # Convert datetime objects to ISO format
    profile_dict['created_date'] = profile.created_date.isoformat()
    profile_dict['last_updated'] = profile.last_updated.isoformat()
    
    # Convert enums to values
    profile_dict['profile_type'] = profile.profile_type.value
    profile_dict['neural_sensitivity'] = profile.neural_sensitivity.value
    
    if not include_sensitive_data:
        # Remove sensitive information
        if 'emergency_contacts' in profile_dict['safety_profile']:
            profile_dict['safety_profile']['emergency_contacts'] = []
        if 'health_conditions' in profile_dict['safety_profile']:
            profile_dict['safety_profile']['health_conditions'] = []
        if 'medications' in profile_dict['safety_profile']:
            profile_dict['safety_profile']['medications'] = []
    
    return profile_dict

def import_profile(profile_data: Dict[str, Any]) -> NeuralProfile:
    """
    Import neural profile from dictionary format.
    
    Args:
        profile_data: Profile data dictionary
        
    Returns:
        NeuralProfile object
    """
    # Handle datetime conversion
    if isinstance(profile_data['created_date'], str):
        profile_data['created_date'] = datetime.fromisoformat(profile_data['created_date'])
    if isinstance(profile_data['last_updated'], str):
        profile_data['last_updated'] = datetime.fromisoformat(profile_data['last_updated'])
    
    # Handle enum conversion
    if isinstance(profile_data['profile_type'], str):
        profile_data['profile_type'] = ProfileType(profile_data['profile_type'])
    if isinstance(profile_data['neural_sensitivity'], str):
        profile_data['neural_sensitivity'] = SensitivityLevel(profile_data['neural_sensitivity'])
    
    # Convert nested dictionaries to dataclass objects
    if 'brainwave_preferences' in profile_data:
        brainwave_prefs = {}
        for freq_name, pref_data in profile_data['brainwave_preferences'].items():
            brainwave_prefs[freq_name] = BrainwavePreference(**pref_data)
        profile_data['brainwave_preferences'] = brainwave_prefs
    
    if 'consciousness_preferences' in profile_data:
        consciousness_prefs = {}
        for state_name, pref_data in profile_data['consciousness_preferences'].items():
            consciousness_prefs[state_name] = ConsciousnessPreference(**pref_data)
        profile_data['consciousness_preferences'] = consciousness_prefs
    
    if 'biofield_profile' in profile_data:
        profile_data['biofield_profile'] = BiofieldProfile(**profile_data['biofield_profile'])
    
    if 'safety_profile' in profile_data:
        profile_data['safety_profile'] = SafetyProfile(**profile_data['safety_profile'])
    
    if 'session_history' in profile_data:
        profile_data['session_history'] = SessionHistory(**profile_data['session_history'])
    
    return NeuralProfile(**profile_data)

def generate_profile_id(name: str) -> str:
    """
    Generate a unique profile ID.
    
    Args:
        name: User's name
        
    Returns:
        Unique profile identifier
    """
    timestamp = datetime.now().isoformat()
    combined = f"{name}_{timestamp}".encode('utf-8')
    return hashlib.sha256(combined).hexdigest()[:16]

def merge_profiles(primary_profile: NeuralProfile, 
                  secondary_profile: NeuralProfile,
                  merge_strategy: str = "weighted_average") -> NeuralProfile:
    """
    Merge two neural profiles using specified strategy.
    
    Args:
        primary_profile: Primary profile (takes precedence)
        secondary_profile: Secondary profile to merge from
        merge_strategy: Strategy for merging ("weighted_average", "primary_priority", "best_of_both")
        
    Returns:
        Merged neural profile
    """
    merged_profile = primary_profile
    
    if merge_strategy == "weighted_average":
        # Average preferences with 70% weight to primary
        for freq_name in secondary_profile.brainwave_preferences:
            if freq_name in merged_profile.brainwave_preferences:
                primary_pref = merged_profile.brainwave_preferences[freq_name]
                secondary_pref = secondary_profile.brainwave_preferences[freq_name]
                
                # Weighted average of intensities
                merged_intensity = (primary_pref.preferred_intensity * 0.7 + 
                                  secondary_pref.preferred_intensity * 0.3)
                primary_pref.preferred_intensity = merged_intensity
    
    elif merge_strategy == "best_of_both":
        # Take the best-performing preferences from each
        for freq_name in secondary_profile.brainwave_preferences:
            if freq_name not in merged_profile.brainwave_preferences:
                # Add new frequency preference
                merged_profile.brainwave_preferences[freq_name] = secondary_profile.brainwave_preferences[freq_name]
    
    # Update session history totals
    merged_profile.session_history.total_sessions += secondary_profile.session_history.total_sessions
    merged_profile.session_history.total_hours += secondary_profile.session_history.total_hours
    
    # Merge favorite states
    for state in secondary_profile.session_history.favorite_states:
        if state not in merged_profile.session_history.favorite_states:
            if len(merged_profile.session_history.favorite_states) < 5:
                merged_profile.session_history.favorite_states.append(state)
    
    merged_profile.last_updated = datetime.now()
    
    return merged_profile