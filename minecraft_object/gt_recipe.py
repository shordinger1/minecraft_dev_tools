from dataclasses import dataclass


@dataclass
class Recipe:
        item_input : list
        fluid_input : list
        item_output : list
        fluid_output : list
        item_output_prob : list
        fluid_output_prob : list

        machine : str
        basic_time : int
        voltage : int



