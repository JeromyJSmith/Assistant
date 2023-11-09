from function import Function, Property
from dotenv import load_dotenv
from assistant import AIAssistant
from dataherald import answer_question

load_dotenv()
class DataheraldFunction(Function):
    def __init__(self):
        super().__init__(
            name="dataherald",
            description="Answer questions on a given database",
            parameters=[
                Property(
                    name="db_name",
                    description="The database to query, possible values are: RealEstate, SenateStock",
                    type="string",
                    required=False,
                ),
                Property(
                    name="question",
                    description="The question to answer",
                    type="string",
                    required=True,
                ),
            ]
        )
    def function(self, db_name, question):
        return answer_question(question, db_name)

if __name__ == "__main__":
    assistant = AIAssistant(
    instruction="",
    model="gpt-3.5-turbo-1106",
    functions=[DataheraldFunction()]
    )
    thread = assistant.create_thread()
    user_input = ""
    while user_input != "bye":
        print("\033[34mType your question or type bye to quit: ")
        user_input = input("\033[32mYou: ")
        message = assistant.chat(
        thread_id=thread.id, content=user_input
        )
        print(f"\033[33m{message}")
    
    