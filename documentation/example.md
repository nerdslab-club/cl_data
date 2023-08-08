## PRETRAIN_DATA
- Long paragraph text, where function token is added for math operations.

#### Masked Token Prediction
No future masking
- input: This is a sample input for testing masked <MASK> prediction.
- output: This is a sample input for testing masked token prediction.

#### Next Token Prediction
With future masking
- input: This is an example
- output: paragraph.

## FINETUNE_DATA

#### FUNC_TO_FUNC_TRANSLATION
- input: ##average([1,2,3])
- output: ##division(##sum([1,2,3]), ##length([1,2,3]))

#### FUNC_TO_NL_TRANSLATION
- input: ##average([1,2,3])
- output: The average of the number 1,2,3

#### NL_TO_FUNC_TRANSLATION **!!! main**
- input: The average of the number 1,2,3
- output: ##average([1,2,3]) => 1

#### NL_TO_NL_TRANSLATION
- input: Function for averaging list of number
- output: @@average(@list)