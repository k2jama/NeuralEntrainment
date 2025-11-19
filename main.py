# 🧪 Neural Entrainment System - Main Orchestrator v2.0 Enhanced
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧠 Consciousness-Aware Biofield Intelligence Framework
# 🌟 Dr. KB Jama, Neural Dialogue Interface Research

"""
Dramatically enhanced main entrypoint: Robust CLI with safety consents, async/parallel processing, deep validation/fixes,
plugin hooks, auditing, and inclusive UX. Deeply integrates configs for adaptive, safe sessions.
"""

import asyncio
import concurrent.futures
import datetime
import json
import logging
import os
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Dict, Any

import jsonschema
from cerberus import Validator as CerberusValidator  # For fuzzy fixes
import joblib
import questionary
import rich.console
import rich.table
import typer
from moviepy.editor import ImageSequenceClip  # Enhanced for animations
from rich.progress import Progress
from rich.prompt import Confirm, Prompt

# System modules - assume src/ in sys.path or adjust
import sys
sys.path.append(str(Path(__file__).parent / "src"))
from metadata_generator import generate_metadata, analyze_consciousness_progression
from session_builder import EntrainmentSession, ConsciousnessIntentionWeaver, NeuralProfile, TransitionType
from signal_generator import SignalConfig, IntentionType
from validator import validate_session_comprehensive, ValidationResult
from visualizer import VisualizationConfig, create_comprehensive_report, visualize_audio, plot_animated_consciousness_journey

# Config paths (now .json as per docs)
CONFIG_DIR = Path("configs")
PRESETS_FILE = CONFIG_DIR / "presets.json"
PROFILES_FILE = CONFIG_DIR / "neural_profile_templates.json"
SAFETY_FILE = CONFIG_DIR / "safety_protocols.json"
BIOFIELD_FILE = CONFIG_DIR / "biofield_configurations.json"
SCHEMA_FILE = CONFIG_DIR / "configuration_schema.json"

# Logging enhanced with structlog
import structlog
structlog.configure(wrapper_class=structlog.BoundLogger)
logger = structlog.get_logger()
logger = logger.bind(module="main.py")
logging.basicConfig(level=logging.INFO)  # Fallback

# Rich console
console = rich.console.Console()

# Typer app enhanced
app = typer.Typer(
    help="Enhanced Neural Entrainment System CLI - Safe, Adaptive, Performant Orchestrator",
    context_settings={"help_option_names": ["-h", "--help"]},
    pretty_exceptions_show_locals=False
)

# Hooks dict for extensibility (e.g., plugins add funcs)
HOOKS = {"pre_build": [], "post_adapt": [], "pre_viz": []}

def register_hook(hook_name: str, func: callable):
    if hook_name in HOOKS:
        HOOKS[hook_name].append(func)

