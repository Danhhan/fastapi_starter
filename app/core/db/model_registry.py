import importlib
import pkgutil
from collections.abc import Iterable


MODEL_PACKAGES: tuple[str, ...] = (
    "app.api.users.models",
)


def import_model_packages(packages: Iterable[str] = MODEL_PACKAGES) -> None:
    for package_name in packages:
        package = importlib.import_module(package_name)

        if not hasattr(package, "__path__"):
            continue

        for _, module_name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
            importlib.import_module(module_name)
