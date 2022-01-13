# Copyright 2022 andremmfaria
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

from argparse import ArgumentParser
from docxtpl import DocxTemplate
import toml

CONFIG_DIR = "./config"


def main() -> None:
    parser = generate_parser()
    args = parser.parse_args()

    config = toml.load(CONFIG_DIR + "/general_config.toml")

    doc = DocxTemplate(args.template)
    variables = toml.load(args.variables)

    doc.render(variables)
    doc.save(config["output_file_name"])


def generate_parser() -> ArgumentParser:
    parser = ArgumentParser(description="Render report template")
    parser.add_argument(
        "--template",
        "-t",
        type=str,
        help="The template path for variable substitution",
    )
    parser.add_argument(
        "--variables",
        "-v",
        type=str,
        help="Variables to be replaced on the template. Must be a toml file",
    )

    return parser
