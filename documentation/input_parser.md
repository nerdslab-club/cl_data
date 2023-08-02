### Input-Parser
Normally we will provide only text to the model, 
model will parse the input and create (value, category) from each token.
Here output means the output of Input-Parser

#### Available categories
categories will be used by the category router.
1. function
2. word
3. integer
4. float
5. list
6. bool

#### Available sub-categories
sub-categories will be used by the category router.
1. return_value
2. default
3. integer
4. float
5. list
6. bool
7. word
8. placeholder

#### Available sub-sub-categories
sub-sub-categories will not be used by category router.
sub-sub-categories will be used by Response-Parser.
1. none
2. placeholder
3. param_one
4. param_two
5. param_three
6. param_four
7. param_five
8. param_last

#### Examples of input and output

1. Function execute
   - input: $$add(3,4)
   - output: [
   (7, {category: "integer", subCategory: "return_value", subSubCategory: "none"})
   ]

2. Function represent
   - input: ##add(3,4)
   - output: [
   (add(), {category: "function", subCategory: "integer", subSubCategory: "none" }), 
   (3, {category: "integer", subCategory: "default", subSubCategory: "param_one" }),
   (4, {category: "integer", subCategory: "default", subSubCategory: "param_last" })
   ]

3. Function represent
   - input: ##division(##sum([2,3,4]), ##length([2,3,4]))
   - output: [
   (division(), {category: "function", subCategory: "float", subSubCategory: "none" }), 
   (sum(), {category: "function", subCategory: "float", subSubCategory: "param_one" }),
   ([2,3,4], {category: "list", subCategory: "default", subSubCategory: "param_last" })
   (length, {category: "function", subCategory: "integer", subSubCategory: "param_last" })
   ([2,3,4], {category: "list", subCategory: "default", subSubCategory: "param_last" })
   ]

4. Natural-Language represent
   - input: function for averaging list of number
   - output: [
   (function, {category: "word", subCategory: "default", subSubCategory: "none" }), 
   (for, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (averaging, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (list, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (of, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (number, {category: "word", subCategory: "default", subSubCategory: "none" }),
   ]

5. Natural-Language represent
   - input: adding 3 plus 2
   - output: [
   (adding, {category: "word", subCategory: "default", subSubCategory: "none" }), 
   (3, {category: "integer", subCategory: "default", subSubCategory: "none" }),
   (plus, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (2, {category: "integer", subCategory: "default", subSubCategory: "none" }),
   ]

6. Function placeholder
   - input: @@avg(@list)
   - output: [
   (avg(), {category: "function", subCategory: "float", subSubCategory: "placeholder" }), 
   (@list, {category: "list", subCategory: "placeholder", subSubCategory: "param_last" }),
   ]

N.B. param_last will be used to identify last param of a function.<br>
N.B. subCategory: "default" is used to indicate using default router for list.<br>
N.B. subCategory: "placeholder" is used to indicate using placeholder tag for list.<br>
N.B. no space in function please, other than between params.<br>
N.B. no space in array/list please.

