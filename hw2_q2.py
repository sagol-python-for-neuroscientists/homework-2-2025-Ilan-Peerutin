from collections import namedtuple
from enum import Enum

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))


def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    new_agents=[]
    agent_idx=0
    met_bool=1
    while agent_idx<len(agent_listing):
        first_agent=agent_listing[agent_idx]
        if met_bool==0:
            new_agents.append(Agent(first_agent[0],first_agent[1]))
            agent_idx+=1
            continue
        if(first_agent[1].name=="HEALTHY" or first_agent[1].name=="DEAD"):
           new_agents.append(Agent(first_agent[0],first_agent[1]))
           agent_idx+=1
           continue
        meeting_idx=agent_idx+1
        while meeting_idx<len(agent_listing):
            second_agent=agent_listing[meeting_idx]
            if(second_agent[1].name=="HEALTHY" or second_agent[1].name=="DEAD"):
                new_agents.append(Agent(second_agent[0],second_agent[1]))
                meeting_idx+=1
                met_bool=0
                continue
            elif(first_agent[1].name==("CURE") and second_agent[1].name==("CURE")):
                new_agents.append(Agent(second_agent[0],second_agent[1]))
                new_agents.append(Agent(first_agent[0],first_agent[1]))
            elif(first_agent[1].name==("CURE")):
                new_agents.append(Agent(second_agent[0],second_agent[1].value-1))
                new_agents.append(Agent(first_agent[0],first_agent[1]))
            elif(second_agent[1].name==("CURE")):
                new_agents.append(Agent(first_agent[0],first_agent[1].value-1))
                new_agents.append(Agent(second_agent[0],second_agent[1]))
            else:
                new_agents.append(Agent(first_agent[0],first_agent[1].value+1))
                new_agents.append(Agent(second_agent[0],second_agent[1].value+1))
            agent_idx=meeting_idx+1
            met_bool=1
            break
    return new_agents
if __name__ == '__main__':
    # Question 2
    param1 = val1
    return_value = meetup(param1)
    print(f"Question 2 solution: {return_value}")