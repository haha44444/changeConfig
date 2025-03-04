# -*- coding: utf-8 -*-

import os
from typing import Any, List
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap


class MOTDProcessor:
    def __init__(self):
        self.yaml = YAML()
        self.yaml.preserve_quotes = True
        self.motd_format: int = 0
        self.motd_prefix_line1 = ""
        self.motd_prefix_line2 = ""
        self.motd_key = ""
        self.line_break = "\n"
        self.config_path = "./config.yml"
        self.motd_txt_path = "./motd.txt"
        print(
            "Yaml MOTD Processing Tools \n"
            "Author: haha44444 \n"
            "Version: 1.0.0 \n"
            "Github: https://github.com/haha44444/YamlMOTDProcessingTools \n"
        )

    def get_motd_format(self) -> None:
        format_help = (
            "\nMOTD format choice: \n"
            "1. First line and second line are random motd. \n"
            "   If first line > 41 char than continue write second line. \n"
            "   If the second line > 41 char. skip the motd. \n"
            "Example: \n"
            "random motd 1: \n"
            "2B im a super string :) \n"
            "2T im a string~~~ \n\n"
            "random motd 2: \n"
            "2B im not a string :(\n"
            "2T im a special string xD\n"
            "... \n\n"

            "2. The first line is fixed. The second line are random motd. \n"
            "Example: \n"
            "random motd 1: \n"
            "2B 2b2t server | support ver: 1.8.x-1.21.x \n"
            "2T im a string\n\n"
            "random motd 2:\n"
            "2B 2b2t server | support ver: 1.8.x-1.21.x\n"
            "2T im not a string \n"
            "... \n\n"
        )

        while True:
            print(format_help)
            choice = input("Choice MOTD format (1/2): \n").strip()
            if choice in {'1', '2'}:
                self.motd_format = int(choice)
                return
            print("Invalid input. Please try again. \n")

    def get_motd_prefix(self) -> None:
        motd_help = (
            "Enter first line and second line MOTD prefix. \n"
        )

        print(motd_help)
        input_str1 = input("first line:").strip()
        input_str2 = input("second line:").strip()
        self.motd_prefix_line1 = input_str1
        self.motd_prefix_line2 = input_str2

    def get_config_key(self) -> None:
        motd_key_help = (
            "Enter the MOTD config key path \n"
            "Example config file: \n:"
            "description: \n"
            "   activated: true \n"
            "   text: \n"
            "     - \"im a motd\" \n"
            "You need enter: description.text \n"
        )
        print(motd_key_help)
        motd_key = input("MOTD key: \n").strip()
        self.motd_key = motd_key

    def load_yaml(self, path: str) -> CommentedMap:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return self.yaml.load(f) or CommentedMap()
        except FileNotFoundError:
            raise RuntimeError(f"Config file {path} does not exist")
        except Exception as e:
            raise RuntimeError(f"YAML load failed: {str(e)}")

    def get_yaml_value(self, data: CommentedMap, path: str) -> Any:
        keys = path.split('.')
        current = data
        try:
            for key in keys:
                current = current[key]
            return current
        except KeyError as e:
            raise KeyError(f"Path {path} does not exist in YAML. Missing keys: {e}")

    def process_text(self, lines: List[str]) -> List[str]:
        processed = []
        for line in lines:
            if self.motd_format == 1:
                if len(line) > 41:
                    parts = [line[i:i + 40] for i in range(0, len(line), 40)]
                    if len(parts) > 2:
                        continue  # skip > 2 lines
                    formatted = self._format_motd1(parts)
                else:
                    formatted = f"{self.motd_prefix_line1}{line}{self.line_break}{self.motd_prefix_line2}"
            else:
                formatted = f"{self.motd_prefix_line1}{self.line_break}{self.motd_prefix_line2}{line}"
            processed.append(formatted)
        return processed

    def _format_motd1(self, parts: List[str]) -> str:
        base = f"{self.motd_prefix_line1}{parts[0]}{self.line_break}"
        if len(parts) == 2:
            return f"{base}{self.motd_prefix_line2}{parts[1]}"
        return base

    def run(self) -> None:
        self.get_motd_format()
        self.get_motd_prefix()
        self.get_config_key()

        # load config
        config_data = self.load_yaml(self.config_path)
        original_motd = self.get_yaml_value(config_data, self.motd_key)

        # processing text
        try:
            with open(self.motd_txt_path, 'r', encoding='utf-8') as f:
                text_lines = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            raise RuntimeError(f"{self.motd_txt_path} does not exist")

        processed_lines = self.process_text(text_lines)

        # update and save config file
        config_data['description']['text'] = original_motd + processed_lines
        with open('config_done.yml', 'w', encoding='utf-8') as f:
            self.yaml.dump(config_data, f)

        print("Output file path: ./config_done.yml")
        os.system("pause")


if __name__ == '__main__':
    try:
        processor = MOTDProcessor()
        processor.run()
    except Exception as e:
        print(f"Runtime error: {str(e)}")
        os.system("pause")