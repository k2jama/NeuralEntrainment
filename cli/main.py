#!/usr/bin/env python3
# 🧠 Neural Entrainment System v2.0 - Consciousness CLI Main Entry Point
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Consciousness-Aware CLI Main Entry Point.

This module provides the main entry point for the Neural Entrainment System CLI,
featuring intelligent command routing, consciousness-aware argument parsing,
neural profile integration, and beautiful terminal interface design.
"""

import sys
import os
import argparse
import logging
import json
from pathlib import Path
from typing import Dict, Any, List, Optional, Callable
import signal
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.interfaces.cli_interface import (
    ConsciousnessCLIInterface,
    create_cli_interface,
    detect_optimal_cli_configuration
)
from src.interfaces.base_interface import InterfaceConfig, ConsciousnessState
from .themes.consciousness_colors import ConsciousnessColorScheme
from .themes.sacred_geometry import SacredGeometrySymbols
from .utils.terminal_detection import detect_terminal_capabilities

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS CLI CONFIGURATION  
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CLI_VERSION = "2.0.0"
CLI_NAME = "Neural Entrainment CLI"
CLI_DESCRIPTION = """
🧠 Neural Entrainment System v2.0 - Consciousness-Aware CLI

A sophisticated command-line interface for consciousness work featuring:
• 🌊 Biofield Intelligence Integration (Schumann, Solfeggio, Golden Ratio)
• 🧠 Neural Profile Adaptation & Safety Protocols  
• ✨ Real-time Consciousness Journey Visualization
• 🛡️ Comprehensive Safety Monitoring & Emergency Controls
• 🎨 Beautiful Terminal Interface with Sacred Geometry
"""

DEFAULT_CONFIG_DIR = Path.home() / ".neural_entrainment"
DEFAULT_SESSIONS_DIR = DEFAULT_CONFIG_DIR / "sessions"
DEFAULT_PROFILES_DIR = DEFAULT_CONFIG_DIR / "profiles"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# CONSCIOUSNESS ENTRY POINT CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ConsciousnessEntryPoint:
    """
    Main consciousness-aware CLI entry point and command router.
    
    This class orchestrates the entire CLI experience, from consciousness-aware
    argument parsing to neural profile detection to command execution with
    appropriate safety protocols and interface adaptations.
    """
    
    def __init__(self):
        self.interface: Optional[ConsciousnessCLIInterface] = None
        self.neural_profile: Optional[Dict[str, Any]] = None
        self.config_dir = DEFAULT_CONFIG_DIR
        self.session_active = False
        self.color_scheme = ConsciousnessColorScheme()
        self.geometry = SacredGeometrySymbols()
        
        # Command registry
        self.commands: Dict[str, Callable] = {}
        self._register_commands()
        
        # Setup signal handlers for graceful shutdown
        signal.signal(signal.SIGINT, self._handle_interrupt)
        signal.signal(signal.SIGTERM, self._handle_interrupt)
    
    def run(self, args: Optional[List[str]] = None) -> int:
        """
        Main CLI entry point with consciousness-aware flow.
        
        Args:
            args: Command line arguments (defaults to sys.argv)
            
        Returns:
            Exit code (0 for success, non-zero for error)
        """
        try:
            # Parse arguments with consciousness awareness
            parsed_args = self._parse_arguments(args or sys.argv[1:])
            
            # Setup logging
            self._setup_logging(parsed_args)
            
            # Initialize consciousness-aware interface
            if not self._initialize_interface(parsed_args):
                return 1
            
            # Execute command with consciousness integration
            return self._execute_command(parsed_args)
            
        except KeyboardInterrupt:
            self._display_graceful_exit()
            return 130  # Standard exit code for SIGINT
        except Exception as e:
            self._display_error(f"Unexpected error: {e}")
            logging.exception("Unexpected CLI error")
            return 1
        finally:
            self._cleanup()
    
    def _parse_arguments(self, args: List[str]) -> argparse.Namespace:
        """Parse command line arguments with consciousness-aware defaults."""
        
        parser = argparse.ArgumentParser(
            description=CLI_DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=self._get_consciousness_epilog()
        )
        
        # Global options
        parser.add_argument(
            '--version', 
            action='version', 
            version=f'{CLI_NAME} {CLI_VERSION}'
        )
        
        parser.add_argument(
            '--config-dir',
            type=Path,
            default=DEFAULT_CONFIG_DIR,
            help='Configuration directory path'
        )
        
        parser.add_argument(
            '--neural-profile',
            type=str,
            help='Neural profile to use (will assess if not provided)'
        )
        
        parser.add_argument(
            '--gentle-mode',
            action='store_true',
            help='Enable gentle mode for sensitive users'
        )
        
        parser.add_argument(
            '--no-color',
            action='store_true',
            help='Disable color output'
        )
        
        parser.add_argument(
            '--quiet', '-q',
            action='store_true',
            help='Quiet mode (minimal output)'
        )
        
        parser.add_argument(
            '--verbose', '-v',
            action='count',
            default=0,
            help='Verbose output (use multiple times for more verbosity)'
        )
        
        # Subcommands
        subparsers = parser.add_subparsers(
            dest='command',
            help='Available consciousness commands',
            metavar='COMMAND'
        )
        
        # Session commands
        session_parser = subparsers.add_parser(
            'session',
            help='🧠 Session management and execution',
            description='Create, run, and manage consciousness sessions'
        )
        self._add_session_arguments(session_parser)
        
        # Profile commands
        profile_parser = subparsers.add_parser(
            'profile',
            help='👤 Neural profile management',
            description='Assess, create, and manage neural profiles'
        )
        self._add_profile_arguments(profile_parser)
        
        # Preset commands
        preset_parser = subparsers.add_parser(
            'preset',
            help='🎛️ Session preset management',
            description='Browse, customize, and manage session presets'
        )
        self._add_preset_arguments(preset_parser)
        
        # Monitor commands
        monitor_parser = subparsers.add_parser(
            'monitor',
            help='📊 Real-time monitoring and analysis',
            description='Monitor sessions and analyze consciousness data'
        )
        self._add_monitor_arguments(monitor_parser)
        
        # If no command provided, show consciousness-aware help
        if not args:
            args = ['--help']
        
        return parser.parse_args(args)
    
    def _setup_logging(self, args: argparse.Namespace) -> None:
        """Setup consciousness-aware logging configuration."""
        
        # Determine log level
        if args.quiet:
            log_level = logging.WARNING
        elif args.verbose == 1:
            log_level = logging.INFO
        elif args.verbose >= 2:
            log_level = logging.DEBUG
        else:
            log_level = logging.WARNING
        
        # Setup logging format
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        # Create log directory
        log_dir = self.config_dir / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        
        # Configure logging
        logging.basicConfig(
            level=log_level,
            format=log_format,
            handlers=[
                logging.FileHandler(log_dir / f"cli_{datetime.now():%Y%m%d}.log"),
                logging.StreamHandler() if args.verbose > 0 else logging.NullHandler()
            ]
        )
        
        logging.info(f"Neural Entrainment CLI v{CLI_VERSION} starting...")
    
    def _initialize_interface(self, args: argparse.Namespace) -> bool:
        """Initialize consciousness-aware CLI interface."""
        
        try:
            # Load or assess neural profile
            self.neural_profile = self._load_neural_profile(args)
            
            # Create interface preferences
            preferences = {
                'gentle_mode': args.gentle_mode,
                'color_enabled': not args.no_color,
                'quiet_mode': args.quiet,
                'verbose_level': args.verbose
            }
            
            # Create and initialize interface
            self.interface = create_cli_interface(self.neural_profile, preferences)
            
            # Display consciousness greeting
            if not args.quiet:
                self._display_consciousness_greeting()
            
            logging.info("CLI interface initialized successfully")
            return True
            
        except Exception as e:
            self._display_error(f"Failed to initialize consciousness interface: {e}")
            logging.error(f"Interface initialization error: {e}")
            return False
    
    def _execute_command(self, args: argparse.Namespace) -> int:
        """Execute the specified command with consciousness awareness."""
        
        command = args.command
        
        if not command:
            self._display_consciousness_help()
            return 0
        
        # Get command handler
        command_handler = self.commands.get(command)
        
        if not command_handler:
            self._display_error(f"Unknown command: {command}")
            return 1
        
        try:
            # Execute command with consciousness context
            return command_handler(args)
            
        except KeyboardInterrupt:
            self._display_gentle_interruption()
            return 130
        except Exception as e:
            self._display_error(f"Command execution error: {e}")
            logging.exception(f"Error executing command '{command}'")
            return 1
    
    def _register_commands(self) -> None:
        """Register consciousness-aware command handlers."""
        
        # Import command modules (will be created next)
        try:
            from .commands.session import SessionCommands
            from .commands.profile import ProfileCommands  
            from .commands.preset import PresetCommands
            from .commands.monitor import MonitorCommands
            
            # Register command handlers
            session_cmds = SessionCommands(self)
            profile_cmds = ProfileCommands(self)
            preset_cmds = PresetCommands(self)
            monitor_cmds = MonitorCommands(self)
            
            self.commands = {
                'session': session_cmds.handle_session_command,
                'profile': profile_cmds.handle_profile_command,
                'preset': preset_cmds.handle_preset_command,
                'monitor': monitor_cmds.handle_monitor_command
            }
            
        except ImportError as e:
            logging.warning(f"Command modules not yet available: {e}")
            # Provide placeholder handlers
            self.commands = {
                'session': self._placeholder_session_command,
                'profile': self._placeholder_profile_command,
                'preset': self._placeholder_preset_command,
                'monitor': self._placeholder_monitor_command
            }
    
    def _load_neural_profile(self, args: argparse.Namespace) -> Dict[str, Any]:
        """Load or assess neural profile for consciousness adaptation."""
        
        profile_path = None
        
        # Check for specified profile
        if args.neural_profile:
            profile_path = self.config_dir / "profiles" / f"{args.neural_profile}.json"
        
        # Try to load existing profile
        if profile_path and profile_path.exists():
            try:
                with open(profile_path, 'r') as f:
                    profile = json.load(f)
                    logging.info(f"Loaded neural profile: {args.neural_profile}")
                    return profile
            except Exception as e:
                logging.warning(f"Failed to load profile {args.neural_profile}: {e}")
        
        # Return default profile for now (assessment will be implemented in profile commands)
        default_profile = {
            'sensitivity_level': 'standard',
            'experience_level': 'intermediate',
            'current_state': 'neutral',
            'integration_capacity': 5,
            'preferences': {
                'gentle_mode': args.gentle_mode,
                'color_preference': not args.no_color
            }
        }
        
        logging.info("Using default neural profile")
        return default_profile
    
    def _display_consciousness_greeting(self) -> None:
        """Display consciousness-aware CLI greeting."""
        
        if not self.interface or not self.interface.terminal_adapter.capabilities.supports_color:
            # Simple text greeting for basic terminals
            print(f"\n{CLI_NAME} v{CLI_VERSION}")
            print("🧠 Welcome to your consciousness journey")
            return
        
        # Rich consciousness greeting with colors and sacred geometry
        colors = self.color_scheme
        symbols = self.geometry
        
        print(f"\n{colors.consciousness_header('═' * 60)}")
        print(f"{colors.consciousness_title('🧠 Neural Entrainment System v2.0')}")
        print(f"{colors.consciousness_subtitle('Consciousness-Aware CLI Interface')}")
        print(f"{colors.consciousness_header('═' * 60)}")
        
        print(f"\n{colors.biofield_accent(symbols.PHI)} Biofield Intelligence: {colors.status_active('Active')}")
        print(f"{colors.consciousness_accent(symbols.INFINITY)} Neural Profile: {colors.neural_profile(self.neural_profile['sensitivity_level'])}")
        print(f"{colors.safety_accent(symbols.DIAMOND)} Safety Protocols: {colors.status_safe('Enabled')}")
        
        print(f"\n{colors.gentle_text('Type')} {colors.command_highlight('--help')} {colors.gentle_text('for consciousness-aware guidance')}")
        print(f"{colors.gentle_text('Use')} {colors.command_highlight('session')} {colors.gentle_text('to begin your journey')}\n")
    
    def _display_consciousness_help(self) -> None:
        """Display consciousness-aware help information."""
        
        print(f"\n🧠 {CLI_NAME} v{CLI_VERSION} - Consciousness Commands:")
        print("\n💫 Core Commands:")
        print("  session    🧠 Create and run consciousness sessions")
        print("  profile    👤 Manage neural profiles and assessments")  
        print("  preset     🎛️ Browse and customize session presets")
        print("  monitor    📊 Real-time session monitoring")
        
        print("\n🌊 Quick Start:")
        print("  neural-cli profile assess    # Assess your neural profile")
        print("  neural-cli preset browse     # Browse consciousness presets")
        print("  neural-cli session run focus # Run a focus enhancement session")
        
        print("\n🛡️ Safety & Comfort:")
        print("  Use --gentle-mode for sensitive neural architecture")
        print("  Emergency stop: Ctrl+C during any session")
        print("  All sessions include real-time safety monitoring")
        
        print(f"\n✨ For detailed help: neural-cli <command> --help\n")
    
    def _display_graceful_exit(self) -> None:
        """Display consciousness-aware graceful exit message."""
        
        if self.session_active:
            print(f"\n🛡️ Session safely terminated")
            print("💚 Your consciousness journey data has been preserved")
        
        print(f"🙏 Thank you for your consciousness work")
        print(f"✨ Journey well until we meet again\n")
    
    def _display_gentle_interruption(self) -> None:
        """Display gentle interruption message for sensitive users."""
        print(f"\n💚 Gently pausing...")
        print(f"🌊 Your session has been safely interrupted")
    
    def _display_error(self, message: str) -> None:
        """Display consciousness-aware error message."""
        
        if self.interface and self.interface.terminal_adapter.capabilities.supports_color:
            colors = self.color_scheme
            print(f"\n{colors.error_symbol()} {colors.error_text(message)}")
        else:
            print(f"\n❌ Error: {message}")
    
    def _cleanup(self) -> None:
        """Cleanup consciousness interface and resources."""
        
        if self.interface:
            self.interface.shutdown()
            self.interface = None
        
        logging.info("CLI cleanup completed")
    
    def _handle_interrupt(self, signum, frame) -> None:
        """Handle interrupt signals gracefully."""
        
        if self.session_active:
            # Trigger emergency stop for active sessions
            if self.interface:
                self.interface.trigger_emergency_stop()
        
        # Raise KeyboardInterrupt for normal handling
        raise KeyboardInterrupt()
    
    # ─────────────────────────────────────────────────────────────────────────────────
    # Argument Parser Setup Methods
    # ─────────────────────────────────────────────────────────────────────────────────
    
    def _add_session_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add session command arguments."""
        
        subparsers = parser.add_subparsers(dest='session_action', help='Session actions')
        
        # Run session
        run_parser = subparsers.add_parser('run', help='Run a consciousness session')
        run_parser.add_argument('preset', help='Preset name or path')
        run_parser.add_argument('--duration', type=int, help='Session duration override')
        run_parser.add_argument('--intensity', type=float, help='Intensity adjustment')
        
        # List sessions
        list_parser = subparsers.add_parser('list', help='List available sessions')
        list_parser.add_argument('--history', action='store_true', help='Show session history')
        
        # Analyze session
        analyze_parser = subparsers.add_parser('analyze', help='Analyze session results')
        analyze_parser.add_argument('session_id', help='Session ID to analyze')
    
    def _add_profile_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add profile command arguments."""
        
        subparsers = parser.add_subparsers(dest='profile_action', help='Profile actions')
        
        # Assess profile
        assess_parser = subparsers.add_parser('assess', help='Assess neural profile')
        assess_parser.add_argument('--quick', action='store_true', help='Quick assessment')
        
        # List profiles  
        list_parser = subparsers.add_parser('list', help='List neural profiles')
        
        # Show profile
        show_parser = subparsers.add_parser('show', help='Show profile details')
        show_parser.add_argument('profile_name', help='Profile to display')
    
    def _add_preset_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add preset command arguments."""
        
        subparsers = parser.add_subparsers(dest='preset_action', help='Preset actions')
        
        # Browse presets
        browse_parser = subparsers.add_parser('browse', help='Browse available presets')
        browse_parser.add_argument('--category', help='Filter by category')
        browse_parser.add_argument('--intention', help='Filter by intention')
        
        # Show preset
        show_parser = subparsers.add_parser('show', help='Show preset details')
        show_parser.add_argument('preset_name', help='Preset to display')
        
        # Customize preset
        customize_parser = subparsers.add_parser('customize', help='Customize preset')
        customize_parser.add_argument('preset_name', help='Preset to customize')
    
    def _add_monitor_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add monitor command arguments."""
        
        subparsers = parser.add_subparsers(dest='monitor_action', help='Monitor actions')
        
        # Real-time monitoring
        realtime_parser = subparsers.add_parser('realtime', help='Real-time session monitoring')
        
        # Analysis
        analyze_parser = subparsers.add_parser('analyze', help='Analyze session data')
        analyze_parser.add_argument('session_file', help='Session data file')
    
    def _get_consciousness_epilog(self) -> str:
        """Get consciousness-aware CLI epilog text."""
        return """
