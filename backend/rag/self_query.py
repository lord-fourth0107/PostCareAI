import opik
from langchain_openai import ChatOpenAI
from loguru import logger
from models.rag_base import Query
from .base import RAGStep
from .prompt_template import SelfQueryTemplate
import openai
from transformers import AutoTokenizer, AutoModelForCausalLM

# model_name = "meta-llama/LLaMA-2-7b"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)
# The `SelfQuery` class defines a method `generate` that processes a given query by invoking a chain
# of operations and returns the original query.
class SelfQuery(RAGStep):
    @opik.track(name="SelfQuery.generate")
    def generate(self, query: Query ) -> Query:
        """
        The function generates a response to a query using a model, with the option to return the
        original query if in mock mode.
        
        :param query: The `query` parameter in the `generate` method is an object of type `Query`. It
        seems like the method is designed to generate a response based on the input query. The code
        snippet you provided is a template for generating a response using a model, but it is currently
        commented out
        :type query: Query
        :return: The function is currently returning the original `query` object. However, based on the
        comments in the code, it seems like the intention might have been to return the `response`
        generated by the model instead. You should update the return statement to return `response`
        instead of `query`.
        """
        if self._mock:
            return query
        prompt = SelfQueryTemplate().create_template()
        # input_text = "What is the LLaMA model?"
        # inputs = tokenizer(input_text, return_tensors="pt")

        # # Generate the output using the model
        # outputs = model.generate(inputs['input_ids'], max_length=50, num_return_sequences=1)
        # output_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        chain = prompt | model
        response = chain.invoke({"question": query})
        return query ## should return response or query check again
if __name__ == "__main__":
    query = Query.from_str("What is the best way to learn Python?")
    self_query = SelfQuery()
    logger.info(self_query.generate(query))
    