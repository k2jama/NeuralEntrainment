#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Validation Utils
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Validation Utilities - Shared validation functions and schemas.

This module provides comprehensive validation utilities for all components of the
Neural Entrainment System, ensuring data integrity, safety compliance, and
consistency across consciousness-aware interfaces and core functionality.
"""

import re
import json
import math
from datetime import datetime, timedelta
from typing import Dict, Any, List, Tuple, Optional, Union, Callable
from dataclasses import dataclass, field
from enum import Enum

# Import shared constants for validation
from .consciousness_constants import (
    CONSCIOUSNESS_STATES,
    BRAINWAVE_FREQUENCIES,
    validate_consciousness_state
)
from .biofield_constants import (
    SOLFEGGIO_FREQUENCIES,
    SCHUMANN_RESONANCE_FREQUENCIES,
    GOLDEN_RATIO_HARMONICS,
    BIOFIELD_COHERENCE_LEVELS
)
from .safety_constants import (
    SAFETY_THRESHOLDS,
    NEURAL_LOAD_LIMITS,
    check_safety_compliance
)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VALIDATION RESULT STRUCTURES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ValidationSeverity(Enum):
    """Severity levels for validation issues."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

@dataclass
class ValidationIssue:
    """Individual validation issue."""
    severity: ValidationSeverity
    field_path: str
    message: str
    value: Any = None
    suggestion: str = ""
    code: str = ""

@dataclass
class ValidationResult:
    """
    Comprehensive validation result with detailed feedback.
    """
    is_valid: bool = True
    is_safe: bool = True
    overall_score: float = 1.0
    issues: List[ValidationIssue] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    critical_issues: List[str] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def add_issue(self, severity: ValidationSeverity, field_path: str, 
                  message: str, value: Any = None, suggestion: str = "", code: str = ""):
        """Add a validation issue."""
        issue = ValidationIssue(severity, field_path, message, value, suggestion, code)
        self.issues.append(issue)
        
        if severity == ValidationSeverity.ERROR:
            self.errors.append(message)
            self.is_valid = False
        elif severity == ValidationSeverity.CRITICAL:
            self.critical_issues.append(message)
            self.is_valid = False
            self.is_safe = False
        elif severity == ValidationSeverity.WARNING:
            self.warnings.append(message)
        
        if suggestion:
            self.suggestions.append(suggestion)
    
    def get_issues_by_severity(self, severity: ValidationSeverity) -> List[ValidationIssue]:
        """Get all issues of a specific severity."""
        return [issue for issue in self.issues if issue.severity == severity]
    
    def has_critical_issues(self) -> bool:
        """Check if there are any critical issues."""
        return len(self.critical_issues) > 0
    
    def calculate_safety_score(self) -> float:
        """Calculate a safety score based on issues."""
        if self.has_critical_issues():
            return 0.0
        
        score = 1.0
        score -= len(self.errors) * 0.2
        score -= len(self.warnings) * 0.1
        
        return max(0.0, score)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# VALIDATION SCHEMAS AND RULES
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Session configuration validation schema
SESSION_CONFIG_SCHEMA = {
    'name': {
        'type': 'string',
        'required': True,
        'min_length': 1,
        'max_length': 100,
        'pattern': r'^[a-zA-Z0-9\s\-_\.]+$'
    },
    'duration_minutes': {
        'type': 'integer',
        'required': True,
        'min_value': 5,
        'max_value': 120,
        'safety_check': True
    },
    'frequency_intensity': {
        'type': 'float',
        'required': True,
        'min_value': 0.1,
        'max_value': 1.0,
        'safety_check': True
    },
    'consciousness_journey': {
        'type': 'array',
        'required': True,
        'min_items': 1,
        'max_items': 8,
        'item_validation': 'consciousness_state'
    },
    'biofield_configuration': {
        'type': 'object',
        'required': False,
        'properties': {
            'schumann_alignment': {'type': 'float', 'min_value': 0.0, 'max_value': 1.0},
            'solfeggio_integration': {'type': 'float', 'min_value': 0.0, 'max_value': 1.0},
            'golden_ratio_harmonics': {'type': 'float', 'min_value': 0.0, 'max_value': 1.0}
        }
    },
    'safety_parameters': {
        'type': 'object',
        'required': False,
        'properties': {
            'comfort_monitoring': {'type': 'boolean', 'default': True},
            'automatic_adjustment': {'type': 'boolean', 'default': True},
            'emergency_stop': {'type': 'boolean', 'default': True}
        }
    }
}

