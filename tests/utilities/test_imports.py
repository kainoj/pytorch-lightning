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

from pytorch_lightning.utilities import _module_available


def test_module_exists():
    """Test if the some 3rd party libs are available."""
    assert _module_available("torch")
    assert _module_available("torch.nn.parallel")
    assert not _module_available("torch.nn.asdf")
    assert not _module_available("asdf")
    assert not _module_available("asdf.bla.asdf")
