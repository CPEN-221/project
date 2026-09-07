---
layout: default
title: Project notes
description: Notes on software design and requirements for the CPEN 221A team project.
hero_title: Project Notes
term: Fall 2026
permalink: /notes/
---

<figure class="project-figure project-figure--wide">
  <img src="{{ '/assets/images/project-notes.jpeg' | relative_url }}" alt="An open notebook with handwritten annotations and diagrams resting on a desk.">
</figure>

# Software design: observation, interviews, and values

For this project, design begins before you decide what to build. You first need to understand what people are trying to do, where the current situation fails them, and which constraints matter. Only then can you make a defensible choice about the software.

## 1. What counts as design

Software design includes at least three kinds of decisions:

- Visual design covers layout, colour, and readability.
- Interaction design covers the steps a person takes and whether those steps feel natural or frustrating.
- Conceptual design covers the ideas and relationships that give the system its structure.

These decisions affect one another. A clean interface cannot rescue a confused conceptual model, and a well-factored implementation cannot make the wrong product useful. Start by asking what problem deserves attention, not what your team already knows how to build.

## 2. Find a problem by watching the work

People often describe an idealized version of their work. Observation shows what actually happens. Watch the sequence of actions, the interruptions, and the tools that people improvise when the official process does not suit them.

Workarounds are especially informative. A spreadsheet used as a scheduling system or a paper note taped beside a monitor points to a need that the existing system has missed. Errors are informative too. They often reveal a mismatch between the user's understanding and the model imposed by the software.

Do not rush to diagnose the problem while you are still observing it. Write down what happened, the circumstances, and anything that surprised you. Interpretation comes next.

## 3. Use interviews to learn why

Observation tells you what someone did. An interview can help you understand why they did it.

Begin with the person's role and routine. Ask for a recent, concrete example: “Can you walk me through the last time this happened?” Questions about an actual event usually produce better evidence than questions about a hypothetical feature.

A useful interview has room to wander. Follow an unexpected detail when it seems important, and allow a pause instead of answering your own question. Avoid yes-or-no questions and questions that suggest the answer you hope to hear. Before you finish, summarize what you think you learned and give the other person a chance to correct you.

## 4. Interpret what you heard

Do more than condense your notes. Look for contradictions, surprises, and points of tension. A person may say that speed matters most, for example, while repeatedly stopping to double-check risky actions. That contradiction may tell you more than either statement alone.

Ask yourself:

- Which goals and values does this person appear to prioritize?
- Where do those goals conflict with the assumptions built into the current tools?
- Which social, technical, legal, or ethical boundaries shape the decision?
- What evidence supports our interpretation, and what are we merely guessing?

Your answers should lead to a specific point of view about the problem and a sensible boundary for the project. They should also reveal what you still need to learn.

## 5. Account for the people and values around the system

