---
layout: default
title: Project notes
description: Supporting software design and requirements notes for the CPEN 221A team project.
hero_title: Project Notes
term: Fall 2026
permalink: /notes/
---

<figure class="project-figure project-figure--wide">
  <img src="{{ '/assets/images/project-notes.jpeg' | relative_url }}" alt="An open notebook with handwritten annotations and diagrams resting on a desk.">
  <figcaption>The supporting notes collect the design and requirements material used across the project.</figcaption>
</figure>

# Software Design: From Observation to Values

## **1. What We Mean by “Design”**

Software design is more than implementation or syntax. It includes how a system **looks**, **works**, and **is structured**.

- **Visual design** – colors, layout, readability.
- **Interaction design** – how users engage with the system; what feels natural or frustrating.
- **Conceptual design** – how the internal structure aligns with the system’s purpose.

Good design begins not with *what we can build*, but with *what problem is worth solving*.

## **2. Finding Problems Worth Solving**

Before we start coding, we should **observe** how people actually work and identify where current tools fall short.

### **Key ideas**

- **Observe before you prescribe.**

    Watch what people do and how they adapt.

- **Workarounds are gold.**

    Improvised solutions reveal unmet needs.

- **Pay attention to “errors.”**

    Mistakes show where a user’s mental model and the system’s model diverge.

“You can observe a lot by just watching.” — Yogi Berra

## **3. From Observation to Interviews**

Observation reveals *what* people do; interviews reveal *why* they do it.

### **Interview flow**

1. **Intro / Background** – Build rapport. “Tell me about what you do here.”
2. **Evoke stories** – Ask for concrete examples. “Walk me through your day.”
3. **Explore emotions** – What frustrates or delights?
4. **Reflect** – Summarize and verify your understanding.
5. **Wrap up** – Invite anything missed.

### **Practical habits**

- Use **silence**; don’t fill pauses.
- Avoid **binary questions**.
- Ask for **stories**, not opinions or hypotheticals.
- Follow unexpected tangents—they often uncover deeper insights.
- Don’t suggest answers or over-guide the conversation.

## **4. Analyzing What You Hear**

After interviews, reflect rather than summarize.

Look for **contradictions, surprises, and tensions**.

Ask:

- What values or priorities are people expressing?
- Where are their goals misaligned with the technology’s assumptions?
- What boundaries—social, technical, or ethical—shape their decisions?

This reflection helps define a **point of view as a designer** and the **scope** of a meaningful project.

## **5. Beyond Empathy: Designing with Values**

Empathy and need finding are only the first step. Software systems affect not just direct users but entire communities.

We must design with **values** in mind—acknowledging long-term, indirect, and systemic impacts.

This approach is called **Value Sensitive Design (VSD)**.

