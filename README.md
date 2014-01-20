#HashColor

HashColor is a simple website that will convert a string into a unique
RGB hexcode.

##How it works
It takes the sha1 hash of the string and converts the hash to hex. The first
6 digits of the hash are used to create the color code. The bits of the digest
are anded with a mask to lighten the colors a bit.