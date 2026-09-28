# Model-Based Vacuum Cleaner

import random
import time


class Environment:
    """Represents a two-room environment (Room A and Room B)."""

    def __init__(self):
      
        self.location_condition = {
            "A": random.choice(["Clean", "Dirty"]),
            "B": random.choice(["Clean", "Dirty"]),
        }

    def get_percept(self, agent_location):
        """Returns current location and its condition."""
        return agent_location, self.location_condition[agent_location]

    def update_state(self, location, action):
        """Updates the environment based on the agent's action."""
        if action == "Suck":
            self.location_condition[location] = "Clean"


class ModelBasedVacuumAgent:
    """Model-Based Reflex Vacuum Cleaner Agent."""

    def __init__(self):
        # Internal Model (Internal State / Memory)
        self.model = {
            "A": "Unknown",
            "B": "Unknown",
        }
        self.current_location = "A"  # Starts at Room A

    def update_internal_state(self, location, status):
        """Updates internal memory based on latest percepts and past actions."""
        self.model[location] = status

    def choose_action(self, status):
        """
        Decision-making logic based on state + rules:
        1. If current room is Dirty -> Suck.
        2. If current room is Clean and other room condition is Dirty or Unknown -> Move.
        3. If both rooms are known to be Clean -> Turn Off / Do Nothing.
        """
      
        if status == "Dirty":
            return "Suck"

        
        if all(cond == "Clean" for cond in self.model.values()):
            return "No Op"  # Shut down / Do nothing

       
        if self.current_location == "A":
            return "Right"
        else:
            return "Left"

    def execute_action(self, action, env):
        """Executes the action and updates position."""
        print(f"  [Action Executed]: {action}")

        if action == "Suck":
            env.update_state(self.current_location, "Clean")
            self.model[self.current_location] = "Clean"
        elif action == "Right":
            self.current_location = "B"
        elif action == "Left":
            self.current_location = "A"


def run_simulation(steps=6):
    env = Environment()
    agent = ModelBasedVacuumAgent()

    print("=" * 50)
    print("MODEL-BASED VACUUM CLEANER AGENT SIMULATION")
    print("=" * 50)
    print(f"Initial Environment State: {env.location_condition}\n")

    for step in range(1, steps + 1):
    
        location, status = env.get_percept(agent.current_location)

     
        agent.update_internal_state(location, status)


        print(f"Step {step}:")
        print(f"  Percept          : Location={location}, Status={status}")
        print(f"  Internal Memory  : {agent.model}")

        action = agent.choose_action(status)

        agent.execute_action(action, env)
        print(f"  Updated Env State: {env.location_condition}")
        print("-" * 50)

        if action == "No Op":
            print("All rooms are clean according to the internal model! Agent stopping.")
            break

        time.sleep(0.5)


if __name__ == "__main__":
    run_simulation()
