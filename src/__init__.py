# src/__init__.py

"""
Neural Entrainment System v2.0 - Source Package
Consciousness-Aware Biofield Intelligence Framework
"""

__version__ = "2.0.0"
__author__ = "Dr. KB Jama"
__description__ = "Consciousness-aware neural entrainment with biofield intelligence"

# Re-export core components for convenient imports from `src`
from .signal_generator import (
    generate_biofield_pink_noise,
    generate_brown_noise,
    generate_white_noise,
    generate_consciousness_aware_carrier_wave,
    apply_isochronic,
    apply_bilateral_panning,
    apply_biorhythm_fm_modulation,
    apply_fm_modulation,
    consciousness_coherence_check,
    assess_intermodulation_harmony,
    assess_phase_relationships,
    coherence_adjust,
    harmonic_analysis,
    generate_pink_noise,
    coherence_check,
)

from .session_builder import (
    EntrainmentSession,
    ConsciousnessIntentionWeaver,
)

from .metadata_generator import (
    generate_metadata,
    analyze_consciousness_progression,
    generate_consciousness_guidance,
    assess_biofield_coherence_potential,
)

from .validator import (
    validate_config,
    assess_neural_architecture_compatibility,
    assess_biofield_coherence_safety,
    validate_consciousness_safety_protocols,
)

from .visualizer import (
    visualize_audio,
    plot_consciousness_journey,
    plot_biofield_coherence_analysis,
)

__all__ = [
    # signal generation
    "generate_biofield_pink_noise",
    "generate_brown_noise",
    "generate_white_noise",
    "generate_consciousness_aware_carrier_wave",
    "apply_isochronic",
    "apply_bilateral_panning",
    "apply_biorhythm_fm_modulation",
    "apply_fm_modulation",
    "consciousness_coherence_check",
    "assess_intermodulation_harmony",
    "assess_phase_relationships",
    "coherence_adjust",
    "harmonic_analysis",
    "generate_pink_noise",
    "coherence_check",
    # session building
    "EntrainmentSession",
    "ConsciousnessIntentionWeaver",
    # metadata
    "generate_metadata",
    "analyze_consciousness_progression",
    "generate_consciousness_guidance",
    "assess_biofield_coherence_potential",
    # validation
    "validate_config",
    "assess_neural_architecture_compatibility",
    "assess_biofield_coherence_safety",
    "validate_consciousness_safety_protocols",
    # visualization
    "visualize_audio",
    "plot_consciousness_journey",
    "plot_biofield_coherence_analysis",
]