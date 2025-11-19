# 🧪 Neural Entrainment System - Consciousness Journey Visualizer v2.0
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠 Consciousness-Aware Biofield Intelligence Framework
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Consciousness Journey Visualizer - Advanced visualization engine for consciousness-aware sessions.

This module provides comprehensive visualization capabilities for neural entrainment sessions,
including consciousness journey mapping, biofield coherence analysis, neural architecture
monitoring, safety protocol visualization, and real-time session monitoring. All visualizations
respect neural architecture sensitivity and provide consciousness-appropriate feedback.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.gridspec import GridSpec
import seaborn as sns
import logging
import warnings
import datetime
import os
import copy
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple, Union
from dataclasses import dataclass, field
from scipy.signal import spectrogram, coherence, welch
from scipy.interpolate import interp1d

# Optional colorcet import with fallback
try:
    import colorcet as cc
    COLORCET_AVAILABLE = True
except ImportError:
    logging.warning("colorcet not available - using matplotlib fallback colormaps")
    COLORCET_AVAILABLE = False

# Suppress specific matplotlib warnings for cleaner output
warnings.filterwarnings('ignore', message='This figure includes Axes that are not compatible with tight_layout')
warnings.filterwarnings('ignore', message='Creating legend with loc="best" can be slow with large amounts of data')
warnings.filterwarnings('ignore', message='tight_layout not applied')

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS VISUALIZATION CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Consciousness state visualization mapping with enhanced aesthetics
CONSCIOUSNESS_STATE_VISUALS = {
    'deep_delta': {
        'color': '#0B0B2F',          # Deep indigo
        'gradient_colors': ['#0B0B2F', '#1A1A4D'],
        'symbol': '●',
        'y_position': 0.0,
        'frequency_range': (0.1, 2.0),
        'label': 'Deep Delta (0.1-2Hz)',
        'description': 'Profound healing & regeneration',
        'alpha': 0.9,
        'glow_intensity': 0.7
    },
    'delta': {
        'color': '#1E3A8A',          # Deep blue
        'gradient_colors': ['#1E3A8A', '#2563EB'],
        'symbol': '●',
        'y_position': 1.0,
        'frequency_range': (1.0, 4.0),
        'label': 'Delta (1-4Hz)',
        'description': 'Deep sleep & restoration',
        'alpha': 0.9,
        'glow_intensity': 0.6
    },
    'theta': {
        'color': '#059669',          # Emerald green
        'gradient_colors': ['#059669', '#10B981'],
        'symbol': 'D',               # Diamond (standard matplotlib)
        'y_position': 2.0,
        'frequency_range': (4.0, 8.0),
        'label': 'Theta (4-8Hz)',
        'description': 'Imagery & deep meditation',
        'alpha': 0.9,
        'glow_intensity': 0.8
    },
    'alpha': {
        'color': '#D97706',          # Amber
        'gradient_colors': ['#D97706', '#F59E0B'],
        'symbol': '^',               # Triangle up (standard matplotlib)
        'y_position': 3.0,
        'frequency_range': (8.0, 13.0),
        'label': 'Alpha (8-13Hz)',
        'description': 'Relaxed awareness & bridge state',
        'alpha': 0.9,
        'glow_intensity': 0.7
    },
    'beta': {
        'color': '#DC2626',          # Red
        'gradient_colors': ['#DC2626', '#EF4444'],
        'symbol': 's',               # Square (standard matplotlib)
        'y_position': 4.0,
        'frequency_range': (13.0, 30.0),
        'label': 'Beta (13-30Hz)',
        'description': 'Alert focus & cognitive activity',
        'alpha': 0.9,
        'glow_intensity': 0.6
    },
    'gamma': {
        'color': '#7C3AED',          # Purple
        'gradient_colors': ['#7C3AED', '#A855F7'],
        'symbol': '*',               # Star (standard matplotlib)
        'y_position': 5.0,
        'frequency_range': (30.0, 80.0),
        'label': 'Gamma (30-80Hz)',
        'description': 'Expanded awareness & insights',
        'alpha': 0.9,
        'glow_intensity': 0.9
    },
    'high_gamma': {
        'color': '#EC4899',          # Fuchsia
        'gradient_colors': ['#EC4899', '#F472B6'],
        'symbol': 'P',               # Plus (filled) (standard matplotlib)
        'y_position': 6.0,
        'frequency_range': (80.0, 200.0),
        'label': 'High Gamma (80-200Hz)',
        'description': 'Transcendent consciousness',
        'alpha': 0.9,
        'glow_intensity': 1.0
    },
    'integration': {
        'color': '#8B5CF6',          # Violet
        'gradient_colors': ['#8B5CF6', '#A78BFA'],
        'symbol': 'o',               # Circle (standard matplotlib)
        'y_position': 3.5,
        'frequency_range': (5.0, 15.0),
        'label': 'Integration',
        'description': 'Consciousness synthesis & grounding',
        'alpha': 0.9,
        'glow_intensity': 0.8
    }
}

# Neural sensitivity visualization profiles
NEURAL_SENSITIVITY_VISUALS = {
    'sensitive': {
        'color': '#F87171',          # Light red
        'line_style': '--',
        'marker_size': 8,
        'alpha': 0.7,
        'label': 'Sensitive Profile'
    },
    'standard': {
        'color': '#60A5FA',          # Light blue
        'line_style': '-',
        'marker_size': 6,
        'alpha': 0.8,
        'label': 'Standard Profile'
    },
    'resilient': {
        'color': '#34D399',          # Light green
        'line_style': '-.',
        'marker_size': 4,
        'alpha': 0.9,
        'label': 'Resilient Profile'
    }
}

# Biofield frequency visualization constants
BIOFIELD_FREQUENCY_VISUALS = {
    'schumann_resonances': {
        'frequencies': [7.83, 14.3, 20.8, 27.3, 33.8, 39.3, 45.9, 52.8],
        'color': '#22C55E',          # Green
        'marker': 'o',
        'size': 100,
        'alpha': 0.7,
        'label': 'Schumann Resonances'
    },
    'solfeggio_frequencies': {
        'frequencies': [174, 285, 396, 417, 528, 639, 741, 852, 963],
        'color': '#3B82F6',          # Blue
        'marker': 's',
        'size': 80,
        'alpha': 0.7,
        'label': 'Solfeggio Frequencies'
    },
    'healing_frequencies': {
        'frequencies': [528, 432, 396, 417, 852],
        'color': '#F59E0B',          # Amber
        'marker': '^',
        'size': 120,
        'alpha': 0.8,
        'label': 'Primary Healing Frequencies'
    }
}

# Safety level visualization mapping
SAFETY_LEVEL_VISUALS = {
    'safe': {'color': '#22C55E', 'alpha': 0.8, 'label': 'Safe'},
    'caution': {'color': '#F59E0B', 'alpha': 0.8, 'label': 'Caution'},
    'warning': {'color': '#EF4444', 'alpha': 0.8, 'label': 'Warning'},
    'unsafe': {'color': '#DC2626', 'alpha': 0.9, 'label': 'Unsafe'},
    'critical': {'color': '#7F1D1D', 'alpha': 1.0, 'label': 'Critical'}
}

# Intention visualization profiles
INTENTION_VISUALS = {
    'neutral': {'color': '#6B7280', 'gradient': ['#6B7280', '#9CA3AF']},
    'release': {'color': '#059669', 'gradient': ['#059669', '#34D399']},
    'focus': {'color': '#DC2626', 'gradient': ['#DC2626', '#F87171']},
    'integrate': {'color': '#7C3AED', 'gradient': ['#7C3AED', '#C084FC']},
    'creativity': {'color': '#D97706', 'gradient': ['#D97706', '#FBBF24']}
}

# Create custom colormaps for enhanced visualization
def create_consciousness_colormap():
    """Create a custom colormap for consciousness state visualization."""
    colors = ['#0B0B2F', '#1E3A8A', '#059669', '#D97706', '#DC2626', '#7C3AED', '#EC4899']
    return LinearSegmentedColormap.from_list('consciousness', colors, N=256)

def create_biofield_colormap():
    """Create a custom colormap for biofield coherence visualization."""
    colors = ['#1F2937', '#3B82F6', '#10B981', '#F59E0B', '#EF4444']
    return LinearSegmentedColormap.from_list('biofield', colors, N=256)

# Custom matplotlib style for consciousness visualizations
try:
    plt.style.use('seaborn-v0_8-darkgrid')
except:
    try:
        plt.style.use('seaborn-darkgrid')
    except:
        logging.warning("Seaborn style not available, using default matplotlib style")

