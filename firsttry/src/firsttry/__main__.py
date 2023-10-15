"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Firsttry."""


if __name__ == "__main__":
    main(prog_name="firsttry")  # pragma: no cover
