#!/bin/bash
clang++ ./singly-linked-list.cc -fsanitize=address -O1 -fno-omit-frame-pointer -o ./singly-linked-list

./singly-linked-list
