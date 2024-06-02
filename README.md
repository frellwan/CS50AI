# ReadMe
A collection of projects from Harvard's CS50ai Course

## Degrees
![image](https://github.com/frellwan/CS50AI/assets/12740967/f72d692a-38dd-41e3-9290-a5c5dd1b3f07)

Implementation of a Breadth-First Search Algorithm to find the degrees of separation between two selected actors, by films they have starred in.

## Tic Tac Toe
![image](https://github.com/frellwan/CS50AI/assets/12740967/925d0981-57bd-44ee-9c7d-3c78f30876b2)

Implementation of a Tic Tac Toe AI using a Minimax Algorithm with Alpha-Beta pruning. Randomisation varies the AI's moves where several have equal utility.

## Knights
![image](https://github.com/frellwan/CS50AI/assets/12740967/da267e30-ede9-484f-9821-615fee2a33ba)

Solutions to 'Knights and Knaves' style logic puzzles using Propositional Logic and Model Checking.

## Minesweeper
![image](https://github.com/frellwan/CS50AI/assets/12740967/35fcce6c-63e1-44a2-a8ed-563aeedaad38)

An AI that plays the classic Windows 'Minesweeper' game, using a knowledge base and inference to generate new knowledge about the game state.

## Pagerank
![image](https://github.com/frellwan/CS50AI/assets/12740967/35679855-f69d-4987-b59f-2f7c8a9996f9)

An AI that ranks web pages by importance - similar to the Google PageRank AI - using both a Random Surfer Model and an Iterative Algorithm.

## Heredity
![image](https://github.com/frellwan/CS50AI/assets/12740967/d4818ea0-4bdc-4787-b70a-387b96b72314)

An AI that predicts the likelihood of members of a family having a 0, 1, or 2 copies of a gene, and a trait caused by that gene, using a Bayesian Network and Inference by Enumeration.

## Crossword
![image](https://github.com/frellwan/CS50AI/assets/12740967/34437fc1-0201-4bc0-823d-a8de3eef5555)

An AI that generates crossword puzzles, by treating the crossword generation as a constraint satisfaction problem and using a backtracking search algorithm.

## Shopping
![image](https://github.com/frellwan/CS50AI/assets/12740967/3c05ccb1-4f79-4ded-a2c8-9807c82899b3)

An AI that predicts whether online shopping customers will complete a purchase, using the Scikit-Learn k-Nearest Neighbour classifier on a customer dataset.

## Nim
![image](https://github.com/frellwan/CS50AI/assets/12740967/44b4b20a-c002-475c-9097-da05198f2c0e)

An AI that teaches itself to play the game 'Nim' using Reinforcement Learning. A Q-Learning algorithm with ε-Greedy Decision Making is used to estimate the value of actions for game states.

## Traffic
![image](https://github.com/frellwan/CS50AI/assets/12740967/fa920328-ac16-4f0e-b6ce-375780e0cf36)

An AI that identifies which traffic sign appears in a photograph, using a TensorFlow convolutional neural network.

## Parser
![image](https://github.com/frellwan/CS50AI/assets/12740967/ad16a62e-2658-4178-9bab-acfaa038524b)

An AI that can parse sentences and extract noun phrases, using the context-free grammar formalism and the Python nltk library.

# Attention
![attention_3_10_1](https://github.com/frellwan/CS50AI/assets/12740967/cb960a55-8cc2-4ac4-a774-ce34ec7bbdb6)

One way to create language models is to build a Masked Language Model, where a language model is trained to predict a “masked” word that is missing from a sequence of text. BERT is a transformer-based language model developed by Google, and it was trained with this approach: the language model was trained to predict a masked word based on the surrounding context words.

BERT uses a transformer architecture and therefore uses an attention mechanism for understanding language. In the base BERT model, the transformer uses 12 layers, where each layer has 12 self-attention heads, for a total of 144 self-attention heads.

