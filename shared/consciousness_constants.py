#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Consciousness Constants
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Consciousness Constants - Comprehensive consciousness state and brainwave definitions.

This module provides authoritative definitions for consciousness states, brainwave
frequencies, state transitions, and consciousness mapping used throughout the
Neural Entrainment System. All consciousness-aware components reference these
standardized definitions.
"""

from typing import Dict, Any, List, Tuple, Optional, Union
from dataclasses import dataclass
from enum import Enum

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# BRAINWAVE FREQUENCY DEFINITIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@dataclass
class BrainwaveRange:
    """Defines a brainwave frequency range with consciousness characteristics."""
    min_frequency: float
    max_frequency: float
    peak_frequency: float
    name: str
    description: str
    consciousness_qualities: List[str]
    typical_states: List[str]
    neural_benefits: List[str]
    cautions: List[str] = None

# Core brainwave frequency ranges
BRAINWAVE_FREQUENCIES = {
    'infra_low': BrainwaveRange(
        min_frequency=0.0,
        max_frequency=0.5,
        peak_frequency=0.1,
        name="Infra-Low",
        description="Ultra-slow rhythms associated with cellular and metabolic processes",
        consciousness_qualities=["cellular_regeneration", "deep_healing", "autonomic_balance"],
        typical_states=["deep_sleep", "coma", "cellular_repair"],
        neural_benefits=["enhanced_healing", "autonomic_regulation", "cellular_synchronization"],
        cautions=["only_for_healing_sessions", "avoid_during_active_states"]
    ),
    
    'deep_delta': BrainwaveRange(
        min_frequency=0.1,
        max_frequency=2.0,
        peak_frequency=1.0,
        name="Deep Delta",
        description="Profound unconscious states and deep healing",
        consciousness_qualities=["profound_rest", "cellular_regeneration", "immune_enhancement"],
        typical_states=["deep_dreamless_sleep", "healing_trance", "profound_meditation"],
        neural_benefits=["growth_hormone_release", "immune_system_boost", "memory_consolidation"],
        cautions=["may_cause_drowsiness", "avoid_when_driving"]
    ),
    
    'delta': BrainwaveRange(
        min_frequency=1.0,
        max_frequency=4.0,
        peak_frequency=2.5,
        name="Delta",
        description="Deep sleep, healing, and regenerative states",
        consciousness_qualities=["deep_rest", "healing", "subconscious_processing"],
        typical_states=["deep_sleep", "trance", "deep_meditation", "healing_states"],
        neural_benefits=["physical_restoration", "memory_consolidation", "toxin_elimination"],
        cautions=["drowsiness_possible", "avoid_before_driving"]
    ),
    
    'theta': BrainwaveRange(
        min_frequency=4.0,
        max_frequency=8.0,
        peak_frequency=6.0,
        name="Theta",
        description="Deep meditation, creativity, and subconscious access",
        consciousness_qualities=["deep_meditation", "creativity", "intuitive_insights", "memory_access"],
        typical_states=["rem_sleep", "deep_meditation", "shamanic_journey", "creative_flow"],
        neural_benefits=["enhanced_creativity", "emotional_healing", "memory_integration"],
        cautions=["may_trigger_emotional_release", "monitor_comfort_levels"]
    ),
    
    'alpha': BrainwaveRange(
        min_frequency=8.0,
        max_frequency=13.0,
        peak_frequency=10.0,
        name="Alpha",
        description="Relaxed awareness, meditation, and learning states",
        consciousness_qualities=["relaxed_awareness", "peaceful_mind", "receptive_learning"],
        typical_states=["meditation", "relaxation", "light_trance", "focused_learning"],
        neural_benefits=["stress_reduction", "enhanced_learning", "improved_mood"],
        cautions=["generally_safe", "ideal_for_beginners"]
    ),
    
    'low_beta': BrainwaveRange(
        min_frequency=13.0,
        max_frequency=16.0,
        peak_frequency=14.0,
        name="Low Beta",
        description="Relaxed focus and calm concentration",
        consciousness_qualities=["calm_focus", "relaxed_attention", "peaceful_productivity"],
        typical_states=["relaxed_focus", "calm_work", "light_concentration"],
        neural_benefits=["sustained_attention", "calm_productivity", "reduced_anxiety"],
        cautions=["generally_safe", "good_for_work_sessions"]
    ),
    
    'beta': BrainwaveRange(
        min_frequency=13.0,
        max_frequency=30.0,
        peak_frequency=18.0,
        name="Beta",
        description="Normal waking consciousness and focused attention",
        consciousness_qualities=["focused_attention", "analytical_thinking", "active_problem_solving"],
        typical_states=["normal_waking", "focused_work", "active_conversation", "problem_solving"],
        neural_benefits=["enhanced_focus", "improved_cognition", "increased_alertness"],
        cautions=["avoid_overstimulation", "monitor_for_anxiety"]
    ),
    
    'high_beta': BrainwaveRange(
        min_frequency=23.0,
        max_frequency=30.0,
        peak_frequency=26.0,
        name="High Beta",
        description="High arousal, anxiety, or intense focus",
        consciousness_qualities=["intense_focus", "high_arousal", "stress_response"],
        typical_states=["intense_concentration", "anxiety", "stress", "excitement"],
        neural_benefits=["peak_performance", "crisis_response", "intense_focus"],
        cautions=["risk_of_anxiety", "limit_exposure_time", "monitor_stress_levels"]
    ),
    
    'gamma': BrainwaveRange(
        min_frequency=30.0,
        max_frequency=100.0,
        peak_frequency=40.0,
        name="Gamma",
        description="Heightened awareness, consciousness integration, and transcendent states",
        consciousness_qualities=["heightened_awareness", "consciousness_integration", "transcendent_insights"],
        typical_states=["peak_experiences", "transcendent_meditation", "heightened_awareness"],
        neural_benefits=["enhanced_consciousness", "neural_synchronization", "peak_insights"],
        cautions=["advanced_users_only", "monitor_neural_load", "limit_exposure"]
    ),
    
    'ultra_gamma': BrainwaveRange(
        min_frequency=80.0,
        max_frequency=200.0,
        peak_frequency=100.0,
        name="Ultra Gamma",
        description="Extreme heightened states and transcendent experiences",
        consciousness_qualities=["transcendent_consciousness", "unity_experiences", "extreme_awareness"],
        typical_states=["mystical_experiences", "unity_consciousness", "transcendent_states"],
        neural_benefits=["consciousness_expansion", "mystical_experiences", "unity_awareness"],
        cautions=["experts_only", "careful_monitoring_required", "limit_duration"]
    )
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS STATES DEFINITIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@dataclass
class ConsciousnessState:
    """Defines a consciousness state with associated characteristics."""
    name: str
    description: str
    dominant_frequency: str
    frequency_range: Tuple[float, float]
    qualities: List[str]
    typical_duration_minutes: Tuple[int, int]
    preparation_needed: bool
    integration_needed: bool
    experience_level_required: str
    safety_considerations: List[str]

# Comprehensive consciousness states
CONSCIOUSNESS_STATES = {
    'neutral': ConsciousnessState(
        name="Neutral Baseline",
        description="Balanced, natural waking state",
        dominant_frequency="alpha",
        frequency_range=(8.0, 13.0),
        qualities=["balanced", "natural", "receptive"],
        typical_duration_minutes=(5, 30),
        preparation_needed=False,
        integration_needed=False,
        experience_level_required="beginner",
        safety_considerations=["generally_safe"]
    ),
    
    'deep_relaxation': ConsciousnessState(
        name="Deep Relaxation",
        description="Profound physical and mental relaxation",
        dominant_frequency="alpha",
        frequency_range=(8.0, 12.0),
        qualities=["deeply_relaxed", "peaceful", "restorative"],
        typical_duration_minutes=(15, 60),
        preparation_needed=False,
        integration_needed=True,
        experience_level_required="beginner",
        safety_considerations=["may_cause_drowsiness"]
    ),
    
    'focused_attention': ConsciousnessState(
        name="Focused Attention",
        description="Clear, sustained attention and concentration",
        dominant_frequency="low_beta",
        frequency_range=(13.0, 16.0),
        qualities=["focused", "alert", "concentrated"],
        typical_duration_minutes=(10, 45),
        preparation_needed=False,
        integration_needed=False,
        experience_level_required="beginner",
        safety_considerations=["avoid_overstimulation"]
    ),
    
    'meditative_awareness': ConsciousnessState(
        name="Meditative Awareness",
        description="Calm, mindful awareness with mental clarity",
        dominant_frequency="alpha",
        frequency_range=(9.0, 12.0),
        qualities=["mindful", "aware", "peaceful", "clear"],
        typical_duration_minutes=(15, 90),
        preparation_needed=True,
        integration_needed=True,
        experience_level_required="intermediate",
        safety_considerations=["generally_safe", "allow_integration_time"]
    ),
    
    'theta_exploration': ConsciousnessState(
        name="Theta Exploration",
        description="Deep meditative states with enhanced creativity",
        dominant_frequency="theta",
        frequency_range=(4.0, 8.0),
        qualities=["creative", "intuitive", "deep", "exploratory"],
        typical_duration_minutes=(20, 60),
        preparation_needed=True,
        integration_needed=True,
        experience_level_required="intermediate",
        safety_considerations=["emotional_release_possible", "comfortable_environment_needed"]
    ),
    
    'healing_trance': ConsciousnessState(
        name="Healing Trance",
        description="Deep healing state for physical and emotional restoration",
        dominant_frequency="delta",
        frequency_range=(1.0, 4.0),
        qualities=["healing", "restorative", "regenerative", "peaceful"],
        typical_duration_minutes=(30, 120),
        preparation_needed=True,
        integration_needed=True,
        experience_level_required="intermediate",
        safety_considerations=["drowsiness_likely", "avoid_driving_after", "healing_reactions_possible"]
    ),
    
    'gamma_awakening': ConsciousnessState(
        name="Gamma Awakening",
        description="Heightened awareness and consciousness integration",
        dominant_frequency="gamma",
        frequency_range=(30.0, 60.0),
        qualities=["heightened", "integrated", "aware", "transcendent"],
        typical_duration_minutes=(10, 30),
        preparation_needed=True,
        integration_needed=True,
        experience_level_required="advanced",
        safety_considerations=["advanced_users_only", "monitor_neural_load", "limit_exposure_time"]
    ),
    
    'transcendent_unity': ConsciousnessState(
        name="Transcendent Unity",
        description="Advanced transcendent states and unity consciousness",
        dominant_frequency="ultra_gamma",
        frequency_range=(60.0, 100.0),
        qualities=["transcendent", "unified", "mystical", "expanded"],
        typical_duration_minutes=(5, 20),
        preparation_needed=True,
        integration_needed=True,
        experience_level_required="expert",
        safety_considerations=["experts_only", "careful_monitoring", "extensive_integration_needed"]
    ),
    
    'creative_flow': ConsciousnessState(
        name="Creative Flow",
        description="Enhanced creativity and artistic expression",
        dominant_frequency="theta",
        frequency_range=(5.0, 8.0),
        qualities=["creative", "flowing", "inspired", "expressive"],
        typical_duration_minutes=(20, 90),
        preparation_needed=True,
        integration_needed=True,
        experience_level_required="intermediate",
        safety_considerations=["emotional_expression_possible", "creative_blocks_may_surface"]
    ),
    
    'learning_state': ConsciousnessState(
        name="Enhanced Learning",
        description="Optimal state for learning and memory formation",
        dominant_frequency="alpha",
        frequency_range=(8.0, 12.0),
        qualities=["receptive", "focused", "retentive", "clear"],
        typical_duration_minutes=(15, 60),
        preparation_needed=False,
        integration_needed=True,
        experience_level_required="beginner",
        safety_considerations=["generally_safe", "avoid_information_overload"]
    )
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS STATE TRANSITIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@dataclass
class StateTransition:
    """Defines a transition between consciousness states."""
    from_state: str
    to_state: str
    transition_time_minutes: Tuple[int, int]  # min, max
    difficulty: str  # "easy", "moderate", "challenging", "advanced"
    transition_method: str
    preparation_needed: bool
    safety_considerations: List[str]

# Safe and effective state transitions
CONSCIOUSNESS_STATE_TRANSITIONS = {
    # From neutral
    ('neutral', 'deep_relaxation'): StateTransition(
        from_state="neutral",
        to_state="deep_relaxation", 
        transition_time_minutes=(5, 15),
        difficulty="easy",
        transition_method="gradual_alpha_entrainment",
        preparation_needed=False,
        safety_considerations=["generally_safe"]
    ),
    
    ('neutral', 'focused_attention'): StateTransition(
        from_state="neutral",
        to_state="focused_attention",
        transition_time_minutes=(3, 10),
        difficulty="easy",
        transition_method="gentle_beta_increase",
        preparation_needed=False,
        safety_considerations=["avoid_overstimulation"]
    ),
    
    ('neutral', 'meditative_awareness'): StateTransition(
        from_state="neutral",
        to_state="meditative_awareness",
        transition_time_minutes=(10, 20),
        difficulty="easy",
        transition_method="alpha_stabilization",
        preparation_needed=True,
        safety_considerations=["ensure_quiet_environment"]
    ),
    
    # From relaxation states
    ('deep_relaxation', 'theta_exploration'): StateTransition(
        from_state="deep_relaxation",
        to_state="theta_exploration",
        transition_time_minutes=(10, 25),
        difficulty="moderate",
        transition_method="alpha_to_theta_bridge",
        preparation_needed=True,
        safety_considerations=["emotional_content_may_arise"]
    ),
    
    ('deep_relaxation', 'healing_trance'): StateTransition(
        from_state="deep_relaxation",
        to_state="healing_trance",
        transition_time_minutes=(15, 30),
        difficulty="moderate",
        transition_method="alpha_to_delta_descent",
        preparation_needed=True,
        safety_considerations=["drowsiness_expected", "safe_environment_essential"]
    ),
    
    # Advanced transitions
    ('meditative_awareness', 'gamma_awakening'): StateTransition(
        from_state="meditative_awareness",
        to_state="gamma_awakening",
        transition_time_minutes=(15, 25),
        difficulty="advanced",
        transition_method="consciousness_elevation",
        preparation_needed=True,
        safety_considerations=["advanced_users_only", "monitor_neural_load"]
    ),
    
    ('gamma_awakening', 'transcendent_unity'): StateTransition(
        from_state="gamma_awakening",
        to_state="transcendent_unity",
        transition_time_minutes=(10, 20),
        difficulty="advanced",
        transition_method="gamma_amplification",
        preparation_needed=True,
        safety_considerations=["experts_only", "extensive_monitoring_required"]
    ),
    
    # Creative transitions
    ('meditative_awareness', 'creative_flow'): StateTransition(
        from_state="meditative_awareness",
        to_state="creative_flow",
        transition_time_minutes=(8, 15),
        difficulty="moderate",
        transition_method="alpha_theta_creative_bridge",
        preparation_needed=True,
        safety_considerations=["creative_materials_helpful"]
    ),
    
    # Learning transitions
    ('focused_attention', 'learning_state'): StateTransition(
        from_state="focused_attention",
        to_state="learning_state",
        transition_time_minutes=(5, 12),
        difficulty="easy",
        transition_method="beta_alpha_learning_optimization",
        preparation_needed=False,
        safety_considerations=["have_learning_materials_ready"]
    )
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS MAPPING AND UTILITIES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Consciousness depth levels
CONSCIOUSNESS_DEPTH_LEVELS = {
    1: {"name": "Surface", "states": ["neutral", "focused_attention"], "safety": "very_safe"},
    2: {"name": "Relaxed", "states": ["deep_relaxation", "meditative_awareness"], "safety": "safe"},
    3: {"name": "Deep", "states": ["theta_exploration", "creative_flow", "learning_state"], "safety": "monitor"},
    4: {"name": "Profound", "states": ["healing_trance"], "safety": "caution"},
    5: {"name": "Transcendent", "states": ["gamma_awakening", "transcendent_unity"], "safety": "advanced_only"}
}

# Experience level requirements
EXPERIENCE_LEVEL_STATES = {
    "beginner": ["neutral", "deep_relaxation", "focused_attention", "learning_state"],
    "intermediate": ["meditative_awareness", "theta_exploration", "creative_flow", "healing_trance"],
    "advanced": ["gamma_awakening"],
    "expert": ["transcendent_unity"]
}

def get_consciousness_state_info(state_name: str) -> Optional[ConsciousnessState]:
    """
    Get detailed information about a consciousness state.
    
    Args:
        state_name: Name of the consciousness state
        
    Returns:
        ConsciousnessState object or None if not found
    """
    return CONSCIOUSNESS_STATES.get(state_name.lower())

def get_brainwave_info(frequency_band: str) -> Optional[BrainwaveRange]:
    """
    Get detailed information about a brainwave frequency range.
    
    Args:
        frequency_band: Name of the frequency band
        
    Returns:
        BrainwaveRange object or None if not found
    """
    return BRAINWAVE_FREQUENCIES.get(frequency_band.lower())

def validate_consciousness_state(state_name: str) -> bool:
    """
    Validate that a consciousness state is recognized.
    
    Args:
        state_name: Name of the consciousness state
        
    Returns:
        True if state is valid
    """
    return state_name.lower() in CONSCIOUSNESS_STATES

def get_frequency_for_consciousness_state(state_name: str) -> Optional[Tuple[float, float]]:
    """
    Get the frequency range for a consciousness state.
    
    Args:
        state_name: Name of the consciousness state
        
    Returns:
        Tuple of (min_freq, max_freq) or None
    """
    state_info = get_consciousness_state_info(state_name)
    return state_info.frequency_range if state_info else None

def find_consciousness_state_by_frequency(frequency: float) -> List[str]:
    """
    Find consciousness states that include the given frequency.
    
    Args:
        frequency: Frequency in Hz
        
    Returns:
        List of consciousness state names
    """
    matching_states = []
    
    for state_name, state_info in CONSCIOUSNESS_STATES.items():
        min_freq, max_freq = state_info.frequency_range
        if min_freq <= frequency <= max_freq:
            matching_states.append(state_name)
    
    return matching_states

def get_safe_transitions(from_state: str, experience_level: str = "beginner") -> List[str]:
    """
    Get safe transitions from a given consciousness state.
    
    Args:
        from_state: Starting consciousness state
        experience_level: User's experience level
        
    Returns:
        List of safe target states
    """
    safe_targets = []
    available_states = EXPERIENCE_LEVEL_STATES.get(experience_level, [])
    
    for (start, end), transition in CONSCIOUSNESS_STATE_TRANSITIONS.items():
        if start == from_state and end in available_states:
            if transition.difficulty in ["easy", "moderate"] or experience_level in ["advanced", "expert"]:
                safe_targets.append(end)
    
    return safe_targets

def calculate_consciousness_depth(state_name: str) -> int:
    """
    Calculate the depth level of a consciousness state.
    
    Args:
        state_name: Name of the consciousness state
        
    Returns:
        Depth level (1-5)
    """
    for level, info in CONSCIOUSNESS_DEPTH_LEVELS.items():
        if state_name in info["states"]:
            return level
    
    return 1  # Default to surface level

def get_integration_time_recommendation(state_name: str) -> int:
    """
    Get recommended integration time for a consciousness state.
    
    Args:
        state_name: Name of the consciousness state
        
    Returns:
        Recommended integration time in minutes
    """
    state_info = get_consciousness_state_info(state_name)
    if not state_info:
        return 5
    
    depth = calculate_consciousness_depth(state_name)
    
    # Integration time based on depth and state requirements
    base_time = {
        1: 2,   # Surface states
        2: 5,   # Relaxed states  
        3: 10,  # Deep states
        4: 20,  # Profound states
        5: 30   # Transcendent states
    }.get(depth, 5)
    
    # Adjust for specific state requirements
    if state_info.integration_needed:
        base_time *= 2
    
    return base_time

def generate_consciousness_journey(start_state: str, 
                                 end_state: str,
                                 experience_level: str = "intermediate",
                                 max_transitions: int = 3) -> List[str]:
    """
    Generate a safe consciousness journey between states.
    
    Args:
        start_state: Starting consciousness state
        end_state: Target consciousness state  
        experience_level: User's experience level
        max_transitions: Maximum number of intermediate transitions
        
    Returns:
        List of states in the journey path
    """
    # Simple pathfinding for now - could be enhanced with graph algorithms
    journey = [start_state]
    current_state = start_state
    
    # Direct transition if available
    if (start_state, end_state) in CONSCIOUSNESS_STATE_TRANSITIONS:
        transition = CONSCIOUSNESS_STATE_TRANSITIONS[(start_state, end_state)]
        if transition.difficulty in ["easy", "moderate"] or experience_level in ["advanced", "expert"]:
            journey.append(end_state)
            return journey
    
    # Find intermediate path
    available_states = EXPERIENCE_LEVEL_STATES.get(experience_level, [])
    
    for _ in range(max_transitions):
        if current_state == end_state:
            break
        
        # Find next safe step
        safe_next_states = get_safe_transitions(current_state, experience_level)
        
        # Choose state that gets us closer to target
        best_next = None
        target_depth = calculate_consciousness_depth(end_state)
        current_depth = calculate_consciousness_depth(current_state)
        
        for next_state in safe_next_states:
            next_depth = calculate_consciousness_depth(next_state)
            
            # Prefer moves toward target depth
            if target_depth > current_depth and next_depth > current_depth:
                best_next = next_state
                break
            elif target_depth < current_depth and next_depth < current_depth:
                best_next = next_state
                break
            elif next_state == end_state:
                best_next = next_state
                break
        
        if best_next:
            current_state = best_next
            journey.append(current_state)
        else:
            break
    
    return journey

def get_consciousness_state_symbol(state_name: str) -> str:
    """
    Get a Unicode symbol representing a consciousness state.
    
    Args:
        state_name: Name of the consciousness state
        
    Returns:
        Unicode symbol for the state
    """
    symbols = {
        'neutral': '○',
        'deep_relaxation': '◑',
        'focused_attention': '□',
        'meditative_awareness': '△',
        'theta_exploration': '◆',
        'healing_trance': '●',
        'gamma_awakening': '✦',
        'transcendent_unity': '🌟',
        'creative_flow': '∿',
        'learning_state': '◈'
    }
    
    return symbols.get(state_name, '○')

def get_state_color_category(state_name: str) -> str:
    """
    Get the color category for a consciousness state.
    
    Args:
        state_name: Name of the consciousness state
        
    Returns:
        Color category name for styling
    """
    depth = calculate_consciousness_depth(state_name)
    
    color_mapping = {
        1: 'neutral',      # Light colors
        2: 'calm',         # Blue/green tones  
        3: 'deep',         # Purple/indigo tones
        4: 'profound',     # Deep blue/violet
        5: 'transcendent'  # Golden/white light
    }
    
    return color_mapping.get(depth, 'neutral')