# Preset configuration validation schema
PRESET_CONFIG_SCHEMA = {
    'preset_id': {
        'type': 'string',
        'required': True,
        'pattern': r'^[a-z0-9_]+$',
        'min_length': 3,
        'max_length': 50
    },
    'name': {
        'type': 'string',
        'required': True,
        'min_length': 1,
        'max_length': 100
    },
    'description': {
        'type': 'string',
        'required': True,
        'min_length': 10,
        'max_length': 500
    },
    'category': {
        'type': 'string',
        'required': True,
        'allowed_values': ['healing', 'meditation', 'creativity', 'learning', 'transcendence', 'custom']
    },
    'experience_level': {
        'type': 'string',
        'required': True,
        'allowed_values': ['beginner', 'intermediate', 'advanced', 'expert']
    },
    'base_configuration': {
        'type': 'object',
        'required': True,
        'schema': SESSION_CONFIG_SCHEMA
    },
    'tags': {
        'type': 'array',
        'required': False,
        'item_type': 'string',
        'max_items': 10
    },
    'created_date': {
        'type': 'datetime',
        'required': True
    },
    'version': {
        'type': 'string',
        'required': True,
        'pattern': r'^\d+\.\d+\.\d+$'
    }
}

# User input validation patterns
USER_INPUT_PATTERNS = {
    'name': r'^[a-zA-Z\s\-\'\.]{1,100}$',
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    'session_name': r'^[a-zA-Z0-9\s\-_\.]{1,100}$',
    'preset_id': r'^[a-z0-9_]{3,50}$',
    'version': r'^\d+\.\d+\.\d+$',
    'duration_string': r'^\d{1,3}(m|min|minutes?)$',
    'intensity_string': r'^\d{1,3}%$',
    'date_string': r'^\d{4}-\d{2}-\d{2}$',
    'time_string': r'^\d{2}:\d{2}(:\d{2})?$'
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CORE VALIDATION FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def validate_session_config(config: Dict[str, Any], 
                           user_profile: Optional[Dict[str, Any]] = None,
                           strict_mode: bool = False) -> ValidationResult:
    """
    Comprehensive validation of session configuration.
    
    Args:
        config: Session configuration to validate
        user_profile: Optional user profile for safety checks
        strict_mode: Whether to apply strict validation rules
        
    Returns:
        ValidationResult with detailed feedback
    """
    result = ValidationResult()
    
    # Validate against schema
    _validate_against_schema(config, SESSION_CONFIG_SCHEMA, result, 'session_config')
    
    # Consciousness journey validation
    if 'consciousness_journey' in config:
        journey = config['consciousness_journey']
        _validate_consciousness_journey(journey, result, strict_mode)
    
    # Biofield configuration validation
    if 'biofield_configuration' in config:
        biofield_config = config['biofield_configuration']
        _validate_biofield_configuration(biofield_config, result)
    
    # Safety validation with user profile
    if user_profile:
        safety_result = check_safety_compliance(config, user_profile)
        if not safety_result['is_safe']:
            for violation in safety_result['violations']:
                result.add_issue(ValidationSeverity.CRITICAL, 'safety', violation)
            for warning in safety_result['warnings']:
                result.add_issue(ValidationSeverity.WARNING, 'safety', warning)
    
    # Calculate neural load
    neural_load = _calculate_neural_load_simple(config)
    result.metadata['neural_load'] = neural_load
    
    if neural_load > 0.8:
        result.add_issue(
            ValidationSeverity.WARNING,
            'neural_load',
            f"High neural load detected: {neural_load:.1%}",
            neural_load,
            "Consider reducing session complexity or intensity"
        )
    
    # Calculate overall validation score
    result.overall_score = result.calculate_safety_score()
    
    return result

def validate_preset_config(preset: Dict[str, Any]) -> ValidationResult:
    """
    Validate preset configuration.
    
    Args:
        preset: Preset configuration to validate
        
    Returns:
        ValidationResult with detailed feedback
    """
    result = ValidationResult()
    
    # Validate against preset schema
    _validate_against_schema(preset, PRESET_CONFIG_SCHEMA, result, 'preset')
    
    # Validate base configuration
    if 'base_configuration' in preset:
        base_result = validate_session_config(preset['base_configuration'])
        
        # Merge results
        for issue in base_result.issues:
            issue.field_path = f"base_configuration.{issue.field_path}"
            result.issues.append(issue)
        
        result.errors.extend(base_result.errors)
        result.warnings.extend(base_result.warnings)
        result.critical_issues.extend(base_result.critical_issues)
    
    # Validate preset-specific requirements
    if 'experience_level' in preset and 'base_configuration' in preset:
        _validate_preset_experience_compatibility(preset, result)
    
    result.overall_score = result.calculate_safety_score()
    
    return result

def sanitize_user_input(input_value: str, 
                       input_type: str,
                       max_length: Optional[int] = None,
                       allow_empty: bool = False) -> str:
    """
    Sanitize and validate user input.
    
    Args:
        input_value: Raw input string
        input_type: Type of input for pattern matching
        max_length: Maximum allowed length
        allow_empty: Whether to allow empty strings
        
    Returns:
        Sanitized input string
        
    Raises:
        ValueError: If input is invalid or unsafe
    """
    if not isinstance(input_value, str):
        raise ValueError(f"Expected string input, got {type(input_value)}")
    
    # Strip whitespace
    sanitized = input_value.strip()
    
    # Check for empty input
    if not sanitized and not allow_empty:
        raise ValueError("Input cannot be empty")
    
    # Length validation
    if max_length and len(sanitized) > max_length:
        raise ValueError(f"Input too long: {len(sanitized)} > {max_length}")
    
    # Pattern validation
    if input_type in USER_INPUT_PATTERNS:
        pattern = USER_INPUT_PATTERNS[input_type]
        if not re.match(pattern, sanitized):
            raise ValueError(f"Invalid format for {input_type}: {sanitized}")
    
    # Additional security checks
    _check_input_security(sanitized)
    
    return sanitized

def validate_frequency_value(frequency: float, 
                           frequency_type: str,
                           context: str = "") -> ValidationResult:
    """
    Validate a frequency value against known ranges and safety limits.
    
    Args:
        frequency: Frequency value in Hz
        frequency_type: Type of frequency (brainwave, solfeggio, etc.)
        context: Additional context for validation
        
    Returns:
        ValidationResult for the frequency
    """
    result = ValidationResult()
    
    # Basic range validation
    if frequency <= 0:
        result.add_issue(
            ValidationSeverity.ERROR,
            'frequency_value',
            f"Frequency must be positive: {frequency}",
            frequency
        )
        return result
    
    if frequency > 1000:  # Arbitrary upper limit for safety
        result.add_issue(
            ValidationSeverity.WARNING,
            'frequency_value',
            f"Very high frequency detected: {frequency} Hz",
            frequency,
            "Consider using lower frequencies for safety"
        )
    
    # Type-specific validation
    if frequency_type == 'brainwave':
        _validate_brainwave_frequency(frequency, result)
    elif frequency_type == 'solfeggio':
        _validate_solfeggio_frequency(frequency, result)
    elif frequency_type == 'schumann':
        _validate_schumann_frequency(frequency, result)
    elif frequency_type == 'golden_ratio':
        _validate_golden_ratio_frequency(frequency, result)
    
    result.overall_score = result.calculate_safety_score()
    
    return result

def validate_consciousness_state_transition(from_state: str, 
                                          to_state: str,
                                          user_experience: str = "beginner") -> ValidationResult:
    """
    Validate a consciousness state transition for safety and appropriateness.
    
    Args:
        from_state: Starting consciousness state
        to_state: Target consciousness state
        user_experience: User's experience level
        
    Returns:
        ValidationResult for the transition
    """
    result = ValidationResult()
    
    # Validate state existence
    if not validate_consciousness_state(from_state):
        result.add_issue(
            ValidationSeverity.ERROR,
            'from_state',
            f"Unknown consciousness state: {from_state}",
            from_state
        )
    
    if not validate_consciousness_state(to_state):
        result.add_issue(
            ValidationSeverity.ERROR,
            'to_state', 
            f"Unknown consciousness state: {to_state}",
            to_state
        )
    
    if not result.is_valid:
        return result
    
    # Import consciousness utilities
    from .consciousness_constants import (
        CONSCIOUSNESS_STATE_TRANSITIONS,
        calculate_consciousness_depth,
        get_safe_transitions
    )
    
    # Check if direct transition exists
    transition_key = (from_state, to_state)
    if transition_key in CONSCIOUSNESS_STATE_TRANSITIONS:
        transition = CONSCIOUSNESS_STATE_TRANSITIONS[transition_key]
        
        # Check experience level compatibility
        if transition.difficulty in ['challenging', 'advanced'] and user_experience == 'beginner':
            result.add_issue(
                ValidationSeverity.WARNING,
                'transition_difficulty',
                f"Challenging transition for {user_experience}: {from_state} -> {to_state}",
                suggestion="Consider intermediate states or gain more experience"
            )
    else:
        # Check depth difference for safety
        from_depth = calculate_consciousness_depth(from_state)
        to_depth = calculate_consciousness_depth(to_state)
        depth_diff = abs(to_depth - from_depth)
        
        if depth_diff > 2:
            result.add_issue(
                ValidationSeverity.WARNING,
                'depth_difference',
                f"Large consciousness depth change: {from_state} (depth {from_depth}) -> {to_state} (depth {to_depth})",
                suggestion="Consider using intermediate states for smoother transition"
            )
    
    # Check for safe transitions
    safe_transitions = get_safe_transitions(from_state, user_experience)
    if to_state not in safe_transitions:
        result.add_issue(
            ValidationSeverity.WARNING,
            'safety',
            f"Transition not in recommended safe transitions for {user_experience}",
            suggestion=f"Recommended targets: {', '.join(safe_transitions[:3])}"
        )
    
    result.overall_score = result.calculate_safety_score()
    
    return result

def validate_biofield_coherence(coherence_data: Dict[str, float]) -> ValidationResult:
    """
    Validate biofield coherence data.
    
    Args:
        coherence_data: Dictionary of biofield coherence values
        
    Returns:
        ValidationResult for the coherence data
    """
    result = ValidationResult()
    
    required_components = ['schumann_resonance', 'solfeggio_harmonics', 'golden_ratio_alignment']
    
    # Check for required components
    for component in required_components:
        if component not in coherence_data:
            result.add_issue(
                ValidationSeverity.WARNING,
                'biofield_components',
                f"Missing biofield component: {component}",
                suggestion=f"Add {component} for complete biofield analysis"
            )
    
    # Validate coherence values
    for component, coherence in coherence_data.items():
        if not isinstance(coherence, (int, float)):
            result.add_issue(
                ValidationSeverity.ERROR,
                f'coherence.{component}',
                f"Invalid coherence value type: {type(coherence)}",
                coherence
            )
            continue
        
        if not (0.0 <= coherence <= 1.0):
            result.add_issue(
                ValidationSeverity.ERROR,
                f'coherence.{component}',
                f"Coherence value out of range [0,1]: {coherence}",
                coherence
            )
        
        # Check for concerning coherence levels
        if coherence < 0.2:
            result.add_issue(
                ValidationSeverity.WARNING,
                f'coherence.{component}',
                f"Low coherence detected in {component}: {coherence:.1%}",
                coherence,
                "Consider focusing on stabilizing this biofield component"
            )
        elif coherence > 0.95:
            result.add_issue(
                ValidationSeverity.INFO,
                f'coherence.{component}',
                f"Exceptionally high coherence in {component}: {coherence:.1%}",
                coherence,
                "Excellent biofield stability"
            )
    
    # Calculate overall coherence if possible
    if len(coherence_data) >= 2:
        from .biofield_constants import calculate_biofield_coherence
        
        schumann = coherence_data.get('schumann_resonance', 0.5)
        solfeggio = coherence_data.get('solfeggio_harmonics', 0.5)
        golden_ratio = coherence_data.get('golden_ratio_alignment', 0.5)
        
        overall_coherence = calculate_biofield_coherence(schumann, solfeggio, golden_ratio)
        result.metadata['overall_coherence'] = overall_coherence
        
        from .biofield_constants import get_biofield_coherence_level
        coherence_level = get_biofield_coherence_level(overall_coherence)
        result.metadata['coherence_level'] = coherence_level
    
    result.overall_score = result.calculate_safety_score()
    
    return result

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# HELPER VALIDATION FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _validate_against_schema(data: Dict[str, Any], 
                           schema: Dict[str, Any],
                           result: ValidationResult,
                           context: str = "") -> None:
    """Validate data against a schema definition."""
    
    for field_name, field_schema in schema.items():
        field_path = f"{context}.{field_name}" if context else field_name
        
        # Check if field exists
        if field_schema.get('required', False) and field_name not in data:
            result.add_issue(
                ValidationSeverity.ERROR,
                field_path,
                f"Required field missing: {field_name}",
                suggestion=f"Add {field_name} to the configuration"
            )
            continue
        
        if field_name not in data:
            continue
        
        value = data[field_name]
        
        # Type validation
        expected_type = field_schema.get('type')
        if expected_type and not _check_type(value, expected_type):
            result.add_issue(
                ValidationSeverity.ERROR,
                field_path,
                f"Invalid type for {field_name}: expected {expected_type}, got {type(value).__name__}",
                value
            )
            continue
        
        # Range validation for numbers
        if expected_type in ['integer', 'float']:
            _validate_number_range(value, field_schema, result, field_path)
        
        # String validation
        elif expected_type == 'string':
            _validate_string(value, field_schema, result, field_path)
        
        # Array validation
        elif expected_type == 'array':
            _validate_array(value, field_schema, result, field_path)
        
        # Object validation
        elif expected_type == 'object':
            _validate_object(value, field_schema, result, field_path)

