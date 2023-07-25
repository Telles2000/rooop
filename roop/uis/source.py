from typing import Any, Optional, IO
import gradio

import roop.globals
from roop.utilities import is_image

NAME = 'ROOP.UIS.SOURCE'


def render() -> None:
    with gradio.Column():
        is_source_image = is_image(roop.globals.source_path)
        source_file = gradio.File(
            file_count='single',
            file_types=['.png', '.jpg', '.jpeg', '.webp'],
            label='source_path',
            value=roop.globals.source_path if is_source_image else None
        )
        source_image = gradio.Image(
            label='source_image',
            value=source_file.value['name'] if is_source_image else None,
            height=200,
            visible=is_source_image
        )
        source_file.change(update, inputs=source_file, outputs=source_image)


def update(file: IO[Any]) -> Optional[dict[Any, Any]]:
    if file and is_image(file.name):
        roop.globals.source_path = file.name
        return gradio.update(value=file.name, visible=True)
    roop.globals.source_path = None
    return gradio.update(value=None, visible=False)
