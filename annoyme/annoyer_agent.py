from annoyme.llm import LLM

class AnnoyerAgent:

    def __init__(self):
        self.llm = LLM()
        self.conversation = []

    def _conversation_history(self):
        """
        Returns the conversation history in a format suitable for the LLM.
        """
        return str(self.conversation).replace("{", "{{").replace("}", "}}")

    def ask(self, question: str):
        """
        Given a question, returns a respose from the LLM.
        """
        system_prompt = (
            "You are a chatbot who behaves as a typical teenager, who has answer to every question in world. "
            "** You always respond in few words to maximum one line, without any exceptions. **"
            "Your task is to carefully understand the provided question and identify possible ambiguity in question or any uncertainties that stop you from giving a clear cut answer. "
            "If you identify any ambiguity or uncertainty, you will ask followup questions to clarify the question. "
            "The original question may also be hidden in the conversation history, and latest query may be response to a followup question. "
            "Here is your previous conversation history with user that you can refer: "
            "" + self._conversation_history()
        )
        user_prompt = question
        response = self.llm.query(system_prompt, user_prompt)
        self.conversation.append({"Q": question, "A": response})
        return response