def _validate_consciousness_journey(journey: List[str], 
                                  result: ValidationResult,
                                  strict_mode: bool) -> None:
    """Validate consciousness journey for safety and feasibility."""
    
    if not journey:
        result.add_issue(
            ValidationSeverity.ERROR,
            'consciousness_journey',
            "Consciousness journey cannot be empty",
            suggestion="Add at least one consciousness state"
        )
        return
    
    # Check each state in journey
    for i, state in enumerate(journey):
        if not validate_consciousness_state(state):
            result.add_issue(
                ValidationSeverity.ERROR,
                f'consciousness_journey[{i}]',
                f"Unknown consciousness state: {state}",
                state
            )
    
    # Check transitions
    for i in range(len(journey) - 1):
        from_state = journey[i]
        to_state = journey[i + 1]
        
        transition_result = validate_consciousness_state_transition(from_state, to_state)
        
        for issue in transition_result.issues:
            if issue.severity == ValidationSeverity.WARNING and strict_mode:
                # Upgrade warnings to errors in strict mode
                issue.severity = ValidationSeverity.ERROR
            
            issue.field_path = f"consciousness_journey[{i}→{i+1}]"
            result.issues.append(issue)

def _validate_biofield_configuration(config: Dict[str, Any], result: ValidationResult) -> None:
    """Validate biofield configuration parameters."""
    
    biofield_components = ['schumann_alignment', 'solfeggio_integration', 'golden_ratio_harmonics']
    
    for component in biofield_components:
        if component in config:
            value = config[component]
            
            if not isinstance(value, (int, float)):
                result.add_issue(
                    ValidationSeverity.ERROR,
                    f'biofield_configuration.{component}',
                    f"Invalid type for {component}: {type(value)}",
                    value
                )
            elif not (0.0 <= value <= 1.0):
                result.add_issue(
                    ValidationSeverity.ERROR,
                    f'biofield_configuration.{component}',
                    f"Value out of range [0,1]: {value}",
                    value
                )

