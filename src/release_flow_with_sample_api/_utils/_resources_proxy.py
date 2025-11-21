from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `release_flow_with_sample_api.resources` module.

    This is used so that we can lazily import `release_flow_with_sample_api.resources` only when
    needed *and* so that users can just import `release_flow_with_sample_api` and reference `release_flow_with_sample_api.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("release_flow_with_sample_api.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
