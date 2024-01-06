### Response-Parser
Response parser will take (value, category) tuple and produce a Natural-Language string.
Input: tuple(value, category)
Output: word

#### Available categories
categories will be used by the category router.
1. function
2. word
3. integer
4. float
5. list
6. bool
7. special Ex. <MUSK>, <BOS>, <EOS>, <PAD>

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
9. execute
10. represent

#### Examples of input and output

1. Function execute
   - input: [
   (add(), {category: "function", subCategory: "integer", subSubCategory: "execute" }), 
   (3, {category: "integer", subCategory: "default", subSubCategory: "param_one" }),
   (4, {category: "integer", subCategory: "default", subSubCategory: "param_last" })
   ]
   - output: 7

2. Function represent
   - input: [
   (division(), {category: "function", subCategory: "float", subSubCategory: "placeholder" }), 
   (sum(), {category: "function", subCategory: "float", subSubCategory: "param_one" }),
   (@list, {category: "list", subCategory: "placeholder", subSubCategory: "param_last" })
   (length, {category: "function", subCategory: "integer", subSubCategory: "param_last" })
   (@list, {category: "list", subCategory: "placeholder", subSubCategory: "param_last" })
   ]
   - output: division(sum(@list), length(@list))

3. Natural-Language represent
   - input: [
   (function, {category: "word", subCategory: "default", subSubCategory: "none" }), 
   (for, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (averaging, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (list, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (of, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (number, {category: "word", subCategory: "default", subSubCategory: "none" }),
   ]
   - output: function for averaging list of number

4. Natural-Language represent
   - input: [
   (adding, {category: "word", subCategory: "default", subSubCategory: "none" }), 
   (3, {category: "integer", subCategory: "default", subSubCategory: "none" }),
   (plus, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (2, {category: "integer", subCategory: "default", subSubCategory: "none" }),
   ]
   - output: adding 3 plus 2

5. Natural-Language represent
   - input: [
   (3, {category: "integer", subCategory: "default", subSubCategory: "none" }), 
   (+, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (2, {category: "integer", subCategory: "default", subSubCategory: "none" }),
   (=, {category: "word", subCategory: "default", subSubCategory: "none" }),
   (add(), {category: "function", subCategory: "integer", subSubCategory: "execute" }), 
   (3, {category: "integer", subCategory: "default", subSubCategory: "param_one" }),
   (2, {category: "integer", subCategory: "default", subSubCategory: "param_last" })
   ]
   - output: 3 + 2 = 5

6. Function IOR represent
   - input: [
   (avg(), {category: "function", subCategory: "list", subSubCategory: "represent" }), 
   ([1,2,3], {category: "list", subCategory: "placeholder", subSubCategory: "param_last" }),
   ]
   - output: avg([1,2,3])

7. Function placeholder
   - input: [
   (avg(), {category: "function", subCategory: "float", subSubCategory: "placeholder" }), 
   (@list, {category: "list", subCategory: "placeholder", subSubCategory: "param_last" }),
   ]
   - output: avg(@list)


N.B. If category: function and subSubCategory: "placeholder" found once all consecutive function execution is halt. <br>
N.B. If category: function and subSubCategory: "represent" found once all consecutive function execution is halt. <br>
