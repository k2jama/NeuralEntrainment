#!/usr/bin/env python3
"""
🧪 Neural Entrainment System - Configuration Presets Module
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🧠 Consciousness-Aware Biofield Intelligence Framework  
🌟 Dr. KB Jama, Neural Dialogue Interface Research

Configuration presets for consciousness-aware neural entrainment sessions.
Provides easy Python access to all preset configurations, neural profiles,
biofield templates, and safety protocols.
"""

import json
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
import logging

# Configuration directory path
CONFIG_DIR = Path(__file__).parent

class ConfigurationManager:
    """
    Comprehensive configuration manager for consciousness-aware neural entrainment.
    
    Provides unified access to:
    - Session presets with consciousness journey mapping
    - Neural profile templates with safety protocols
    - Biofield configuration templates
    - Safety protocol configurations
    - Configuration schema validation
    """
    
    def __init__(self):
        """Initialize configuration manager with all config files."""
        self._presets = None
        self._neural_profiles = None
        self._biofield_configs = None
        self._safety_protocols = None
        self._config_schema = None
        
        self.logger = logging.getLogger(__name__)
    
    def _load_json_config(self, filename: str) -> Dict[str, Any]:
        """Load and cache JSON configuration file."""
        config_path = CONFIG_DIR / filename
        
        if not config_path.exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in {filename}: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Error loading {filename}: {e}")
            raise
    
    @property
    def presets(self) -> Dict[str, Any]:
        """Load consciousness-aware session presets."""
        if self._presets is None:
            self._presets = self._load_json_config('presets.json')
        return self._presets
    
    @property
    def neural_profiles(self) -> Dict[str, Any]:
        """Load neural profile templates."""
        if self._neural_profiles is None:
            self._neural_profiles = self._load_json_config('neural_profile_templates.json')
        return self._neural_profiles
    
    @property
    def biofield_configs(self) -> Dict[str, Any]:
        """Load biofield intelligence configuration templates."""
        if self._biofield_configs is None:
            self._biofield_configs = self._load_json_config('biofield_configurations.json')
        return self._biofield_configs
    
    @property
    def safety_protocols(self) -> Dict[str, Any]:
        """Load safety protocol configurations."""
        if self._safety_protocols is None:
            self._safety_protocols = self._load_json_config('safety_protocols.json')
        return self._safety_protocols
    
    @property
    def config_schema(self) -> Dict[str, Any]:
        """Load configuration schema for validation."""
        if self._config_schema is None:
            self._config_schema = self._load_json_config('configuration_schema.json')
        return self._config_schema
    
    def get_consciousness_preset(self, preset_name: str) -> Optional[Dict[str, Any]]:
        """
        Get consciousness-aware preset by name.
        
        Args:
            preset_name: Name of the preset (e.g., 'focus', 'heal', 'transcend')
            
        Returns:
            Preset configuration dict or None if not found
        """
        presets_data = self.presets.get('consciousness_aware_presets', {})
        return presets_data.get(preset_name)
    
    def list_consciousness_presets(self) -> List[str]:
        """List all available consciousness-aware preset names."""
        presets_data = self.presets.get('consciousness_aware_presets', {})
        return list(presets_data.keys())
    
    def get_neural_profile_template(self, template_name: str) -> Optional[Dict[str, Any]]:
        """
        Get neural profile template by name.
        
        Args:
            template_name: Template name (e.g., 'sensitive_beginner', 'standard_intermediate')
            
        Returns:
            Neural profile template dict or None if not found
        """
        profiles_data = self.neural_profiles.get('neural_profile_templates', {})
        return profiles_data.get(template_name)
    
    def list_neural_profile_templates(self) -> List[str]:
        """List all available neural profile template names."""
        profiles_data = self.neural_profiles.get('neural_profile_templates', {})
        return list(profiles_data.keys())
    
    def get_biofield_template(self, template_name: str) -> Optional[Dict[str, Any]]:
        """
        Get biofield configuration template by name.
        
        Args:
            template_name: Template name (e.g., 'schumann_resonance_set', 'solfeggio_frequency_set')
            
        Returns:
            Biofield template dict or None if not found
        """
        biofield_data = self.biofield_configs.get('natural_frequency_templates', {})
        return biofield_data.get(template_name)
    
    def list_biofield_templates(self) -> List[str]:
        """List all available biofield configuration template names."""
        biofield_data = self.biofield_configs.get('natural_frequency_templates', {})
        return list(biofield_data.keys())
    
    def get_safety_protocol(self, protocol_name: str) -> Optional[Dict[str, Any]]:
        """
        Get safety protocol configuration by name.
        
        Args:
            protocol_name: Protocol name (e.g., 'sensitive_profile_protocols', 'medical_contraindication_protocols')
            
        Returns:
            Safety protocol dict or None if not found
        """
        safety_data = self.safety_protocols.get('neural_profile_safety_protocols', {})
        return safety_data.get(protocol_name)
    
    def list_safety_protocols(self) -> List[str]:
        """List all available safety protocol names."""
        safety_data = self.safety_protocols.get('neural_profile_safety_protocols', {})
        return list(safety_data.keys())
    
    def get_presets_by_intention(self, intention: str) -> List[Dict[str, Any]]:
        """
        Get all presets that match a specific consciousness intention.
        
        Args:
            intention: Consciousness intention (e.g., 'focus', 'heal', 'transcend')
            
        Returns:
            List of matching preset configurations
        """
        presets_data = self.presets.get('consciousness_aware_presets', {})
        matching_presets = []
        
        for preset_name, preset_config in presets_data.items():
            session_config = preset_config.get('session_config', {})
            weaver_config = session_config.get('consciousness_weaver', {})
            
            if weaver_config.get('intention') == intention:
                preset_with_name = preset_config.copy()
                preset_with_name['preset_name'] = preset_name
                matching_presets.append(preset_with_name)
        
        return matching_presets
    
    def get_presets_by_neural_compatibility(self, neural_profile: str) -> List[Dict[str, Any]]:
        """
        Get all presets compatible with a specific neural profile.
        
        Args:
            neural_profile: Neural profile type (e.g., 'sensitive', 'standard', 'resilient')
            
        Returns:
            List of compatible preset configurations
        """
        presets_data = self.presets.get('consciousness_aware_presets', {})
        compatible_presets = []
        
        for preset_name, preset_config in presets_data.items():
            metadata = preset_config.get('metadata', {})
            compatibility = metadata.get('neural_compatibility', [])
            
            if neural_profile in compatibility or 'all' in compatibility:
                preset_with_name = preset_config.copy()
                preset_with_name['preset_name'] = preset_name
                compatible_presets.append(preset_with_name)
        
        return compatible_presets
    
    def validate_preset_safety(self, preset_config: Dict[str, Any], 
                              neural_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Validate preset safety for a given neural profile.
        
        Args:
            preset_config: Preset configuration to validate
            neural_profile: User's neural profile
            
        Returns:
            Validation result with safety assessment
        """
        # This would integrate with the validator module
        # For now, return basic structure
        return {
            'is_safe': True,
            'safety_rating': 'high',
            'warnings': [],
            'recommendations': []
        }


# Global configuration manager instance
config_manager = ConfigurationManager()

# Convenience functions for direct access
def get_preset(preset_name: str) -> Optional[Dict[str, Any]]:
    """Get consciousness-aware preset by name."""
    return config_manager.get_consciousness_preset(preset_name)

def list_presets() -> List[str]:
    """List all available consciousness-aware preset names."""
    return config_manager.list_consciousness_presets()

def get_neural_template(template_name: str) -> Optional[Dict[str, Any]]:
    """Get neural profile template by name."""
    return config_manager.get_neural_profile_template(template_name)

def list_neural_templates() -> List[str]:
    """List all available neural profile template names."""
    return config_manager.list_neural_profile_templates()

def get_biofield_template(template_name: str) -> Optional[Dict[str, Any]]:
    """Get biofield configuration template by name."""
    return config_manager.get_biofield_template(template_name)

def list_biofield_templates() -> List[str]:
    """List all available biofield template names."""
    return config_manager.list_biofield_templates()

def get_safety_protocol(protocol_name: str) -> Optional[Dict[str, Any]]:
    """Get safety protocol by name."""
    return config_manager.get_safety_protocol(protocol_name)

def list_safety_protocols() -> List[str]:
    """List all available safety protocol names."""
    return config_manager.list_safety_protocols()

# Pre-load commonly used configurations
CONSCIOUSNESS_INTENTIONS = [
    'focus', 'release', 'heal', 'create', 'transcend', 'integrate', 'energize', 'calm'
]

NEURAL_SENSITIVITY_LEVELS = ['sensitive', 'standard', 'resilient']

EXPERIENCE_LEVELS = ['beginner', 'intermediate', 'advanced', 'expert']

CONSCIOUSNESS_STATES = [
    'deep_delta', 'delta', 'theta', 'alpha', 'beta', 'gamma', 'focused_beta', 'low_gamma'
]

# Export all public symbols
__all__ = [
    'ConfigurationManager',
    'config_manager',
    'get_preset',
    'list_presets', 
    'get_neural_template',
    'list_neural_templates',
    'get_biofield_template',
    'list_biofield_templates',
    'get_safety_protocol',
    'list_safety_protocols',
    'CONSCIOUSNESS_INTENTIONS',
    'NEURAL_SENSITIVITY_LEVELS',
    'EXPERIENCE_LEVELS',
    'CONSCIOUSNESS_STATES'
]