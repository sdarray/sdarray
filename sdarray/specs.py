def _load_specs():
    from pathlib import Path
    import toml
    import sdarray as sd

    specs_dir = Path(sd.__path__[0]) / "specs"

    for path in specs_dir.glob("*/*.toml"):
        with open(path) as f:
            globals()[path.stem] = toml.load(f)


_load_specs()