def _calculate_neural_load_simple(config: Dict[str, Any]) -> float:
    """Calculate a simple neural load estimate."""
    
    load_factors = []
    
    # Duration factor
    duration = config.get('duration_minutes', 30)
    duration_factor = min(1.0, duration / 60)
    load_factors.append(duration_factor * 0.3)
    
    # Intensity factor
    intensity = config.get('frequency_intensity', 0.5)
    load_factors.append(intensity * 0.3)
    
    # Journey complexity
    journey = config.get('consciousness_journey', [])
    journey_factor = min(1.0, len(journey) / 5)
    load_factors.append(journey_factor * 0.2)
    
    # Biofield complexity
    biofield_config = config.get('biofield_configuration', {})
    biofield_factor = len(biofield_config) / 10  # Rough estimate
    load_factors.append(min(1.0, biofield_factor) * 0.2)
    
    return sum(load_factors)

def _validate_preset_experience_compatibility(preset: Dict[str, Any], result: ValidationResult) -> None:
    """Validate that preset difficulty matches experience level."""
    
    experience_level = preset['experience_level']
    base_config = preset['base_configuration']
    
    neural_load = _calculate_neural_load_simple(base_config)
    
    # Experience level thresholds
    max_loads = {
        'beginner': 0.4,
        'intermediate': 0.6,
        'advanced': 0.8,
        'expert': 1.0
    }
    
    max_load = max_loads.get(experience_level, 0.4)
    
    if neural_load > max_load:
        result.add_issue(
            ValidationSeverity.WARNING,
            'experience_compatibility',
            f"Preset complexity ({neural_load:.1%}) may be too high for {experience_level} users",
            neural_load,
            f"Consider reducing complexity or changing experience level requirement"
        )

