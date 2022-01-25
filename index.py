"""
Project : xixunyun-sign
Author  : Womsxd
License : GNU Affero General Public License v3.0
GitHub  : https://github.com/Womsxd/xixunyun-sign
"""
import main


def main_handler(event: dict, context: dict):
    main.main()
    return 0
