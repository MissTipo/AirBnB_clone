#!/usr/bin/env python3
import cmd

class Hellopeers(cmd.Cmd):
    prompt = "(HBNB) "

    def do_welcome(self, line):
        if line:
            print("welcome", line)
        else:
            print("welcome no arguments")

    def do_greet(self, line):
        print("Hello Boss", line)

    def do_EOF(self, line):
        return True

if __name__ == "__main__":
    Hellopeers().cmdloop('Welcome')
