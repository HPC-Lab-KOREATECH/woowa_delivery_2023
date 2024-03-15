from collections.abc import Callable, MutableMapping
from importlib.abc import SourceLoader
from types import TracebackType
from typing import Any

from django.http.request import HttpRequest, QueryDict
from django.http.response import Http404, HttpResponse
from django.utils.safestring import SafeText

DEBUG_ENGINE: Any
HIDDEN_SETTINGS: Any
CLEANSED_SUBSTITUTE: str
CURRENT_DIR: Any

class CallableSettingWrapper:
    def __init__(self, callable_setting: Callable[..., Any] | type[Any]) -> None: ...

def cleanse_setting(key: int | str, value: Any) -> Any: ...
def get_safe_settings() -> dict[str, Any]: ...
def technical_500_response(
    request: Any, exc_type: Any, exc_value: Any, tb: Any, status_code: int = ...
) -> Any: ...
def get_default_exception_reporter_filter() -> ExceptionReporterFilter: ...
def get_exception_reporter_filter(
    request: HttpRequest | None,
) -> ExceptionReporterFilter: ...

class ExceptionReporterFilter:
    def get_post_parameters(self, request: Any) -> Any: ...
    def get_traceback_frame_variables(self, request: Any, tb_frame: Any) -> Any: ...

class SafeExceptionReporterFilter(ExceptionReporterFilter):
    def is_active(self, request: HttpRequest | None) -> bool: ...
    def get_cleansed_multivaluedict(
        self, request: HttpRequest, multivaluedict: QueryDict
    ) -> QueryDict: ...
    def get_post_parameters(
        self, request: HttpRequest | None
    ) -> MutableMapping[str, Any]: ...
    def cleanse_special_types(self, request: HttpRequest | None, value: Any) -> Any: ...
    def get_traceback_frame_variables(self, request: Any, tb_frame: Any) -> Any: ...

class ExceptionReporter:
    request: HttpRequest | None = ...
    filter: ExceptionReporterFilter = ...
    exc_type: type[BaseException] | None = ...
    exc_value: str | None = ...
    tb: TracebackType | None = ...
    is_email: bool = ...
    template_info: None = ...
    template_does_not_exist: bool = ...
    postmortem: None = ...
    def __init__(
        self,
        request: HttpRequest | None,
        exc_type: type[BaseException] | None,
        exc_value: str | BaseException | None,
        tb: TracebackType | None,
        is_email: bool = ...,
    ) -> None: ...
    def get_traceback_data(self) -> dict[str, Any]: ...
    def get_traceback_html(self) -> SafeText: ...
    def get_traceback_text(self) -> SafeText: ...
    def get_traceback_frames(self) -> list[Any]: ...
    def _get_lines_from_file(
        self,
        filename: str,
        lineno: int,
        context_lines: int,
        loader: SourceLoader | None = ...,
        module_name: str | None = ...,
    ) -> Any: ...

def technical_404_response(
    request: HttpRequest, exception: Http404
) -> HttpResponse: ...
def default_urlconf(request: HttpResponse | None) -> HttpResponse: ...
