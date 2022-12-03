#! /bin/sh
# Rebuild if necessary
make $1.out

# Execute the program defaulting to checking against the example.
ext=${2:-ex}
./$1.out $1.$ext
