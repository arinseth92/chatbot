import random
import re
import math

class AdvancedRuleBot:
    GREETINGS = {"hi", "hello", "hey", "hii", "hiya"}
    EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye", "later", "see ya"}
    MENU_TEXT = (
        "\nI can:\n"
        "1. Chat with you 👋\n"
        "2. Tell you about my planet 🌍\n"
        "3. Solve math problems ➗✖️➕➖\n"
        "4. Tell you about Intellipaat 🎓\n"
        "Type the number (1-4) to choose a mode, or 'menu' to see these options again!"
    )
    NEGATIVE_RES = {"no", "nope", "nah", "not now", "not a chance", "sorry"}

    def __init__(self):
        self.user_name = ""
        self.mode = None

    def run(self):
        self.greet()
        while True:
            user_input = input("> ").strip().lower()
            if self.handle_exit(user_input):
                break
            if user_input == "menu":
                self.show_menu()
                continue
            if self.mode is None:
                self.set_mode(user_input)
                continue
            self.handle_mode(user_input)

    def greet(self):
        self.user_name = input("👽 Hello Earthling! What's your name?\n> ").strip().title()
        print(f"\n👋 Hi {self.user_name}! ", end="")
        first_input = input("Say 'hi', 'hello', or anything to start:\n> ").strip().lower()
        if first_input in self.GREETINGS:
            print(f"\n🤖 Hi {self.user_name}, what can I do for you, sir?")
            self.show_menu()
        elif first_input in self.NEGATIVE_RES:
            print("No worries! Have a cosmic day 🌌")
            exit()
        else:
            print("I'm ready to help you! Here's what I can do:")
            self.show_menu()

    def handle_exit(self, user_input):
        if any(cmd in user_input for cmd in self.EXIT_COMMANDS):
            print(f"\n👋 Goodbye {self.user_name}! May your day be stellar 🚀")
            return True
        return False

    def show_menu(self):
        print(self.MENU_TEXT)
        self.mode = None

    def set_mode(self, user_input):
        if user_input == "1":
            self.mode = "chat"
            print("\n🎉 Chat Mode activated! Let's have some fun. Type anything!")
        elif user_input == "2":
            self.mode = "planet"
            print("\n🪐 Planet Mode activated! Ask me about my planet, or type anything to get a random fact.")
        elif user_input == "3":
            self.mode = "math"
            print("\n🧮 Math Mode activated! Type math problems like '2+2', 'factorial 5', or 'divide 10 2'.")
        elif user_input == "4":
            self.mode = "intellipaat"
            print("\n🎓 Intellipaat Mode activated! Ask me about Intellipaat, or type anything for a random fact.")
        else:
            print("Please choose a valid option (1-4) or type 'menu' to see choices again.")

    def handle_mode(self, user_input):
        if self.mode == "chat":
            self.chat_mode(user_input)
        elif self.mode == "planet":
            self.planet_mode(user_input)
        elif self.mode == "math":
            self.math_mode(user_input)
        elif self.mode == "intellipaat":
            self.intellipaat_mode(user_input)
        else:
            print("Unknown mode. Type 'menu' to start over.")
            self.mode = None

    def chat_mode(self, user_input):
        if user_input in self.GREETINGS:
            print(f"👋 Hi again, {self.user_name}! How's your day going?")
        elif "how are you" in user_input:
            print("I'm just a bunch of code, but I'm feeling out-of-this-world! 🚀 How are you?")
        elif "thank" in user_input:
            print("You're welcome! 😊 Any other questions for me?")
        elif "who are you" in user_input or "what are you" in user_input:
            print("I'm an advanced rule-based bot from a faraway planet. Here to chat and help!")
        else:
            print(random.choice([
                "That's interesting! Tell me more.",
                "Wow, I hadn't thought of that. What else?",
                "You have a cosmic sense of humor! 😄",
                "I see, go on!",
                "Let's keep chatting! 🌟"
            ]))

    def planet_mode(self, user_input):
        facts = [
            "My planet has lakes of liquid crystal and forests of singing trees! 🌲🎶",
            "Gravity here is so gentle, you can jump 10 meters high!",
            "We have three moons that glow in different colors at night.",
            "Coffee is the universal beverage on my planet. ☕",
            "The sunsets are purple and gold every day.",
            "Our main sport is rock-floating. It's exactly what it sounds like."
        ]
        print(random.choice(facts))

    def math_mode(self, user_input):
        try:
            # Word commands
            if user_input.startswith("add"):
                nums = re.findall(r'\d+', user_input)
                if len(nums) >= 2:
                    result = sum(map(int, nums))
                    print(f"➕ The answer is {result}")
                else:
                    print("Please provide two numbers. Example: add 3 5")
                return
            if user_input.startswith("subtract"):
                nums = re.findall(r'\d+', user_input)
                if len(nums) >= 2:
                    result = int(nums[0]) - int(nums[1])
                    print(f"➖ The answer is {result}")
                else:
                    print("Please provide two numbers. Example: subtract 10 7")
                return
            if user_input.startswith("multiply"):
                nums = re.findall(r'\d+', user_input)
                if len(nums) >= 2:
                    result = int(nums[0]) * int(nums[1])
                    print(f"✖️ The answer is {result}")
                else:
                    print("Please provide two numbers. Example: multiply 4 5")
                return
            if user_input.startswith("divide"):
                nums = re.findall(r'\d+', user_input)
                if len(nums) >= 2:
                    if int(nums[1]) == 0:
                        print("Cannot divide by zero! 🚫")
                    else:
                        result = int(nums[0]) / int(nums[1])
                        print(f"➗ The answer is {result}")
                else:
                    print("Please provide two numbers. Example: divide 20 4")
                return
            # Equation: 2+2, 10-5, etc.
            if re.match(r'^\d+\s*[\+\-\*\/]\s*\d+$', user_input):
                print(f"🧮 The answer is {eval(user_input)}")
                return
            # Factorial
            if "factorial" in user_input:
                num = int(re.findall(r'\d+', user_input)[0])
                print(f"🧩 The factorial of {num} is {math.factorial(num)}")
                return
            # Square root
            if "square root" in user_input:
                num = int(re.findall(r'\d+', user_input)[0])
                print(f"🟢 The square root of {num} is {math.sqrt(num):.4f}")
                return
            print("I didn't understand that. Try '2+2', 'multiply 4 5', or 'factorial 5'.")
        except Exception as e:
            print(f"Oops! I couldn't solve that: {e}")

    def intellipaat_mode(self, user_input):
        facts = [
            "Intellipaat is a global leader in professional online education. 🌍",
            "They offer unique ways to learn new skills and boost your career 🚀.",
            "At Intellipaat, you can learn data science, cloud, AI, and more!",
            "Intellipaat helps thousands of learners upskill every day.",
            "Their courses are designed by experts for real-world jobs."
        ]
        print(random.choice(facts))


if __name__ == "__main__":
    bot = AdvancedRuleBot()
    bot.run()