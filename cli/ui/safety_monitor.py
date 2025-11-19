#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Safety Monitor UI Component
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Safety Monitor UI Component - Neural load and safety protocol visualization.

This module provides comprehensive safety monitoring visualization including:
- Real-time neural load monitoring with safety thresholds
- Comfort level tracking and user feedback integration
- Safety protocol status and alert display
- Emergency controls and rapid response indicators
- Neural architecture compatibility monitoring
- Session safety analytics and trend visualization
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
# SAFETY MONITORING CONSTANTS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# Safety threshold definitions
NEURAL_LOAD_THRESHOLDS = {
    'safe': {'range': (0.0, 0.6), 'color': 'status_safe', 'symbol': '✓', 'description': 'Safe'},
    'caution': {'range': (0.6, 0.8), 'color': 'status_caution', 'symbol': '⚠', 'description': 'Caution'},
    'warning': {'range': (0.8, 0.9), 'color': 'status_warning', 'symbol': '⚠', 'description': 'Warning'},
    'critical': {'range': (0.9, 1.0), 'color': 'status_danger', 'symbol': '🚨', 'description': 'Critical'}
}

COMFORT_LEVEL_THRESHOLDS = {
    'very_comfortable': {'range': (0.8, 1.0), 'color': 'status_safe', 'symbol': '😊', 'description': 'Very Comfortable'},
    'comfortable': {'range': (0.6, 0.8), 'color': 'status_safe', 'symbol': '😌', 'description': 'Comfortable'},
    'neutral': {'range': (0.4, 0.6), 'color': 'gentle_text', 'symbol': '😐', 'description': 'Neutral'},
    'uncomfortable': {'range': (0.2, 0.4), 'color': 'status_caution', 'symbol': '😟', 'description': 'Uncomfortable'},
    'very_uncomfortable': {'range': (0.0, 0.2), 'color': 'status_danger', 'symbol': '😰', 'description': 'Very Uncomfortable'}
}

# Safety protocol status
SAFETY_PROTOCOL_STATUS = {
    'active': {'color': 'status_active', 'symbol': '●', 'description': 'Active'},
    'standby': {'color': 'status_caution', 'symbol': '◐', 'description': 'Standby'},
    'inactive': {'color': 'gentle_text', 'symbol': '○', 'description': 'Inactive'},
    'emergency': {'color': 'status_danger', 'symbol': '🚨', 'description': 'Emergency'}
}

