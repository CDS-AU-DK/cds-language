#!/usr/bin/env bash

VENVNAME=lang101
jupyter kernelspec uninstall $VENVNAME
rm -r $VENVNAME