#!/usr/bin/env bash

clear && docker run "$(docker build -q .)"