🌊 Consciousness Sovereignty Principles:
• Your neural architecture is unique and respected
• All sessions include comprehensive safety protocols  
• Emergency stop available at any time (Ctrl+C)
• Gentle mode available for sensitive neural types
• Your consciousness data remains private and local

🧠 For support and guidance: https://neural-entrainment.example.com/cli-guide
✨ May your consciousness journey be safe, beautiful, and transformative
        """
    
    # ─────────────────────────────────────────────────────────────────────────────────
    # Placeholder Command Handlers (until command modules are created)
    # ─────────────────────────────────────────────────────────────────────────────────
    
    def _placeholder_session_command(self, args: argparse.Namespace) -> int:
        """Placeholder session command handler."""
        print("🧠 Session commands coming soon...")
        print("   This will provide full session management and execution")
        return 0
    
    def _placeholder_profile_command(self, args: argparse.Namespace) -> int:
        """Placeholder profile command handler."""
        print("👤 Profile commands coming soon...")
        print("   This will provide neural profile assessment and management")
        return 0
    
    def _placeholder_preset_command(self, args: argparse.Namespace) -> int:
        """Placeholder preset command handler."""
        print("🎛️ Preset commands coming soon...")
        print("   This will provide preset browsing and customization")
        return 0
    
    def _placeholder_monitor_command(self, args: argparse.Namespace) -> int:
        """Placeholder monitor command handler."""
        print("📊 Monitor commands coming soon...")
        print("   This will provide real-time session monitoring")
        return 0

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MAIN ENTRY POINT
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main() -> int:
    """
    Main CLI entry point for consciousness-aware neural entrainment.
    
    Returns:
        Exit code (0 for success)
    """
    entry_point = ConsciousnessEntryPoint()
    return entry_point.run()

if __name__ == "__main__":
    sys.exit(main())