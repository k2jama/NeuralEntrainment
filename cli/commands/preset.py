#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Preset Commands
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Preset Commands - Consciousness-aware preset browsing and management.

This module provides comprehensive preset management capabilities including:
- Intelligent preset browsing with neural profile filtering
- Detailed preset visualization and analysis
- Preset customization and modification
- Biofield intelligence integration previews
- Safety compatibility checking
- Personalized preset recommendations
"""

import sys
import os
import json
import argparse
import math
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple, TYPE_CHECKING
from datetime import datetime
import logging

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# CLI imports
from ..themes.consciousness_colors import ConsciousnessColorScheme
from ..themes.sacred_geometry import SacredGeometrySymbols, ConsciousnessVisualization
from ..themes.biofield_aesthetics import BiofieldAesthetics

if TYPE_CHECKING:
    from ..main import ConsciousnessEntryPoint

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PRESET MANAGEMENT CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Preset directories
DEFAULT_PRESETS_DIR = Path(__file__).parent.parent.parent / "config"
CUSTOM_PRESETS_DIR = Path.home() / ".neural_entrainment" / "custom_presets"

# Preset categories for organization
PRESET_CATEGORIES = {
    'focus': {
        'name': 'Focus & Concentration',
        'symbol': '🧠',
        'description': 'Enhance cognitive performance and concentration'
    },
    'relaxation': {
        'name': 'Relaxation & Stress Relief', 
        'symbol': '🌊',
        'description': 'Release stress and promote deep relaxation'
    },
    'meditation': {
        'name': 'Meditation & Mindfulness',
        'symbol': '🧘',
        'description': 'Support meditation practice and mindful awareness'
    },
    'healing': {
        'name': 'Healing & Recovery',
        'symbol': '💚',
        'description': 'Promote healing and cellular regeneration'
    },
    'creativity': {
        'name': 'Creativity & Flow',
        'symbol': '✨',
        'description': 'Enhance creative flow and inspiration'
    },
    'consciousness': {
        'name': 'Consciousness Exploration',
        'symbol': '🌌',
        'description': 'Explore expanded states of consciousness'
    },
    'sleep': {
        'name': 'Sleep & Rest',
        'symbol': '🌙',
        'description': 'Support healthy sleep and deep rest'
    },
    'energy': {
        'name': 'Energy & Vitality',
        'symbol': '⚡',
        'description': 'Boost energy and vitality'
    }
}

# Intention mappings
INTENTION_CATEGORIES = {
    'focus': ['concentration', 'study', 'cognitive_enhancement', 'mental_clarity'],
    'release': ['stress_relief', 'tension_release', 'emotional_clearing'],
    'heal': ['healing', 'regeneration', 'recovery', 'restoration'],
    'create': ['creativity', 'flow_state', 'inspiration', 'artistic'],
    'transcend': ['consciousness_expansion', 'transcendence', 'spiritual'],
    'integrate': ['integration', 'balance', 'wholeness', 'harmony'],
    'energize': ['energy_boost', 'vitality', 'activation', 'motivation'],
    'calm': ['relaxation', 'peace', 'serenity', 'tranquility']
}

# Experience level requirements
EXPERIENCE_REQUIREMENTS = {
    'beginner': ['gentle', 'basic', 'intro', 'foundation'],
    'intermediate': ['standard', 'moderate', 'balanced'],
    'advanced': ['deep', 'intense', 'complex', 'advanced'],
    'expert': ['transcendent', 'mastery', 'expert', 'extreme']
}

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PRESET COMMANDS CLASS  
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class PresetCommands:
    """
    Consciousness-aware preset browsing and management commands.
    
    This class provides comprehensive preset management including intelligent
    filtering, detailed analysis, customization capabilities, and personalized
    recommendations based on neural profiles and consciousness intentions.
    """
    
    def __init__(self, entry_point: 'ConsciousnessEntryPoint'):
        self.entry_point = entry_point
        self.color_scheme = ConsciousnessColorScheme()
        self.symbols = SacredGeometrySymbols()
        self.biofield = BiofieldAesthetics()
        self.consciousness_viz = ConsciousnessVisualization()
        
        # Ensure directories exist
        CUSTOM_PRESETS_DIR.mkdir(parents=True, exist_ok=True)
        
        # Load preset data
        self.presets_data = self._load_presets_data()
        self.filtered_presets = None
        
    def handle_preset_command(self, args: argparse.Namespace) -> int:
        """
        Main preset command handler with consciousness-aware routing.
        
        Args:
            args: Parsed command line arguments
            
        Returns:
            Exit code (0 for success)
        """
        try:
            action = getattr(args, 'preset_action', None)
            
            if action == 'browse':
                return self._browse_presets(args)
            elif action == 'show':
                return self._show_preset_details(args)
            elif action == 'customize':
                return self._customize_preset(args)
            elif action == 'create':
                return self._create_custom_preset(args)
            elif action == 'recommend':
                return self._recommend_presets(args)
            elif action == 'search':
                return self._search_presets(args)
            else:
                return self._show_preset_help()
                
        except KeyboardInterrupt:
            print(f"\n{self.color_scheme.gentle_text('Preset browsing gently paused')}")
            return 130
        except Exception as e:
            self._display_error(f"Preset command error: {e}")
            logging.exception("Preset command error")
            return 1
    
    def _browse_presets(self, args: argparse.Namespace) -> int:
        """
        Browse presets with consciousness-aware filtering and display.
        
        Args:
            args: Arguments including category and intention filters
            
        Returns:
            Exit code (0 for success)
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        # Display browse header
        print(f"\n{colors.consciousness_header('◆' * 70)}")
        print(f"{colors.consciousness_title('🧠 Consciousness-Aware Preset Browser')}")
        print(f"{colors.consciousness_header('◆' * 70)}")
        
        # Apply filters
        filtered_presets = self._apply_preset_filters(args)
        
        if not filtered_presets:
            print(f"\n{colors.gentle_text('No presets match your filters.')}")
            self._suggest_filter_adjustments()
            return 0
        
        # Display filtering information
        self._display_filter_summary(args, len(filtered_presets))
        
        # Group presets by category for display
        categorized_presets = self._categorize_presets(filtered_presets)
        
        # Display presets by category
        for category, presets in categorized_presets.items():
            self._display_preset_category(category, presets)
        
        # Show personalized recommendations
        if hasattr(args, 'recommendations') and args.recommendations:
            self._show_personalized_recommendations()
        
        # Interactive preset exploration
        return self._interactive_preset_explorer(filtered_presets)
    
    def _apply_preset_filters(self, args: argparse.Namespace) -> Dict[str, Any]:
        """Apply filters to preset collection based on arguments and neural profile."""
        
        presets = self.presets_data.get('consciousness_aware_presets', {})
        filtered = {}
        
        # Get neural profile for intelligent filtering
        neural_profile = self.entry_point.neural_profile
        user_sensitivity = neural_profile.get('sensitivity_level', 'standard')
        user_experience = neural_profile.get('experience_level', 'intermediate')
        
        for preset_name, preset_data in presets.items():
            include_preset = True
            
            # Category filter
            category_filter = getattr(args, 'category', None)
            if category_filter:
                preset_category = self._get_preset_category(preset_data)
                if preset_category != category_filter:
                    include_preset = False
            
            # Intention filter
            intention_filter = getattr(args, 'intention', None)
            if intention_filter:
                preset_intention = preset_data.get('consciousness_weaver', {}).get('intention', '')
                if preset_intention != intention_filter:
                    include_preset = False
            
            # Neural profile compatibility filter
            if include_preset:
                compatibility = self._check_preset_compatibility(preset_data, neural_profile)
                if compatibility['safety_rating'] == 'unsafe':
                    include_preset = False
                elif compatibility['safety_rating'] == 'caution' and user_sensitivity == 'sensitive':
                    include_preset = False
            
            # Experience level appropriateness
            if include_preset:
                preset_experience = self._get_preset_experience_requirement(preset_data)
                if not self._is_experience_appropriate(preset_experience, user_experience):
                    include_preset = False
            
            if include_preset:
                filtered[preset_name] = preset_data
        
        return filtered
    
    def _display_filter_summary(self, args: argparse.Namespace, count: int) -> None:
        """Display current filters and result count."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        # Show applied filters
        filters = []
        
        if hasattr(args, 'category') and args.category:
            category_info = PRESET_CATEGORIES.get(args.category, {})
            symbol = category_info.get('symbol', '○')
            name = category_info.get('name', args.category)
            filters.append(f"{symbol} {name}")
        
        if hasattr(args, 'intention') and args.intention:
            filters.append(f"✨ Intention: {args.intention.title()}")
        
        # Neural profile filtering info
        neural_profile = self.entry_point.neural_profile
        sensitivity = neural_profile.get('sensitivity_level', 'standard')
        experience = neural_profile.get('experience_level', 'intermediate')
        
        print(f"\n{colors.biofield_accent('🔍 Active Filters:')}")
        if filters:
            for f in filters:
                print(f"  • {colors.gentle_text(f)}")
        
        print(f"  • {colors.neural_profile(f'Neural Profile: {sensitivity.title()}, {experience.title()}')}")
        print(f"  • {colors.status_safe('✓ Safety Compatible Only')}")
        
        print(f"\n{colors.consciousness_accent(f'Found {count} suitable consciousness sessions:')}")
    
    def _categorize_presets(self, presets: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """Categorize presets for organized display."""
        
        categorized = {}
        
        for preset_name, preset_data in presets.items():
            category = self._get_preset_category(preset_data)
            
            if category not in categorized:
                categorized[category] = {}
            
            categorized[category][preset_name] = preset_data
        
        return categorized
    
    def _display_preset_category(self, category: str, presets: Dict[str, Any]) -> None:
        """Display a category of presets with beautiful formatting."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        # Get category information
        category_info = PRESET_CATEGORIES.get(category, {
            'name': category.title(),
            'symbol': '○',
            'description': 'Consciousness session category'
        })
        
        symbol = category_info['symbol']
        name = category_info['name']
        description = category_info['description']
        
        # Category header
        print(f"\n{colors.consciousness_header('─' * 60)}")
        print(f"{colors.consciousness_accent(f'{symbol} {name}')}")
        print(f"{colors.gentle_text(description)}")
        print(f"{colors.consciousness_header('─' * 60)}")
        
        # Display presets in this category
        for i, (preset_name, preset_data) in enumerate(presets.items(), 1):
            self._display_preset_summary(preset_name, preset_data, i)
    
    def _display_preset_summary(self, preset_name: str, preset_data: Dict[str, Any], index: int) -> None:
        """Display a concise preset summary."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        # Extract key information
        metadata = preset_data.get('metadata', {})
        description = metadata.get('description', 'Neural entrainment session')
        consciousness_journey = metadata.get('consciousness_journey', 'Standard progression')
        
        session_config = preset_data.get('session_config', {})
        total_duration = session_config.get('total_duration', 1800)
        
        consciousness_weaver = session_config.get('consciousness_weaver', {})
        intention = consciousness_weaver.get('intention', 'neutral')
        biofield_enabled = consciousness_weaver.get('biofield_intelligence', False)
        
        # Compatibility check
        neural_profile = self.entry_point.neural_profile
        compatibility = self._check_preset_compatibility(preset_data, neural_profile)
        safety_rating = compatibility['safety_rating']
        
        # Safety color and symbol
        safety_colors = {
            'safe': colors.status_safe,
            'caution': colors.status_caution,
            'unsafe': colors.status_danger
        }
        
        safety_symbols = {
            'safe': '✓',
            'caution': '⚠',
            'unsafe': '✗'
        }
        
        safety_color = safety_colors.get(safety_rating, colors.gentle_text)
        safety_symbol = safety_symbols.get(safety_rating, '○')
        
        # Display preset summary
        print(f"\n{colors.command_highlight(f'{index:2}.')} {colors.consciousness_accent(preset_name)}")
        print(f"    {colors.gentle_text(description)}")
        print(f"    {symbols.HOURGLASS} {colors.gentle_text(self._format_duration(total_duration))} | "
              f"{symbols.INFINITY} {colors.biofield_accent(intention.title())} | "
              f"{safety_color(safety_symbol)} {safety_color(safety_rating.title())}")
        
        if biofield_enabled:
            biofield_features = []
            if consciousness_weaver.get('schumann_alignment', 0) > 0:
                biofield_features.append('🌍 Schumann')
            if consciousness_weaver.get('solfeggio_integration', False):
                biofield_features.append('🎵 Solfeggio')
            if consciousness_weaver.get('golden_ratio_harmonics', False):
                biofield_features.append('Φ Golden Ratio')
            
            if biofield_features:
                features_text = ' | '.join(biofield_features)
                print(f"    {colors.biofield_accent('🌊 Biofield:')} {colors.gentle_text(features_text)}")
        
        # Consciousness journey preview
        if consciousness_journey != 'Standard progression':
            print(f"    {colors.consciousness_accent('✨ Journey:')} {colors.gentle_text(consciousness_journey)}")
    
    def _interactive_preset_explorer(self, presets: Dict[str, Any]) -> int:
        """Provide interactive preset exploration interface."""
        
        colors = self.color_scheme
        
        preset_list = list(presets.keys())
        
        print(f"\n{colors.consciousness_accent('Interactive Preset Explorer:')}")
        print(f"{colors.gentle_text('Enter preset number for details, or:')}")
        print(f"  {colors.command_highlight('q')} - Quit")
        print(f"  {colors.command_highlight('r')} - Get personalized recommendations")
        print(f"  {colors.command_highlight('f')} - Change filters")
        print(f"  {colors.command_highlight('h')} - Help")
        
        while True:
            try:
                choice = input(f"\n{colors.command_highlight('Your choice: ')}").strip().lower()
                
                if choice in ['q', 'quit', 'exit']:
                    print(f"{colors.gentle_text('Happy consciousness exploring! 🧠✨')}")
                    break
                elif choice in ['r', 'recommend']:
                    self._show_personalized_recommendations()
                elif choice in ['f', 'filter']:
                    self._interactive_filter_modification()
                elif choice in ['h', 'help']:
                    self._show_explorer_help()
                else:
                    # Try to parse as preset number
                    try:
                        preset_num = int(choice)
                        if 1 <= preset_num <= len(preset_list):
                            preset_name = preset_list[preset_num - 1]
                            self._show_detailed_preset_info(preset_name, presets[preset_name])
                        else:
                            print(f"{colors.gentle_text(f'Please enter a number between 1 and {len(preset_list)}')}")
                    except ValueError:
                        print(f"{colors.gentle_text('Invalid choice. Enter number, q, r, f, or h')}")
                        
            except KeyboardInterrupt:
                print(f"\n{colors.gentle_text('Explorer closed gently')}")
                break
        
        return 0
    
    def _show_detailed_preset_info(self, preset_name: str, preset_data: Dict[str, Any]) -> None:
        """Show detailed information about a specific preset."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_header('◆' * 60)}")
        print(f"{colors.consciousness_title(f'🧠 {preset_name} - Detailed Information')}")
        print(f"{colors.consciousness_header('◆' * 60)}")
        
        # Metadata section
        metadata = preset_data.get('metadata', {})
        description = metadata.get('description', 'Neural entrainment session')
        consciousness_journey = metadata.get('consciousness_journey', 'Standard progression')
        recommended_experience = metadata.get('recommended_experience', 'intermediate')
        
        print(f"\n{colors.biofield_accent('📋 Session Overview:')}")
        print(f"  Description: {colors.gentle_text(description)}")
        print(f"  Consciousness Journey: {colors.consciousness_accent(consciousness_journey)}")
        print(f"  Recommended Experience: {colors.neural_profile(recommended_experience.title())}")
        
        # Session configuration
        session_config = preset_data.get('session_config', {})
        total_duration = session_config.get('total_duration', 1800)
        integration_duration = session_config.get('integration_duration', 180)
        
        print(f"\n{colors.biofield_accent(f'{symbols.HOURGLASS} Duration & Timing:')}")
        print(f"  Total Duration: {colors.gentle_text(self._format_duration(total_duration))}")
        if session_config.get('include_integration', False):
            print(f"  Integration Time: {colors.gentle_text(self._format_duration(integration_duration))}")
        
        # Consciousness weaver settings
        consciousness_weaver = session_config.get('consciousness_weaver', {})
        intention = consciousness_weaver.get('intention', 'neutral')
        adaptation_strength = consciousness_weaver.get('adaptation_strength', 0.8)
        
        print(f"\n{colors.consciousness_accent(f'{symbols.INFINITY} Consciousness Settings:')}")
        print(f"  Primary Intention: {colors.biofield_accent(intention.title())}")
        print(f"  Adaptation Strength: {colors.gentle_text(f'{adaptation_strength:.1%}')}")
        
        # Biofield intelligence
        biofield_enabled = consciousness_weaver.get('biofield_intelligence', False)
        if biofield_enabled:
            print(f"\n{colors.biofield_accent('🌊 Biofield Intelligence:')}")
            
            schumann_alignment = consciousness_weaver.get('schumann_alignment', 0)
            if schumann_alignment > 0:
                print(f"  🌍 Schumann Resonance: {colors.schumann(f'{schumann_alignment:.1%} alignment')}")
            
            if consciousness_weaver.get('solfeggio_integration', False):
                print(f"  🎵 Solfeggio Frequencies: {colors.solfeggio('Integrated')}")
            
            if consciousness_weaver.get('golden_ratio_harmonics', False):
                print(f"  Φ Golden Ratio Harmonics: {colors.golden_ratio('Active')}")
            
            natural_frequency_boost = consciousness_weaver.get('natural_frequency_boost', 1.0)
            if natural_frequency_boost != 1.0:
                print(f"  🌿 Natural Frequency Boost: {colors.gentle_text(f'{natural_frequency_boost:.1f}x')}")
        
        # Phase analysis
        phases = preset_data.get('phases', [])
        if phases:
            print(f"\n{colors.consciousness_accent('✨ Consciousness Journey Phases:')}")
            
            phase_names = []
            for i, phase in enumerate(phases[:6]):  # Show first 6 phases
                phase_name = phase.get('name', f'Phase {i+1}')
                consciousness_target = phase.get('consciousness_target_state', 'transition')
                duration = phase.get('duration', 0)
                biofield_target = phase.get('biofield_coherence_target', 0.7)
                
                phase_names.append(consciousness_target)
                
                print(f"  {i+1:2}. {colors.gentle_text(phase_name)} "
                      f"({colors.gentle_text(self._format_duration(duration))}) "
                      f"→ {colors.get_consciousness_state_color(consciousness_target)(consciousness_target)} "
                      f"[{colors.biofield_accent(f'{biofield_target:.0%}')} coherence]")
            
            if len(phases) > 6:
                print(f"      ... and {len(phases) - 6} more phases")
            
            # Consciousness journey visualization
            journey_viz = self.consciousness_viz.create_consciousness_journey_line(
                phase_names[:5], 0, 55
            )
            print(f"\n{colors.gentle_text('Consciousness Journey Map:')}")
            for line in journey_viz:
                print(f"  {colors.gentle_text(line)}")
        
        # Safety and compatibility analysis
        neural_profile = self.entry_point.neural_profile
        compatibility = self._check_preset_compatibility(preset_data, neural_profile)
        
        print(f"\n{colors.safety_accent('🛡️ Safety & Compatibility Analysis:')}")
        
        safety_rating = compatibility['safety_rating']
        safety_color = {
            'safe': colors.status_safe,
            'caution': colors.status_caution, 
            'unsafe': colors.status_danger
        }.get(safety_rating, colors.gentle_text)
        
        print(f"  Safety Rating: {safety_color(safety_rating.title())}")
        
        if compatibility.get('warnings'):
            print(f"  Warnings:")
            for warning in compatibility['warnings']:
                print(f"    ⚠ {colors.status_caution(warning)}")
        
        if compatibility.get('recommendations'):
            print(f"  Recommendations:")
            for rec in compatibility['recommendations']:
                print(f"    💡 {colors.gentle_text(rec)}")
        
        # Action options
        print(f"\n{colors.consciousness_accent('Available Actions:')}")
        print(f"  • {colors.command_highlight('neural-cli session run ' + preset_name)} - Run this session")
        if compatibility['safety_rating'] != 'unsafe':
            print(f"  • {colors.command_highlight('neural-cli preset customize ' + preset_name)} - Customize parameters")
        print(f"  • Press Enter to return to preset browser")
        
        input(f"\n{colors.gentle_text('Press Enter to continue...')}")
    
    def _check_preset_compatibility(self, preset_data: Dict[str, Any], neural_profile: Dict[str, Any]) -> Dict[str, Any]:
        """Check preset compatibility with neural profile."""
        
        # This would integrate with the v2.0 validator for real compatibility checking
        # For now, provide simplified compatibility analysis
        
        compatibility = {
            'safety_rating': 'safe',
            'compatibility_score': 0.8,
            'warnings': [],
            'recommendations': []
        }
        
        sensitivity = neural_profile.get('sensitivity_level', 'standard')
        experience = neural_profile.get('experience_level', 'intermediate')
        
        # Check experience level requirements
        preset_experience = self._get_preset_experience_requirement(preset_data)
        
        experience_levels = ['beginner', 'intermediate', 'advanced', 'expert']
        user_exp_index = experience_levels.index(experience) if experience in experience_levels else 1
        preset_exp_index = experience_levels.index(preset_experience) if preset_experience in experience_levels else 1
        
        if preset_exp_index > user_exp_index + 1:
            compatibility['safety_rating'] = 'caution'
            compatibility['warnings'].append(f'This session is designed for {preset_experience} users')
            compatibility['recommendations'].append('Consider building more experience with simpler sessions first')
        
        # Check sensitivity compatibility
        if sensitivity == 'sensitive':
            session_config = preset_data.get('session_config', {})
            total_duration = session_config.get('total_duration', 1800)
            
            if total_duration > 2400:  # More than 40 minutes
                compatibility['safety_rating'] = 'caution'
                compatibility['warnings'].append('Long session duration for sensitive users')
                compatibility['recommendations'].append('Consider using gentle mode or shorter duration')
            
            # Check for complex biofield features
            consciousness_weaver = session_config.get('consciousness_weaver', {})
            adaptation_strength = consciousness_weaver.get('adaptation_strength', 0.8)
            
            if adaptation_strength > 0.9:
                compatibility['warnings'].append('High adaptation strength - monitor comfort closely')
        
        return compatibility
    
    def _get_preset_category(self, preset_data: Dict[str, Any]) -> str:
        """Determine preset category from preset data."""
        
        metadata = preset_data.get('metadata', {})
        
        # Try to get explicit category
        if 'category' in metadata:
            return metadata['category']
        
        # Infer from intention
        session_config = preset_data.get('session_config', {})
        consciousness_weaver = session_config.get('consciousness_weaver', {})
        intention = consciousness_weaver.get('intention', '').lower()
        
        # Map intentions to categories
        intention_to_category = {
            'focus': 'focus',
            'release': 'relaxation',
            'heal': 'healing',
            'create': 'creativity',
            'transcend': 'consciousness',
            'integrate': 'meditation',
            'energize': 'energy',
            'calm': 'relaxation'
        }
        
        return intention_to_category.get(intention, 'meditation')
    
    def _get_preset_experience_requirement(self, preset_data: Dict[str, Any]) -> str:
        """Determine experience requirement for preset."""
        
        metadata = preset_data.get('metadata', {})
        return metadata.get('recommended_experience', 'intermediate')
    
    def _is_experience_appropriate(self, required_experience: str, user_experience: str) -> bool:
        """Check if user experience level is appropriate for preset."""
        
        experience_levels = ['beginner', 'intermediate', 'advanced', 'expert']
        
        try:
            required_index = experience_levels.index(required_experience)
            user_index = experience_levels.index(user_experience)
            
            # Allow same level or higher, or one level below for advanced users
            return user_index >= required_index or (user_index >= required_index - 1 and user_index >= 1)
            
        except ValueError:
            return True  # If levels don't match standard categories, allow
    
    def _show_personalized_recommendations(self) -> None:
        """Show personalized preset recommendations based on neural profile."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_header('◆' * 60)}")
        print(f"{colors.consciousness_title('🎯 Personalized Recommendations')}")
        print(f"{colors.consciousness_header('◆' * 60)}")
        
        neural_profile = self.entry_point.neural_profile
        sensitivity = neural_profile.get('sensitivity_level', 'standard')
        experience = neural_profile.get('experience_level', 'intermediate')
        current_state = neural_profile.get('current_state', 'neutral')
        
        print(f"\n{colors.biofield_accent('Based on your neural profile:')}")
        print(f"  Sensitivity: {colors.neural_profile(sensitivity.title())}")
        print(f"  Experience: {colors.neural_profile(experience.title())}")
        print(f"  Current State: {colors.consciousness_accent(current_state.title())}")
        
        # Generate personalized recommendations
        recommendations = self._generate_personalized_recommendations(neural_profile)
        
        print(f"\n{colors.consciousness_accent('🌟 Recommended Sessions:')}")
        for i, rec in enumerate(recommendations[:5], 1):
            preset_name = rec['name']
            reason = rec['reason']
            match_score = rec['score']
            
            print(f"  {i}. {colors.consciousness_accent(preset_name)}")
            print(f"     {colors.gentle_text(reason)} {colors.biofield_accent(f'({match_score:.0%} match)')}")
    
    def _generate_personalized_recommendations(self, neural_profile: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate personalized preset recommendations."""
        
        recommendations = []
        presets = self.presets_data.get('consciousness_aware_presets', {})
        
        for preset_name, preset_data in presets.items():
            score = self._calculate_preset_match_score(preset_data, neural_profile)
            reason = self._generate_recommendation_reason(preset_data, neural_profile)
            
            recommendations.append({
                'name': preset_name,
                'score': score,
                'reason': reason,
                'data': preset_data
            })
        
        # Sort by score and return top recommendations
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        return recommendations[:10]
    
    def _calculate_preset_match_score(self, preset_data: Dict[str, Any], neural_profile: Dict[str, Any]) -> float:
        """Calculate how well a preset matches a neural profile."""
        
        score = 0.5  # Base score
        
        # Experience level compatibility
        preset_experience = self._get_preset_experience_requirement(preset_data)
        user_experience = neural_profile.get('experience_level', 'intermediate')
        
        if self._is_experience_appropriate(preset_experience, user_experience):
            score += 0.2
        
        # Sensitivity compatibility
        sensitivity = neural_profile.get('sensitivity_level', 'standard')
        compatibility = self._check_preset_compatibility(preset_data, neural_profile)
        
        if compatibility['safety_rating'] == 'safe':
            score += 0.2
        elif compatibility['safety_rating'] == 'caution':
            score += 0.1
        
        # Duration appropriateness
        session_config = preset_data.get('session_config', {})
        total_duration = session_config.get('total_duration', 1800)
        
        if sensitivity == 'sensitive' and total_duration <= 1800:
            score += 0.1
        elif sensitivity == 'resilient' and total_duration >= 1800:
            score += 0.1
        
        return min(1.0, score)
    
    def _generate_recommendation_reason(self, preset_data: Dict[str, Any], neural_profile: Dict[str, Any]) -> str:
        """Generate explanation for why a preset is recommended."""
        
        reasons = []
        
        sensitivity = neural_profile.get('sensitivity_level', 'standard')
        experience = neural_profile.get('experience_level', 'intermediate')
        
        # Experience match
        preset_experience = self._get_preset_experience_requirement(preset_data)
        if preset_experience == experience:
            reasons.append(f"Perfect match for {experience} level")
        
        # Sensitivity considerations
        if sensitivity == 'sensitive':
            session_config = preset_data.get('session_config', {})
            if session_config.get('gentle_mode', False):
                reasons.append("includes gentle mode")
            
            total_duration = session_config.get('total_duration', 1800)
            if total_duration <= 1800:
                reasons.append("appropriate duration for sensitive users")
        
        # Biofield features
        consciousness_weaver = preset_data.get('session_config', {}).get('consciousness_weaver', {})
        if consciousness_weaver.get('biofield_intelligence', False):
            reasons.append("enhanced with biofield intelligence")
        
        if not reasons:
            reasons.append("well-suited for your profile")
        
        return " • ".join(reasons[:2])  # Limit to 2 reasons for brevity
    
    def _format_duration(self, seconds: int) -> str:
        """Format duration in human-readable format."""
        
        if seconds < 60:
            return f"{seconds}s"
        elif seconds < 3600:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            if remaining_seconds == 0:
                return f"{minutes}m"
            else:
                return f"{minutes}m {remaining_seconds}s"
        else:
            hours = seconds // 3600
            remaining_minutes = (seconds % 3600) // 60
            return f"{hours}h {remaining_minutes}m"
    
    def _load_presets_data(self) -> Dict[str, Any]:
        """Load preset data from configuration files."""
        
        try:
            presets_file = DEFAULT_PRESETS_DIR / "presets.json"
            
            if presets_file.exists():
                with open(presets_file, 'r') as f:
                    return json.load(f)
                    
        except Exception as e:
            logging.error(f"Failed to load presets data: {e}")
        
        return {'consciousness_aware_presets': {}}
    
    # Placeholder methods for remaining functionality
    def _show_preset_details(self, args: argparse.Namespace) -> int:
        """Show detailed preset information."""
        preset_name = getattr(args, 'preset_name', '')
        presets = self.presets_data.get('consciousness_aware_presets', {})
        
        if preset_name in presets:
            self._show_detailed_preset_info(preset_name, presets[preset_name])
            return 0
        else:
            self._display_error(f"Preset '{preset_name}' not found")
            return 1
    
    def _customize_preset(self, args: argparse.Namespace) -> int:
        """Customize existing preset."""
        print("🛠️ Preset customization functionality coming soon...")
        return 0
    
    def _create_custom_preset(self, args: argparse.Namespace) -> int:
        """Create custom preset."""
        print("🎨 Custom preset creation functionality coming soon...")
        return 0
    
    def _recommend_presets(self, args: argparse.Namespace) -> int:
        """Recommend presets based on neural profile."""
        self._show_personalized_recommendations()
        return 0
    
    def _search_presets(self, args: argparse.Namespace) -> int:
        """Search presets by keywords."""
        print("🔍 Preset search functionality coming soon...")
        return 0
    
    def _show_preset_help(self) -> int:
        """Show preset command help."""
        print("🎛️ Preset Help:")
        print("  browse               - Browse available presets")
        print("  browse --category <c> - Browse by category")
        print("  browse --intention <i> - Browse by intention")
        print("  show <preset>        - Show preset details")
        print("  customize <preset>   - Customize preset")
        print("  create               - Create custom preset")
        print("  recommend            - Get personalized recommendations")
        print("  search <keywords>    - Search presets")
        return 0
    
    def _display_error(self, message: str) -> None:
        """Display error message."""
        print(f"\n{self.color_scheme.error_symbol()} {self.color_scheme.error_text(message)}")

# Additional helper methods would continue here...