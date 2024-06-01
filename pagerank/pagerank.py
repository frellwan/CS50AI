import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    n = len(corpus)

    # Copy the corpus of pages and initialize each value to 1/# pages
    sample_pages = dict.fromkeys(corpus, (1-damping_factor)/n)

    size = len(corpus[page])
    # If this page has no links all pages are equally likely with p = 1/# pages
    if size == 0:
        sample_pages.update(dict.fromkeys(sample_pages, 1/n))

    # Otherwise add damping_factor/size for each link in page
    else:
        for link in corpus[page]:
            sample_pages[link] += damping_factor/size

    return sample_pages


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initialize probability dict to 0 for all pages
    sample_pages = dict.fromkeys(corpus, 0.0)

    # Initially choose a random page
    sample = random.choice(list(corpus.keys()))

    # Randomly sample from corpus n times
    for i in range(n):
        # Calculate transition probabilities using current page
        transition_probs = transition_model(corpus, sample, damping_factor)

        # randomly choose a new page based on transition probabilities
        keys = list(transition_probs.keys())
        values = list(transition_probs.values())
        sample = random.choices(keys, weights=values)[0]

        # Update 'probability' for page
        sample_pages[sample] += 1.0/n

    return sample_pages


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    n = len(corpus)

    # Copy the corpus of pages and initialize each value to 1/n
    sample_pages = dict.fromkeys(corpus, 1.0/n)

    d_factor = (1-damping_factor)/n

    # Randomly sample from corpus n times
    converged = False
    while not converged:
        converged = True

        # Create dictionary for updated pr's
        updated_pr = dict.fromkeys(corpus, d_factor)

        for corpus_page, links in corpus.items():
            # If there are links update the linked pages
            if len(links) > 0:
                for page in links:
                    updated_pr[page] += damping_factor * sample_pages[corpus_page]/len(links)
            else:
                for page in sample_pages:
                    updated_pr[page] += damping_factor * sample_pages[corpus_page]/len(sample_pages)

        for page in sample_pages:
            current_pr = sample_pages[page]

            sample_pages[page] = updated_pr[page]
            if abs(current_pr - updated_pr[page]) > 0.001:
                converged = False

    return sample_pages


if __name__ == "__main__":
    main()