@dataclass
class VisualizationConfig:
    """Configuration for consciousness visualization parameters."""
    figure_size: Tuple[int, int] = (16, 12)
    dpi: int = 150
    color_theme: str = 'consciousness_aware'
    animation_enabled: bool = True
    real_time_updates: bool = True
    safety_overlay: bool = True
    biofield_analysis: bool = True
    neural_profile_adaptation: bool = True
    output_dir: str = 'output'  # Configurable output directory
    save_figures: bool = True   # Option to disable auto-saving

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ADVANCED CONSCIOUSNESS JOURNEY VISUALIZATION
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def plot_consciousness_journey_3D(metadata: Dict[str, Any], 
                                 neural_profile: Optional[Dict[str, Any]] = None,
                                 config: VisualizationConfig = VisualizationConfig()) -> plt.Figure:
    """
    Create an advanced 3D consciousness journey visualization with biofield intelligence.
    
    Args:
        metadata: Complete session metadata with consciousness analysis
        neural_profile: Neural profile for adaptation
        config: Visualization configuration
        
    Returns:
        Interactive 3D matplotlib figure with consciousness journey mapping
    """
    # Set up 3D figure with consciousness-aware styling
    fig = plt.figure(figsize=config.figure_size, dpi=config.dpi)
    fig.patch.set_facecolor('#0F0F23')  # Deep space background
    
    # Create 3D subplot
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('#1A1A2E')
    
    # Extract consciousness analysis data
    consciousness_analysis = metadata.get('consciousness_analysis', {})
    biofield_analysis = metadata.get('biofield_analysis', {})
    phases = metadata.get('phases', [])
    
    if not phases:
        ax.text(0.5, 0.5, 0.5, 'No consciousness journey data available', 
               transform=ax.transAxes, ha='center', va='center', fontsize=14, color='white')
        return fig
    
    # Extract journey data
    state_sequence = consciousness_analysis.get('state_sequence', [])
    transition_quality = consciousness_analysis.get('transition_quality_timeline', [])
    biofield_alignment = consciousness_analysis.get('biofield_alignment_timeline', [])
    coherence_progression = consciousness_analysis.get('coherence_progression', [])
    
    # Neural profile adaptation
    if neural_profile:
        sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
        experience_level = neural_profile.get('experience_level', 'intermediate')
    else:
        sensitivity_level = 'standard'
        experience_level = 'intermediate'
    
    # Time axis
    phase_durations = [phase.get('duration', 0) for phase in phases]
    cumulative_times = np.cumsum([0] + phase_durations[:-1])
    total_duration = sum(phase_durations)
    
    # Create detailed time points for smooth curves
    detailed_times = []
    detailed_states = []
    detailed_coherence = []
    detailed_biofield = []
    detailed_quality = []
    
    for i, (phase, state) in enumerate(zip(phases, state_sequence)):
        duration = phase.get('duration', 0)
        start_time = cumulative_times[i] if i < len(cumulative_times) else 0
        
        # Create time points within phase
        phase_times = np.linspace(start_time, start_time + duration, max(10, duration // 30))
        detailed_times.extend(phase_times)
        
        # Map consciousness state to numerical value
        state_visual = CONSCIOUSNESS_STATE_VISUALS.get(state, CONSCIOUSNESS_STATE_VISUALS['alpha'])
        state_y = state_visual['y_position']
        detailed_states.extend([state_y] * len(phase_times))
        
        # Interpolate metrics
        coherence_val = coherence_progression[i] if i < len(coherence_progression) else 0.7
        biofield_val = biofield_alignment[i] if i < len(biofield_alignment) else 0.7
        quality_val = transition_quality[i] if i < len(transition_quality) else 0.7
        
        detailed_coherence.extend([coherence_val] * len(phase_times))
        detailed_biofield.extend([biofield_val] * len(phase_times))
        detailed_quality.extend([quality_val] * len(phase_times))
    
    # Convert to arrays for processing
    x_times = np.array(detailed_times) / 60  # Convert to minutes
    y_states = np.array(detailed_states)
    z_coherence = np.array(detailed_coherence)
    biofield_values = np.array(detailed_biofield)
    quality_values = np.array(detailed_quality)
    
    # Create consciousness journey trajectory
    consciousness_cmap = create_consciousness_colormap()
    
    # Plot main consciousness trajectory
    scatter = ax.scatter(x_times, y_states, z_coherence, 
                        c=biofield_values, cmap='viridis', 
                        s=50 + quality_values * 100,  # Size varies with transition quality
                        alpha=0.7, edgecolors='white', linewidths=0.5)
    
    # Add consciousness state transition lines
    ax.plot(x_times, y_states, z_coherence, color='white', alpha=0.6, linewidth=2, linestyle='-')
    
    # Mark phase boundaries
    for i, (phase, state) in enumerate(zip(phases, state_sequence)):
        start_time = cumulative_times[i] / 60 if i < len(cumulative_times) else 0
        state_visual = CONSCIOUSNESS_STATE_VISUALS.get(state, CONSCIOUSNESS_STATE_VISUALS['alpha'])
        y_pos = state_visual['y_position']
        coherence_val = coherence_progression[i] if i < len(coherence_progression) else 0.7
        
        # Phase marker
        ax.scatter([start_time], [y_pos], [coherence_val], 
                  color=state_visual['color'], s=200, 
                  marker=state_visual['symbol'], alpha=0.9,
                  edgecolors='white', linewidths=2)
        
        # Phase label
        if experience_level in ['advanced', 'expert']:  # Detailed labels for experienced users
            phase_label = f"P{i+1}: {state.title()}"
            ax.text(start_time, y_pos, coherence_val + 0.1, phase_label, 
                   fontsize=8, color='white', alpha=0.8)
    
    # Add integration windows
    integration_windows = consciousness_analysis.get('integration_windows', [])
    for window in integration_windows:
        start_time = window.get('start_time', 0) / 60
        end_time = window.get('end_time', 0) / 60
        # Create integration window visualization
        window_x = np.linspace(start_time, end_time, 10)
        window_y = np.full_like(window_x, 3.5)  # Integration level
        window_z = np.full_like(window_x, 0.9)  # High coherence
        
        ax.plot(window_x, window_y, window_z, color='violet', linewidth=4, alpha=0.6)
        ax.text(np.mean(window_x), 3.5, 0.95, 'Integration', 
               fontsize=9, color='violet', alpha=0.8, ha='center')
    
    # Neural sensitivity adaptation overlay
    if config.neural_profile_adaptation:
        sensitivity_visual = NEURAL_SENSITIVITY_VISUALS[sensitivity_level]
        # Add sensitivity boundary
        ax.plot([0, total_duration/60], [0, 0], [0.3, 0.3], 
               color=sensitivity_visual['color'], 
               linestyle=sensitivity_visual['line_style'],
               linewidth=3, alpha=0.7, 
               label=f'Safety Threshold ({sensitivity_level})')
    
    # Biofield frequency markers
    if config.biofield_analysis:
        # Mark significant biofield moments
        biofield_metrics = biofield_analysis.get('coherence_metrics', {})
        schumann_alignment = biofield_metrics.get('schumann_alignment', 0)
        solfeggio_presence = biofield_metrics.get('solfeggio_presence', 0)
        
        if schumann_alignment > 0.5:
            # Add Schumann resonance indicator
            mid_time = total_duration / 2 / 60
            ax.scatter([mid_time], [1.0], [schumann_alignment], 
                      color='green', s=300, marker='o', alpha=0.7,
                      label='Schumann Alignment')
        
        if solfeggio_presence > 0.3:
            # Add Solfeggio frequency indicator  
            mid_time = total_duration / 2 / 60
            ax.scatter([mid_time], [2.0], [solfeggio_presence], 
                      color='blue', s=300, marker='s', alpha=0.7,
                      label='Solfeggio Presence')
    
    # Customize 3D axes
    ax.set_xlabel('Time (minutes)', fontsize=12, color='white')
    ax.set_ylabel('Consciousness State', fontsize=12, color='white')
    ax.set_zlabel('Coherence Level', fontsize=12, color='white')
    
    # Set consciousness state labels
    state_positions = [visual['y_position'] for visual in CONSCIOUSNESS_STATE_VISUALS.values()]
    state_labels = [visual['label'] for visual in CONSCIOUSNESS_STATE_VISUALS.values()]
    ax.set_yticks(state_positions)
    ax.set_yticklabels(state_labels, fontsize=9, color='white')
    
    # Coherence level formatting
    ax.set_zlim(0, 1)
    ax.set_zticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.set_zticklabels(['0%', '25%', '50%', '75%', '100%'], color='white')
    
    # Styling
    ax.tick_params(colors='white', labelsize=9)
    ax.grid(True, alpha=0.3)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    
    # Title with consciousness journey quality
    journey_quality = consciousness_analysis.get('journey_quality_rating', 'unknown')
    overall_coherence = biofield_analysis.get('coherence_metrics', {}).get('overall_coherence', 0)
    
    title = f"Consciousness Journey Visualization\n"
    title += f"Quality: {journey_quality.title()} | "
    title += f"Biofield Coherence: {overall_coherence:.2f} | "
    title += f"Neural Profile: {sensitivity_level.title()}"
    
    ax.set_title(title, fontsize=14, color='white', pad=20)
    
    # Add colorbar for biofield alignment
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.5, aspect=20, pad=0.1)
    cbar.set_label('Biofield Alignment', fontsize=10, color='white')
    cbar.ax.tick_params(colors='white', labelsize=8)
    
    # Legend
    if config.neural_profile_adaptation or config.biofield_analysis:
        legend = ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98), 
                          fontsize=9, framealpha=0.8)
        legend.get_frame().set_facecolor('#1A1A2E')
        for text in legend.get_texts():
            text.set_color('white')
    
    # Save high-quality version
    plt.tight_layout()
    
    return fig