def _check_type(value: Any, expected_type: str) -> bool:
    """Check if value matches expected type."""
    
    type_map = {
        'string': str,
        'integer': int,
        'float': (int, float),
        'boolean': bool,
        'array': list,
        'object': dict,
        'datetime': datetime
    }
    
    expected_python_type = type_map.get(expected_type)
    if expected_python_type is None:
        return True  # Unknown type, skip validation
    
    return isinstance(value, expected_python_type)

def _validate_number_range(value: Union[int, float], 
                         schema: Dict[str, Any],
                         result: ValidationResult,
                         field_path: str) -> None:
    """Validate number against range constraints."""
    
    if 'min_value' in schema and value < schema['min_value']:
        result.add_issue(
            ValidationSeverity.ERROR,
            field_path,
            f"Value below minimum: {value} < {schema['min_value']}",
            value
        )
    
    if 'max_value' in schema and value > schema['max_value']:
        result.add_issue(
            ValidationSeverity.ERROR,
            field_path,
            f"Value above maximum: {value} > {schema['max_value']}",
            value
        )

def _validate_string(value: str, 
                   schema: Dict[str, Any],
                   result: ValidationResult,
                   field_path: str) -> None:
    """Validate string against constraints."""
    
    if 'min_length' in schema and len(value) < schema['min_length']:
        result.add_issue(
            ValidationSeverity.ERROR,
            field_path,
            f"String too short: {len(value)} < {schema['min_length']}",
            value
        )
    
    if 'max_length' in schema and len(value) > schema['max_length']:
        result.add_issue(
            ValidationSeverity.ERROR,
            field_path,
            f"String too long: {len(value)} > {schema['max_length']}",
            value
        )
    
    if 'pattern' in schema:
        pattern = schema['pattern']
        if not re.match(pattern, value):
            result.add_issue(
                ValidationSeverity.ERROR,
                field_path,
                f"String does not match pattern: {pattern}",
                value
            )
    
    if 'allowed_values' in schema and value not in schema['allowed_values']:
        result.add_issue(
            ValidationSeverity.ERROR,
            field_path,
            f"Value not in allowed list: {value}",
            value,
            f"Allowed values: {', '.join(schema['allowed_values'])}"
        )

