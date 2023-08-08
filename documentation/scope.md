### Limitations/Scope
1. Multiple function call math is not in the scope.
2. Function overloading isn't supported.
3. Will not train for paragraph level next token prediction.
4. N.B of Input, Output and Response Parser


for language context learning find a task, find data, separate common part,
train on that task, add that part on the main model.

So we can train part by part.

### Task: 
- Next word prediction
  - Taklami detector is a NWP model
  - https://thecleverprogrammer.com/2023/07/17/next-word-prediction-model-using-python/
- Musked word prediction. -> https://www.youtube.com/watch?v=fmnFOzmdUBE&ab_channel=DataScienceinyourpocket

NEXT Reinforcement learning:
 - Create a task.
 - Do an action.
 - Choose a reward.

OpenAi embedding(text-embedding-ada-002) vs Sentence Transformer embedding 

### Model Archi
Decoder only model, category probability and output probability.