def plot_neural_architecture_dashboard(neural_profile: Dict[str, Any], 
                                     session_data: Optional[Dict[str, Any]] = None,
                                     config: VisualizationConfig = VisualizationConfig()) -> plt.Figure:
    """
    Create a comprehensive neural architecture compatibility dashboard.
    
    Args:
        neural_profile: Neural profile data
        session_data: Optional session data for analysis
        config: Visualization configuration
        
    Returns:
        Neural architecture dashboard figure
    """
    # Create dashboard layout
    fig = plt.figure(figsize=config.figure_size, dpi=config.dpi)
    fig.patch.set_facecolor('#0F0F23')
    
    # Create grid layout for dashboard
    gs = GridSpec(3, 4, figure=fig, hspace=0.4, wspace=0.3)
    
    # Extract neural profile data
    sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
    current_state = neural_profile.get('current_state', 'neutral')
    experience_level = neural_profile.get('experience_level', 'intermediate')
    integration_capacity = neural_profile.get('integration_capacity', 5)
    custom_factors = neural_profile.get('custom_factors', {})
    
    # 1. Neural Profile Overview (Radar Chart)
    ax1 = fig.add_subplot(gs[0, :2], projection='polar')
    ax1.set_facecolor('#1A1A2E')
    
    # Define neural profile metrics
    metrics = ['Sensitivity', 'Processing Speed', 'Integration Capacity', 
              'Noise Tolerance', 'Transition Smoothing', 'Duration Extension']
    
    # Map profile to values (0-1 scale)
    sensitivity_map = {'sensitive': 0.8, 'standard': 0.5, 'resilient': 0.3}
    experience_map = {'beginner': 0.3, 'intermediate': 0.6, 'advanced': 0.8, 'expert': 1.0}
    
    values = [
        sensitivity_map.get(sensitivity_level, 0.5),  # Sensitivity
        experience_map.get(experience_level, 0.6),    # Processing Speed
        min(1.0, integration_capacity / 10),          # Integration Capacity
        1.0 - sensitivity_map.get(sensitivity_level, 0.5),  # Noise Tolerance
        0.8 if experience_level in ['advanced', 'expert'] else 0.5,  # Transition Smoothing
        experience_map.get(experience_level, 0.6)     # Duration Extension
    ]
    
    # Add custom factors
    for factor, value in custom_factors.items():
        if len(metrics) < 8:  # Limit to 8 metrics for clarity
            metrics.append(factor.replace('_', ' ').title())
            values.append(min(1.0, max(0.0, value / 2)))  # Normalize custom factors
    
    # Create radar chart
    angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False)
    values = np.array(values)
    
    # Close the plot
    angles = np.concatenate((angles, [angles[0]]))
    values = np.concatenate((values, [values[0]]))
    
    # Plot radar chart
    sensitivity_color = NEURAL_SENSITIVITY_VISUALS[sensitivity_level]['color']
    ax1.plot(angles, values, color=sensitivity_color, linewidth=3, alpha=0.8)
    ax1.fill(angles, values, color=sensitivity_color, alpha=0.3)
    
    # Customize radar chart
    ax1.set_xticks(angles[:-1])
    ax1.set_xticklabels(metrics, fontsize=10, color='white')
    ax1.set_ylim(0, 1)
    ax1.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax1.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], 
                       fontsize=9, color='white', alpha=0.7)
    ax1.grid(True, alpha=0.3)
    ax1.set_title(f'Neural Profile: {sensitivity_level.title()}', 
                 fontsize=12, color='white', pad=20)
    
    # 2. Processing Load Utilization
    ax2 = fig.add_subplot(gs[0, 2:])
    ax2.set_facecolor('#1A1A2E')
    
    if session_data and 'neural_load_assessment' in session_data.get('consciousness_analysis', {}):
        load_data = session_data['consciousness_analysis']['neural_load_assessment']
        total_load = load_data.get('total_load', 0)
        load_limit = load_data.get('load_limit', 10)
        utilization = load_data.get('utilization', 0)
        
        # Create utilization gauge
        theta = np.linspace(0, np.pi, 100)
        gauge_x = np.cos(theta)
        gauge_y = np.sin(theta)
        
        # Background gauge
        ax2.fill_between(gauge_x, 0, gauge_y, alpha=0.2, color='gray')
        
        # Utilization fill
        util_theta = theta[theta <= np.pi * utilization]
        util_x = np.cos(util_theta)
        util_y = np.sin(util_theta)
        
        # Color based on utilization level
        if utilization < 0.7:
            color = '#22C55E'  # Green - safe
        elif utilization < 0.9:
            color = '#F59E0B'  # Amber - caution
        else:
            color = '#EF4444'  # Red - warning
        
        ax2.fill_between(util_x, 0, util_y, alpha=0.8, color=color)
        
        # Utilization text
        ax2.text(0, 0.5, f'{utilization:.1%}\nUtilization', 
                ha='center', va='center', fontsize=12, color='white', weight='bold')
        
        # Load values
        ax2.text(0, -0.2, f'Load: {total_load:.1f} / {load_limit:.1f}', 
                ha='center', va='center', fontsize=10, color='white', alpha=0.8)
        
    else:
        ax2.text(0, 0.5, 'No Load Data\nAvailable', 
                ha='center', va='center', fontsize=12, color='white', alpha=0.6)
    
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-0.3, 1.2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Neural Load Utilization', fontsize=12, color='white')
    
    # 3. Consciousness State Compatibility Matrix
    ax3 = fig.add_subplot(gs[1, :2])
    ax3.set_facecolor('#1A1A2E')
    
    # Define consciousness states and compatibility
    states = ['deep_delta', 'delta', 'theta', 'alpha', 'beta', 'gamma', 'high_gamma']
    
    # Create compatibility matrix based on experience and sensitivity
    compatibility_matrix = np.zeros((len(states), 1))
    
    for i, state in enumerate(states):
        base_compatibility = 0.5
        
        # Experience level adjustments
        if experience_level == 'beginner':
            if state in ['alpha', 'beta', 'theta']:
                base_compatibility = 0.9
            elif state in ['delta', 'gamma']:
                base_compatibility = 0.6
            else:
                base_compatibility = 0.2
        elif experience_level == 'intermediate':
            if state in ['alpha', 'beta', 'theta', 'delta', 'gamma']:
                base_compatibility = 0.8
            else:
                base_compatibility = 0.4
        elif experience_level in ['advanced', 'expert']:
            base_compatibility = 0.9 if state != 'high_gamma' else 0.7
        
        # Sensitivity adjustments
        if sensitivity_level == 'sensitive':
            if state in ['gamma', 'high_gamma']:
                base_compatibility *= 0.6
            elif state == 'deep_delta':
                base_compatibility *= 0.8
        elif sensitivity_level == 'resilient':
            base_compatibility = min(1.0, base_compatibility * 1.2)
        
        compatibility_matrix[i, 0] = base_compatibility
    
    # Create heatmap
    im = ax3.imshow(compatibility_matrix, cmap='RdYlGn', aspect='auto', vmin=0, vmax=1)
    
    # Set state labels
    state_labels = [CONSCIOUSNESS_STATE_VISUALS[state]['label'] for state in states]
    ax3.set_yticks(range(len(states)))
    ax3.set_yticklabels(state_labels, fontsize=9, color='white')
    ax3.set_xticks([0])
    ax3.set_xticklabels(['Compatibility'], fontsize=10, color='white')
    
    # Add compatibility values
    for i in range(len(states)):
        text = ax3.text(0, i, f'{compatibility_matrix[i, 0]:.2f}', 
                       ha='center', va='center', color='black', weight='bold')
    
    ax3.set_title('State Compatibility', fontsize=12, color='white')
    
    # 4. Experience Level Progression
    ax4 = fig.add_subplot(gs[1, 2:])
    ax4.set_facecolor('#1A1A2E')
    
    # Experience progression visualization
    levels = ['Beginner', 'Intermediate', 'Advanced', 'Expert']
    current_index = levels.index(experience_level.title()) if experience_level.title() in levels else 1
    
    # Create progression bar
    for i, level in enumerate(levels):
        if i <= current_index:
            color = '#22C55E'  # Completed levels
            alpha = 0.8
        else:
            color = '#374151'  # Uncompleted levels
            alpha = 0.4
        
        rect = patches.Rectangle((i, 0), 0.8, 1, linewidth=2, 
                               edgecolor='white', facecolor=color, alpha=alpha)
        ax4.add_patch(rect)
        
        # Level label
        ax4.text(i + 0.4, 0.5, level, ha='center', va='center', 
                fontsize=10, color='white', weight='bold')
    
    # Current level indicator
    arrow = patches.FancyArrowPatch((current_index + 0.4, -0.2), (current_index + 0.4, 0),
                                   arrowstyle='->', color='yellow', linewidth=3)
    ax4.add_patch(arrow)
    ax4.text(current_index + 0.4, -0.4, 'Current', ha='center', va='center',
            fontsize=9, color='yellow', weight='bold')
    
    ax4.set_xlim(-0.2, len(levels) - 0.2)
    ax4.set_ylim(-0.5, 1.2)
    ax4.set_aspect('equal')
    ax4.axis('off')
    ax4.set_title('Experience Progression', fontsize=12, color='white')
    
    # 5. Current State Analysis
    ax5 = fig.add_subplot(gs[2, :2])
    ax5.set_facecolor('#1A1A2E')
    
    # Current state visualization
    state_colors = {
        'calm': '#22C55E', 'focused': '#3B82F6', 'agitated': '#EF4444',
        'neutral': '#6B7280', 'meditative': '#7C3AED', 'anxious': '#F59E0B',
        'tired': '#8B5CF6'
    }
    
    current_color = state_colors.get(current_state, '#6B7280')
    
    # Create state circle
    circle = patches.Circle((0.5, 0.5), 0.3, color=current_color, alpha=0.8)
    ax5.add_patch(circle)
    
    # State label
    ax5.text(0.5, 0.5, current_state.title(), ha='center', va='center',
            fontsize=14, color='white', weight='bold')
    
    # State description
    descriptions = {
        'calm': 'Balanced and peaceful',
        'focused': 'Alert and concentrated', 
        'agitated': 'Restless or stimulated',
        'neutral': 'Neither calm nor agitated',
        'meditative': 'Deep and contemplative',
        'anxious': 'Worried or tense',
        'tired': 'Fatigued or low energy'
    }
    
    description = descriptions.get(current_state, 'Unknown state')
    ax5.text(0.5, 0.1, description, ha='center', va='center',
            fontsize=10, color='white', alpha=0.8)
    
    ax5.set_xlim(0, 1)
    ax5.set_ylim(0, 1)
    ax5.set_aspect('equal')
    ax5.axis('off')
    ax5.set_title('Current State', fontsize=12, color='white')
    
    # 6. Session Recommendations
    ax6 = fig.add_subplot(gs[2, 2:])
    ax6.set_facecolor('#1A1A2E')
    
    # Generate recommendations based on profile
    recommendations = []
    
    if sensitivity_level == 'sensitive':
        recommendations.append('• Use lower volume settings')
        recommendations.append('• Prefer shorter sessions')
        recommendations.append('• Include integration phases')
    
    if experience_level == 'beginner':
        recommendations.append('• Start with simple presets')
        recommendations.append('• Focus on alpha/theta states')
        recommendations.append('• Read guidance carefully')
    
    if current_state == 'agitated':
        recommendations.append('• Begin with calming frequencies')
        recommendations.append('• Avoid high beta/gamma initially')
        recommendations.append('• Use grounding techniques')
    
    if current_state == 'tired':
        recommendations.append('• Consider energizing frequencies')
        recommendations.append('• Shorter session duration')
        recommendations.append('• Focus on alertness states')
    
    # Default recommendations
    if not recommendations:
        recommendations = [
            '• Profile supports standard sessions',
            '• Explore various consciousness states',
            '• Monitor comfort levels'
        ]
    
    # Display recommendations
    recommendation_text = '\n'.join(recommendations[:6])  # Limit to 6 recommendations
    ax6.text(0.05, 0.95, 'Recommendations:', fontsize=12, color='white', 
            weight='bold', transform=ax6.transAxes, va='top')
    ax6.text(0.05, 0.85, recommendation_text, fontsize=10, color='white',
            transform=ax6.transAxes, va='top', alpha=0.9)
    
    ax6.axis('off')
    
    # Overall title
    fig.suptitle(f'Neural Architecture Dashboard - {sensitivity_level.title()} Profile', 
                fontsize=16, color='white', y=0.95)
    
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    return fig