Direct users are not the only people affected by software. [Value sensitive design](https://en.wikipedia.org/wiki/Value_sensitive_design) offers a way to examine the human values involved in a design. For this project, use it as a prompt for four lines of inquiry.

### Stakeholders

Identify the people who will use the system and the people who may experience its consequences without choosing to use it. Navigation software, for example, helps drivers find a faster route but may direct traffic through a residential neighbourhood. The residents are stakeholders even though they never opened the application.

### Time

Consider what happens after the first use. People adapt to a tool, organizations build procedures around it, and old versions eventually become difficult to support. A design that is harmless during a small trial may behave differently after years of use.

### Scale

Ask what changes if many people adopt the system. Predictive text can save a few seconds on one message. At scale, it may also contribute to a larger volume of messages and a stronger expectation that people remain available. Small design choices can become social conventions when a system is widely used.

### Values

Name the values at stake rather than treating them as a general desire to “do good.” Autonomy, privacy, dignity, fairness, sustainability, and community may point toward different designs. If two values conflict, state the trade-off your team is making and who will bear its cost.

## 6. Allow for reuse and non-use

People will sometimes use software in ways its designers did not anticipate. A spreadsheet may become a drawing surface; a browser may become the main environment for an entire job. Such reuse can expose useful flexibility in a design.

Refusing a technology can be equally deliberate. Someone may opt out of facial recognition because the convenience is not worth the loss of privacy. Where non-use is possible, the system should not punish it through needless barriers or degraded access.

## 7. Values also appear in code

The same questions arise in software construction. A class, API, or protocol determines who can use a capability, which operations are easy, and which assumptions later programmers inherit. Defaults and names also steer behaviour.

Correctness remains essential, but it is not the only test of a design. As you work on the project, be prepared to explain whose problem your design addresses, what evidence shaped it, and which trade-offs appear in its interfaces.

# Responsible design: generating ideas and checking consequences

Once your team understands the problem, you need alternatives. The first plausible solution often looks inevitable only because nobody made time to propose a second one.

## 1. Diverge, then converge

Design usually moves back and forth between two modes:

| Divergent thinking | Convergent thinking |
| --- | --- |
| Generate alternatives | Compare and combine ideas |
| Expand the range of possibilities | Resolve conflicts and constraints |
| Defer feasibility judgments briefly | Test feasibility and trade-offs |
| Aim for breadth | Aim for a coherent choice |

Divergence gives the team material to work with. Convergence turns that material into a design you can defend and implement. Converging too early leaves promising ideas unexplored; diverging indefinitely leaves you with no decision.

## 2. Make room for alternatives

During brainstorming, record ideas before debating them. Build on another person's suggestion, and include ideas that seem impractical if they expose a useful assumption. Quantity is helpful at this stage because the obvious ideas tend to arrive first.

Lateral-thinking prompts can loosen a stuck discussion. Ask what would happen if a familiar assumption were reversed, push a flawed idea to an absurd extreme, or examine the part of the system everyone has ignored. You can also look outside the immediate domain. Other tools, physical spaces, and improvised user practices may suggest a different way to frame the problem.

None of these techniques guarantees a good answer. Their purpose is to prevent the team from mistaking habit for necessity.

## 3. Organize features around concepts

As you converge, look for concepts that describe meaningful units of behaviour. A concept names an idea that makes sense to the person using the system, such as a Post, Comment, Session, or Favourite. Screen widgets and data structures are possible implementations of that idea.

A useful concept has a clear purpose, a meaning that can be explained without referring to its implementation, and boundaries that let it change without disturbing unrelated parts of the system. Thinking in concepts helps turn a loose feature list into a model that the team can discuss.

## 4. Keep concepts as independent as the design permits

Concepts will interact, but one should not silently drag in another. Suppose a `Post` implementation always contains `Comment` objects. Any application that wants posts must now accept comments as well. That is an intrinsic dependency built into the component.

If commenting is optional in the product, make the relationship explicit outside the two concepts. A dependency diagram can help the team see which relationships are necessary and which are accidental. This is one application of David Parnas's information-hiding principle: hide decisions that other modules do not need to know.

## 5. Use values while generating and selecting ideas

Values can open new directions during divergence. Asking how a design would work for a child, a non-user, or someone with limited connectivity may produce alternatives the team had not considered.

During convergence, those same values become criteria. Which proposal protects autonomy? Which one excludes people? What information does each proposal collect, and is that information necessary? Treat the answers as design evidence, alongside cost and technical feasibility.

## 6. Check intended and unintended consequences

Responsible innovation requires attention to both benefits and harms. For each serious proposal, ask who benefits if it works, who could be harmed even when it works as intended, and how it might be misused. Then ask what changes when the system fails.

You will not foresee every outcome. The point is to notice plausible consequences early enough to change the design.

## 7. Do this work before implementation makes it expensive

Ethical risks discovered late can force a redesign, invalidate collected data, or expose people to harm. They can also damage the trust on which a product depends. A small team cannot study every possible consequence, but its size is not a reason to ignore the most credible ones.

Document the risks you considered, the evidence available, and any uncertainty that remains. This record will make later decisions easier to revisit.

## 8. Borrow methods from responsible-technology practice

Several established methods can provide prompts when your team is unsure where to begin:

- Ethical OS uses scenarios to surface possible misuse and unintended effects.
- Consequence Scanning asks a team to map the direct and indirect effects of a product decision.
- Society-Centered Design broadens the design brief beyond an individual user to communities and institutions.
- B Corp assessments and responsible-innovation labs offer examples of organizational accountability.

The work of Safiya Noble, Ruha Benjamin, Joy Buolamwini, Rumman Chowdhury, and Kathy Pham offers concrete studies of how technical systems interact with power, discrimination, and public institutions. Consult the work itself rather than treating the names as a checklist.

## 9. Frame the intended social impact

Some projects address problems involving dignity, agency, inclusion, or justice. These problems are often entangled with policy, institutions, and behaviour, so software alone will not settle them.

The following heuristic can help compare possible areas of impact:

> Social impact ≈ importance of the service × vulnerability of the affected population × scale of the effect

Treat this as a reminder to examine all three factors, not as a calculation or proof that one project is more worthy than another. A service may be important but reach few people; a widely used system may have only a small effect on each person; a vulnerable population may face constraints the team does not yet understand.

Treat claims about impact as hypotheses. Test them through stakeholder research and revise them when the evidence changes.

## 10. Write an impact case

An impact case states the reasoning behind a proposal in a form that others can question:

1. The problem of *X* matters because _____.
2. We propose *Y* as a response.
3. We believe *Y* could address *X* because _____.
4. We will examine *N* to learn whether that belief is supported.

Choose a measure that speaks to the problem, not merely to activity. Downloads, page views, or time spent may be easy to count without showing that anyone's situation improved.

## 11. Map the surrounding system

A stakeholder map can reveal relationships that a user-centred view misses. Begin with roughly five groups connected to the problem. These might include users, non-users, community organizations, service providers, regulators, or funders. Name a few actual organizations or roles within each group.

For each group, ask what it wants, what influence it holds, what constraints it faces, and what it may fail to see. Then look across the map. Where are goals aligned? Where are they in conflict? Which structural gap could your team realistically address?

The map will be incomplete. Its value lies in making the team's current understanding visible and open to correction.

## 12. Carry the reasoning into the project

Keep a record of alternatives, not just the winning idea. State the values and evidence used to choose among them. Finally, identify a consequence that would cause your team to revise or abandon the design. These notes will make the later requirements, architecture, and reflection stages much more concrete.

# Software requirements

Once you have a problem and a proposed solution, you will probably want to start coding. A prototype can be the quickest way to learn whether an idea is feasible, particularly when it is cheap to build and safe to discard. Early consumer products often develop this way. The [history of Facebook](https://en.wikipedia.org/wiki/History_of_Facebook), for example, shows a rough initial product changing as its audience grew.

That approach has limits. A prototype may be expensive to deploy, a client may need an agreed definition of success, or a failure may put people's health or safety at risk. The troubled launch of [HealthCare.gov](https://en.wikipedia.org/wiki/HealthCare.gov) is a familiar example of a public service whose early technical failures had immediate consequences for its users.

Requirements make the conditions for acceptance explicit. A requirement is a statement that must be true for the system to be considered acceptable. For a mobile game, one requirement might be:

> During play, the frame rate must not fall below 60 frames per second on any supported device.

The number is not automatically a good requirement. The team still needs a reason for choosing it and a practical way to verify it. Once written, however, it gives implementation and testing a shared target.

## Why write requirements down?

Software is built incrementally, so it is fair to ask why a team should specify requirements before it knows every detail. Written requirements help the team decide what to build, plan tests, estimate work, and recognize when a release is ready. They also expose disagreements that otherwise appear late in implementation.

Mockups and prototypes express some requirements implicitly. They may show the steps in a task or the intended layout. They say little about properties that are hard to see. A mockup cannot tell you that the average page-load time must remain below one second, for example. An explicit statement can.

Requirements originate with people, organizations, laws, contracts, physical constraints, and earlier design decisions. A team may need to interview users, interpret policy with a lawyer, negotiate with a client, or test a prototype before it can state a requirement responsibly. Requirements engineering extends design work by identifying the properties the finished system must satisfy and the sources that justify them.

## Formality and its trade-offs

Some projects specify requirements formally. Formal methods can reveal contradictions or link a high-level requirement to the code and tests that implement it. That traceability is useful in systems where failure is costly.

Precision also takes time, and premature formalization can narrow a design before the team understands the problem. For this project, natural-language requirements are appropriate, but they still need careful review.

Aim for requirements that are:

- complete enough to cover the behaviour and constraints that matter;
- precise enough that two readers do not arrive at incompatible interpretations;
- consistent with one another; and
- verifiable through a test, inspection, analysis, or demonstration.

Here, “complete” means that the set contains what the team needs to judge whether the product meets its stated goals. It need not describe every implementation detail.

## Example: a to-do list

Consider these initial requirements for a small to-do list application:

- A user must be able to add a to-do item with one action.
- Each item must contain text and a completed state.
- A user must be able to edit an item's text.
- A user must be able to change an item's completed state.
- A user must be able to delete an item.
- Changes to an item must be saved without a separate save action.

The list is a useful start, but it needs scrutiny.

### Completeness

Is the list ordered? How long should items persist? Are there user accounts? Where is the data stored? Can a deletion be undone? The relevant questions depend on the product, but the team must look for omissions that would change its estimate or its definition of success.

### Precision

Where does a new item appear? How long may its text be? What exactly counts as one action? If the team leaves those questions open, programmers and testers may make different, equally plausible assumptions.

### Consistency

The six statements appear compatible, but new details may create a conflict. Suppose a new item is always added at the end of a long list, but the view does not scroll to it. Technically, one action added the item. From the user's perspective, nothing happened. The team must decide what “able to add” means and revise the related requirements together.

### Verifiability

The automatic-save requirement is difficult to guarantee under every failure. A full disk, lost connection, or hardware fault can prevent a save. A more useful requirement would state the conditions under which saving must succeed and what the application must tell the user when it cannot.

These weaknesses do not make the first draft useless. They show where the team needs another decision. Better requirements reduce ambiguity, make risks visible, and give implementation and testing a common checklist.

## Requirements must also be defensible

Completeness, precision, consistency, and verifiability are not enough. A requirement can satisfy all four and still be illegal, unethical, or unjust.

Historic redlining in the United States illustrates the danger. A lending system could encode a precise, easily tested rule that denies applicants from a particular racial group. Its technical clarity would not make the rule acceptable. Automating discrimination can instead conceal it behind an apparently neutral process and apply it at greater scale.

When reviewing your requirements, ask where each one came from, who benefits from it, and who could be harmed by it. If a requirement encodes an unjust assumption, making it more precise is not the solution. Remove or replace the assumption.

---