[Value sensitive design - Wikipedia](https://en.wikipedia.org/wiki/Value_sensitive_design)

## **6. Value Sensitive Design: The Four Criteria**

VSD asks designers to think about:

### **(a) Stakeholders**

Who is affected—directly or indirectly?

- **Direct stakeholders** interact with the system.
- **Indirect stakeholders** are affected by its consequences.
- **Non-targeted stakeholders** may be drawn in unintentionally.

**Example:** *The Waze Effect* — navigation apps reroute cars through residential neighborhoods, benefiting drivers but harming residents who were never consulted.

### **(b) Time**

How do impacts evolve?

A technology’s meaning changes as novelty fades and integration deepens. Consider **long-term adaptation, obsolescence,** and **re-appropriation**.

### **(c) Pervasiveness**

What happens when adoption becomes widespread?

Design assumptions at small scale become social norms at large scale.

Example: predictive text systems make communication faster but also increase message volume and expectations of constant responsiveness.

### **(d) Values**

What matters most to those affected?

Values include autonomy, dignity, fairness, sustainability, and community.

Design decisions amplify some and suppress others. We must identify the trade-offs we are willing to make.

## **7. Re-appropriation and Non-Use**

Users often repurpose systems beyond their original design—turning spreadsheets into art or browsers into operating environments. This **re-appropriation** shows flexibility and creativity.

Equally important is **choosing not to use** technology.

Non-use (for example, opting out of facial recognition) is a deliberate design response that must be supported rather than punished.

## **8. Software Is Not Neutral**

Every line of code reflects priorities.

Default settings, optimization criteria, and even naming choices encode a worldview.

When software scales, those values scale with it—and eventually shape user behavior and social norms.

Designing responsibly means asking:

- *Who benefits?*
- *Who bears the cost?*
- *Which values are we embedding?*

## **9. Why This Matters in CPEN 221**

In this course, software design is not abstract—it shapes how we write code and how others build on it.

When you design a **class**, **API**, or **protocol**, you are:

- Defining **who can use it** and **how**.
- Deciding **what’s easy** and **what’s hard**.
- Encoding **assumptions and priorities** that persist over time.

As engineers, we must design for clarity, sustainability, and fairness—not just correctness.

### **Summary Thought**

Software systems don’t just reflect society—they reshape it.

The engineer’s task is not only to make systems **functionally correct**, but to make them **socially and ethically coherent**.


# Designing Responsibly: From Divergence to Social Impact

## **1. Two Modes of Design Thinking: Diverge and Converge**

Design is both **creative exploration** and **structured reasoning**.

In engineering practice, we move repeatedly between **divergent** and **convergent** modes.

| **Divergent Thinking**            | **Convergent Thinking**                 |
| --------------------------------- | --------------------------------------- |
| Generate ideas freely             | Synthesize and unify ideas              |
| Expand the space of possibilities | Reduce complexity and resolve conflicts |
| Ignore barriers                   | Identify trade-offs and constraints     |
| Goal: breadth and discovery       | Goal: coherence and clarity             |

We start by generating many ideas, even implausible ones, and then narrow toward designs that are coherent, viable, and aligned with real needs .

---

## **2. Techniques for Divergent Design**

Divergent design involves deliberately breaking habitual patterns.

### **Brainstorming**

- Work collaboratively and build on others’ suggestions (“yes, and…”).
- Aim for *quantity* before *quality*.
- Include wild or “bad” ideas—sometimes they spark the best solutions.

### **Lateral Thinking**

- Challenge assumptions (“What if the opposite were true?”).
- Take a flawed idea and push it to extremes.
- Examine neglected parts of a system.

### **Foraging for Inspiration**

- Browse books, online forums, and physical spaces.
- Pay attention to unusual artifacts, errors, or user improvisations.

A design problem often hides in what people are already *hacking around*.

---

## **3. From Features to Concepts**

After brainstorming, we **converge** on higher-level **concepts**—abstract building blocks that encapsulate purpose and behavior.

### **What Is a Concept?**

A *concept* is not a UI element or data structure; it’s a **semantically meaningful unit** of functionality.

A good concept is:

- **Purposive** — fulfills a user need.
- **Semantic** — user-facing, not an implementation detail.
- **Modular** — independent and reusable.

Examples: Post, Comment, Upvote, Favorite, User, Session.

Each expresses *what* is accomplished, not *how* it’s coded .

By converging on concepts, we move from scattered features to a **coherent model of the system**.

---

## **4. Dependency Diagrams and Independence**

Concepts interact, but they should remain as **independent** as possible.

Dependencies should be *extrinsic* (arising from context) rather than *intrinsic* (hard-coded inside components).

### **Example**

If Post internally references Comment, any app using Post must also include Comment.

That’s an **intrinsic dependency**—it reduces reusability.

The goal is to define concepts that can stand alone, with dependencies made explicit in **dependency diagrams** that describe inclusion relationships rather than hidden couplings.

This approach traces back to **David Parnas’s** principle of *information hiding*—a timeless idea in software design.

---

## **5. Integrating Values into Divergence and Convergence**

Values—accessibility, privacy, dignity, community—aren’t afterthoughts.

During divergence, they inspire *new directions* (“What would this look like if we designed for children or non-users?”).

During convergence, they *constrain and guide* the final structure (“How do we preserve autonomy and fairness?”).

Good design balances creativity with conscience.

---

## **6. Responsible Innovation: Doing No Harm, Creating Good**

Technology shapes society. As engineers, we have **agency** in how that happens.

**Responsible innovation** combines two commitments:

1. **Do no harm** — avoid enabling bias, exploitation, inequity, or environmental harm.
2. **Create positive impact** — advance human rights, fairness, and sustainability .

We must question both the *intended* and *unintended* consequences of what we build.

“I lay awake at night thinking about what we could have done to avoid the product being used this way.”

— Early Facebook engineer

Being a responsible technologist means anticipating ripple effects and designing systems that protect—not erode—public trust.

---

## **7. The Case for Responsible Tech**

Responsible innovation isn’t only ethical—it’s pragmatic.

### **Why It Matters**

- **Attracts talent.** Engineers increasingly want to work for organizations that align with their values.
- **Builds loyalty.** Users trust companies that are transparent and socially aware.
- **Prevents disasters.** Addressing ethical risks early saves reputations and resources .

### **Common Excuses to Challenge**

- “We’re too small to worry about that.”
- “We don’t have enough data to know.”
- “This doesn’t apply to us.”

Responsible design is not a luxury—it’s a discipline.

---

## **8. Frameworks and Role Models**

Practical frameworks help you incorporate social and ethical reflection:

- **Ethical OS** – scenario planning for unintended consequences.
- **Consequence Scanning** – mapping second-order effects.
- **Society-Centered Design** – designing for collective well-being.
- **B Corp / Responsible Innovation Labs** – institutional accountability.

Scholars and practitioners to follow: Safiya Noble, Ruha Benjamin, Joy Buolamwini, Rumman Chowdhury, Kathy Pham, and others who connect technology to justice and inclusion .

---

## **9. Social Innovation: Framing Meaningful Problems**

Engineering for impact means tackling **meaningful, not just technical, problems**.

Social innovation addresses issues that limit **dignity, agency, inclusivity, and justice** .

### **The Social Impact Equation**

Social Impact ≈ ( Essentialness of Service ) × ( Vulnerability of Target Population ) × ( Scale of Effect )

Problems in this space are **wicked problems**—complex, interconnected, and resistant to simple solutions.

They often exist in **complex systems**, where variables are numerous and interactions unpredictable.

Our tools must therefore evolve: iterative learning, stakeholder research, and humility.

---

## **10. The Impact Case Framework**

To ground social design in evidence, use an **Impact Case**—a concise, testable articulation of your logic.

### **Template**

1. The problem of *X* is important because _____.
2. Our solution to address this problem is *Y*.
3. We believe *Y* is a good solution because _____.
4. We will measure *N* to prove that *Y* effectively addresses *X*.

The Impact Case forces you to align purpose, evidence, and measurement.

It’s as relevant to software tools as to social ventures—because all systems have impact.

---

## **11. Mapping Your Ecosystem**

To understand a problem, map its **stakeholders** and **structures**.

Steps:

1. Identify ≈ 5 stakeholder groups (users, communities, policymakers, etc.).
2. Choose 2–3 notable actors in each group.
3. Ask: What are their motivations, strengths, blind spots, and needs?
4. Analyze: What does this space need? What are structural gaps? Where can you add value?

This exercise connects need finding, systems thinking, and ethical reflection—core habits for responsible software engineers.

---

## **12. Takeaways**

- **Diverge boldly**, **converge thoughtfully**.
- **Ground your designs in values**—they shape not only code but culture.
- **Use frameworks like Impact Case and ecosystem mapping** to test your assumptions.
- **Remember:** good intentions aren’t enough; good processes are.

*Solve important problems.*

*Good intentions aren’t enough.*

*Impact requires evidence and empathy.*


# Software Requirements

Once you have a problem, a solution, and a design specification, it's entirely reasonable to start thinking about code. What libraries should we use? What platform is best? Who will build what? After all, there's no better way to test the feasibility of an idea than to build it, deploy it, and find out if it works. Right?

It depends. This mentality towards product design works fine if building and deploying something is cheap and getting feedback has no consequences. Simple consumer applications often benefit from this simplicity, especially early stage ones, because there's little to lose. For example, if you are starting a company, and do not even know if there is a market opportuniity yet, it may be worth quickly prototyping an idea, seeing if there's interest, and then later thinking about how to carefully architect a product that meets that opportunity. This is [how products such as Facebook started](https://en.wikipedia.org/wiki/History_of_Facebook), with a poorly implemented prototype that revealed an opportunity, which was only later translated into a functional, reliable software service.

However, what if prototyping a beta *isn't* cheap to build? What if your product only has one shot at adoption? What if you're building something for a client and they want to define success? Worse yet, what if your product could *kill* people if it's not built properly? Consider the U.S. [HealthCare.gov](http://HealthCare.gov) [launch](https://en.wikipedia.org/wiki/HealthCare.gov), for example, which was lambasted for its countless defects and poor scalability at launch, only working for 1,100 simultaneous users, when 50,000 were exected and 250,000 actually arrived. To prevent disastrous launches like this, software teams have to be more careful about translating a design specification into a specific explicit set of goals that must be satisfied in order for the implementation to be complete. We call these goals *requirements* and we call this process of *requirements engineering*.

In principle, requirements are a relatively simple concept. They are simply statements of what must be true about a system to make the system acceptable. For example, suppose you were designing an interactive mobile game. You might want to write the requirement *The frame rate must never drop below 60 frames per second.* This could be important for any number of reasons: the game may rely on interactive speeds, your company's reputation may be for high fidelity graphics, or perhaps that high frame rate is key to creating a sense of realism. Or, imagine your game company has a reputation for high performance, high fidelity graphics, high frame rate graphics, and achieving any less would erode your company's brand. Whatever the reasons, expressing it as a requirement makes it explicit that any version of the software that doesn't meet that requirement is unacceptable, and sets a clear goal for engineering to meet.

The general idea of writing down requirements is actually a controversial one. Why not just discover what a system needs to do incrementally, through testing, user feedback, and other methods? Some of the original arguments for writing down requirements actually acknowledged that software is necessarily built incrementally, but that it is nevertheless useful to write down requirements from the outset. This is because requirements help you plan everything: what you have to build, what you have to test, and how to know when you're done. The theory is that by defining requirements explicitly, you plan, and by planning, you save time.

Do you really have to plan by *writing down* requirements? For example, why not do what designers do, expressing requirements in the form of prototypes and mockups. These *implicitly* state requirements, because they suggest what the software is supposed to do without saying it directly. But for some types of requirements, they actually imply nothing. For example, how responsive should a web page be to be? A prototype doesn't really say; an explicit requirement of *an average page load time of less than 1 second* is quite explicit. Requirements can therefore be thought of more like an architect's blueprint: they provide explicit definitions and scaffolding of project success.

And yet, like design, requirements come from the world and the people in it and not from software. Because they come from the world, requirements are rarely objective or unambiguous. For example, some requirements come from law, such as the European Union's [General Data Protection Regulation](https://eugdpr.org/) regulation, which specifies a set of data privacy requirements that all software systems used by EU citizens must meet. Other requirements might come from public pressure for change, as in Twitter's decision to label particular tweets as having false information or hate speech. Therefore, the methods that people use to do requirements engineering are quite diverse. Requirements engineers may work with lawyers to interpret policy. They might work with regulators to negotiate requirements. They might also use design methods, such as user research methods and rapid prototyping to iteratively converge toward requirements. Therefore, the big difference between design and requirements engineering is that requirements engineers take the process one step further than designers, enumerating *in detail* every property that the software must satisfy, and engaging with every source of requirements a system might need to meet, not just user needs.

There are some approaches to specifying requirements *formally*. These techniques allow requirements engineers to automatically identify *conflicting* requirements, so they don't end up proposing a design that can't possibly exist. Some even use systems to make requirements *traceable*, meaning the high level requirement can be linked directly to the code that meets that requirement. All of this formality has tradeoffs: not only does it take more time to be so precise, but it can negatively effect creativity in concept generation as well.

Expressing requirements in natural language can mitigate these effects, at the expense of precision. They just have to be *complete*, *precise*, *non-conflicting*, and *verifiable*. For example, consider a design for a simple to do list application. Its requirements might be something like the following:

- Users must be able to add to-do list items with a single action.
- To-do list items must contain text and a binary completed state.
- Users must be able to edit the text of to-do list items.
- Users must be able to toggle the completed state of to-do list items.
- Users must be able to delete to-do list items.
- All changes made to the state of to-do list items must be saved automatically without user intervention.

Let's review these requirements against the criteria for good requirements that I listed above:

- Is it *complete*? I can think of a few more requirements: is the list ordered? How long does state persist? Are there user accounts? Where is data stored? What does it look like? What kinds of user actions must be supported? Is delete undoable? Even just on these completeness dimension, you can see how even a very simple application can become quite complex. When you're generating requirements, your job is to make sure you haven't forgotten important requirements.
- Is the list *precise*? Not really. When you add a to do list item, is it added at the beginning? The end? Wherever a user request it be added? How long can the to do list item text be? Clearly the requirement above is imprecise. And imprecise requirements lead to imprecise goals, which means that engineers might not meet them. Is this to do list team okay with not meeting its goals?
- Are the requirements *non-conflicting*? I *think* they are since they all seem to be satisfiable together. But some of the missing requirements might conflict. For example, suppose we clarified the imprecise requirement about where a to do list item is added. If the requirement was that it was added to the end, is there also a requirement that the window scroll to make the newly added to do item visible? If not, would the first requirement of making it possible for users to add an item with a single action be achieveable? They could add it, but they wouldn't know they had added it because of this usability problem, so is this requirement met? This example shows that reasoning through requirements is ultimately about interpreting words, finding source of ambiguity, and trying to eliminate them with more words.
- Finally, are they *verifiable*? Some more than others. For example, is there a way to guarantee that the state saves successfully all the time? That may be difficult to prove given the vast number of ways the operating environment might prevent saving, such as a failing hard drive or an interrupted internet connection. This requirement might need to be revised to allow for failures to save, which itself might have implications for other requirements in the list.

Now, the flaws above don't make the requirements "wrong". They just make them "less good." The more complete, precise, non-conflicting, and testable your requirements are, the easier it is to anticipate risk, estimate work, and evaluate progress, since requirements essentially give you a to do list for implementation and testing.

Lastly, remember that requirements are translated from a design, and designs have many more qualities than just completeness, preciseness, feasibility, and verifiability. Designs must also be legal, ethical, and just. Consider, for example, the anti-Black redlining practices pervasive throughout the United States. Even through the 1980's, it was standard practice for banks to lend to lower-income white residents, but not Black residents, even middle-income or upper-income ones. Banks in the 1980's wrote software to automate many lending decisions; would a software requirement such as this have been legal, ethical, or just?

No loan application with an applicant self-identified as a person of color should be approved.

That requirement is both precise and verifiable. In the 1980s, it was legal. But was it ethical or just? Absolutely not. Therefore, requirements, no matter how formally extracted from a design specification, no matter how consistent with law, and no matter how aligned with an organization's priorities, should be free of racist ideas. Requirements are just one of many ways that such ideas are manifested, and ultimately hidden in code.

---
