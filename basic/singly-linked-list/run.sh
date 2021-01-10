#!/bin/bash
g++ ./singly-linked-list.cc -fsanitize=address -g3 -O1 -fno-omit-frame-pointer -o ./singly-linked-list.x

./singly-linked-list.x
