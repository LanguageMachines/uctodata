#!/usr/bin/env python3

import glob
import os
import sys

PREAMBLE = """
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

"""

for configfile in glob.glob('config/tokconfig*'):
    configname = os.path.basename(configfile)
    print("Processing " + configname,file=sys.stderr)
    rules = []
    with open(configfile,'r',encoding='utf-8') as f:
        inruleorder = False
        for line in f:
            line = line.strip()
            if line and line[0] != '#':
                if line == "[RULE-ORDER]":
                    inruleorder = True
                elif line and line[0] == '[':
                    break #done
                elif inruleorder:
                    rules += [ rule.strip() for rule in line.split(' ') if rule.strip() ]

    if not rules:
        print("No rules found, not creating any set", file=sys.stderr)
    else:
        print(len(rules), " rules found", file=sys.stderr)

        with open('setdefinitions/' + configname + '.foliaset.ttl', 'w', encoding='utf-8') as f:
            f.write("@base <http://folia.science.ru.nl/setdefinition/uctodata/" + configname + "/> .")
            f.write(PREAMBLE)
            f.write("<#Set." + configname + ">\n")
            f.write("    a skos:Collection ;\n")
            for rule in rules:
                f.write("    skos:member <#" + rule + "> ;\n")
            f.write("    skos:notation \"" + configname + "\" .\n\n")

            for rule in rules:
                f.write("<#" + rule + ">\n")
                f.write("    a skos:Concept ;\n")
                f.write("    skos:notation \"" + rule + "\" .\n\n")
