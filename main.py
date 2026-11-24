#!/usr/bin/env python3
"""Entry for make.fun bounty news-image-20261124.

The front page for Tuesday 24 November 2026 is the entry.png beside
this file. The program copies it to the output directory, using only
the Python standard library. Outside the grader's container,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT, "entry.png"))