def _validate_array(value: List[Any], 
                  schema: Dict[str, Any],
                  result: ValidationResult,
                  field_path: str) -> None:
    """Validate array against constraints."""
    
    if 'min_items' in schema and len(value) < schema['min_items']:
        result.add_issue(
            ValidationSeverity.ERROR,
            field_path,
            f"Array too short: {len(value)} < {schema['min_items']}",
            value
        )
    
    if 'max_items' in schema and len(value) > schema['max_items']:
        result.add_issue(
            ValidationSeverity.ERROR,
            field_path,
            f"Array too long: {len(value)} > {schema['max_items']}",
            value
        )

def _validate_object(value: Dict[str, Any], 
                   schema: Dict[str, Any],
                   result: ValidationResult,
                   field_path: str) -> None:
    """Validate object against schema."""
    
    if 'schema' in schema:
        # Nested schema validation
        _validate_against_schema(value, schema['schema'], result, field_path)
    
    if 'properties' in schema:
        # Property validation
        for prop_name, prop_schema in schema['properties'].items():
            if prop_name in value:
                prop_value = value[prop_name]
                prop_path = f"{field_path}.{prop_name}"
                
                if 'type' in prop_schema:
                    if not _check_type(prop_value, prop_schema['type']):
                        result.add_issue(
                            ValidationSeverity.ERROR,
                            prop_path,
                            f"Invalid type: expected {prop_schema['type']}",
                            prop_value
                        )

