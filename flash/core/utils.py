# Copyright The PyTorch Lightning team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import Callable, Dict, Mapping, Sequence, Union

def bind_method(obj, func, target_func_name=None):
    setattr(obj, target_func_name or func.__name__, func.__get__(obj, type(obj)))

def get_callable_name(fn_or_class: Union[Callable, object]) -> str:
    return getattr(fn_or_class, "__name__", fn_or_class.__class__.__name__).lower()


def get_callable_dict(fn: Union[Callable, Mapping, Sequence]) -> Union[Dict, Mapping]:
    if isinstance(fn, Mapping):
        return fn
    elif isinstance(fn, Sequence):
        return {get_callable_name(f): f for f in fn}
    elif callable(fn):
        return {get_callable_name(fn): fn}
