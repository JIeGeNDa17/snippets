#!/usr/bin/env bash
git branch --merged | grep -v '\*\|main' | xargs -r git branch -d
