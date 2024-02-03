import os
import re
from random import choice, randint
from os import path
from dataclasses import dataclass


@dataclass
class Term:
    term: str
    definition: str

    
def definition_cleaner(definition:str) -> str:
    txt = definition.replace('Definition: ', '')
    clean_txt = re.sub(r"id:.*\]\[", "", txt)
    clean_txt= clean_txt.replace('[', '').replace(']', '')
    return clean_txt


class Library:
    def __init__(self) -> None:
        self.terms_loc = os.path.expanduser('~/Documents/Org-Roam')
        self.answers = []

    @property
    def terms(self) -> list:
        terms_library = []
        
        folder = os.listdir(self.terms_loc)

        folder = [org_file for org_file in folder if ".org" in org_file]

        for item in folder:

            with open(f'{self.terms_loc}/{item}', "r") as a_file:
                file = a_file.read().strip().split('\n')

            terms_library.append(
                Term(
                    term = file[5].replace('Term: ', ''),
                    definition = definition_cleaner(file[6])))

        return terms_library


    def mk_question(self) -> dict:
        question = {}
        used_opts= []
        
        used_opts.append(randint(1, 5))

        answer = self.terms.pop()

        question.update({used_opts[0] : answer.definition})

        while (len(question) <= 3):
            opts = randint(1, 5)
            
            if opts not in used_opts:
                used_opts.append(opts)
                rand_term = choice(self.terms)
                question.update({opts: rand_term.definition })

        return dict(sorted(question.items()))




practice = Library()
for item in practice.terms:
    question = practice.mk_question()
    print(len(question))
