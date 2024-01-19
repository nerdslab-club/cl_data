# Curious Learner Data

In this repository we have created training and testing data for curious learner generative model. As curious learner 
is a generative next word prediction model, so  each question or prompt may have multiple answers equally correct.
That's why we created the data in such a way that we can generate random answer between the equally correct answers 
each time. And we can generate as many example as we want. 

## Table of Contents

- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [License](#license)
- [Testing](#testing)

## Project Overview

As making a generative LLM is a mammoth task need huge computational power and engineering effort, 
so to prove our models credibility we have to scope the data on which the model will be trained and tested.
We have identified four task which can scope the training and testing data as well as our computational need.
These are,
1. [Function to Function Translation Dataset](func_func) 
2. [Function to Natural Language Translation Dataset](func_nl)
3. [Natural Language to Function Translation Dataset](nl_func)
4. [Natural Language & Function to Natural Language & Function Translation Dataset](nlf_nlf)

Initially we also thought of providing a generalized LLM which can use our 98 functions, but quickly we realized 
the complexity & the scale of that task. And after detail analysis we discard the idea.
For that we have create some data those are,

1. [~~Masked Token Dataset~~](pretrain_data/masked_token_sample_generator.py)
2. [~~Next Token Dataset~~](pretrain_data/next_token_sample_generator.py)

But they aren't used anywhere.

## Folder Structure

Briefly describing the purpose of each major folder in your project.

- `documentation` in this folder you can find example of each training task data and their conversion by IO and Response Parser 
- `functioon_representation` in this package you can find the signature and definition of the available 98 functions - see the [function_representation/README.md](function_representation/README.md) for more details.

- `func_func` in this package you can find function to function translation dataset between the available 98 functions
- `func_nl` in this package you can find the function to natural language translation dataset for the available 98 functions.
- `nl_func` in this package you can find the natural language to function translation dataset for the available 98 functions.
- `nlf_nlf` in this package you can find the natural language & function to natural language & function translation dataset for the available 98 functions.

- `preatain_data` in this package we have the unused masked token dataset and next token dataset for pre-training LLM.

- `io_parser` this is the input output parser package, which converts the input and output string into io_parser_output. 
See [documentation/input_parser.md](documentation/input_parser.md) and [documentation/output_parser.md](documentation/output_parser.md)
for more detail.  
  - `io_parser.py` this is the entry point for IO parser code.
  - `io_parser_utility.py` this file contain IO parser related utility functions
  - `category_parser_utility.py` this file contain category parser related utility functions

IO Parser takes a string and generate the IO parser tuple with token and category map,
The first item of the tuple is token and the second item is category map.
For example,
```python
input = "##division(4.5,2)"
output = [
   (
     "<function MathFunctions.division at 0x117b828c0>",
     {
        "type":"function",
        "subType":"float",
        "subSubType":"execute"
     }
   ),
   (
     4.5,
     {
        "type":"float",
        "subType":"default",
        "subSubType":"param_one"
     }
   ),
   (
     2,
     {
        "type":"integer",
        "subType":"default",
        "subSubType":"param_last"
     },
   )
]
```

- `src` contains the source code of your project.
  - `costants.py` this file contains all available `TaskTypes`, `CategoryType`, `CategorySubType`,
  `CategorySubSubType`,`PlaceholderTokenType`,`FunctionPrefix`,`PretrainTasks`,`SpecialTokens` and `Constants`.
  - `random_value_generator.py` this file have utility functions for generating random values for all data types.
  - `utility.py` contains all utility functions used throughout the project.

- `demonstration.ipynb` is the code demonstration notebook.
- `README.md` is the main documentation file.

## License
This repository is licensed under the GNU Affero General Public License - see the [LICENSE.md](LICENSE) file for details.

## Testing

[demonstration.ipynb](demonstration.ipynb) contain all the test code with proper value assertion, please go through that,
to understand the code and data conversion.