# Monitoring intervals and timeframes
NEURAL_LOAD_HISTORY_MINUTES = 5
COMFORT_CHECK_INTERVALS = [300, 600, 900]  # 5, 10, 15 minutes
SAFETY_ALERT_COOLDOWN = 30  # seconds

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# SAFETY MONITOR CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class SafetyMonitor:
    """
    Comprehensive safety monitoring and visualization component.
    
    This class provides real-time safety monitoring including neural load tracking,
    comfort level assessment, safety protocol status, emergency controls, and
    neural architecture compatibility monitoring in a beautiful terminal interface.
    """
    
    def __init__(self, terminal_adapter: TerminalConsciousnessAdapter):
        self.terminal_adapter = terminal_adapter
        self.color_scheme = ConsciousnessColorScheme()
        self.symbols = SacredGeometrySymbols()
        self.consciousness_viz = ConsciousnessVisualization()
        self.biofield = BiofieldAesthetics()
        
        # Safety monitoring state
        self.current_neural_load = 0.0
        self.current_comfort_level = 0.8
        self.neural_load_history = []
        self.comfort_level_history = []
        self.last_comfort_check = datetime.now()
        self.last_alert_time = {}
        
        # Safety protocol status
        self.safety_protocols = {
            'neural_load_monitor': 'active',
            'comfort_checker': 'active',
            'emergency_stop': 'active',
            'neural_compatibility': 'active',
            'biofield_safety': 'active'
        }
        
        # Alert state
        self.active_alerts = []
        self.alert_history = []
        
        # Animation state
        self.animation_frame = 0
        self.last_update = time.time()
    
    def show_safety_status(self, 
                          neural_load: float,
                          comfort_level: float,
                          session_duration: float = 0.0) -> None:
        """
        Display comprehensive safety status.
        
        Args:
            neural_load: Current neural load (0.0-1.0)
            comfort_level: Current comfort level (0.0-1.0)
            session_duration: Current session duration in seconds
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        # Update current values
        self.current_neural_load = neural_load
        self.current_comfort_level = comfort_level
        self._update_history(neural_load, comfort_level)
        
        # Display safety header
        print(f"\n{colors.consciousness_header('🛡️' * 60)}")
        print(f"{colors.consciousness_title('🛡️ Neural Safety Monitor')}")
        print(f"{colors.consciousness_header('🛡️' * 60)}")
        
        # Overall safety status
        overall_status = self._calculate_overall_safety_status(neural_load, comfort_level)
        status_info = self._get_safety_status_info(overall_status)
        
        print(f"\n{colors.safety_accent('Overall Safety Status:')} "
              f"{getattr(colors, status_info['color'])(f\"{status_info['symbol']} {status_info['description']}\")}")
        
        # Neural load monitoring
        self._display_neural_load_status(neural_load)
        
        # Comfort level monitoring
        self._display_comfort_level_status(comfort_level, session_duration)
        
        # Safety protocols status
        self._display_safety_protocols_status()
        
        # Active alerts
        if self.active_alerts:
            self._display_active_alerts()
        
        # Safety trends
        if len(self.neural_load_history) > 5:
            self._display_safety_trends()
    
    def show_neural_load_monitor(self, 
                                neural_load: float,
                                neural_profile: Dict[str, Any] = None,
                                show_history: bool = True) -> None:
        """
        Display detailed neural load monitoring.
        
        Args:
            neural_load: Current neural load (0.0-1.0)
            neural_profile: User's neural profile for contextualization
            show_history: Whether to show neural load history
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_header('🧠' * 50)}")
        print(f"{colors.consciousness_title('🧠 Neural Load Monitor')}")
        print(f"{colors.consciousness_header('🧠' * 50)}")
        
        # Neural load display
        load_threshold = self._get_neural_load_threshold(neural_load)
        threshold_info = NEURAL_LOAD_THRESHOLDS[load_threshold]
        
        # Create neural load visualization
        load_bar = colors.create_progress_bar(neural_load, 30)
        load_percentage = f"{neural_load:.1%}"
        
        print(f"\n{colors.biofield_accent('Current Neural Load:')} {load_bar} {load_percentage}")
        print(f"{colors.biofield_accent('Status:')} "
              f"{getattr(colors, threshold_info['color'])(f\"{threshold_info['symbol']} {threshold_info['description']}\")}")
        
        # Neural profile contextualization
        if neural_profile:
            sensitivity = neural_profile.get('sensitivity_level', 'standard')
            experience = neural_profile.get('experience_level', 'intermediate')
            
            print(f"\n{colors.neural_profile('Neural Profile Context:')}")
            print(f"  Sensitivity: {colors.neural_profile(sensitivity.title())}")
            print(f"  Experience: {colors.neural_profile(experience.title())}")
            
            # Personalized recommendations
            recommendations = self._get_neural_load_recommendations(neural_load, neural_profile)
            if recommendations:
                print(f"\n{colors.consciousness_accent('Recommendations:')}")
                for rec in recommendations:
                    print(f"  • {colors.gentle_text(rec)}")
        
        # Neural load visualization
        if self.terminal_adapter.capabilities.supports_unicode:
            neural_viz = self._create_neural_load_visualization(neural_load)
            print(f"\n{colors.gentle_text('Neural Load Pattern:')}")
            for line in neural_viz:
                print(f"  {line}")
        
        # History display
        if show_history and len(self.neural_load_history) > 3:
            self._display_neural_load_history()
    
    def show_comfort_assessment(self, 
                              comfort_level: float,
                              session_time: float,
                              check_intervals: List[float] = None) -> None:
        """
        Display comfort level assessment and tracking.
        
        Args:
            comfort_level: Current comfort level (0.0-1.0)
            session_time: Current session time in seconds
            check_intervals: List of comfort check intervals
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        if check_intervals is None:
            check_intervals = COMFORT_CHECK_INTERVALS
        
        print(f"\n{colors.consciousness_header('💚' * 50)}")
        print(f"{colors.consciousness_title('💚 Comfort Assessment')}")
        print(f"{colors.consciousness_header('💚' * 50)}")
        
        # Comfort level display
        comfort_threshold = self._get_comfort_level_threshold(comfort_level)
        threshold_info = COMFORT_LEVEL_THRESHOLDS[comfort_threshold]
        
        comfort_bar = colors.create_progress_bar(comfort_level, 30)
        comfort_percentage = f"{comfort_level:.1%}"
        
        print(f"\n{colors.biofield_accent('Current Comfort:')} {comfort_bar} {comfort_percentage}")
        print(f"{colors.biofield_accent('Assessment:')} "
              f"{getattr(colors, threshold_info['color'])(f\"{threshold_info['symbol']} {threshold_info['description']}\")}")
        
        # Session time and check schedule
        print(f"\n{colors.gentle_text('Session Progress:')}")
        print(f"  Current Time: {colors.gentle_text(self._format_duration(session_time))}")
        
        # Show upcoming comfort checks
        next_check = None
        for interval in check_intervals:
            if session_time < interval:
                next_check = interval - session_time
                break
        
        if next_check:
            print(f"  Next Check: {colors.gentle_text(self._format_duration(next_check))}")
        else:
            print(f"  {colors.status_safe('All scheduled checks complete')}")
        
        # Comfort trend
        if len(self.comfort_level_history) > 3:
            trend = self._calculate_comfort_trend()
            trend_symbol = {'improving': '↗', 'stable': '→', 'declining': '↘'}.get(trend, '→')
            trend_color = {'improving': colors.status_safe, 'stable': colors.gentle_text, 'declining': colors.status_caution}.get(trend, colors.gentle_text)
            
            print(f"  Trend: {trend_color(f'{trend_symbol} {trend.title()}')}")
        
        # Comfort recommendations
        if comfort_level < 0.6:
            recommendations = self._get_comfort_recommendations(comfort_level)
            print(f"\n{colors.consciousness_accent('Comfort Recommendations:')}")
            for rec in recommendations:
                print(f"  • {colors.gentle_text(rec)}")
    
    def show_safety_alerts(self, alerts: List[Dict[str, Any]] = None) -> None:
        """
        Display active safety alerts and warnings.
        
        Args:
            alerts: List of active alert dictionaries
        """
        colors = self.color_scheme
        symbols = self.symbols
        
        if alerts is not None:
            self.active_alerts = alerts
        
        if not self.active_alerts:
            print(f"\n{colors.status_safe('✓ No active safety alerts')}")
            return
        
        print(f"\n{colors.consciousness_header('⚠️' * 50)}")
        print(f"{colors.consciousness_title('⚠️ Safety Alerts')}")
        print(f"{colors.consciousness_header('⚠️' * 50)}")
        
        for i, alert in enumerate(self.active_alerts, 1):
            alert_type = alert.get('type', 'general')
            severity = alert.get('severity', 'warning')
            message = alert.get('message', 'Safety alert')
            timestamp = alert.get('timestamp', datetime.now())
            recommendations = alert.get('recommendations', [])
            
            # Alert header
            severity_colors = {
                'info': colors.gentle_text,
                'warning': colors.status_caution,
                'critical': colors.status_danger
            }
            severity_symbols = {
                'info': 'ℹ',
                'warning': '⚠',
                'critical': '🚨'
            }
            
            severity_color = severity_colors.get(severity, colors.status_caution)
            severity_symbol = severity_symbols.get(severity, '⚠')
            
            print(f"\n{severity_color(f'{severity_symbol} Alert {i}:')} {severity_color(message)}")
            print(f"  {colors.gentle_text('Type:')} {colors.gentle_text(alert_type.title())}")
            print(f"  {colors.gentle_text('Time:')} {colors.gentle_text(timestamp.strftime('%H:%M:%S'))}")
            
            # Recommendations
            if recommendations:
                print(f"  {colors.consciousness_accent('Actions:')}")
                for rec in recommendations:
                    print(f"    • {colors.gentle_text(rec)}")
    
    def show_emergency_controls(self) -> None:
        """Display emergency control interface."""
        
        colors = self.color_scheme
        symbols = self.symbols
        
        print(f"\n{colors.consciousness_header('🚨' * 50)}")
        print(f"{colors.consciousness_title('🚨 Emergency Controls')}")
        print(f"{colors.consciousness_header('🚨' * 50)}")
        
        # Emergency stop status
        emergency_status = self.safety_protocols.get('emergency_stop', 'active')
        status_info = SAFETY_PROTOCOL_STATUS[emergency_status]
        
        print(f"\n{colors.status_danger('Emergency Stop:')} "
              f"{getattr(colors, status_info['color'])(f\"{status_info['symbol']} {status_info['description']}\")}")
        
        # Emergency controls
        print(f"\n{colors.consciousness_accent('Available Emergency Actions:')}")
        print(f"  {colors.command_highlight('Ctrl+C')} - Immediate session termination")
        print(f"  {colors.command_highlight('ESC')} - Gentle session pause")
        print(f"  {colors.gentle_text('Session will auto-stop if critical thresholds are exceeded')}")
        
        # Safety contact information
        print(f"\n{colors.safety_accent('Safety Resources:')}")
        print(f"  • {colors.gentle_text('If you feel unwell, stop the session immediately')}")
        print(f"  • {colors.gentle_text('Consult healthcare provider if symptoms persist')}")
        print(f"  • {colors.gentle_text('Report serious issues to system administrator')}")
    
    def _display_neural_load_status(self, neural_load: float) -> None:
        """Display neural load status section."""
        
        colors = self.color_scheme
        
        load_threshold = self._get_neural_load_threshold(neural_load)
        threshold_info = NEURAL_LOAD_THRESHOLDS[load_threshold]
        
        print(f"\n{colors.biofield_accent('Neural Load Monitoring:')}")
        
        # Load bar with thresholds marked
        load_bar = self._create_neural_load_bar_with_thresholds(neural_load, 35)
        print(f"  Current Load: {load_bar}")
        
        # Status and description
        status_display = getattr(colors, threshold_info['color'])(f"{threshold_info['symbol']} {threshold_info['description']}")
        print(f"  Status: {status_display}")
        
        # Threshold information
        print(f"  {colors.gentle_text('Thresholds:')} "
              f"{colors.status_safe('Safe: 0-60%')} | "
              f"{colors.status_caution('Caution: 60-80%')} | "
              f"{colors.status_warning('Warning: 80-90%')} | "
              f"{colors.status_danger('Critical: 90%+')}")
    
    def _display_comfort_level_status(self, comfort_level: float, session_duration: float) -> None:
        """Display comfort level status section."""
        
        colors = self.color_scheme
        
        comfort_threshold = self._get_comfort_level_threshold(comfort_level)
        threshold_info = COMFORT_LEVEL_THRESHOLDS[comfort_threshold]
        
        print(f"\n{colors.biofield_accent('Comfort Level Monitoring:')}")
        
        comfort_bar = colors.create_progress_bar(comfort_level, 30)
        print(f"  Current Comfort: {comfort_bar} {comfort_level:.1%}")
        
        status_display = getattr(colors, threshold_info['color'])(f"{threshold_info['symbol']} {threshold_info['description']}")
        print(f"  Assessment: {status_display}")
        
        # Time since last check
        time_since_check = (datetime.now() - self.last_comfort_check).total_seconds()
        print(f"  Last Check: {colors.gentle_text(self._format_duration(time_since_check))} ago")
    
    def _display_safety_protocols_status(self) -> None:
        """Display safety protocols status."""
        
        colors = self.color_scheme
        
        print(f"\n{colors.biofield_accent('Safety Protocols:')}")
        
        for protocol, status in self.safety_protocols.items():
            status_info = SAFETY_PROTOCOL_STATUS[status]
            status_display = getattr(colors, status_info['color'])(f"{status_info['symbol']} {status_info['description']}")
            
            protocol_name = protocol.replace('_', ' ').title()
            print(f"  {protocol_name}: {status_display}")
    
    def _display_active_alerts(self) -> None:
        """Display active alerts section."""
        
        colors = self.color_scheme
        
        print(f"\n{colors.status_caution('Active Alerts:')}")
        
        for alert in self.active_alerts[:3]:  # Show max 3 most recent
            severity = alert.get('severity', 'warning')
            message = alert.get('message', 'Safety alert')
            
            if severity == 'critical':
                print(f"  🚨 {colors.status_danger(message)}")
            else:
                print(f"  ⚠ {colors.status_caution(message)}")
    
    def _display_safety_trends(self) -> None:
        """Display safety trend analysis."""
        
        colors = self.color_scheme
        
        print(f"\n{colors.consciousness_accent('Safety Trends:')}")
        
        # Neural load trend
        neural_trend = self._calculate_neural_load_trend()
        trend_symbols = {'improving': '↘', 'stable': '→', 'increasing': '↗'}
        trend_colors = {'improving': colors.status_safe, 'stable': colors.gentle_text, 'increasing': colors.status_caution}
        
        neural_symbol = trend_symbols.get(neural_trend, '→')
        neural_color = trend_colors.get(neural_trend, colors.gentle_text)
        
        print(f"  Neural Load: {neural_color(f'{neural_symbol} {neural_trend.title()}')}")
        
        # Comfort trend
        comfort_trend = self._calculate_comfort_trend()
        comfort_symbol = trend_symbols.get(comfort_trend, '→')
        comfort_color = trend_colors.get(comfort_trend, colors.gentle_text)
        
        print(f"  Comfort: {comfort_color(f'{comfort_symbol} {comfort_trend.title()}')}")
    
    def _display_neural_load_history(self) -> None:
        """Display neural load history graph."""
        
        colors = self.color_scheme
        
        print(f"\n{colors.gentle_text('Neural Load History (Last 5 minutes):')}")
        
        # Create simple ASCII graph
        history_viz = self._create_neural_load_history_graph()
        for line in history_viz:
            print(f"  {line}")
    
    def _calculate_overall_safety_status(self, neural_load: float, comfort_level: float) -> str:
        """Calculate overall safety status."""
        
        neural_threshold = self._get_neural_load_threshold(neural_load)
        comfort_threshold = self._get_comfort_level_threshold(comfort_level)
        
        # Critical conditions
        if neural_threshold == 'critical' or comfort_threshold == 'very_uncomfortable':
            return 'critical'
        
        # Warning conditions
        if neural_threshold == 'warning' or comfort_threshold == 'uncomfortable':
            return 'warning'
        
        # Caution conditions
        if neural_threshold == 'caution' or comfort_threshold == 'neutral':
            return 'caution'
        
        # Safe
        return 'safe'
    
    def _get_safety_status_info(self, status: str) -> Dict[str, str]:
        """Get safety status display information."""
        
        status_info = {
            'safe': {'color': 'status_safe', 'symbol': '✓', 'description': 'All Systems Safe'},
            'caution': {'color': 'status_caution', 'symbol': '⚠', 'description': 'Monitor Closely'},
            'warning': {'color': 'status_warning', 'symbol': '⚠', 'description': 'Warning Conditions'},
            'critical': {'color': 'status_danger', 'symbol': '🚨', 'description': 'Critical - Stop Session'}
        }
        
        return status_info.get(status, status_info['caution'])
    
    def _get_neural_load_threshold(self, neural_load: float) -> str:
        """Determine neural load threshold level."""
        
        for threshold, info in NEURAL_LOAD_THRESHOLDS.items():
            if info['range'][0] <= neural_load <= info['range'][1]:
                return threshold
        
        return 'critical' if neural_load > 0.9 else 'safe'
    
    def _get_comfort_level_threshold(self, comfort_level: float) -> str:
        """Determine comfort level threshold."""
        
        for threshold, info in COMFORT_LEVEL_THRESHOLDS.items():
            if info['range'][0] <= comfort_level <= info['range'][1]:
                return threshold
        
        return 'very_uncomfortable' if comfort_level < 0.2 else 'very_comfortable'
    
    def _create_neural_load_bar_with_thresholds(self, neural_load: float, width: int) -> str:
        """Create neural load progress bar with threshold markers."""
        
        colors = self.color_scheme
        
        filled = int(neural_load * width)
        
        # Create bar with threshold colors
        bar = ""
        for i in range(width):
            pos = i / width
            
            if i < filled:
                if pos < 0.6:
                    char = colors.status_safe('█')
                elif pos < 0.8:
                    char = colors.status_caution('█')
                elif pos < 0.9:
                    char = colors.status_warning('█')
                else:
                    char = colors.status_danger('█')
            else:
                char = colors.gentle_text('░')
            
            bar += char
        
        return f"[{bar}] {neural_load:.1%}"
    
    def _create_neural_load_visualization(self, neural_load: float) -> List[str]:
        """Create neural load pattern visualization."""
        
        lines = []
        colors = self.color_scheme
        width = 40
        
        # Create brain wave pattern representing neural load
        for row in range(4):
            line = ""
            for col in range(width):
                x = col / width * 4 * math.pi
                t = self.animation_frame * 0.1
                
                # Higher neural load = more intense/frequent waves
                freq_factor = 1.0 + neural_load * 3.0
                amplitude_factor = 0.5 + neural_load * 0.5
                
                wave_value = math.sin(x * freq_factor + t) * amplitude_factor
                row_offset = row * math.pi / 8
                final_value = wave_value * math.cos(row_offset)
                
                if abs(final_value) > 0.6:
                    char = '█'
                elif abs(final_value) > 0.3:
                    char = '▓'
                elif abs(final_value) > 0.1:
                    char = '▒'
                else:
                    char = '░'
                
                line += char
            
            # Color based on neural load level
            if neural_load < 0.6:
                colored_line = colors.status_safe(line)
            elif neural_load < 0.8:
                colored_line = colors.status_caution(line)
            else:
                colored_line = colors.status_danger(line)
            
            lines.append(colored_line)
        
        return lines
    
    def _create_neural_load_history_graph(self) -> List[str]:
        """Create ASCII graph of neural load history."""
        
        lines = []
        colors = self.color_scheme
        
        if len(self.neural_load_history) < 3:
            return [colors.gentle_text("Not enough history data")]
        
        # Use last 20 data points
        history = self.neural_load_history[-20:]
        width = min(len(history), 40)
        height = 5
        
        # Create graph
        for row in range(height):
            line = ""
            threshold = 1.0 - (row / height)  # Top row = 100%, bottom = 0%
            
            for col in range(width):
                if col < len(history):
                    value = history[col]
                    if value >= threshold - 0.2:  # Show if within range
                        if value < 0.6:
                            char = colors.status_safe('▓')
                        elif value < 0.8:
                            char = colors.status_caution('▓')
                        else:
                            char = colors.status_danger('▓')
                    else:
                        char = colors.gentle_text('░')
                else:
                    char = ' '
                
                line += char
            
            # Add scale
            scale_label = f"{threshold:.0%}"
            lines.append(f"{scale_label:>4} │{line}")
        
        # Add time axis
        time_axis = "     └" + "─" * width
        lines.append(colors.gentle_text(time_axis))
        
        return lines
    
    def _calculate_neural_load_trend(self) -> str:
        """Calculate neural load trend from history."""
        
        if len(self.neural_load_history) < 3:
            return 'stable'
        
        recent = self.neural_load_history[-3:]
        if recent[-1] > recent[0] + 0.1:
            return 'increasing'
        elif recent[-1] < recent[0] - 0.1:
            return 'improving'
        else:
            return 'stable'
    
    def _calculate_comfort_trend(self) -> str:
        """Calculate comfort level trend from history."""
        
        if len(self.comfort_level_history) < 3:
            return 'stable'
        
        recent = self.comfort_level_history[-3:]
        if recent[-1] > recent[0] + 0.1:
            return 'improving'
        elif recent[-1] < recent[0] - 0.1:
            return 'declining'
        else:
            return 'stable'
    
    def _get_neural_load_recommendations(self, neural_load: float, neural_profile: Dict[str, Any]) -> List[str]:
        """Get personalized neural load recommendations."""
        
        recommendations = []
        sensitivity = neural_profile.get('sensitivity_level', 'standard')
        
        if neural_load > 0.8:
            recommendations.extend([
                "Consider pausing the session for a few minutes",
                "Take slow, deep breaths to reduce neural activity",
                "Lower session intensity if adjustable"
            ])
        elif neural_load > 0.6:
            recommendations.extend([
                "Monitor closely for any discomfort",
                "Prepare to pause if load continues increasing"
            ])
        
        if sensitivity == 'sensitive' and neural_load > 0.5:
            recommendations.append("Your neural profile suggests extra caution at this level")
        
        return recommendations
    
    def _get_comfort_recommendations(self, comfort_level: float) -> List[str]:
        """Get comfort improvement recommendations."""
        
        recommendations = []
        
        if comfort_level < 0.4:
            recommendations.extend([
                "Stop the session and rest in a comfortable position",
                "Ensure you're in a calm, safe environment",
                "Consider ending the session for today"
            ])
        elif comfort_level < 0.6:
            recommendations.extend([
                "Adjust your position or environment",
                "Take a few minutes to relax and breathe",
                "Consider lowering session intensity"
            ])
        
        return recommendations
    
    def _update_history(self, neural_load: float, comfort_level: float) -> None:
        """Update monitoring history."""
        
        current_time = datetime.now()
        
        # Add to history
        self.neural_load_history.append(neural_load)
        self.comfort_level_history.append(comfort_level)
        
        # Limit history size (keep last 5 minutes of data, assuming 30-second intervals)
        max_history = 10
        if len(self.neural_load_history) > max_history:
            self.neural_load_history = self.neural_load_history[-max_history:]
        if len(self.comfort_level_history) > max_history:
            self.comfort_level_history = self.comfort_level_history[-max_history:]
    
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
        if current_time - self.last_update > 0.5:  # Update every 500ms
            self.animation_frame += 1
            self.last_update = current_time
    
    def add_safety_alert(self, alert_type: str, severity: str, message: str, recommendations: List[str] = None) -> None:
        """Add a new safety alert."""
        
        alert = {
            'type': alert_type,
            'severity': severity,
            'message': message,
            'timestamp': datetime.now(),
            'recommendations': recommendations or []
        }
        
        self.active_alerts.append(alert)
        self.alert_history.append(alert)
        
        # Limit active alerts
        if len(self.active_alerts) > 5:
            self.active_alerts = self.active_alerts[-5:]
    
    def clear_alerts(self) -> None:
        """Clear active alerts."""
        self.active_alerts.clear()