def plot_biofield_intelligence_analysis(audio: np.ndarray, sample_rate: int, 
                                       metadata: Optional[Dict[str, Any]] = None,
                                       config: VisualizationConfig = VisualizationConfig()) -> plt.Figure:
    """
    Create comprehensive biofield intelligence analysis visualization.
    
    Args:
        audio: Audio signal data
        sample_rate: Sample rate
        metadata: Session metadata with biofield analysis
        config: Visualization configuration
        
    Returns:
        Biofield intelligence analysis figure
    """
    # Create figure with biofield-aware layout
    fig = plt.figure(figsize=config.figure_size, dpi=config.dpi)
    fig.patch.set_facecolor('#0F1419')  # Deep blue-black for biofield theme
    
    # Create grid layout
    gs = GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3)
    
    # Input validation
    if len(audio) == 0:
        fig.text(0.5, 0.5, 'No audio data available for biofield analysis', 
                ha='center', va='center', fontsize=14, color='white')
        return fig
    
    # Convert mono to stereo if needed
    if audio.ndim == 1:
        audio = np.stack([audio, audio], axis=1)
    elif audio.ndim == 2 and audio.shape[1] == 1:
        audio = np.tile(audio, (1, 2))
    
    # Extract biofield analysis data
    biofield_metrics = {}
    if metadata and 'biofield_analysis' in metadata:
        biofield_metrics = metadata['biofield_analysis'].get('coherence_metrics', {})
    
    # 1. Schumann Resonance Alignment Spectrum
    ax1 = fig.add_subplot(gs[0, :])
    ax1.set_facecolor('#0F1419')
    
    # Perform spectral analysis
    # Ensure we have proper array dimensions
    if audio.ndim == 1 or (audio.ndim == 2 and audio.shape[1] == 1):
        audio_mono = audio.flatten() if audio.ndim == 2 else audio
    else:
        audio_mono = audio[:, 0]
    
    # Calculate nperseg safely
    nperseg = min(2048, len(audio_mono)//4)
    if nperseg < 4:
        nperseg = min(256, len(audio_mono)//2)
    
    frequencies, power = welch(audio_mono, sample_rate, nperseg=nperseg)
    
    # Plot power spectrum
    ax1.loglog(frequencies, power, color='cyan', alpha=0.7, linewidth=1)
    ax1.fill_between(frequencies, power, alpha=0.3, color='cyan')
    
    # Mark Schumann resonances
    schumann_freqs = BIOFIELD_FREQUENCY_VISUALS['schumann_resonances']['frequencies']
    for freq in schumann_freqs:
        if freq <= sample_rate / 2:  # Within Nyquist limit
            ax1.axvline(freq, color='green', linestyle='--', alpha=0.8, linewidth=2)
            ax1.text(freq, np.max(power) * 0.8, f'{freq}Hz', 
                    rotation=90, fontsize=8, color='green', ha='center')
    
    # Mark Solfeggio frequencies (if in range)
    solfeggio_freqs = [f for f in BIOFIELD_FREQUENCY_VISUALS['solfeggio_frequencies']['frequencies'] 
                      if f <= sample_rate / 2]
    for freq in solfeggio_freqs:
        ax1.axvline(freq, color='blue', linestyle=':', alpha=0.6, linewidth=2)
    
    ax1.set_xlabel('Frequency (Hz)', color='white', fontsize=10)
    ax1.set_ylabel('Power Spectral Density', color='white', fontsize=10)
    ax1.set_title('Biofield Frequency Spectrum with Natural Resonances', 
                 color='white', fontsize=12)
    ax1.tick_params(colors='white', labelsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0.1, min(100, sample_rate/2))
    
    # Add legend
    ax1.plot([], [], color='green', linestyle='--', label='Schumann Resonances')
    ax1.plot([], [], color='blue', linestyle=':', label='Solfeggio Frequencies')
    legend = ax1.legend(loc='upper right', fontsize=9, framealpha=0.8)
    legend.get_frame().set_facecolor('#0F1419')
    for text in legend.get_texts():
        text.set_color('white')
    
    # 2. Coherence Metrics Dashboard
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.set_facecolor('#0F1419')
    
    # Create coherence radar chart
    coherence_metrics = ['Schumann', 'Solfeggio', 'Golden Ratio', 'Frequency Harmony', 
                        'Transition', 'Intention', 'Neural Compat.']
    
    coherence_values = [
        biofield_metrics.get('schumann_alignment', 0),
        biofield_metrics.get('solfeggio_presence', 0),
        biofield_metrics.get('golden_ratio_harmonics', 0),
        biofield_metrics.get('frequency_harmony', 0),
        biofield_metrics.get('transition_smoothness', 0),
        biofield_metrics.get('intention_congruence', 0),
        biofield_metrics.get('neural_compatibility', 0)
    ]
    
    # Create mini radar chart
    angles = np.linspace(0, 2 * np.pi, len(coherence_metrics), endpoint=False)
    values = np.array(coherence_values)
    
    # Close the plot
    angles = np.concatenate((angles, [angles[0]]))
    values = np.concatenate((values, [values[0]]))
    
    # Create polar subplot
    ax2_polar = fig.add_subplot(gs[1, 0], projection='polar')
    ax2_polar.set_facecolor('#0F1419')
    
    # Plot coherence metrics
    ax2_polar.plot(angles, values, color='#00D9FF', linewidth=2, alpha=0.8)
    ax2_polar.fill(angles, values, color='#00D9FF', alpha=0.3)
    
    # Customize polar chart
    ax2_polar.set_xticks(angles[:-1])
    ax2_polar.set_xticklabels(coherence_metrics, fontsize=8, color='white')
    ax2_polar.set_ylim(0, 1)
    ax2_polar.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax2_polar.set_yticklabels(['20%', '40%', '60%', '80%', '100%'], 
                             fontsize=7, color='white', alpha=0.7)
    ax2_polar.grid(True, alpha=0.3)
    ax2_polar.set_title('Coherence Metrics', color='white', fontsize=11, pad=15)
    
    # Remove the original ax2
    ax2.remove()
    
    # 3. Golden Ratio Harmonic Analysis
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.set_facecolor('#0F1419')
    
    # Analyze harmonic relationships
    dominant_freqs = frequencies[np.argsort(power)[-10:]]  # Top 10 frequencies
    golden_ratio = 1.618033988749895
    
    # Create harmonic relationship matrix
    harmonic_matrix = np.zeros((len(dominant_freqs), len(dominant_freqs)))
    
    for i, freq1 in enumerate(dominant_freqs):
        for j, freq2 in enumerate(dominant_freqs):
            if freq1 != freq2 and freq1 > 0:
                ratio = freq2 / freq1
                # Check for golden ratio relationships
                for power in range(-2, 3):
                    target_ratio = golden_ratio ** power
                    if abs(ratio - target_ratio) / target_ratio < 0.1:
                        harmonic_matrix[i, j] = target_ratio
                        break
    
    # Plot harmonic matrix
    im = ax3.imshow(harmonic_matrix, cmap='plasma', aspect='auto', vmin=0, vmax=3)
    ax3.set_title('Golden Ratio Harmonics', color='white', fontsize=11)
    ax3.set_xlabel('Frequency Index', color='white', fontsize=9)
    ax3.set_ylabel('Frequency Index', color='white', fontsize=9)
    ax3.tick_params(colors='white', labelsize=8)
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax3, shrink=0.8)
    cbar.set_label('Harmonic Ratio', color='white', fontsize=9)
    cbar.ax.tick_params(colors='white', labelsize=8)
    
    # 4. Natural Frequency Presence Heatmap
    ax4 = fig.add_subplot(gs[1, 2])
    ax4.set_facecolor('#0F1419')
    
    # Create frequency presence analysis
    natural_freq_categories = ['Schumann', 'Solfeggio', 'Healing', 'Chakra']
    frequency_ranges = {
        'Schumann': [7.83, 14.3, 20.8, 27.3, 33.8],
        'Solfeggio': [174, 285, 396, 417, 528, 639, 741, 852],
        'Healing': [528, 432, 396, 417, 852],
        'Chakra': [256, 288, 320, 341, 384, 426, 480]  # Approximate chakra frequencies
    }
    
    presence_matrix = np.zeros((len(natural_freq_categories), 1))
    
    for i, category in enumerate(natural_freq_categories):
        category_freqs = frequency_ranges[category]
        presence_score = 0
        
        for freq in category_freqs:
            if freq <= sample_rate / 2 and len(frequencies) > 0:
                # Find closest frequency in spectrum
                freq_idx = np.argmin(np.abs(frequencies - freq))
                # Validate index and calculate presence based on power at that frequency
                if (isinstance(freq_idx, (int, np.integer)) and 
                    0 <= freq_idx < len(power) and 
                    len(frequencies) > freq_idx and
                    frequencies[freq_idx] != 0):
                    presence_score += power[freq_idx] / np.max(power)
        
        presence_matrix[i, 0] = presence_score / len(category_freqs)
    
    # Plot presence heatmap
    im = ax4.imshow(presence_matrix, cmap='viridis', aspect='auto', vmin=0, vmax=1)
    ax4.set_yticks(range(len(natural_freq_categories)))
    ax4.set_yticklabels(natural_freq_categories, fontsize=9, color='white')
    ax4.set_xticks([0])
    ax4.set_xticklabels(['Presence'], fontsize=9, color='white')
    ax4.set_title('Natural Frequency\nPresence', color='white', fontsize=11)
    ax4.tick_params(colors='white', labelsize=8)
    
    # Add presence values
    for i in range(len(natural_freq_categories)):
        text = ax4.text(0, i, f'{presence_matrix[i, 0]:.3f}', 
                       ha='center', va='center', color='white', weight='bold', fontsize=9)
    
    # 5. Biofield Coherence Timeline
    ax5 = fig.add_subplot(gs[2, :])
    ax5.set_facecolor('#0F1419')
    
    if metadata and 'biofield_analysis' in metadata:
        coherence_timeline = metadata['biofield_analysis'].get('coherence_timeline', [])
        
        if coherence_timeline:
            # Create time axis
            time_points = np.linspace(0, len(audio) / sample_rate / 60, len(coherence_timeline))
            
            # Plot coherence timeline
            ax5.plot(time_points, coherence_timeline, color='#00FF88', linewidth=3, alpha=0.8)
            ax5.fill_between(time_points, coherence_timeline, alpha=0.3, color='#00FF88')
            
            # Add coherence zones
            for i, coherence_level in enumerate(coherence_timeline):
                if coherence_level > 0.8:
                    color = '#00FF88'  # High coherence - green
                elif coherence_level > 0.6:
                    color = '#FFD700'  # Medium coherence - gold
                else:
                    color = '#FF6B6B'  # Low coherence - red
                
                ax5.scatter(time_points[i], coherence_level, color=color, s=50, alpha=0.7)
            
            # Add threshold lines
            ax5.axhline(y=0.8, color='green', linestyle='--', alpha=0.6, label='High Coherence')
            ax5.axhline(y=0.6, color='orange', linestyle='--', alpha=0.6, label='Medium Coherence')
            ax5.axhline(y=0.4, color='red', linestyle='--', alpha=0.6, label='Low Coherence')
            
            # Customization
            ax5.set_xlabel('Time (minutes)', color='white', fontsize=10)
            ax5.set_ylabel('Biofield Coherence', color='white', fontsize=10)
            ax5.set_title('Biofield Coherence Evolution Throughout Session', 
                         color='white', fontsize=12)
            ax5.tick_params(colors='white', labelsize=9)
            ax5.grid(True, alpha=0.3)
            ax5.set_ylim(0, 1)
            
            # Legend
            legend = ax5.legend(loc='upper right', fontsize=9, framealpha=0.8)
            legend.get_frame().set_facecolor('#0F1419')
            for text in legend.get_texts():
                text.set_color('white')
        else:
            ax5.text(0.5, 0.5, 'No coherence timeline data available', 
                    transform=ax5.transAxes, ha='center', va='center', 
                    fontsize=12, color='white', alpha=0.6)
            ax5.axis('off')
    else:
        # Create synthetic coherence analysis from audio
        # Segment audio and analyze coherence
        segment_duration = 30  # 30 second segments
        segment_samples = int(segment_duration * sample_rate)
        num_segments = len(audio) // segment_samples
        
        if num_segments > 1:
            coherence_timeline = []
            time_points = []
            
            for i in range(num_segments):
                start_idx = i * segment_samples
                end_idx = min((i + 1) * segment_samples, len(audio))
                segment = audio[start_idx:end_idx]
                
                # Calculate segment coherence (cross-correlation between channels)
                if segment.shape[1] == 2:
                    correlation = np.corrcoef(segment[:, 0], segment[:, 1])[0, 1]
                    coherence_val = abs(correlation)
                else:
                    coherence_val = 0.7  # Default for mono
                
                coherence_timeline.append(coherence_val)
                time_points.append((start_idx + end_idx) / 2 / sample_rate / 60)
            
            # Plot coherence timeline
            ax5.plot(time_points, coherence_timeline, color='#00FF88', linewidth=3, alpha=0.8)
            ax5.fill_between(time_points, coherence_timeline, alpha=0.3, color='#00FF88')
            
            ax5.set_xlabel('Time (minutes)', color='white', fontsize=10)
            ax5.set_ylabel('Channel Coherence', color='white', fontsize=10)
            ax5.set_title('Estimated Biofield Coherence (Channel Correlation)', 
                         color='white', fontsize=12)
            ax5.tick_params(colors='white', labelsize=9)
            ax5.grid(True, alpha=0.3)
            ax5.set_ylim(0, 1)
        else:
            ax5.text(0.5, 0.5, 'Insufficient audio data for coherence analysis', 
                    transform=ax5.transAxes, ha='center', va='center', 
                    fontsize=12, color='white', alpha=0.6)
            ax5.axis('off')
    
    # Overall title with biofield metrics
    overall_coherence = biofield_metrics.get('overall_coherence', 0)
    schumann_alignment = biofield_metrics.get('schumann_alignment', 0)
    solfeggio_presence = biofield_metrics.get('solfeggio_presence', 0)
    
    title = f"Biofield Intelligence Analysis\n"
    title += f"Overall Coherence: {overall_coherence:.3f} | "
    title += f"Schumann: {schumann_alignment:.3f} | "
    title += f"Solfeggio: {solfeggio_presence:.3f}"
    
    fig.suptitle(title, fontsize=14, color='white', y=0.95)
    
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    return fig

def plot_safety_monitoring_dashboard(validation_result: Dict[str, Any],
                                   neural_profile: Optional[Dict[str, Any]] = None,
                                   real_time_metrics: Optional[Dict[str, Any]] = None,
                                   config: VisualizationConfig = VisualizationConfig()) -> plt.Figure:
    """
    Create real-time safety monitoring dashboard.
    
    Args:
        validation_result: Validation results from validator
        neural_profile: Neural profile for context
        real_time_metrics: Optional real-time session metrics
        config: Visualization configuration
        
    Returns:
        Safety monitoring dashboard figure
    """
    # Create dashboard layout
    fig = plt.figure(figsize=config.figure_size, dpi=config.dpi)
    fig.patch.set_facecolor('#1A0000')  # Dark red background for safety theme
    
    # Create grid layout
    gs = GridSpec(3, 4, figure=fig, hspace=0.4, wspace=0.3)
    
    # Extract validation data
    is_valid = validation_result.get('is_valid', True)
    safety_rating = validation_result.get('safety_rating', 'safe')
    errors = validation_result.get('errors', [])
    warnings = validation_result.get('warnings', [])
    
    # 1. Overall Safety Status
    ax1 = fig.add_subplot(gs[0, :2])
    ax1.set_facecolor('#1A0000')
    
    # Safety status indicator
    safety_colors = SAFETY_LEVEL_VISUALS
    current_safety = safety_colors.get(safety_rating, safety_colors['safe'])
    
    # Create large status circle
    circle = patches.Circle((0.5, 0.5), 0.4, color=current_safety['color'], 
                           alpha=current_safety['alpha'])
    ax1.add_patch(circle)
    
    # Safety status text
    status_text = "SAFE" if is_valid else "UNSAFE"
    ax1.text(0.5, 0.5, status_text, ha='center', va='center', 
            fontsize=24, color='white', weight='bold')
    
    # Safety level
    ax1.text(0.5, 0.3, safety_rating.upper(), ha='center', va='center',
            fontsize=14, color='white', alpha=0.9)
    
    # Issue count
    issue_text = f"Errors: {len(errors)} | Warnings: {len(warnings)}"
    ax1.text(0.5, 0.1, issue_text, ha='center', va='center',
            fontsize=12, color='white', alpha=0.8)
    
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Safety Status', fontsize=14, color='white', weight='bold')
    
    # 2. Neural Load Monitor
    ax2 = fig.add_subplot(gs[0, 2:])
    ax2.set_facecolor('#1A0000')
    
    # Neural load gauge
    if 'neural_load_assessment' in validation_result:
        load_data = validation_result['neural_load_assessment']
        utilization = load_data.get('utilization', 0)
        total_load = load_data.get('total_load', 0)
        load_limit = load_data.get('load_limit', 10)
    else:
        utilization = 0.5  # Default
        total_load = 5
        load_limit = 10
    
    # Create load gauge
    angles = np.linspace(0, np.pi, 100)
    gauge_x = np.cos(angles) 
    gauge_y = np.sin(angles)
    
    # Background gauge
    ax2.plot(gauge_x, gauge_y, color='gray', linewidth=20, alpha=0.3)
    
    # Load indicator
    load_angle = np.pi * utilization
    load_angles = angles[angles <= load_angle]
    load_x = np.cos(load_angles)
    load_y = np.sin(load_angles)
    
    # Color based on load level
    if utilization < 0.7:
        load_color = '#22C55E'  # Green - safe
    elif utilization < 0.9:
        load_color = '#F59E0B'  # Amber - caution
    else:
        load_color = '#EF4444'  # Red - overload
    
    if len(load_x) > 0:
        ax2.plot(load_x, load_y, color=load_color, linewidth=20, alpha=0.9)
    
    # Load percentage text
    ax2.text(0, 0.3, f'{utilization:.0%}', ha='center', va='center',
            fontsize=20, color='white', weight='bold')
    ax2.text(0, 0.1, 'Neural Load', ha='center', va='center',
            fontsize=12, color='white')
    ax2.text(0, -0.1, f'{total_load:.1f} / {load_limit:.1f}', ha='center', va='center',
            fontsize=10, color='white', alpha=0.8)
    
    # Threshold markers
    ax2.axvline(x=np.cos(np.pi * 0.7), color='yellow', linestyle='--', alpha=0.7)
    ax2.axvline(x=np.cos(np.pi * 0.9), color='orange', linestyle='--', alpha=0.7)
    
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-0.2, 1.2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Neural Load Monitor', fontsize=12, color='white')
    
    # 3. Issue Tracking
    ax3 = fig.add_subplot(gs[1, :])
    ax3.set_facecolor('#1A0000')
    
    # Create issue timeline
    all_issues = []
    
    # Add errors
    for i, error in enumerate(errors[:5]):  # Limit to 5 most recent
        issue_text = error if isinstance(error, str) else error.get('message', 'Unknown error')
        all_issues.append(('ERROR', issue_text[:60], '#EF4444'))
    
    # Add warnings  
    for i, warning in enumerate(warnings[:5]):
        warning_text = warning if isinstance(warning, str) else warning.get('message', 'Unknown warning')
        all_issues.append(('WARNING', warning_text[:60], '#F59E0B'))
    
    if all_issues:
        # Plot issues
        y_positions = range(len(all_issues))
        
        for i, (issue_type, message, color) in enumerate(all_issues):
            # Issue type indicator
            ax3.barh(i, 1, height=0.6, color=color, alpha=0.7)
            
            # Issue text
            ax3.text(0.05, i, f"{issue_type}: {message}", 
                    va='center', fontsize=10, color='white', weight='bold')
        
        ax3.set_xlim(0, 1)
        ax3.set_ylim(-0.5, len(all_issues) - 0.5)
        ax3.set_yticks([])
        ax3.set_xticks([])
    else:
        ax3.text(0.5, 0.5, 'No Safety Issues Detected', transform=ax3.transAxes,
                ha='center', va='center', fontsize=14, color='green', weight='bold')
    
    ax3.set_title('Safety Issues & Warnings', fontsize=12, color='white')
    ax3.axis('off')
    
    # 4. Real-time Metrics (if available)
    ax4 = fig.add_subplot(gs[2, :2])
    ax4.set_facecolor('#1A0000')
    
    if real_time_metrics:
        # Plot real-time safety metrics
        metrics_names = list(real_time_metrics.keys())[:4]  # Limit to 4 metrics
        metrics_values = [real_time_metrics[name] for name in metrics_names]
        
        colors = ['#22C55E', '#F59E0B', '#3B82F6', '#EC4899']
        
        bars = ax4.bar(metrics_names, metrics_values, color=colors[:len(metrics_names)], 
                      alpha=0.8)
        
        # Add value labels
        for bar, value in zip(bars, metrics_values):
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                    f'{value:.3f}', ha='center', va='bottom', 
                    color='white', fontsize=10)
        
        ax4.set_ylabel('Metric Value', color='white', fontsize=10)
        ax4.set_title('Real-time Safety Metrics', fontsize=12, color='white')
        ax4.tick_params(colors='white', labelsize=9)
        ax4.set_ylim(0, 1)
    else:
        ax4.text(0.5, 0.5, 'Real-time Metrics\nNot Available', 
                transform=ax4.transAxes, ha='center', va='center',
                fontsize=12, color='white', alpha=0.6)
        ax4.axis('off')
    
    # 5. Neural Profile Safety Compatibility
    ax5 = fig.add_subplot(gs[2, 2:])
    ax5.set_facecolor('#1A0000')
    
    if neural_profile:
        # Safety compatibility metrics
        sensitivity_level = neural_profile.get('sensitivity_level', 'standard')
        experience_level = neural_profile.get('experience_level', 'intermediate')
        
        # Create compatibility indicators
        compatibility_factors = ['Duration', 'Complexity', 'Frequency Range', 'Transitions']
        
        # Calculate compatibility scores based on profile
        if sensitivity_level == 'sensitive':
            scores = [0.6, 0.7, 0.8, 0.6]  # More conservative scores
        elif sensitivity_level == 'resilient':
            scores = [0.9, 0.9, 0.8, 0.9]  # Higher tolerance
        else:
            scores = [0.8, 0.8, 0.8, 0.8]  # Standard scores
        
        # Adjust for experience level
        if experience_level == 'beginner':
            scores = [s * 0.8 for s in scores]
        elif experience_level in ['advanced', 'expert']:
            scores = [min(1.0, s * 1.2) for s in scores]
        
        # Create horizontal bar chart
        colors = ['#22C55E' if s > 0.7 else '#F59E0B' if s > 0.5 else '#EF4444' for s in scores]
        bars = ax5.barh(compatibility_factors, scores, color=colors, alpha=0.8)
        
        # Add score labels
        for bar, score in zip(bars, scores):
            width = bar.get_width()
            ax5.text(width + 0.02, bar.get_y() + bar.get_height()/2,
                    f'{score:.2f}', ha='left', va='center',
                    color='white', fontsize=10)
        
        ax5.set_xlabel('Compatibility Score', color='white', fontsize=10)
        ax5.set_title(f'Profile Compatibility\n({sensitivity_level}, {experience_level})', 
                     fontsize=11, color='white')
        ax5.tick_params(colors='white', labelsize=9)
        ax5.set_xlim(0, 1.2)
    else:
        ax5.text(0.5, 0.5, 'Neural Profile\nNot Available', 
                transform=ax5.transAxes, ha='center', va='center',
                fontsize=12, color='white', alpha=0.6)
        ax5.axis('off')
    
    # Overall dashboard title
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fig.suptitle(f'Safety Monitoring Dashboard - {timestamp}', 
                fontsize=16, color='white', y=0.95)
    
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    return fig

