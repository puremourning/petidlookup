# Copyright 2016 Ben Jackson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from . import lookup

import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument( '--file', '-f', type=str, help='Input file name' )
  parser.add_argument( '--outfile', '-o', type=str, help='Output file name' )
  args = parser.parse_args()
  lookup.run( args )
