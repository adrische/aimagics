__version__ = "0.0.1"


# Added manually
from .core import AIMagics, line_magic_quotes, cell_magic_dummy_character
from fastcore.aio import enable_async_magics

def load_ipython_extension(ipython):
    "Makes magics available after running `%load_ext aimagics` in Jupyter / ipython"

    ipython.register_magics(AIMagics)

    enable_async_magics(ipython)

    if hasattr(ipython, "input_transformers_cleanup"):
        ipython.input_transformers_cleanup.insert(0, line_magic_quotes)
        ipython.input_transformers_cleanup.insert(0, cell_magic_dummy_character)
    elif hasattr(ipython, "input_transformer_manager"):
        ipython.input_transformer_manager.cleanup_transforms.insert(0, line_magic_quotes)
        ipython.input_transformer_manager.cleanup_transforms.insert(0, cell_magic_dummy_character)