@lru_cache(maxsize=5)
def load_json_cached(file_path: str) -> Dict:
    """Cached loader with validation."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Config not found: {path}")
    with path.open("r") as f:
        data = json.load(f)
    logger.info("Loaded config", file=str(path))
    return data

def deep_merge(dict1: Dict, dict2: Dict) -> Dict:
    """Recursive merge, dict2 overrides."""
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result

def validate_config_against_schema(config: Dict, schema_key: str) -> List[str]:
    """Enhanced validation with jsonschema + cerberus for fixes."""
    schemas = load_json_cached(str(SCHEMA_FILE)).get("schema_definitions", {})
    schema = schemas.get(schema_key)
    if not schema:
        raise ValueError(f"Schema not found: {schema_key}")
    try:
        jsonschema.validate(instance=config, schema=schema)
        return []
    except jsonschema.exceptions.ValidationError as e:
        return [f"Error at {e.json_path}: {e.message}"]

def suggest_fixes(errors: List[str], config: Dict) -> Dict:
    """Fuzzy auto-fixes using cerberus."""
    v = CerberusValidator()  # Stub - expand with rules from schema
    # Example: Cap durations
    for err in errors:
        if "duration" in err and "maximum" in err:
            for phase in config.get("phases", []):
                phase["duration"] = min(phase["duration"], 3600)
    return config

def adapt_config_with_profile(preset_config: Dict, profile: Dict) -> Dict:
    """Enhanced with scaling, contraindications, and hooks."""
    adapted = deep_merge(preset_config, profile.get("session_modifications", {}))
    adaptive = profile.get("adaptive_settings", {})
    for phase in adapted.get("phases", []):
        phase["neural_load_factor"] = phase.get("neural_load_factor", 1.0) * adaptive.get("neural_load_scaling", 1.0)
        for layer in phase.get("layers", []):
            for key in ["fm_depth", "level"]:  # Generalize
                if key in layer:
                    layer[key] *= adaptive.get("neural_load_scaling", 1.0)
    contras = profile.get("profile", {}).get("contraindications", {})
    for contra, val in contras.items():
        if val == True or val == "caution":
            if contra == "gamma_states":
                for phase in adapted["phases"]:
                    if "gamma" in phase.get("consciousness_target_state", ""):
                        phase["consciousness_target_state"] = "beta"
                        logger.warning("Adapted to avoid gamma states", phase=phase["name"])
            elif contra == "long_sessions":
                adapted["session_config"]["total_duration"] = min(adapted["session_config"].get("total_duration", 7200), 1800)
    for hook in HOOKS["post_adapt"]:
        adapted = hook(adapted)
    return adapted

def apply_safety_protocols(config: Dict, safety: Dict, profile_level: str) -> Dict:
    """Enhanced with monitoring injection and emergency setups."""
    protocols = safety.get("neural_profile_safety_protocols", {}).get(f"{profile_level}_profile_protocols", {})
    limits = protocols.get("mandatory_precautions", {}).get("intensity_limits", {})
    config["session_config"]["max_volume"] = limits.get("maximum_volume", 0.8)
    for phase in config.get("phases", []):
        phase["duration"] = min(phase["duration"], limits.get("maximum_session_duration", 7200))
    monitoring = protocols.get("monitoring_parameters", {})
    if monitoring.get("neural_load_monitoring") == "continuous":
        config["session_config"]["monitoring"] = {"type": "continuous", "params": monitoring}
    emergency = safety.get("emergency_response_protocols", {})
    config["session_config"]["emergency"] = emergency.get("immediate_response_procedures", {})
    return config

def apply_biofield_optimizations(config: Dict, biofield: Dict, intention: str) -> Dict:
    """Enhanced dynamic injection with matching."""
    templates = biofield.get("natural_frequency_templates", {})
    intent_map = {"focus": "schumann_resonance_set", "heal": "solfeggio_frequency_set"}  # Expand
    template_key = intent_map.get(intention, "schumann_resonance_set")
    template = templates.get(template_key, {})
    fundamental = template.get("frequencies", {}).get("fundamental", {}).get("frequency", 7.83)
    for phase in config.get("phases", []):
        if "grounding" in phase.get("name", "").lower() or "integration" in phase.get("type", ""):
            phase["layers"].append({
                "carrier": fundamental,
                "carrier_type": "sine",
                "beat": 0,
                "level": 0.7,
                "biofield_effects": template.get("biofield_effects", [])
            })
            logger.info("Injected biofield", phase=phase["name"], freq=fundamental)
    return config

async def build_session_async(adapted_config: Dict, out_dir: str, viz: bool, report: bool, preview: bool) -> str:
    """Enhanced async build with hooks and previews."""
    neural_profile_dict = adapted_config.get("neural_profile", {})
    neural_profile = NeuralProfile(
        sensitivity_level=neural_profile_dict.get("sensitivity_level", "standard"),
        current_state=neural_profile_dict.get("current_state", "neutral"),
        experience_level=neural_profile_dict.get("experience_level", "beginner"),
        integration_capacity=neural_profile_dict.get("integration_capacity", 4),
        custom_factors=neural_profile_dict.get("custom_factors", {})
    )
    weaver_config = adapted_config.get("session_config", {}).get("consciousness_weaver", {})
    intention = IntentionType(weaver_config.get("intention", "neutral"))
    weaver = ConsciousnessIntentionWeaver(intention, neural_profile)
    
    signal_cfg = SignalConfig(
        sample_rate=adapted_config.get("session_config", {}).get("sample_rate", 44100),
        intention=weaver_config.get("intention", "neutral"),
        coherence_enhancement=weaver_config.get("adaptation_strength", 0.1)
    )
    session = EntrainmentSession(signal_cfg, weaver)
    
    with Progress(console=console) as progress:
        phase_task = progress.add_task("Building phases...", total=len(adapted_config["phases"]))
        for phase in adapted_config["phases"]:
            for hook in HOOKS["pre_build"]:
                phase = hook(phase)
            transition_type = TransitionType(phase.get("animation_type", "linear").upper())
            session.add_phase(phase["duration"], phase["layers"], transition_type)
            if preview:
                # Partial metadata for preview
                partial_md = generate_metadata({"phases": [phase]})
                plot_consciousness_journey_3D(partial_md, None, VisualizationConfig())
            progress.advance(phase_task)
    
    audio = session.build()
    metadata = generate_metadata(adapted_config)
    
    timestamp = datetime.datetime.now().isoformat().replace(":", "-")
    output_path = Path(out_dir) / f"session_{timestamp}.wav"
    output_path.parent.mkdir(exist_ok=True)
    session.save(str(output_path))
    joblib.dump(metadata, str(output_path.with_suffix(".json")))
    
    if viz:
        viz_cfg = VisualizationConfig(output_dir=str(output_path.parent), animation_enabled=True)
        visualize_audio(audio, signal_cfg.sample_rate, metadata, neural_profile_dict, viz_cfg)
    
    if report:
        create_comprehensive_report(audio, signal_cfg.sample_rate, metadata, neural_profile_dict, viz_cfg)
    
    logger.info("Build complete", path=str(output_path), coherence=metadata.get("biofield_coherence", 0))
    return str(output_path)

@app.command()
def build(
    preset: str = typer.Option(..., prompt=True, help="Preset name from presets.json"),
    profile: str = typer.Option(..., prompt=True, help="Profile from neural_profile_templates.json"),
    output: Optional[str] = typer.Option(None, help="Output WAV path; auto-timestamp if none"),
    out_dir: str = typer.Option("output/", help="Base output directory"),
    viz: bool = typer.Option(True, "--viz/--no-viz", help="Generate visualizations"),
    report: bool = typer.Option(True, "--report/--no-report", help="Generate comprehensive report"),
    dry_run: bool = typer.Option(False, "--dry-run", help="Simulate and save config only"),
    custom_json: Optional[str] = typer.Option(None, help="Path to custom overrides JSON"),
    preview: bool = typer.Option(False, "--preview", help="Preview viz per phase"),
    expert: bool = typer.Option(False, "--expert", help="Enable advanced options")
):
    """Core build command with enhanced safety, adaptations, and async."""
    if not Confirm.ask("I acknowledge the medical disclaimer and consent to proceed (details in safety.json)?", default=False):
        raise typer.Abort()
    
    with Progress(console=console) as progress:
        load_task = progress.add_task("Loading configs...", total=6)
        
        presets = load_json_cached(str(PRESETS_FILE))["consciousness_aware_presets"]
        profiles = load_json_cached(str(PROFILES_FILE))["neural_profile_templates"]
        safety = load_json_cached(str(SAFETY_FILE))
        biofield = load_json_cached(str(BIOFIELD_FILE))
        
        preset_config = presets.get(preset)
        profile_data = profiles.get(profile)
        if not preset_config or not profile_data:
            raise ValueError(f"Invalid preset '{preset}' or profile '{profile}' - run 'manage preset list'")
        
        progress.advance(load_task)
        adapted = adapt_config_with_profile(preset_config, profile_data)
        if custom_json:
            custom = load_json_cached(custom_json)
            adapted = deep_merge(adapted, custom)
            progress.advance(load_task)
        
        adapted = apply_safety_protocols(adapted, safety, profile_data["profile"]["sensitivity_level"])
        progress.advance(load_task)
        adapted = apply_biofield_optimizations(adapted, biofield, adapted["session_config"]["consciousness_weaver"]["intention"])
        progress.advance(load_task)
        
        errors = validate_config_against_schema(adapted, "session_config_schema")  # Adjust to match schema keys
        validation = validate_session_comprehensive(adapted)
        if errors or not validation.is_valid:
            table = rich.table.Table(title="Validation Issues")
            table.add_column("Type")
            table.add_column("Message")
            for err in errors + [i.message for i in validation.errors + validation.warnings]:
                table.add_row("Error/Warning", err)
            console.print(table)
            if questionary.confirm("Attempt auto-fix?").ask():
                adapted = suggest_fixes(errors, adapted)
                # Re-validate
                errors = validate_config_against_schema(adapted, "session_config_schema")
                if errors:
                    raise ValueError("Auto-fix failed - manual review required")
            else:
                raise typer.Abort()
        progress.advance(load_task)
        
        if dry_run:
            dry_path = Path(out_dir) / "dry_run_config.json"
            with dry_path.open("w") as f:
                json.dump(adapted, f, indent=4)
            console.print(f"[yellow]Dry run complete: {dry_path}[/yellow]")
            return
        
        progress.update(load_task, description="Building async...")
        loop = asyncio.get_event_loop()
        output_path = loop.run_until_complete(build_session_async(adapted, out_dir, viz, report, preview))
        if output:
            os.rename(output_path, output)
            output_path = output
        console.print(f"[green]Session built: {output_path}[/green]")
        progress.advance(load_task)

@app.command()
def validate(
    config_file: str = typer.Argument(..., help="Config JSON to validate"),
    profile: Optional[str] = typer.Option(None, help="Optional profile to apply first"),
    fix: bool = typer.Option(False, "--fix", help="Attempt auto-fixes"),
    export: str = typer.Option("json", help="Export format: json/yaml/csv")
):
    """Advanced validation with optional fixes and exports."""
    config = load_json_cached(config_file)
    if profile:
        profiles = load_json_cached(str(PROFILES_FILE))["neural_profile_templates"]
        profile_data = profiles.get(profile)
        if not profile_data:
            raise ValueError(f"Profile not found: {profile}")
        config = adapt_config_with_profile(config, profile_data)
    
    errors = validate_config_against_schema(config, "session_config_schema")
    validation: ValidationResult = validate_session_comprehensive(config)
    
    table = rich.table.Table(title="Validation Results")
    table.add_column("Level", style="bold")
    table.add_column("Category")
    table.add_column("Message")
    for issue in validation.errors + validation.warnings + validation.recommendations:
        table.add_row(str(issue.level), str(issue.category), issue.message)
    for err in errors:
        table.add_row("Schema Error", "Config", err)
    console.print(table)
    console.print(f"Safety Rating: {validation.safety_rating}", style="bold green" if validation.is_valid else "bold red")
    
    if fix and (validation.warnings or errors):
        config = suggest_fixes(errors + [i.message for i in validation.warnings], config)
        # Re-validate and report changes
        console.print("[yellow]Applied fixes - re-run to confirm.[/yellow]")
    
    if export == "json":
        with open("validation.json", "w") as f:
            json.dump(validation.__dict__, f, indent=4)
    elif export == "yaml":
        import yaml
        with open("validation.yaml", "w") as f:
            yaml.dump(validation.__dict__, f)
    elif export == "csv":
        import csv
        with open("validation.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Level", "Category", "Message"])
            for issue in validation.errors + validation.warnings + validation.recommendations:
                writer.writerow([str(issue.level), str(issue.category), issue.message])

@app.command()
def viz(
    session_file: str = typer.Argument(..., help="WAV session file"),
    types: str = typer.Option("comprehensive,animated", help="Comma-separated: comprehensive,animated,journey,dashboard"),
    format: str = typer.Option("png,mp4", help="Comma-separated formats"),
    out_dir: str = typer.Option("output/", help="Output dir"),
    theme: str = typer.Option("dark", help="Theme: dark,light,colorblind")
):
    """Advanced viz with multi-types and formats."""
    from scipy.io.wavfile import read
    sr, audio = read(session_file)
    metadata_path = Path(session_file).with_suffix(".json")
    metadata = load_json_cached(str(metadata_path)) if metadata_path.exists() else {}
    neural_profile = metadata.get("neural_profile", {})  # Assume
    
    viz_cfg = VisualizationConfig(output_dir=out_dir, color_theme=theme, animation_enabled="animated" in types)
    
    for viz_type in types.split(","):
        if viz_type == "animated":
            fig = plot_animated_consciousness_journey(metadata, audio, viz_cfg)
            if "mp4" in format.split(","):
                # Save ani as MP4
                ani = fig  # Assume returns ani obj
                frames = [ani.new_frame_seq() for _ in range(ani._interval * 30)]  # Stub
                clip = ImageSequenceClip(frames, fps=30)
                clip.write_videofile(f"{out_dir}/{viz_type}.mp4")
        elif viz_type == "comprehensive":
            create_comprehensive_report(audio, sr, metadata, neural_profile, viz_cfg)
        # Add others similarly
    console.print("[green]Visualizations complete.[/green]")

@app.command()
def manage(
    resource: str = typer.Argument(..., help="Resource: preset/profile/biofield/safety/schema"),
    action: str = typer.Argument(..., help="Action: list/create/edit/delete/search"),
    name: Optional[str] = typer.Option(None, help="Resource name"),
    template: Optional[str] = typer.Option(None, help="Template for create"),
    validate: bool = typer.Option(True, "--validate/--no-validate", help="Validate on save")
):
    """Advanced manager with search and validation."""
    files_map = {
        "preset": PRESETS_FILE,
        "profile": PROFILES_FILE,
        "biofield": BIOFIELD_FILE,
        "safety": SAFETY_FILE,
        "schema": SCHEMA_FILE
    }
    file = files_map.get(resource)
    if not file:
        raise ValueError(f"Invalid resource: {resource}")
    data = load_json_cached(str(file))
    key = f"{resource}s" if resource != "schema" else "schema_definitions"  # Adjust
    
    if action == "list":
        console.print(list(data.get(key, {}).keys()))
    elif action == "search":
        from difflib import get_close_matches
        query = Prompt.ask("Search term")
        matches = get_close_matches(query, data.get(key, {}).keys(), n=5, cutoff=0.6)
        console.print(matches)
    elif action == "create" and name:
        schemas = load_json_cached(str(SCHEMA_FILE))["schema_definitions"]
        new = {}  # Start empty
        if template:
            new = deep_merge(new, data.get(key, {}).get(template, {}))
        # Interactive edit
        for field in schemas.get(f"{resource}_schema", {}).get("properties", {}):
            val = questionary.text(f"{field} (type: {schemas[field]['type']}):").ask()
            new[field] = val  # Type cast stub
        data[key][name] = new
        if validate:
            errors = validate_config_against_schema(new, f"{resource}_schema")
            if errors:
                raise ValueError("Validation failed on create")
        with file.open("w") as f:
            json.dump(data, f, indent=4)
        console.print(f"[green]Created {resource} '{name}'[/green]")
    elif action == "edit" and name:
        if name not in data.get(key, {}):
            raise ValueError("Not found")
        # Stub: Open in editor or interactive
        os.system(f"nano {file}")  # Primitive; improve with questionary loop
    elif action == "delete" and name:
        if name in data.get(key, {}):
            del data[key][name]
            with file.open("w") as f:
                json.dump(data, f, indent=4)
        else:
            raise ValueError("Not found")

@app.command()
def batch(
    presets: str = typer.Option(..., help="Comma-separated presets"),
    profiles: str = typer.Option(..., help="Comma-separated profiles"),
    parallel: int = typer.Option(4, help="Max parallel processes"),
    out_dir: str = typer.Option("bulk/", help="Output dir"),
    viz: bool = typer.Option(False, "--viz/--no-viz"),
    report: bool = typer.Option(True, "--report/--no-report"),
    audit: str = typer.Option("csv", help="Audit format post-batch")
):
    """Parallel batch builds with auditing."""
    if not Confirm.ask("Consent for batch processing?"):
        raise typer.Abort()
    
    preset_list = [p.strip() for p in presets.split(",")]
    profile_list = [p.strip() for p in profiles.split(",")]
    combos = [(pt, pf) for pt in preset_list for pf in profile_list]
    
    outputs = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=parallel) as executor:
        futures = []
        for pt, pf in combos:
            # Partial build func
            futures.append(executor.submit(build_session_async, 
                                           adapt_config_with_profile(load_json_cached(str(PRESETS_FILE))["consciousness_aware_presets"][pt], 
                                                                     load_json_cached(str(PROFILES_FILE))["neural_profile_templates"][pf]),
                                           out_dir, viz, report, False))
        for future in concurrent.futures.as_completed(futures):
            try:
                outputs.append(future.result())
            except Exception as e:
                logger.error("Batch error", exc=str(e))
    
    if audit:
        metrics = []
        for out in outputs:
            md_path = Path(out).with_suffix(".json")
            if md_path.exists():
                md = load_json_cached(str(md_path))
                analysis = analyze_consciousness_progression(md)  # Assume returns dict
                metrics.append({"session": out, "coherence": analysis.get("biofield_coherence_target", 0), "quality": analysis.get("journey_quality_rating", "N/A")})
        if audit == "csv":
            import pandas as pd
            pd.DataFrame(metrics).to_csv(f"{out_dir}/batch_audit.csv", index=False)
        console.print("[green]Batch & audit complete.[/green]")

@app.command()
def audit(
    session_dir: str = typer.Option("output/", help="Dir to audit"),
    export: str = typer.Option("csv", help="Format: csv/json"),
    plot: bool = typer.Option(False, "--plot/--no-plot", help="Generate summary plots")
):
    """Audit sessions with metrics and optional plots."""
    metadata_files = list(Path(session_dir).glob("*.json"))
    metrics = []
    for mf in metadata_files:
        md = load_json_cached(str(mf))
        analysis = analyze_consciousness_progression(md)
        metrics.append({
            "file": str(mf),
            "intention": md.get("session_config", {}).get("consciousness_weaver", {}).get("intention", "unknown"),
            "coherence": analysis.get("biofield_coherence_target", 0),
            "quality": analysis.get("journey_quality_rating", "unknown"),
            "duration": md.get("session_config", {}).get("total_duration", 0)
        })
    
    table = rich.table.Table(title="Audit Summary")
    table.add_column("File")
    table.add_column("Intention")
    table.add_column("Coherence")
    table.add_column("Quality")
    table.add_column("Duration (s)")
    for m in metrics:
        table.add_row(m["file"], m["intention"], str(m["coherence"]), m["quality"], str(m["duration"]))
    console.print(table)
    
    if export == "csv":
        import pandas as pd
        pd.DataFrame(metrics).to_csv("audit.csv", index=False)
    elif export == "json":
        with open("audit.json", "w") as f:
            json.dump(metrics, f, indent=4)
    
    if plot:
        import matplotlib.pyplot as plt
        import pandas as pd
        df = pd.DataFrame(metrics)
        df.plot(x="file", y="coherence", kind="bar")
        plt.savefig("audit_plot.png")
        console.print("[green]Plot saved: audit_plot.png[/green]")

if __name__ == "__main__":
    # Example plugin register
    def example_hook(config):
        config["hooked"] = True
        return config
    register_hook("post_adapt", example_hook)
    
    app()