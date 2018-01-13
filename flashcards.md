# Agent

a computer system capable of autonomous action in some environment, in order to achiee its delegated goals

Formal definition $Ag: R^E \rightarrow Ac$
or $<see,action>$

Mapping history to an action.

# How is an agent different to an object?

- they're autonomous
- they're capable of reactive/proactive behaviour
- they're not passive

# Agent actuator

A thing an agent uses to change the environment (ie variable, robotic arm, POST request)

# Reactive system

A system which responds to changs in its environment in real time

# Purely reactive system

A system which only responds to the last state (not previous ones)

# Pro-active system

- A system which 'takes the initiative'
- Not event driven
- Has goals

# Social Ability

An ability to interact with other agents, requires Cooperation, coordination, and negotiation.

## Cooperation

Working together, usually because its:

- cheaper
- faster
- impossible otherwise
- produces a better result:

## Coordination

Managing 'interdependencies' (i.e. non-shareable resources) between agents

## Negotiation

The ability to reach an agreement

# Environment

Different situations an agent can be in

## Inaccessible

Don't know the complete picture

## Non-deterministic

non-deterministic

## Episodic

Only care about the current episode (state), and not previous ones

## Dynamic

Changes by itself

## Continuous

Non-finite number of actions or percepts (observations)


# Intentional System

"A system where behaviour can be predicted by the method of attributing belief, desires, and rational acumen"
(A way of abstracting how an agent behaves)
*e.g. Agent A believed it needed paper, so it ordered some*

# Run (and its maths)

$r: e_0 \rightarrow^{a_0}\ e_1 \rightarrow^{a_1}\ e_2 \rightarrow^{a_2}\ e_3 \ldots$

`State -> Action -> State -> Action ....`

**$R$** is the set of all possible finite runs over E and Ac
**$R^{Ac}$** is the set of all runs ending with an action
**$R^{E}$** is the set of all runs ending with a state
**$R(Ag,Env)$** is all possible runs for a given Environment and Agent.

# State Transformer Function

$\tau : R^{Ac} \rightarrow  \wp(E)$

function dictating what possible states an action and history will lead to (non-deterministic)

# System (formally)

An agent and an environment

$<Ag,Env>$

# Environment (formally)

States, first state, and state transfer function.

$<E,e_0,\tau>$

# 2 Agents being Behaviourally Equivalent

with respect to an environment: iff $R(Ag_1,Env) = R(Ag_2,Env)$, (agents will have the same run given the same environment)

# Percept
Output of a 'see' function, input of the 'action' function (which picks the action).

or if there's state, it's combined with the previous state in the 'next' function to find the next state (which is then fed into the 'action' function)

# Difference between State and Stateless

State:
```
see: E -> Per
next: I x Per -> I
action: I -> Ac
```
stateless:
```
see: E -> Per
action: Per -> Ac
```

# Indestinguishable environments

the agent's `see` function outputs the same for both environments

# Measuring Utility

Either by state or by run.