def _validate_brainwave_frequency(frequency: float, result: ValidationResult) -> None:
    """Validate brainwave frequency against known ranges."""
    
    # Find which brainwave range this frequency falls into
    matched_range = None
    for range_name, range_info in BRAINWAVE_FREQUENCIES.items():
        if range_info.min_frequency <= frequency <= range_info.max_frequency:
            matched_range = range_name
            break
    
    if matched_range:
        result.metadata['brainwave_range'] = matched_range
        range_info = BRAINWAVE_FREQUENCIES[matched_range]
        
        # Check safety considerations
        if range_info.cautions:
            for caution in range_info.cautions:
                if 'only' in caution and 'expert' in caution:
                    result.add_issue(
                        ValidationSeverity.WARNING,
                        'brainwave_safety',
                        f"Frequency {frequency} Hz is in {matched_range} range: {caution}",
                        frequency
                    )
    else:
        result.add_issue(
            ValidationSeverity.WARNING,
            'brainwave_range',
            f"Frequency {frequency} Hz does not match known brainwave ranges",
            frequency,
            "Consider using frequencies within established brainwave ranges"
        )

def _validate_solfeggio_frequency(frequency: float, result: ValidationResult) -> None:
    """Validate against Solfeggio frequencies."""
    
    # Check if it matches a known Solfeggio frequency (within 1% tolerance)
    matched_solfeggio = None
    min_difference = float('inf')
    
    for solfeggio_name, solfeggio_info in SOLFEGGIO_FREQUENCIES.items():
        difference = abs(frequency - solfeggio_info.frequency)
        tolerance = solfeggio_info.frequency * 0.01  # 1% tolerance
        
        if difference <= tolerance and difference < min_difference:
            matched_solfeggio = solfeggio_name
            min_difference = difference
    
    if matched_solfeggio:
        result.metadata['solfeggio_frequency'] = matched_solfeggio
    else:
        result.add_issue(
            ValidationSeverity.INFO,
            'solfeggio_match',
            f"Frequency {frequency} Hz does not closely match known Solfeggio frequencies",
            frequency,
            "Consider using established Solfeggio frequencies for optimal healing properties"
        )

