#!/usr/bin/env python3
# coding: utf-8

"""A simple python3 script template.
"""

import invoke  # http://docs.pyinvoke.org/en/latest/getting_started.html


@invoke.task
def new(ctx, day):
    """new: an invoke task template"""
    ctx.run("cp day.py day{}.py".format(day))
    ctx.run("touch day{}_input.txt".format(day))
