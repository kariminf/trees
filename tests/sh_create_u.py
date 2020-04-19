#!/usr/bin/env python
# -*- coding: utf-8 -*-

#  Copyright 2020 Abdelkrime Aries <kariminfo0@gmail.com>
#
#  ---- AUTHORS ----
#  2020	Abdelkrime Aries <kariminfo0@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shajara.create import GenerateProcessor
from shajara import Tree

rep = {
    "label": "a",
    "children": {
        "ab": {
            "label": "b",
            "children": {
                "be": {"label": "e"},
                "bf": {"label": "f"}
            }
        },
        "ac": {"label": "c"},
        "ad": {"label": "d"}
    }
}

def test_generate_processor():
    generator = GenerateProcessor(rep)
    t = Tree()
    assert t.current_node().label == ""
    t.process(processor=generator)
    assert t.current_node().label == "a"
    t.select_child("ab")
    assert t.current_node().label == "b"
    t.select_child("be")
    assert t.current_node().label == "e"
    t.up().select_child("bf")
    assert t.current_node().label == "f"
    t.up().up().select_child("ac")
    assert t.current_node().label == "c"
    t.up().select_child("ad")
    assert t.current_node().label == "d"