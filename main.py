"""
Entry point for Annoy-Me
"""
from colorama import Fore, Style
from dotenv import load_dotenv

from annoyme.annoyer_agent import AnnoyerAgent

def main():
    load_dotenv()

    agent = AnnoyerAgent()
    print("-" * 80)
    
    while True:        
        question = input("\nEnter your question, (or q|quit): ").strip()
        if question.lower() in ("q", "quit"):
            break

        answer = agent.ask(question)
        print(Fore.LIGHTBLUE_EX)
        print(answer, Style.RESET_ALL)

if __name__ == "__main__":
    main()
