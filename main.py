from bigo import questions as big_o
from binsearch import questions as bsearch
# from binsearchtree import questions as ...
from graph import questions as graphs
from hashing import questions as hashing
from insertion import insertion_sort as isort
from quicksort import questions as qsort
from stringsearch import questions as strsearch
from random import randint


BIGO_QUESTIONS = {1: big_o.equality,
                  2: big_o.worse,
                  3: big_o.bigo,
                  4: big_o.order
                  }

GRAPH_QUESTIONS = {1: graphs.trace_breadth,
                   2: graphs.trace_depth,
                   3: graphs.trace_best,
                   4: graphs.trace_mst,
                   5: graphs.trace_tsp}

HASH_QUESTIONS = {1: hashing.produced,
                  2: hashing.result,
                  3: hashing.search,
                  4: hashing.deletion}

ISORT_QUESTIONS = {1: isort.recognition,
                   2: isort.traces,
                   3: isort.iteration_recognition,
                   # 4: isort.explain_stability
                   }

QSORT_QUESTIONS = {1: qsort.trace,
                   2: qsort.spot_wrong
                   }

STR_QUESTIONS = {1: strsearch.bf_comps,
                 2: strsearch.create_table,
                 3: strsearch.create_string,
                 4: strsearch.apply_kmp}

BINSEARCH_QUESTIONS = {1: bsearch.trace,
                       2: bsearch.recursive_calls}

ALL_QUESTIONS = {1: BIGO_QUESTIONS,
                 2: BINSEARCH_QUESTIONS,
                 3: ISORT_QUESTIONS,
                 4: QSORT_QUESTIONS,
                 5: HASH_QUESTIONS,
                 6: STR_QUESTIONS,
                 7: GRAPH_QUESTIONS
                 }


def qsort_trace_only():
    while True:
        QSORT_QUESTIONS.get(1)()


def random_questions():
    topic = ALL_QUESTIONS.get(randint(1, len(ALL_QUESTIONS)))
    quest = topic.get(randint(1, len(topic)))
    quest()
    del topic, quest  # GC topic, quest to prevent case of being stuck


if __name__ == '__main__':
    # User determines whether random questions or not
    user_inp = ''
    while (user_inp != 'random') and (user_inp != 'order'):
        print(f"\n\nPlease enter either of the following strings below: ")
        print(f"    'random' - Questions will be chosen at random")
        print(f"    'order' - Questions will be called in order learned")
        user_inp = str(input("\nEnter choice: "))
    # Picks random question from all hashes storing question functions
    if (user_inp == 'random'):
        while True:
            random_questions()
    # Goes through each question once
    elif (user_inp == 'order'):
        for topic in ALL_QUESTIONS.values():
            for question in topic.values():
                question()