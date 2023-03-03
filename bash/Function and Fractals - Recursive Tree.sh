#!/usr/bin/env bash

drawLine() {
  for rows in $( seq 1 $1 ); do
      for underscore in $( seq 1 100 ); do
          printf "_"
      done
      printf "\n"
  done
}