def plot_integration_effectiveness_analysis(metadata: Dict[str, Any],
                                          session_history: Optional[List[Dict[str, Any]]] = None,
                                          config: VisualizationConfig = VisualizationConfig()) -> plt.Figure:
    """
    Create integration effectiveness analysis visualization.
    
    Args:
        metadata: Current session metadata
        session_history: Optional historical session data
        config: Visualization configuration
        
    Returns:
        Integration effectiveness analysis figure
    """
    # Create figure with integration theme
    fig = plt.figure(figsize=config.figure_size, dpi=config.dpi)
    fig.patch.set_facecolor('#0A0A2E')  # Deep purple for integration theme
    
    # Create grid layout
    gs = GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3)
    
    # Extract integration data
    consciousness_analysis = metadata.get('consciousness_analysis', {})
    integration_windows = consciousness_analysis.get('integration_windows', [])
    phases = metadata.get('phases', [])
    
    # 1. Integration Windows Timeline
    ax1 = fig.add_subplot(gs[0, :])
    ax1.set_facecolor('#0A0A2E')
    
    if integration_windows and phases:
        # Create timeline
        total_duration = sum(phase.get('duration', 0) for phase in phases)
        
        # Plot session timeline
        session_times = np.linspace(0, total_duration/60, 100)
        baseline = np.zeros_like(session_times)
        ax1.fill_between(session_times, baseline, 0.2, alpha=0.3, color='gray', 
                        label='Session Duration')
        
        # Mark integration windows
        for i, window in enumerate(integration_windows):
            start_time = window.get('start_time', 0) / 60
            end_time = window.get('end_time', 0) / 60
            integration_type = window.get('type', 'natural')
            potential = window.get('integration_potential', 0.7)
            
            # Integration window bar
            ax1.fill_between([start_time, end_time], [0, 0], [potential, potential], 
                           alpha=0.8, color='violet', label=f'Integration {i+1}' if i < 3 else "")
            
            # Window label
            mid_time = (start_time + end_time) / 2
            ax1.text(mid_time, potential + 0.05, f'I{i+1}\n({potential:.2f})', 
                    ha='center', va='bottom', fontsize=9, color='white')
        
        # Mark phase boundaries
        cumulative_time = 0
        for i, phase in enumerate(phases):
            cumulative_time += phase.get('duration', 0) / 60
            ax1.axvline(cumulative_time, color='white', alpha=0.5, linestyle='--')
        
        ax1.set_xlabel('Time (minutes)', color='white', fontsize=10)
        ax1.set_ylabel('Integration Potential', color='white', fontsize=10)
        ax1.set_title('Integration Windows Throughout Session', color='white', fontsize=12)
        ax1.tick_params(colors='white', labelsize=9)
        ax1.set_ylim(0, 1.1)
        ax1.grid(True, alpha=0.3)
        
        # Legend
        legend = ax1.legend(loc='upper right', fontsize=9, framealpha=0.8)
        legend.get_frame().set_facecolor('#0A0A2E')
        for text in legend.get_texts():
            text.set_color('white')
    
    else:
        ax1.text(0.5, 0.5, 'No Integration Windows Detected', 
                transform=ax1.transAxes, ha='center', va='center',
                fontsize=12, color='white', alpha=0.6)
        ax1.axis('off')
    
    # 2. Integration Quality Metrics
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.set_facecolor('#0A0A2E')
    
    if integration_windows:
        # Calculate integration quality metrics
        avg_potential = np.mean([w.get('integration_potential', 0) for w in integration_windows])
        total_integration_time = sum((w.get('end_time', 0) - w.get('start_time', 0)) 
                                   for w in integration_windows)
        
        # Integration quality gauge
        angle = np.pi * avg_potential
        gauge_angles = np.linspace(0, np.pi, 100)
        gauge_x = np.cos(gauge_angles)
        gauge_y = np.sin(gauge_angles)
        
        # Background gauge
        ax2.plot(gauge_x, gauge_y, color='gray', linewidth=15, alpha=0.3)
        
        # Quality indicator
        if angle > 0:
            quality_angles = gauge_angles[gauge_angles <= angle]
            quality_x = np.cos(quality_angles)
            quality_y = np.sin(quality_angles)
            
            # Color based on quality
            if avg_potential > 0.8:
                color = '#22C55E'  # Excellent
            elif avg_potential > 0.6:
                color = '#F59E0B'  # Good
            else:
                color = '#EF4444'  # Needs improvement
            
            if len(quality_x) > 0:
                ax2.plot(quality_x, quality_y, color=color, linewidth=15, alpha=0.9)
        
        # Quality text
        ax2.text(0, 0.3, f'{avg_potential:.1%}', ha='center', va='center',
                fontsize=16, color='white', weight='bold')
        ax2.text(0, 0.1, 'Integration\nQuality', ha='center', va='center',
                fontsize=10, color='white')
        ax2.text(0, -0.1, f'{total_integration_time/60:.1f}min total', 
                ha='center', va='center', fontsize=9, color='white', alpha=0.8)
        
    else:
        ax2.text(0, 0.5, 'No Integration\nData Available', ha='center', va='center',
                fontsize=12, color='white', alpha=0.6)
    
    ax2.set_xlim(-1.1, 1.1)
    ax2.set_ylim(-0.2, 1.2)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Integration Quality', fontsize=11, color='white')
    
    # 3. Healing Frequency Analysis
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.set_facecolor('#0A0A2E')
    
    # Analyze healing frequency presence
    healing_freqs = {'528 Hz': 0, '432 Hz': 0, '396 Hz': 0, '417 Hz': 0, '852 Hz': 0}
    
    for phase in phases:
        for layer in phase.get('layers', []):
            carrier = layer.get('carrier', 0)
            # Check for healing frequencies (within 5Hz tolerance)
            if abs(carrier - 528) <= 5:
                healing_freqs['528 Hz'] += phase.get('duration', 0)
            elif abs(carrier - 432) <= 5:
                healing_freqs['432 Hz'] += phase.get('duration', 0)
            elif abs(carrier - 396) <= 5:
                healing_freqs['396 Hz'] += phase.get('duration', 0)
            elif abs(carrier - 417) <= 5:
                healing_freqs['417 Hz'] += phase.get('duration', 0)
            elif abs(carrier - 852) <= 5:
                healing_freqs['852 Hz'] += phase.get('duration', 0)
    
    # Convert to minutes and create pie chart
    freq_names = list(healing_freqs.keys())
    freq_durations = [duration/60 for duration in healing_freqs.values()]
    total_healing_time = sum(freq_durations)
    
    if total_healing_time > 0:
        # Filter out zero durations
        non_zero_names = [name for name, duration in zip(freq_names, freq_durations) if duration > 0]
        non_zero_durations = [duration for duration in freq_durations if duration > 0]
        
        # Create pie chart
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'][:len(non_zero_names)]
        wedges, texts, autotexts = ax3.pie(non_zero_durations, labels=non_zero_names, 
                                          colors=colors, autopct='%1.1f%%', startangle=90)
        
        # Style pie chart
        for text in texts:
            text.set_color('white')
            text.set_fontsize(9)
        for autotext in autotexts:
            autotext.set_color('black')
            autotext.set_fontsize(8)
            autotext.set_weight('bold')
        
    else:
        ax3.text(0, 0, 'No Healing\nFrequencies\nDetected', ha='center', va='center',
                fontsize=11, color='white', alpha=0.6)
        ax3.set_xlim(-1, 1)
        ax3.set_ylim(-1, 1)
    
    ax3.set_title('Healing Frequencies', fontsize=11, color='white')
    
    # 4. Consciousness State Integration Pattern
    ax4 = fig.add_subplot(gs[1, 2])
    ax4.set_facecolor('#0A0A2E')
    
    # Analyze consciousness state patterns during integration
    state_sequence = consciousness_analysis.get('state_sequence', [])
    if state_sequence:
        # Count states during integration windows
        integration_states = {}
        
        for window in integration_windows:
            phase_index = window.get('phase_index', 0)
            if phase_index < len(state_sequence):
                state = state_sequence[phase_index]
                if state in integration_states:
                    integration_states[state] += 1
                else:
                    integration_states[state] = 1
        
        if integration_states:
            # Create bar chart
            states = list(integration_states.keys())
            counts = list(integration_states.values())
            
            bars = ax4.bar(range(len(states)), counts, 
                          color=[CONSCIOUSNESS_STATE_VISUALS.get(state, {'color': 'gray'})['color'] 
                                for state in states],
                          alpha=0.8)
            
            ax4.set_xticks(range(len(states)))
            ax4.set_xticklabels([state.title() for state in states], 
                               rotation=45, fontsize=9, color='white')
            ax4.set_ylabel('Integration Count', color='white', fontsize=9)
            ax4.tick_params(colors='white', labelsize=8)
            
            # Add count labels
            for bar, count in zip(bars, counts):
                height = bar.get_height()
                ax4.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                        str(count), ha='center', va='bottom', 
                        color='white', fontsize=9)
        else:
            ax4.text(0.5, 0.5, 'No State\nIntegration\nData', 
                    transform=ax4.transAxes, ha='center', va='center',
                    fontsize=10, color='white', alpha=0.6)
            ax4.axis('off')
    else:
        ax4.text(0.5, 0.5, 'No State\nSequence\nAvailable', 
                transform=ax4.transAxes, ha='center', va='center',
                fontsize=10, color='white', alpha=0.6)
        ax4.axis('off')
    
    ax4.set_title('Integration States', fontsize=11, color='white')
    
    # 5. Historical Integration Progress (if available)
    ax5 = fig.add_subplot(gs[2, :])
    ax5.set_facecolor('#0A0A2E')
    
    if session_history:
        # Track integration effectiveness over time
        session_dates = []
        integration_scores = []
        
        for session in session_history[-10:]:  # Last 10 sessions
            date_str = session.get('date', '')
            if date_str:
                session_dates.append(date_str)
                
                # Calculate integration score
                session_metadata = session.get('metadata', {})
                session_windows = session_metadata.get('consciousness_analysis', {}).get('integration_windows', [])
                if session_windows:
                    avg_score = np.mean([w.get('integration_potential', 0) for w in session_windows])
                    integration_scores.append(avg_score)
                else:
                    integration_scores.append(0.5)  # Default score
        
        if integration_scores:
            # Plot progress
            x_positions = range(len(integration_scores))
            ax5.plot(x_positions, integration_scores, marker='o', linewidth=2, 
                    markersize=8, color='#8A2BE2', alpha=0.8)
            ax5.fill_between(x_positions, integration_scores, alpha=0.3, color='#8A2BE2')
            
            # Add trend line
            if len(integration_scores) > 2:
                z = np.polyfit(x_positions, integration_scores, 1)
                p = np.poly1d(z)
                ax5.plot(x_positions, p(x_positions), "--", color='yellow', alpha=0.8, linewidth=2)
            
            # Customize
            ax5.set_xticks(x_positions[::max(1, len(x_positions)//5)])  # Show max 5 labels
            ax5.set_xticklabels([session_dates[i] for i in x_positions[::max(1, len(x_positions)//5)]], 
                               rotation=45, fontsize=9, color='white')
            ax5.set_ylabel('Integration Score', color='white', fontsize=10)
            ax5.set_title('Integration Progress Over Time', color='white', fontsize=12)
            ax5.tick_params(colors='white', labelsize=9)
            ax5.grid(True, alpha=0.3)
            ax5.set_ylim(0, 1)
            
            # Add current session marker
            current_avg = np.mean([w.get('integration_potential', 0) for w in integration_windows]) if integration_windows else 0.5
            ax5.scatter([len(integration_scores)], [current_avg], s=200, color='red', 
                       marker='*', zorder=5, label='Current Session')
            
            # Legend
            legend = ax5.legend(loc='upper left', fontsize=9, framealpha=0.8)
            legend.get_frame().set_facecolor('#0A0A2E')
            for text in legend.get_texts():
                text.set_color('white')
        else:
            ax5.text(0.5, 0.5, 'Insufficient Session History for Progress Analysis', 
                    transform=ax5.transAxes, ha='center', va='center',
                    fontsize=12, color='white', alpha=0.6)
            ax5.axis('off')
    else:
        ax5.text(0.5, 0.5, 'No Session History Available', 
                transform=ax5.transAxes, ha='center', va='center',
                fontsize=12, color='white', alpha=0.6)
        ax5.axis('off')
    
    # Overall title
    integration_count = len(integration_windows)
    avg_potential = np.mean([w.get('integration_potential', 0) for w in integration_windows]) if integration_windows else 0
    
    title = f"Integration Effectiveness Analysis\n"
    title += f"Integration Windows: {integration_count} | "
    title += f"Average Potential: {avg_potential:.2%}"
    
    fig.suptitle(title, fontsize=14, color='white', y=0.95)
    
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    return fig

def visualize_audio(audio: np.ndarray, sample_rate: int, 
                   metadata: Optional[Dict[str, Any]] = None,
                   neural_profile: Optional[Dict[str, Any]] = None,
                   config: VisualizationConfig = VisualizationConfig()) -> None:
    """
    Comprehensive consciousness-aware audio visualization with all analysis components.
    
    Args:
        audio: Audio signal data
        sample_rate: Sample rate 
        metadata: Complete session metadata
        neural_profile: Neural profile for adaptation
        config: Visualization configuration
    """
    logging.info("Starting comprehensive consciousness-aware visualization...")
    
    try:
        # Input validation
        if len(audio) == 0:
            raise ValueError("Input audio cannot be empty")
        
        if sample_rate <= 0:
            raise ValueError(f"Invalid sample rate: {sample_rate}")
        
        # Convert mono to stereo if needed
        if audio.ndim == 1:
            audio = np.stack([audio, audio], axis=1)
        elif audio.ndim == 2 and audio.shape[1] == 1:
            audio = np.tile(audio, (1, 2))
        
        # 1. Create 3D Consciousness Journey Visualization
        try:
            fig_journey = plot_consciousness_journey_3D(metadata or {}, neural_profile, config)
            if config.save_figures:
                output_path = Path(config.output_dir)
                output_path.mkdir(exist_ok=True)
                fig_journey.savefig(output_path / 'consciousness_journey_3d.png', 
                                   dpi=config.dpi, bbox_inches='tight', facecolor='#0F0F23')
            plt.close(fig_journey)
            logging.info("3D Consciousness Journey visualization complete")
        except Exception as e:
            logging.warning(f"3D Consciousness Journey visualization failed: {e}")
        
        # 2. Create Neural Architecture Dashboard
        if neural_profile:
            try:
                fig_neural = plot_neural_architecture_dashboard(neural_profile, metadata, config)
                if config.save_figures:
                    output_path = Path(config.output_dir)
                    output_path.mkdir(exist_ok=True)
                    fig_neural.savefig(output_path / 'neural_architecture_dashboard.png', 
                                      dpi=config.dpi, bbox_inches='tight', facecolor='#0F0F23')
                plt.close(fig_neural)
                logging.info("Neural Architecture Dashboard complete")
            except Exception as e:
                logging.warning(f"Neural Architecture Dashboard failed: {e}")
        
        # 3. Create Biofield Intelligence Analysis
        try:
            fig_biofield = plot_biofield_intelligence_analysis(audio, sample_rate, metadata, config)
            if config.save_figures:
                output_path = Path(config.output_dir)
                output_path.mkdir(exist_ok=True)
                fig_biofield.savefig(output_path / 'biofield_intelligence_analysis.png', 
                                    dpi=config.dpi, bbox_inches='tight', facecolor='#0F1419')
            plt.close(fig_biofield)
            logging.info("Biofield Intelligence Analysis complete")
        except Exception as e:
            logging.warning(f"Biofield Intelligence Analysis failed: {e}")
        
        # 4. Create Safety Monitoring Dashboard (if validation data available)
        if metadata and any(key in metadata for key in ['errors', 'warnings', 'safety_rating', 'neural_load_assessment']):
            try:
                # Create validation result structure from metadata
                validation_result = {
                    'is_valid': metadata.get('validation', {}).get('metadata_complete', True),
                    'safety_rating': 'safe',  # Default, can be extracted from metadata
                    'errors': [],
                    'warnings': [],
                    'neural_load_assessment': metadata.get('consciousness_analysis', {}).get('neural_load_assessment', {})
                }
                
                fig_safety = plot_safety_monitoring_dashboard(validation_result, neural_profile, None, config)
                if config.save_figures:
                    output_path = Path(config.output_dir)
                    output_path.mkdir(exist_ok=True)
                    fig_safety.savefig(output_path / 'safety_monitoring_dashboard.png', 
                                      dpi=config.dpi, bbox_inches='tight', facecolor='#1A0000')
                plt.close(fig_safety)
                logging.info("Safety Monitoring Dashboard complete")
            except Exception as e:
                logging.warning(f"Safety Monitoring Dashboard failed: {e}")
        
        # 5. Create Integration Effectiveness Analysis
        try:
            fig_integration = plot_integration_effectiveness_analysis(metadata or {}, None, config)
            if config.save_figures:
                output_path = Path(config.output_dir)
                output_path.mkdir(exist_ok=True)
                fig_integration.savefig(output_path / 'integration_effectiveness_analysis.png', 
                                       dpi=config.dpi, bbox_inches='tight', facecolor='#0A0A2E')
            plt.close(fig_integration)
            logging.info("Integration Effectiveness Analysis complete")
        except Exception as e:
            logging.warning(f"Integration Effectiveness Analysis failed: {e}")
        
        # 6. Create Traditional Audio Analysis (Enhanced with Spectrograms)
        try:
            fig_main, axs = plt.subplots(4, 2, figsize=(16, 16), dpi=config.dpi)
            fig_main.patch.set_facecolor('#0F0F23')
            
            # Set all subplot backgrounds
            for ax in axs.flat:
                ax.set_facecolor('#1A1A2E')
            
            # Waveform with consciousness state overlay
            t = np.arange(len(audio)) / sample_rate
            axs[0, 0].plot(t, audio[:, 0], color='cyan', alpha=0.8, linewidth=0.5, label='Left')
            axs[0, 0].plot(t, audio[:, 1], color='magenta', alpha=0.7, linewidth=0.5, label='Right')
            
            # Add consciousness state regions if metadata available
            if metadata and 'phases' in metadata:
                phases = metadata['phases']
                state_sequence = metadata.get('consciousness_analysis', {}).get('state_sequence', [])
                cumulative_time = 0
                
                for i, phase in enumerate(phases):
                    duration = phase.get('duration', 0)
                    end_time = cumulative_time + duration
                    
                    if i < len(state_sequence):
                        state = state_sequence[i]
                        state_visual = CONSCIOUSNESS_STATE_VISUALS.get(state, CONSCIOUSNESS_STATE_VISUALS['alpha'])
                        
                        axs[0, 0].axvspan(cumulative_time, end_time, 
                                         color=state_visual['color'], alpha=0.2, 
                                         label=state.title() if i < 5 else "")
                    
                    cumulative_time = end_time
            
            axs[0, 0].set_title('Consciousness-Aware Waveform', color='white', fontsize=12)
            axs[0, 0].set_xlabel('Time (s)', color='white')
            axs[0, 0].set_ylabel('Amplitude', color='white')
            axs[0, 0].tick_params(colors='white')
            axs[0, 0].grid(True, alpha=0.3)
            legend = axs[0, 0].legend(loc='upper right', fontsize=8, framealpha=0.8)
            legend.get_frame().set_facecolor('#1A1A2E')
            for text in legend.get_texts():
                text.set_color('white')
            
            # Enhanced Power Spectrum with biofield markers
            fft_left = np.fft.rfft(audio[:, 0])
            freqs = np.fft.rfftfreq(len(audio[:, 0]), 1/sample_rate)
            power_db = 20 * np.log10(np.abs(fft_left) + 1e-10)
            power = np.abs(fft_left) ** 2  # Power spectrum for peak analysis
            
            axs[0, 1].semilogx(freqs[1:], power_db[1:], color='cyan', alpha=0.8, linewidth=1)
            axs[0, 1].fill_between(freqs[1:], power_db[1:], alpha=0.3, color='cyan')
            
            # Mark biofield frequencies
            for freq in BIOFIELD_FREQUENCY_VISUALS['schumann_resonances']['frequencies']:
                if 1 <= freq <= sample_rate/2:
                    axs[0, 1].axvline(freq, color='green', linestyle='--', alpha=0.7)
            
            for freq in [528, 432, 396, 417]:  # Key healing frequencies
                if 1 <= freq <= sample_rate/2:
                    axs[0, 1].axvline(freq, color='gold', linestyle=':', alpha=0.8)
            
            axs[0, 1].set_title('Biofield-Enhanced Power Spectrum', color='white', fontsize=12)
            axs[0, 1].set_xlabel('Frequency (Hz)', color='white')
            axs[0, 1].set_ylabel('Power (dB)', color='white')
            axs[0, 1].tick_params(colors='white')
            axs[0, 1].grid(True, alpha=0.3)
            axs[0, 1].set_xlim(1, min(1000, sample_rate/2))
            
            # **NEW: Spectrogram with Consciousness State Overlays**
            axs[1, 0].set_facecolor('#1A1A2E')
            
            # Generate spectrogram
            # Downsample if audio is too long to prevent memory issues
            max_samples = 500000  # ~11 seconds at 44.1kHz
            if len(audio) > max_samples:
                step = len(audio) // max_samples
                audio_ds = audio[::step]
                sr_ds = sample_rate // step
            else:
                audio_ds = audio
                sr_ds = sample_rate
            
            frequencies_spec, times_spec, Sxx = spectrogram(audio_ds[:, 0], sr_ds, 
                                                          nperseg=min(1024, len(audio_ds)//4),
                                                          noverlap=None)
            
            # Convert to dB and clip for better visualization
            Sxx_db = 10 * np.log10(np.abs(Sxx) + 1e-10)
            Sxx_db = np.clip(Sxx_db, np.percentile(Sxx_db, 5), np.percentile(Sxx_db, 95))
            
            # Plot spectrogram
            im_spec = axs[1, 0].pcolormesh(times_spec, frequencies_spec, Sxx_db, 
                                          shading='gouraud', cmap='plasma', alpha=0.8)
            
            # Mark biofield frequencies on spectrogram
            for freq in BIOFIELD_FREQUENCY_VISUALS['schumann_resonances']['frequencies']:
                if freq <= sr_ds / 2:
                    axs[1, 0].axhline(freq, color='green', alpha=0.7, linewidth=1, linestyle='--')
            
            for freq in [528, 432, 396, 417, 852]:  # Key healing frequencies
                if freq <= sr_ds / 2:
                    axs[1, 0].axhline(freq, color='gold', alpha=0.6, linewidth=1, linestyle=':')
            
            # Add consciousness state regions to spectrogram
            if metadata and 'phases' in metadata:
                phases = metadata['phases']
                state_sequence = metadata.get('consciousness_analysis', {}).get('state_sequence', [])
                cumulative_time = 0
                
                for i, phase in enumerate(phases):
                    duration = phase.get('duration', 0)
                    end_time = cumulative_time + duration
                    
                    if i < len(state_sequence) and end_time <= times_spec[-1]:
                        state = state_sequence[i]
                        state_visual = CONSCIOUSNESS_STATE_VISUALS.get(state, CONSCIOUSNESS_STATE_VISUALS['alpha'])
                        
                        # Vertical region for consciousness state
                        axs[1, 0].axvspan(cumulative_time, end_time, 
                                         color=state_visual['color'], alpha=0.15)
                        
                        # State label
                        mid_time = (cumulative_time + end_time) / 2
                        axs[1, 0].text(mid_time, sr_ds/2 * 0.9, state[:5], 
                                      rotation=90, fontsize=8, color='white', 
                                      ha='center', va='top', alpha=0.8)
                    
                    cumulative_time = end_time
            
            axs[1, 0].set_title('Consciousness-Aware Spectrogram', color='white', fontsize=12)
            axs[1, 0].set_xlabel('Time (s)', color='white')
            axs[1, 0].set_ylabel('Frequency (Hz)', color='white')
            axs[1, 0].tick_params(colors='white')
            axs[1, 0].set_ylim(0, min(100, sr_ds/2))  # Focus on lower frequencies
            
            # Add colorbar for spectrogram
            cbar_spec = plt.colorbar(im_spec, ax=axs[1, 0], shrink=0.8)
            cbar_spec.set_label('Power (dB)', color='white', fontsize=9)
            cbar_spec.ax.tick_params(colors='white', labelsize=8)
            
            # Phase Difference with coherence analysis
            phase_left = np.unwrap(np.angle(fft_left))
            fft_right = np.fft.rfft(audio[:, 1])
            phase_right = np.unwrap(np.angle(fft_right))
            phase_diff = phase_left - phase_right
            
            axs[1, 1].plot(freqs[1:100], phase_diff[1:100], color='orange', alpha=0.8)
            axs[1, 1].set_title('Phase Difference (Biofield Coherence)', color='white', fontsize=12)
            axs[1, 1].set_xlabel('Frequency (Hz)', color='white')
            axs[1, 1].set_ylabel('Phase Difference (rad)', color='white')
            axs[1, 1].tick_params(colors='white')
            axs[1, 1].grid(True, alpha=0.3)
            
            # Enhanced Coherence with consciousness markers
            nperseg = min(256, len(audio) // 4)
            f_coh, Cxy = coherence(audio[:, 0], audio[:, 1], fs=sample_rate, nperseg=nperseg)
            
            axs[2, 0].plot(f_coh, Cxy, color='lime', linewidth=2, alpha=0.8)
            axs[2, 0].fill_between(f_coh, Cxy, alpha=0.3, color='lime')
            
            # Coherence threshold lines
            axs[2, 0].axhline(y=0.7, color='green', linestyle='--', alpha=0.7, label='High Coherence')
            axs[2, 0].axhline(y=0.5, color='yellow', linestyle='--', alpha=0.7, label='Medium Coherence')
            
            axs[2, 0].set_title('Channel Coherence Analysis', color='white', fontsize=12)
            axs[2, 0].set_xlabel('Frequency (Hz)', color='white')
            axs[2, 0].set_ylabel('Coherence', color='white')
            axs[2, 0].tick_params(colors='white')
            axs[2, 0].grid(True, alpha=0.3)
            axs[2, 0].set_xlim(0, 50)
            legend = axs[2, 0].legend(loc='upper right', fontsize=9, framealpha=0.8)
            legend.get_frame().set_facecolor('#1A1A2E')
            for text in legend.get_texts():
                text.set_color('white')
            
            # Frequency Harmony Web/Network Visualization (New Feature)
            axs[2, 1].set_facecolor('#1A1A2E')
            
            # Find dominant frequency peaks for harmony analysis
            peak_threshold = np.percentile(power, 85)  # Top 15% of power
            peak_indices = np.where(power > peak_threshold)[0]
            dominant_freqs = freqs[peak_indices]
            dominant_powers = power[peak_indices]
            
            if len(dominant_freqs) > 1:
                # Create harmony web visualization
                for i, freq1 in enumerate(dominant_freqs[:8]):  # Limit to 8 peaks
                    for j, freq2 in enumerate(dominant_freqs[:8]):
                        if i < j and freq1 > 0:
                            # Calculate harmonic relationship
                            ratio = freq2 / freq1
                            # Check for simple harmonic ratios
                            simple_ratios = [2.0, 1.5, 1.33, 1.25, 1.2]  # Octave, 5th, 4th, maj3rd, etc.
                            
                            for target_ratio in simple_ratios:
                                if abs(ratio - target_ratio) / target_ratio < 0.1:
                                    # Draw connection line
                                    x_pos = [i * 0.1 + 0.1, j * 0.1 + 0.1]
                                    y_pos = [0.5 + i * 0.05, 0.5 + j * 0.05]
                                    
                                    alpha = min(1.0, (dominant_powers[i] + dominant_powers[j]) / (2 * np.max(dominant_powers)))
                                    axs[2, 1].plot(x_pos, y_pos, 'yellow', alpha=alpha, linewidth=2)
                                    break
                    
                    # Plot frequency node
                    axs[2, 1].scatter(i * 0.1 + 0.1, 0.5 + i * 0.05, 
                                     s=100 * dominant_powers[i] / np.max(dominant_powers),
                                     c='cyan', alpha=0.8, edgecolors='white')
                    
                    # Frequency label
                    axs[2, 1].text(i * 0.1 + 0.1, 0.3 + i * 0.05, f'{freq1:.0f}Hz',
                                  fontsize=8, color='white', ha='center')
            
            axs[2, 1].set_title('Frequency Harmony Network', color='white', fontsize=12)
            axs[2, 1].set_xlim(0, 1)
            axs[2, 1].set_ylim(0, 1)
            axs[2, 1].axis('off')
            
            # Metadata Summary with consciousness insights
            if metadata:
                session_overview = metadata.get('session_overview', {})
                consciousness_analysis = metadata.get('consciousness_analysis', {})
                biofield_analysis = metadata.get('biofield_analysis', {})
                
                summary_text = f"""
Session Analysis Summary:
Duration: {session_overview.get('total_duration', 0)//60:.0f}m {session_overview.get('total_duration', 0)%60:.0f}s
Intention: {session_overview.get('intention', 'Not specified').title()}
Phases: {session_overview.get('num_phases', 0)}

Consciousness Journey:
Quality: {consciousness_analysis.get('journey_quality_rating', 'Unknown').title()}
States: {len(consciousness_analysis.get('state_sequence', []))} transitions
Integration Windows: {len(consciousness_analysis.get('integration_windows', []))}

Biofield Analysis:
Overall Coherence: {biofield_analysis.get('coherence_metrics', {}).get('overall_coherence', 0):.3f}
Schumann Alignment: {biofield_analysis.get('coherence_metrics', {}).get('schumann_alignment', 0):.3f}
Solfeggio Presence: {biofield_analysis.get('coherence_metrics', {}).get('solfeggio_presence', 0):.3f}
                """
                
                if neural_profile:
                    summary_text += f"""
Neural Profile:
Sensitivity: {neural_profile.get('sensitivity_level', 'Unknown').title()}
Experience: {neural_profile.get('experience_level', 'Unknown').title()}
Current State: {neural_profile.get('current_state', 'Unknown').title()}
                """
                
                axs[3, 0].text(0.05, 0.95, summary_text, transform=axs[3, 0].transAxes, 
                              fontsize=10, color='white', verticalalignment='top', 
                              fontfamily='monospace',
                              bbox=dict(boxstyle='round,pad=0.5', facecolor='#2A2A4E', alpha=0.8))
                
                # Safety considerations
                safety_considerations = []
                if consciousness_analysis.get('safety_considerations'):
                    safety_considerations.extend(consciousness_analysis['safety_considerations'][:3])
                
                if biofield_analysis.get('safety_considerations'):
                    safety_considerations.extend(biofield_analysis['safety_considerations'][:2])
                
                if safety_considerations:
                    safety_text = "Safety Notes:\n" + "\n".join(f"• {note}" for note in safety_considerations)
                    axs[3, 0].text(0.05, 0.45, safety_text, transform=axs[3, 0].transAxes,
                                  fontsize=9, color='yellow', verticalalignment='top',
                                  bbox=dict(boxstyle='round,pad=0.3', facecolor='#4A2A00', alpha=0.8))
            else:
                axs[3, 0].text(0.5, 0.5, 'No consciousness metadata available', 
                              ha='center', va='center', transform=axs[3, 0].transAxes,
                              fontsize=12, color='white', alpha=0.6)
            
            axs[3, 0].set_xlim(0, 1)
            axs[3, 0].set_ylim(0, 1)
            axs[3, 0].axis('off')
            
            # Real-time consciousness state indicator
            axs[3, 1].set_facecolor('#1A1A2E')
            
            if metadata and 'consciousness_analysis' in metadata:
                state_sequence = metadata['consciousness_analysis'].get('state_sequence', [])
                coherence_progression = metadata['consciousness_analysis'].get('coherence_progression', [])
                
                if state_sequence and coherence_progression:
                    # Create consciousness state flow
                    for i, (state, coherence_val) in enumerate(zip(state_sequence, coherence_progression)):
                        state_visual = CONSCIOUSNESS_STATE_VISUALS.get(state, CONSCIOUSNESS_STATE_VISUALS['alpha'])
                        
                        # State circle with proper clipping
                        circle = patches.Circle((i * 0.15 + 0.1, 0.7), 0.05, 
                                              color=state_visual['color'], 
                                              alpha=np.clip(coherence_val, 0.3, 1.0))
                        axs[3, 1].add_patch(circle)
                        
                        # State label
                        axs[3, 1].text(i * 0.15 + 0.1, 0.55, state[:4], 
                                      ha='center', va='center', fontsize=8, color='white')
                        
                        # Coherence value
                        axs[3, 1].text(i * 0.15 + 0.1, 0.45, f'{coherence_val:.2f}', 
                                      ha='center', va='center', fontsize=7, color='white', alpha=0.8)
                
                axs[3, 1].text(0.5, 0.9, 'Consciousness State Flow', 
                              ha='center', va='center', transform=axs[3, 1].transAxes,
                              fontsize=11, color='white', weight='bold')
                axs[3, 1].text(0.5, 0.3, '(Size = Coherence Level)', 
                              ha='center', va='center', transform=axs[3, 1].transAxes,
                              fontsize=9, color='white', alpha=0.7)
            else:
                axs[3, 1].text(0.5, 0.5, 'No consciousness\nstate data', 
                              ha='center', va='center', transform=axs[3, 1].transAxes,
                              fontsize=11, color='white', alpha=0.6)
            
            axs[3, 1].set_xlim(0, 1)
            axs[3, 1].set_ylim(0, 1)
            axs[3, 1].axis('off')
            
            # Overall title with consciousness awareness
            intention_title = "Enhanced Consciousness-Aware Neural Entrainment Analysis"
            if metadata and 'session_overview' in metadata:
                intention = metadata['session_overview'].get('intention', '')
                if intention:
                    intention_title += f" - {intention.title()} Session"
            
            fig_main.suptitle(intention_title, fontsize=16, color='white', fontweight='bold')
            
            # Save comprehensive analysis
            plt.tight_layout(rect=[0, 0, 1, 0.93])
            if config.save_figures:
                output_path = Path(config.output_dir)
                output_path.mkdir(exist_ok=True)
                fig_main.savefig(output_path / 'comprehensive_consciousness_analysis.png', 
                                dpi=config.dpi, bbox_inches='tight', facecolor='#0F0F23')
            plt.close(fig_main)
            logging.info("Enhanced consciousness analysis visualization complete")
            
        except Exception as e:
            logging.error(f"Enhanced audio analysis failed: {e}")
        
        # Display completion message with output paths
        if config.save_figures:
            output_path = Path(config.output_dir)
            logging.info(f"All consciousness-aware visualizations saved to: {output_path.absolute()}")
            logging.info("Generated files:")
            logging.info("• consciousness_journey_3d.png - 3D consciousness journey")
            logging.info("• neural_architecture_dashboard.png - Neural profile dashboard")
            logging.info("• biofield_intelligence_analysis.png - Biofield coherence analysis")
            logging.info("• safety_monitoring_dashboard.png - Safety monitoring")
            logging.info("• integration_effectiveness_analysis.png - Integration analysis")
            logging.info("• comprehensive_consciousness_analysis.png - Enhanced complete analysis")
        else:
            logging.info("All consciousness-aware visualizations complete (figures not saved)")
        
        # Return output path for external use
        return Path(config.output_dir) if config.save_figures else None
        
    except Exception as e:
        logging.error(f"Comprehensive visualization failed: {e}")
        raise

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# LEGACY COMPATIBILITY FUNCTIONS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def plot_animated_consciousness_journey(metadata: Dict[str, Any], 
                                      neural_profile: Optional[Dict[str, Any]] = None,
                                      config: VisualizationConfig = VisualizationConfig()) -> plt.Figure:
    """
    Create an animated 3D consciousness journey visualization.
    
    Args:
        metadata: Complete session metadata with consciousness analysis
        neural_profile: Neural profile for adaptation
        config: Visualization configuration
        
    Returns:
        Animated matplotlib figure with rotating 3D consciousness journey
    """
    if not config.animation_enabled:
        logging.info("Animation disabled, using static visualization")
        return plot_consciousness_journey_3D(metadata, neural_profile, config)
    
    try:
        # Create base 3D figure
        fig = plot_consciousness_journey_3D(metadata, neural_profile, config)
        ax = fig.axes[0]  # Get the 3D axis
        
        # Animation function
        def animate_rotation(frame):
            ax.view_init(elev=30, azim=30 + frame * 2)  # Slow rotation
            return ax.collections + ax.lines + ax.texts
        
        # Create animation
        anim = animation.FuncAnimation(fig, animate_rotation, frames=180, 
                                     interval=100, blit=False, repeat=True)
        
        # Save animation if requested
        if config.save_figures:
            output_path = Path(config.output_dir)
            output_path.mkdir(exist_ok=True)
            try:
                anim.save(output_path / 'consciousness_journey_animated.gif', 
                         writer='pillow', fps=10)
                logging.info("Animated consciousness journey saved as GIF")
            except Exception as e:
                logging.warning(f"Could not save animation: {e}")
        
        return fig
    
    except Exception as e:
        logging.error(f"Animation creation failed: {e}")
        return plot_consciousness_journey_3D(metadata, neural_profile, config)

def create_comprehensive_report(audio: np.ndarray, sample_rate: int,
                              metadata: Optional[Dict[str, Any]] = None,
                              neural_profile: Optional[Dict[str, Any]] = None,
                              config: Optional[VisualizationConfig] = None) -> Dict[str, Any]:
    """
    Create a comprehensive consciousness analysis report with all visualizations.
    
    Args:
        audio: Audio signal data
        sample_rate: Sample rate
        metadata: Session metadata
        neural_profile: Neural profile
        config: Visualization configuration
        
    Returns:
        Dictionary with all generated visualizations and analysis
    """
    if config is None:
        config = VisualizationConfig()
    
    logging.info("Creating comprehensive consciousness analysis report...")
    
    # Ensure output directory exists
    output_path = Path(config.output_dir)
    output_path.mkdir(exist_ok=True)
    
    report = {
        'timestamp': datetime.datetime.now().isoformat(),
        'config': config.__dict__,
        'output_directory': str(output_path.absolute()),
        'generated_files': [],
        'analysis_summary': {}
    }
    
    try:
        # Generate all visualizations
        visualize_audio(audio, sample_rate, metadata, neural_profile, config)
        
        # Check which files were generated
        expected_files = [
            'consciousness_journey_3d.png',
            'neural_architecture_dashboard.png',
            'biofield_intelligence_analysis.png', 
            'safety_monitoring_dashboard.png',
            'integration_effectiveness_analysis.png',
            'comprehensive_consciousness_analysis.png'
        ]
        
        for filename in expected_files:
            file_path = output_path / filename
            if file_path.exists():
                report['generated_files'].append(str(file_path))
        
        # Extract analysis summary from metadata
        if metadata:
            session_overview = metadata.get('session_overview', {})
            consciousness_analysis = metadata.get('consciousness_analysis', {})
            biofield_analysis = metadata.get('biofield_analysis', {})
            
            report['analysis_summary'] = {
                'duration': session_overview.get('total_duration', 0),
                'intention': session_overview.get('intention', 'unknown'),
                'journey_quality': consciousness_analysis.get('journey_quality_rating', 'unknown'),
                'biofield_coherence': biofield_analysis.get('coherence_metrics', {}).get('overall_coherence', 0),
                'integration_windows': len(consciousness_analysis.get('integration_windows', [])),
                'neural_profile': neural_profile.get('sensitivity_level', 'unknown') if neural_profile else 'none'
            }
        
        logging.info(f"Comprehensive report complete: {len(report['generated_files'])} files generated")
        
    except Exception as e:
        logging.error(f"Report generation failed: {e}")
        report['error'] = str(e)
    
    return report

def plot_consciousness_journey(metadata: Dict[str, Any], figsize: tuple = (14, 10)) -> plt.Figure:
    """Legacy compatibility function for basic consciousness journey plotting."""
    return plot_consciousness_journey_3D(metadata, None, VisualizationConfig(figure_size=figsize))

def plot_biofield_coherence_analysis(audio: np.ndarray, sample_rate: int, 
                                    metadata: Optional[Dict[str, Any]] = None) -> plt.Figure:
    """Legacy compatibility function for biofield coherence analysis."""
    return plot_biofield_intelligence_analysis(audio, sample_rate, metadata, VisualizationConfig())

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
__description__ = "Consciousness journey visualizer with advanced biofield intelligence analysis"

# Export public API
__all__ = [
    # Main visualization functions
    'visualize_audio',
    'plot_consciousness_journey_3D',
    'plot_neural_architecture_dashboard',
    'plot_biofield_intelligence_analysis',
    'plot_safety_monitoring_dashboard',
    'plot_integration_effectiveness_analysis',
    
    # New enhanced functions
    'plot_animated_consciousness_journey',
    'create_comprehensive_report',
    
    # Configuration
    'VisualizationConfig',
    
    # Legacy compatibility
    'plot_consciousness_journey',
    'plot_biofield_coherence_analysis',
    
    # Utilities
    'create_consciousness_colormap',
    'create_biofield_colormap',
    
    # Constants for customization
    'CONSCIOUSNESS_STATE_VISUALS',
    'NEURAL_SENSITIVITY_VISUALS',
    'BIOFIELD_FREQUENCY_VISUALS',
    'SAFETY_LEVEL_VISUALS',
    'INTENTION_VISUALS'
]

logging.info(f"Consciousness Journey Visualizer v{__version__} initialized - "
            f"Advanced consciousness visualization with biofield intelligence ready")