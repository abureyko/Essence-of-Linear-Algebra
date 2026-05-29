from pathlib import Path


def save_lesson_figure(fig, current_file, filename):
    """Save a lesson figure into the shared README-ready gallery."""
    project_root = Path(current_file).resolve().parent
    if project_root.name == "02_linear_span":
        project_root = project_root.parent

    plots_dir = project_root / "assets" / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    output_path = plots_dir / filename
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    print(f"График сохранен: {output_path}")