def _validate_schumann_frequency(frequency: float, result: ValidationResult) -> None:
    """Validate against Schumann resonance frequencies."""
    
    matched_mode = None
    for mode_name, mode_info in SCHUMANN_RESONANCE_FREQUENCIES.items():
        if abs(frequency - mode_info.frequency) <= 0.5:  # 0.5 Hz tolerance
            matched_mode = mode_name
            break
    
    if matched_mode:
        result.metadata['schumann_mode'] = matched_mode
    else:
        result.add_issue(
            ValidationSeverity.INFO,
            'schumann_match',
            f"Frequency {frequency} Hz does not match known Schumann resonance modes",
            frequency,
            "Consider using Schumann resonance frequencies for optimal Earth connection"
        )

def _validate_golden_ratio_frequency(frequency: float, result: ValidationResult) -> None:
    """Validate against golden ratio harmonics."""
    
    matched_harmonic = None
    for harmonic_name, harmonic_info in GOLDEN_RATIO_HARMONICS.items():
        if abs(frequency - harmonic_info.frequency) <= 0.1:  # 0.1 Hz tolerance
            matched_harmonic = harmonic_name
            break
    
    if matched_harmonic:
        result.metadata['golden_ratio_harmonic'] = matched_harmonic
    else:
        result.add_issue(
            ValidationSeverity.INFO,
            'golden_ratio_match',
            f"Frequency {frequency} Hz does not match known golden ratio harmonics",
            frequency,
            "Consider using golden ratio harmonics for optimal natural resonance"
        )

def _check_input_security(input_str: str) -> None:
    """Check input for potential security issues."""
    
    # Check for potential injection patterns
    dangerous_patterns = [
        r'<script.*?>',
        r'javascript:',
        r'onload=',
        r'onerror=',
        r'eval\(',
        r'exec\(',
        r'import\s+os',
        r'import\s+subprocess'
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, input_str, re.IGNORECASE):
            raise ValueError(f"Potentially dangerous input detected: {pattern}")
    
    # Check for excessively long inputs that might cause DoS
    if len(input_str) > 10000:
        raise ValueError("Input too long - possible DoS attempt")

def create_validation_report(validation_results: List[ValidationResult]) -> Dict[str, Any]:
    """
    Create a comprehensive validation report from multiple results.
    
    Args:
        validation_results: List of ValidationResult objects
        
    Returns:
        Comprehensive validation report
    """
    report = {
        'overall_valid': True,
        'overall_safe': True,
        'total_issues': 0,
        'issues_by_severity': {
            'critical': 0,
            'error': 0,
            'warning': 0,
            'info': 0
        },
        'average_score': 0.0,
        'recommendations': [],
        'detailed_results': []
    }
    
    if not validation_results:
        return report
    
    total_score = 0.0
    all_recommendations = set()
    
    for result in validation_results:
        # Update overall status
        if not result.is_valid:
            report['overall_valid'] = False
        if not result.is_safe:
            report['overall_safe'] = False
        
        # Count issues by severity
        for issue in result.issues:
            report['issues_by_severity'][issue.severity.value] += 1
            report['total_issues'] += 1
        
        # Collect recommendations
        all_recommendations.update(result.suggestions)
        
        # Add to detailed results
        report['detailed_results'].append({
            'is_valid': result.is_valid,
            'is_safe': result.is_safe,
            'score': result.overall_score,
            'issues_count': len(result.issues),
            'metadata': result.metadata
        })
        
        total_score += result.overall_score
    
    # Calculate averages
    report['average_score'] = total_score / len(validation_results)
    report['recommendations'] = list(all_recommendations)
    
    return report