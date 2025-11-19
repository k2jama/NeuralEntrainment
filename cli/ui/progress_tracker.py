#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Progress Tracker UI Component
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Progress Tracker UI Component - Session progress tracking and phase visualization.

This module provides comprehensive session progress visualization including:
- Real-time session progress tracking with phase transitions
- Consciousness journey mapping and milestone tracking
- Phase-specific progress indicators and time remaining
- Session completion estimation and adaptive timing
- Integration period tracking and preparation
- Historical progress comparison and session insights
"""

import time
import math
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta

from ..themes.consciousness_colors import ConsciousnessColorScheme
from ..themes.sacred_geometry import SacredGeometrySymbols, ConsciousnessVisualization
from ..themes.biofield_aesthetics import BiofieldAesthetics
from ...src.interfaces.cli_interface import TerminalConsciousnessAdapter

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROGRESS TRACKING CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Phase status constants
PHASE_STATUS_PENDING = "pending"
PHASE_STATUS_ACTIVE = "active"  
PHASE_STATUS_COMPLETED = "completed"
PHASE_STATUS_TRANSITIONING = "transitioning"

# Progress milestone markers
PROGRESS_MILESTONES = {
    0.0: {'name': 'Session Start', 'symbol': '🌱', 'description': 'Beginning consciousness journey'},
    0.25: {'name': 'First Quarter', 'symbol': '🌓', 'description': 'Initial states established'},
    0.5: {'name': 'Midpoint', 'symbol': '🌕', 'description': 'Peak consciousness experience'},
    0.75: {'name': 'Final Quarter', 'symbol': '🌗', 'description': 'Integration beginning'},
    1.0: {'name': 'Completion', 'symbol': '🌟', 'description': 'Journey complete'}
}

# Session phases categorization
PHASE_CATEGORIES = {
    'preparation': {'symbol': '🌱', 'color': 'gentle_text', 'description': 'Preparation'},
    'entrainment': {'symbol': '🌊', 'color': 'consciousness_accent', 'description': 'Neural Entrainment'},
    'peak': {'symbol': '⭐', 'color': 'biofield_accent', 'description': 'Peak Experience'},
    'integration': {'symbol': '🤲', 'color': 'neural_profile', 'description': 'Integration'},
    'completion': {'symbol': '🙏', 'color': 'status_safe', 'description': 'Completion'}
}

# Time estimation factors
TIME_ESTIMATION_WINDOW = 5  # minutes for adaptive timing
PROGRESS_SMOOTHING_FACTOR = 0.8
COMPLETION_CONFIDENCE_THRESHOLD = 0.85

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# PROGRESS TRACKER CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ProgressTracker:
    """
    Comprehensive session progress tracking and visualization component.
    
    This class provides real-time session progress monitoring including phase
    transitions, consciousness journey mapping, milestone tracking, and adaptive
    time estimation in a beautiful consciousness-aware terminal interface.
    """
    
    def __init__(self, terminal_adapter: TerminalConsciousnessAdapter):
        self.terminal_adapter = terminal_adapter
        self.color_scheme = ConsciousnessColorScheme()
        self.symbols = SacredGeometrySymbols()
        self.consciousness_viz = ConsciousnessVisualization()
        self.biofield = BiofieldAesthetics()
        
        # Progress tracking state
        self.session_start_time = None
        self.session_duration = 0
        self.total_session_duration = 1800  # Default 30 minutes
        self.overall_progress = 0.0
        self.current_phase_index = 0
        self.current_phase_progress = 0.0
        
        # Phase data
        self.phases = []
        self.phase_status = {}
        self.phase_start_times = {}
        self.completed_milestones = set()
        
        # Progress history for adaptive estimation
        self.progress_history = []
        self.time_history = []
        
        # Animation and display state
        self.animation_frame = 0
        self.last_update = time.time()
        self.progress_animations = {}
    
    def initialize_session(self, 
                          phases: List[Dict[str, Any]], 
                          total_duration: int,
                          start_time: datetime = None) -> None:
        """
        Initialize progress tracking for a new session.
        
        Args:
            phases: List of session phases with duration and metadata
            total_duration: Total session duration in seconds
            start_time: Session start time (defaults to now)
        """
        self.phases = phases.copy()
        self.total_session_duration = total_duration
        self.session_start_time = start_time or datetime.now()
        
        # Initialize phase tracking
        self.phase_status = {}
        self.phase_start_times = {}
        
        for i, phase in enumerate(self.phases):
            self.phase_status[i] = PHASE_STATUS_PENDING
            
        # Set first phase as active
        if self.phases:
            self.phase_status[0] = PHASE_STATUS_ACTIVE
            self.phase_start_times[0] = self.session_start_time
        
        # Reset progress tracking
        self.overall_progress = 0.0
        self.current_phase_index = 0
        self.current_phase_progress = 0.0
        self.completed_milestones.clear()
        self.progress_history.clear()
        self.time_history.clear()
    
    def update_progress(self, 
                       elapsed_time: float,
                       current_phase: int = None,
                       phase_progress: float = None) -> None:
        """
        Update session progress with current timing information.
        
        Args:
            elapsed_time: Total elapsed session time in seconds
            current_phase: Current active phase index (optional)
            phase_progress: Progress within current phase (0.0-1.0, optional)
        """
        self.session_duration = elapsed_time
        self.overall_progress = min(1.0, elapsed_time / self.total_session_duration)
        
        # Update phase information if provided
        if current_phase is not None:
            self._update_phase_status(current_phase)
        
        if phase_progress is not None:
            self.current_phase_progress = phase_progress
        else:
            # Calculate phase progress from elapsed time
            self.current_phase_progress = self._calculate_current_phase_progress(elapsed_time)
        
        # Update progress history for adaptive estimation
        self._update_progress_history(elapsed_time, self.overall_progress)
        
        # Check for milestone completion
        self._check_milestone_completion()
        
        # Update phase timings
        self._update_phase_timings()
    
    def show_session_progress(self, 
                            show_details: bool = True,
                            show_timeline: bool = True) -> None:
        """
        Display comprehensive session progress information.
        
        Args:
            show_details: Whether to show detailed phase information
            show_timeline: Whether to show consciousness journey timeline
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        # Progress header
        print(f"\n{colors.consciousness_header('✨' * 60)}")
        print(f"{colors.consciousness_title('✨ Session Progress Tracker')}")
        print(f"{colors.consciousness_header('✨' * 60)}")
        
        # Overall progress display
        self._display_overall_progress()
        
        # Current phase information
        if self.phases:
            self._display_current_phase_info()
        
        # Timeline visualization
        if show_timeline and self.phases:
            self._display_consciousness_timeline()
        
        # Detailed phase breakdown
        if show_details and self.phases:
            self._display_phase_details()
        
        # Time estimates and predictions
        self._display_time_estimates()
        
        # Recent milestones
        if self.completed_milestones:
            self._display_recent_milestones()
    
    def show_phase_transitions(self, 
                             transition_duration: float = 30.0) -> None:
        """
        Display phase transition visualization.
        
        Args:
            transition_duration: Duration of transition animation in seconds
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        if not self.phases or self.current_phase_index >= len(self.phases):
            return
        
        current_phase = self.phases[self.current_phase_index]
        next_phase_index = self.current_phase_index + 1
        
        print(f"\n{colors.consciousness_header('🔄' * 50)}")
        print(f"{colors.consciousness_title('🔄 Phase Transition')}")
        print(f"{colors.consciousness_header('🔄' * 50)}")
        
        # Current phase information
        current_name = current_phase.get('name', f'Phase {self.current_phase_index + 1}')
        current_state = current_phase.get('consciousness_target_state', 'neutral')
        
        print(f"\n{colors.biofield_accent('Completing:')} {colors.consciousness_accent(current_name)}")
        print(f"{colors.biofield_accent('State:')} {colors.get_consciousness_state_color(current_state)(current_state.title())}")
        
        # Next phase information
        if next_phase_index < len(self.phases):
            next_phase = self.phases[next_phase_index]
            next_name = next_phase.get('name', f'Phase {next_phase_index + 1}')
            next_state = next_phase.get('consciousness_target_state', 'neutral')
            
            print(f"\n{colors.biofield_accent('Transitioning to:')} {colors.consciousness_accent(next_name)}")
            print(f"{colors.biofield_accent('Target State:')} {colors.get_consciousness_state_color(next_state)(next_state.title())}")
            
            # Transition visualization
            if self.terminal_adapter.capabilities.supports_unicode:
                transition_viz = self._create_phase_transition_visualization(
                    current_state, next_state, self.current_phase_progress
                )
                print(f"\n{colors.gentle_text('Consciousness Transition:')}")
                for line in transition_viz:
                    print(f"  {line}")
        else:
            print(f"\n{colors.consciousness_accent('Approaching session completion...')}")
    
    def show_progress_analytics(self) -> None:
        """Display progress analytics and insights."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_header('📊' * 50)}")
        print(f"{colors.consciousness_title('📊 Progress Analytics')}")
        print(f"{colors.consciousness_header('📊' * 50)}")
        
        # Session statistics
        elapsed_minutes = self.session_duration / 60
        progress_rate = self.overall_progress / (elapsed_minutes / 60) if elapsed_minutes > 0 else 0
        
        print(f"\n{colors.biofield_accent('Session Statistics:')}")
        print(f"  Elapsed Time: {colors.gentle_text(self._format_duration(self.session_duration))}")
        print(f"  Overall Progress: {colors.consciousness_accent(f'{self.overall_progress:.1%}')}")
        print(f"  Progress Rate: {colors.gentle_text(f'{progress_rate:.2f}x real-time')}")
        
        # Phase completion analysis
        completed_phases = sum(1 for status in self.phase_status.values() if status == PHASE_STATUS_COMPLETED)
        total_phases = len(self.phases)
        
        if total_phases > 0:
            phase_completion_rate = completed_phases / total_phases
            print(f"  Phase Completion: {colors.neural_profile(f'{completed_phases}/{total_phases} ({phase_completion_rate:.1%})')}")
        
        # Milestone analysis
        milestone_count = len(self.completed_milestones)
        print(f"  Milestones Reached: {colors.biofield_accent(str(milestone_count))}")
        
        # Progress trend analysis
        if len(self.progress_history) > 3:
            trend = self._analyze_progress_trend()
            trend_color = colors.status_safe if trend == 'steady' else colors.status_caution
            print(f"  Progress Trend: {trend_color(trend.title())}")
        
        # Estimated completion
        estimated_completion = self._estimate_completion_time()
        if estimated_completion:
            print(f"  Estimated Completion: {colors.consciousness_accent(estimated_completion.strftime('%H:%M:%S'))}")
    
    def _display_overall_progress(self) -> None:
        """Display overall session progress."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        # Progress bar with milestones marked
        progress_bar = self._create_milestone_progress_bar(self.overall_progress, 50)
        elapsed_time = self._format_duration(self.session_duration)
        total_time = self._format_duration(self.total_session_duration)
        
        print(f"\n{colors.consciousness_accent('Overall Progress:')}")
        print(f"  {progress_bar}")
        print(f"  {colors.gentle_text(f'Time: {elapsed_time} / {total_time} ({self.overall_progress:.1%})')}")
    
    def _display_current_phase_info(self) -> None:
        """Display current phase information."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        if self.current_phase_index >= len(self.phases):
            print(f"\n{colors.consciousness_accent('Session Complete - Integration Period')}")
            return
        
        current_phase = self.phases[self.current_phase_index]
        phase_name = current_phase.get('name', f'Phase {self.current_phase_index + 1}')
        consciousness_state = current_phase.get('consciousness_target_state', 'neutral')
        phase_duration = current_phase.get('duration', 300)
        
        # Phase category
        phase_category = self._get_phase_category(current_phase)
        category_info = PHASE_CATEGORIES.get(phase_category, PHASE_CATEGORIES['entrainment'])
        
        print(f"\n{colors.consciousness_accent('Current Phase:')}")
        print(f"  {category_info['symbol']} {colors.consciousness_accent(phase_name)} "
              f"({self.current_phase_index + 1}/{len(self.phases)})")
        
        state_color = colors.get_consciousness_state_color(consciousness_state)
        print(f"  Target State: {state_color(consciousness_state.title())}")
        
        # Phase progress
        phase_progress_bar = colors.create_progress_bar(self.current_phase_progress, 30)
        remaining_phase_time = phase_duration * (1.0 - self.current_phase_progress)
        
        print(f"  Progress: {phase_progress_bar}")
        print(f"  Remaining: {colors.gentle_text(self._format_duration(remaining_phase_time))}")
    
    def _display_consciousness_timeline(self) -> None:
        """Display consciousness journey timeline."""
        
        colors = self.color_scheme
        
        print(f"\n{colors.consciousness_accent('Consciousness Journey Timeline:')}")
        
        # Extract consciousness states for timeline
        phase_states = []
        for phase in self.phases:
            state = phase.get('consciousness_target_state', 'neutral')
            phase_states.append(state)
        
        # Create timeline visualization
        timeline_viz = self.consciousness_viz.create_consciousness_journey_line(
            phase_states, self.current_phase_index, 55
        )
        
        for line in timeline_viz:
            print(f"  {line}")
    
    def _display_phase_details(self) -> None:
        """Display detailed phase information."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_accent('Phase Details:')}")
        
        for i, phase in enumerate(self.phases):
            phase_name = phase.get('name', f'Phase {i + 1}')
            consciousness_state = phase.get('consciousness_target_state', 'neutral')
            duration = phase.get('duration', 300)
            
            # Phase status
            status = self.phase_status.get(i, PHASE_STATUS_PENDING)
            
            if status == PHASE_STATUS_COMPLETED:
                status_symbol = colors.status_safe('✓')
            elif status == PHASE_STATUS_ACTIVE:
                status_symbol = colors.consciousness_accent('●')
            elif status == PHASE_STATUS_TRANSITIONING:
                status_symbol = colors.biofield_accent('◐')
            else:
                status_symbol = colors.gentle_text('○')
            
            # Phase category
            phase_category = self._get_phase_category(phase)
            category_info = PHASE_CATEGORIES.get(phase_category, PHASE_CATEGORIES['entrainment'])
            category_symbol = category_info['symbol']
            
            state_color = colors.get_consciousness_state_color(consciousness_state)
            
            print(f"  {status_symbol} {i+1:2}. {category_symbol} {colors.gentle_text(phase_name)} "
                  f"→ {state_color(consciousness_state)} "
                  f"({colors.gentle_text(self._format_duration(duration))})")
    
    def _display_time_estimates(self) -> None:
        """Display time estimates and predictions."""
        
        colors = self.color_scheme
        
        print(f"\n{colors.consciousness_accent('Time Estimates:')}")
        
        # Remaining time (basic calculation)
        remaining_time = self.total_session_duration - self.session_duration
        print(f"  Time Remaining: {colors.gentle_text(self._format_duration(max(0, remaining_time)))}")
        
        # Adaptive completion estimate
        estimated_completion = self._estimate_completion_time()
        if estimated_completion:
            print(f"  Estimated Completion: {colors.consciousness_accent(estimated_completion.strftime('%H:%M:%S'))}")
        
        # Session efficiency
        if self.overall_progress > 0:
            efficiency = self.overall_progress / (self.session_duration / self.total_session_duration)
            efficiency_text = f"{efficiency:.1%}"
            efficiency_color = colors.status_safe if efficiency >= 0.95 else colors.gentle_text
            print(f"  Session Efficiency: {efficiency_color(efficiency_text)}")
    
    def _display_recent_milestones(self) -> None:
        """Display recently completed milestones."""
        
        colors = self.color_scheme
        
        # Get recent milestones (completed in this session)
        recent_milestones = []
        for progress_value in self.completed_milestones:
            if progress_value in PROGRESS_MILESTONES:
                milestone = PROGRESS_MILESTONES[progress_value]
                recent_milestones.append((progress_value, milestone))
        
        if recent_milestones:
            print(f"\n{colors.consciousness_accent('Milestones Achieved:')}")
            
            # Sort by progress value
            recent_milestones.sort(key=lambda x: x[0])
            
            for progress_value, milestone in recent_milestones[-3:]:  # Show last 3
                symbol = milestone['symbol']
                name = milestone['name']
                description = milestone['description']
                
                print(f"  {symbol} {colors.biofield_accent(name)} - {colors.gentle_text(description)}")
    
    def _create_milestone_progress_bar(self, progress: float, width: int) -> str:
        """Create progress bar with milestone markers."""
        
        colors = self.color_scheme
        
        filled = int(progress * width)
        
        bar = ""
        for i in range(width):
            pos = i / width
            
            # Check if this position is a milestone
            is_milestone = False
            for milestone_progress in PROGRESS_MILESTONES.keys():
                if abs(pos - milestone_progress) < 0.02:  # Within 2% tolerance
                    is_milestone = True
                    break
            
            if i < filled:
                if is_milestone:
                    bar += colors.biofield_accent('◆')
                else:
                    bar += colors.consciousness_accent('█')
            else:
                if is_milestone:
                    if milestone_progress in self.completed_milestones:
                        bar += colors.status_safe('◇')
                    else:
                        bar += colors.gentle_text('◇')
                else:
                    bar += colors.gentle_text('░')
        
        return f"[{bar}] {progress:.1%}"
    
    def _create_phase_transition_visualization(self, 
                                             from_state: str, 
                                             to_state: str,
                                             progress: float) -> List[str]:
        """Create phase transition visualization."""
        
        lines = []
        colors = self.color_scheme
        width = 40
        
        # State symbols
        from_symbol = self._get_consciousness_symbol(from_state)
        to_symbol = self._get_consciousness_symbol(to_state)
        
        # Create transition line
        transition_pos = int(progress * (width - 6))
        
        line = f"{from_symbol} "
        
        for i in range(width - 6):
            if i == transition_pos:
                line += colors.consciousness_accent('●')
            elif i < transition_pos:
                line += colors.gentle_text('─')
            else:
                line += colors.gentle_text('╌')
        
        line += f" {to_symbol}"
        
        lines.append(line)
        
        # Progress information
        from_color = colors.get_consciousness_state_color(from_state)
        to_color = colors.get_consciousness_state_color(to_state)
        
        transition_info = f"{from_color(from_state)} → {to_color(to_state)} ({progress:.1%})"
        lines.append(transition_info.center(width))
        
        return lines
    
    def _get_consciousness_symbol(self, consciousness_state: str) -> str:
        """Get symbol for consciousness state."""
        
        symbols = self.symbols
        
        symbol_mapping = {
            'deep_delta': symbols.FILLED_CIRCLE,
            'delta': symbols.CIRCLE,
            'theta': symbols.DIAMOND,
            'alpha': symbols.TRIANGLE_UP,
            'beta': symbols.SQUARE,
            'gamma': symbols.STAR,
            'neutral': symbols.CIRCLE
        }
        
        return symbol_mapping.get(consciousness_state, symbols.CIRCLE)
    
    def _get_phase_category(self, phase: Dict[str, Any]) -> str:
        """Determine phase category from phase data."""
        
        # Try explicit category first
        if 'category' in phase:
            return phase['category']
        
        # Infer from phase name
        phase_name = phase.get('name', '').lower()
        
        if 'prep' in phase_name or 'ground' in phase_name:
            return 'preparation'
        elif 'integrat' in phase_name or 'rest' in phase_name or 'consolidat' in phase_name:
            return 'integration'
        elif 'peak' in phase_name or 'climax' in phase_name or 'transcend' in phase_name:
            return 'peak'
        elif 'complet' in phase_name or 'end' in phase_name or 'finish' in phase_name:
            return 'completion'
        else:
            return 'entrainment'
    
    def _update_phase_status(self, new_phase_index: int) -> None:
        """Update phase status based on current phase."""
        
        if new_phase_index != self.current_phase_index:
            # Mark previous phase as completed
            if self.current_phase_index < len(self.phases):
                self.phase_status[self.current_phase_index] = PHASE_STATUS_COMPLETED
            
            # Set new phase as active
            if new_phase_index < len(self.phases):
                self.phase_status[new_phase_index] = PHASE_STATUS_ACTIVE
                self.phase_start_times[new_phase_index] = datetime.now()
            
            self.current_phase_index = new_phase_index
    
    def _calculate_current_phase_progress(self, elapsed_time: float) -> float:
        """Calculate progress within current phase."""
        
        if self.current_phase_index >= len(self.phases):
            return 1.0
        
        # Calculate phase start time
        phase_start_time = 0
        for i in range(self.current_phase_index):
            if i < len(self.phases):
                phase_start_time += self.phases[i].get('duration', 300)
        
        # Calculate progress within current phase
        current_phase = self.phases[self.current_phase_index]
        phase_duration = current_phase.get('duration', 300)
        phase_elapsed = elapsed_time - phase_start_time
        
        return min(1.0, max(0.0, phase_elapsed / phase_duration))
    
    def _update_progress_history(self, elapsed_time: float, progress: float) -> None:
        """Update progress history for adaptive estimation."""
        
        self.time_history.append(elapsed_time)
        self.progress_history.append(progress)
        
        # Keep only recent history (last 10 data points)
        max_history = 10
        if len(self.progress_history) > max_history:
            self.progress_history = self.progress_history[-max_history:]
            self.time_history = self.time_history[-max_history:]
    
    def _check_milestone_completion(self) -> None:
        """Check if any new milestones have been completed."""
        
        for milestone_progress in PROGRESS_MILESTONES.keys():
            if (self.overall_progress >= milestone_progress and 
                milestone_progress not in self.completed_milestones):
                self.completed_milestones.add(milestone_progress)
    
    def _update_phase_timings(self) -> None:
        """Update phase timing information."""
        
        # This would update adaptive phase timing based on actual progress
        # For now, we'll keep it simple
        pass
    
    def _estimate_completion_time(self) -> Optional[datetime]:
        """Estimate session completion time based on progress trend."""
        
        if len(self.progress_history) < 3 or self.overall_progress <= 0:
            return None
        
        # Simple linear regression on recent progress
        recent_times = self.time_history[-5:]
        recent_progress = self.progress_history[-5:]
        
        if len(recent_times) < 2:
            return None
        
        # Calculate progress rate
        time_diff = recent_times[-1] - recent_times[0]
        progress_diff = recent_progress[-1] - recent_progress[0]
        
        if time_diff <= 0 or progress_diff <= 0:
            return None
        
        progress_rate = progress_diff / time_diff
        
        # Estimate remaining time
        remaining_progress = 1.0 - self.overall_progress
        estimated_remaining_time = remaining_progress / progress_rate
        
        # Add to current time
        completion_time = datetime.now() + timedelta(seconds=estimated_remaining_time)
        
        return completion_time
    
    def _analyze_progress_trend(self) -> str:
        """Analyze progress trend from history."""
        
        if len(self.progress_history) < 3:
            return 'unknown'
        
        recent_progress = self.progress_history[-3:]
        
        # Calculate trend
        if all(recent_progress[i] >= recent_progress[i-1] * 0.95 for i in range(1, len(recent_progress))):
            return 'steady'
        elif recent_progress[-1] > recent_progress[0] * 1.1:
            return 'accelerating'
        else:
            return 'variable'
    
    def _format_duration(self, seconds: float) -> str:
        """Format duration in human-readable format."""
        
        if seconds < 60:
            return f"{seconds:.0f}s"
        elif seconds < 3600:
            minutes = seconds // 60
            remaining_seconds = seconds % 60
            if remaining_seconds == 0:
                return f"{minutes:.0f}m"
            else:
                return f"{minutes:.0f}m {remaining_seconds:.0f}s"
        else:
            hours = seconds // 3600
            remaining_minutes = (seconds % 3600) // 60
            return f"{hours:.0f}h {remaining_minutes:.0f}m"
    
    def update_animation_frame(self) -> None:
        """Update animation frame for continuous animations."""
        current_time = time.time()
        if current_time - self.last_update > 0.5:
            self.animation_frame += 1
            self.last_update = current_time
    
    def get_completion_percentage(self) -> float:
        """Get overall session completion percentage."""
        return self.overall_progress * 100
    
    def get_current_phase_name(self) -> str:
        """Get current phase name."""
        if self.current_phase_index < len(self.phases):
            return self.phases[self.current_phase_index].get('name', f'Phase {self.current_phase_index + 1}')
        else:
            return 'Session Complete'
    
    def get_estimated_remaining_time(self) -> float:
        """Get estimated remaining time in seconds."""
        return max(0, self.total_session_duration - self.session_duration)