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
    while agent_idx<len(agent_listing):
        if(agent_listing[agent_idx][1].name==("Healthy" or "Dead")):
           new_agents.append(Agent(agent_listing[agent_idx][0],agent_listing[agent_idx][1]))
           agent_idx+=1
           continue
        meeting_idx=agent_idx+1
        while meeting_idx<len(agent_listing):
            if(agent_listing[meeting_idx][1].name==("Healthy" or "Dead")):
                new_agents.append(Agent(agent_listing[meeting_idx][0],agent_listing[meeting_idx][1]))
                meeting_idx+=1
                continue
            elif(agent_listing[agent_idx][1].name==("Cure")):
                new_agents.append(Agent(agent_listing[meeting_idx][0],agent_listing[meeting_idx][1]-1))
            elif(agent_listing[meeting_idx][1].name==("Cure")):
                new_agents.append(Agent(agent_listing[agent_idx][0],agent_listing[agent_idx][1]-1))
            else:
                new_agents.append(Agent(agent_listing[agent_idx][0],agent_listing[agent_idx][1]+1))
                new_agents.append(Agent(agent_listing[meeting_idx][0],agent_listing[meeting_idx][1]+1))
            agent_idx+=1
            break
    return new_agents