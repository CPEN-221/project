---
layout: default
title: Team project
description: Project stages, submission milestones, and supporting design notes for CPEN 221A.
term: Fall 2026
permalink: /
---

# Overview

Students should define a project and work on it over ~7 weeks (Oct 20 - December 5).

Projects should be chosen to be relevant to UBC campus life (to assist students, staff, faculty, community members, ...).

Team work is important.

The scope of the project should reflect group size and be equivalent of 1 credit of work. In other words, each student should expect to spend ~3 hours a week on the project. This would be ~15 person hours of work each week and ~105 person hours of work over the entire term.

Each project should involve:

- some user interaction;
- preferably a data set that can be read from a file or set of files;
- client-server pattern (some communication between two or more machines);
- use at least one external library - beyond the standard Java libraries.

Each group should:

- follow the project development process;
- track milestones using github (e.g., github issues);
- use git branching and merging;
- apply good testing practices;
- support easy building/compilation of the project.

Project complexity and algorithmic sophistication is not required for an A but may be required for an A+. 

> **We will emphasize process for the project, with multiple stages. If we think a project has too little or too much work then we will let you know. The milestones underscore the preliminary design over the final implementation.**

For the project, you do not need to use Java — you can use Rust, Go, TypeScript, C++, maybe even Python — but your work should integrate the core concepts covered in the course: specifications, testing, abstract data types and concurrency. 

> You can freely use Generative AI with suitable documentation of your prompts and mechanisms for verifying correctness. You should consider the environmental costs of using Generative AI when you use these tools. The timeline for this project assumes that each team will make some careful use of Generative AI tools.

[Explained: Generative AI’s environmental impact](https://news.mit.edu/2025/explained-generative-ai-environmental-impact-0117)

---

# Design your Team

The first step of any software project is defining *why* the project is happening at all:

- What problem is it solving?
- Who's coming together to solve it?
- Do they have the skills to solve it?

In this phase, you're going to answer these questions, designing your team intentionally.

> Throughout, remember that teams are effective because they 1) trust each other and 2) want to work together. Trusting relationships are necessary for collaboration: they provide the *psychological safety* [(](https://canvas.uw.edu/courses/1399096/assignments/5585523#edmondson)[Edmondson, 1999](https://journals.sagepub.com/doi/abs/10.2307/2666999)[)](https://canvas.uw.edu/courses/1399096/assignments/5585523#edmondson) necessary for risk taking, feedback, and open communication.

## Step 1: Understand your roles

This is a critical step, as it ensures at least one person is responsible for every important function of a team. 

- Who is your **project manager** (PM)? In this class, a great PM:
    - Inspires the team with their vision of how everyone should work together.
    - Offers strategic advice to any team member who must choose between several different ways to get their job done.
    - Motivates the team to stay on task and complete the project.
    - Maintains a positive working environment and actively constructs their team's culture.
    - Promotes fair play among team members and recognizes their individuality.
    - Is humble, and recognizes and accepts that their team members may have more expertise on a particular topic than they have.
    - Monitors work assignments and day-to-day scheduling.
    - Finds the team members the resources they need to complete their tasks (e.g. a time and place to work, meeting coordination, computing power, disk space, expert consultants).
    - Evaluates how the team works together and improves their process to make the team more efficient and effective.
    - Lets their team members work autonomously, without micromanaging them.
    - Facilitates communication between team members and with external parties
- Who is your **designer**? In this class, a great designer:
    - Deepens the team's understanding of the problem the team is addressing
    - Envisions the design
    - Prototypes the design
    - Specifies the requirements of the design
    - Ensures that the implementation of the design meets the specifications
    - Tests the design to ensure that it meets the needs of who it was designed to help
    - Tests the usability of the design to make sure that it is learnable and prevents errors
    - Creates and curates visual content such as icons, images, fonts, and colors
    - Manages the style guidelines for the implementation and ensures compliance toward them
- Who are your **developers**? In this class, developers:
    - Verifies that the design can be implemented
    - Verifies that requirements are achievable
    - Implements the design to ensure requirements are met
    - Verifies that the implementation meets requirements
    - Triages issues
    - Resolves issues
    - Ensures a stable deployment

The person in each role should be someone who has the skills for the role *or* is eager to learn the skills for the role.

The roles are not exclusive, and individuals in each role are expected to support others in different roles. However, each team is required to designate a primary individual for each of the three roles.

The PM should start immediately, facilitating all remaining steps.

## Step 2: Choose your team's mission and name

**PM leads**

Now that you know each other and your roles, your organization needs a reason for being:

- What is its overarching goal and its overarching values?
- Are you trying to make the world a safer place? A healthier place? Get a high grade in this class? Dismantle racist structures?

The designer and PM should lead this conversation, helping the team identify a larger purpose that will focus everyone's work in the same direction and help resolve disagreements about how to spend your time, because every bit of work will serve different goals.

One way to distill this reason for being is by writing a **mission statement.** You can see several examples of mission statements on [this blog post](https://blog.hubspot.com/marketing/inspiring-company-mission-statements). For example, imagine I started a company that was committed to ensuring that the internet was a platform that eradicated racism, rather than amplifying it. I might write a mission statement like this:

*Advancing an anti-racist internet.*

Once you've chosen a mission, **choose a team name** that captures your teams’s purpose.

Once you've chosen a name, have your designer choose a logo to represent your organization. (Consider just choosing a Creative Commons logo from the [Noun Project](https://thenounproject.com/), rather than designing something yourself). You'll use this logo in your GitHub organization later.

Create a GitHub repository for your project.

## Step 3: Select and describe a design problem

**DESIGNER leads**

Your team's designer should lead a conversation about: **what problem do they want to solve** within the company's mission. Remember that **problems are *not* solutions**—they are a narrative about some way the world functions that has unwanted consequences. For example, climate change is a problem, solar energy is a solution; diabetes is a problem, chronic disease management in primary health care is a solution. Solutions are what you make to change the causality of a problem so that its consequences no longer occur.

Discuss, debate, and deliberate outside of class to arrive at a problem you're all excited about solving this quarter.

Because we'll have limited time in this class to build and deploy a software solution, here are a few constraints on the problem you choose:

- It could be a **small problem**, not requiring a massive, complex solution. (Your team may be more ambitious but be careful.)
- It does **not** have to be completely novel. It can be an extension to, or adaptation of, an existing software solution.

To represent your problem, your designer should **write a description of your problem**, which details the scope of the problem, its consequences in the world, the things that cause the problem, and why existing solutions don't resolve the problem (if you choose a solution that already exists, just explain the problem it solves as if the solution doesn't exist). Convince your reader that your organization has a reason for being.

Note, as state above, your problem should **not** refer to a solution; "a solution that does X does not exist" is not a statement of a problem. That's like motivating the need for Instagram by saying "The world is broken because it doesn't have Instagram." The problem motivating instagram would be something like, "People love sharing photos, but all existing solutions for sharing them involve clumsy, impersonal file sharing."

Continuing the anti-racism example from above, a good problem statement might be something like:

> *The internet and the social media platforms are often used as platforms to advance racist causes and racist hate speech. For example, Facebook's most widely shared content are regularly the perspectives of racist commentators, and Twitter is often a place where Black Americans are harassed and bullied by white supremacists. Some social media platforms offer modest ways of mitigating the harm of racist speech, such as blocking people on Twitter or muting particular news sources, but these designs do little to eradicate racism itself. Within the constraint's of the United State's first Amendment, how the internet become a place that not only prevents the spread of racist ideas, but also helps the people that believe those ideas overcome their racist bias?*

That's it. No solution, just a problem.

**Store your final draft of the problem in your GitHub repository's README file.**

> While you are free to choose your own problem and solution, your software app must nevertheless be *authentic*.

> An authentic app is one that is designed to respond to a genuine problem and that offers a novel and effective solution to it—or at least contributes ideas towards such a solution.

> To be genuine, a problem need not be widely recognized or even to have been formulated explicitly by others. It should however be sufficiently compelling, when presented, that others agree that it is a problem worth solving. It must also be well focused enough that it is possible to assess whether or not purported solutions actually solve the problem.

# Design Your Solution

Having articulated the problem, it is now time to envision a solution.

### Constraints

- **Your design should adequately address your problem**. It doesn't have to be a *perfect* solution to a *big* problem; a meaningful, *incremental* solution to a *small* problem is just fine. The focus of this class is on engineering, not design.
- **Your design must be interactive**. It cannot be static content; it must accept and respond to some form of user input.
- **Your design should be something your team can implement in *4 weeks* of part-time effort**. Your solution should be a [minimally viable product](https://en.wikipedia.org/wiki/Minimum_viable_product), which provides value to your target audience, but doesn't necessarily achieve all possible functionality. That means real functionality and real content (if appropriate), but not *all* the functionality you can imagine or *all* of the content you can imagine. Think of YouTube, but just video playing, basic video uploading, like and dislike buttons, and ten of the best cat videos you've ever seen. That's enough to provide the smallest possible value that YouTube can provide (and probably pretty close to what they initially launched).
- **You should be able to build your solution using free components and services**. Don't spend your own money. You can if you want, but you're not required to, and if you do, be sensitive to your teammates' concerns about this.
- **What you build doesn't have to be a graphical user interface.** If you want to build something command line based or even an API, that's okay too. You still need to specify how someone interacts with your design, detailing the commands or APIs that you want to build and explaining in natural language what their behavior is.

### Describe your Design

**DESIGNERS lead**

We recommend opening a [Miro.](http://miro.com/) board, sharing your screen, and sketching while you and your teammate's brainstorm.

Your job is to write a brief **design specification** that details the **interaction design** for your solution. A design specification details **what** the software will do in terms of functionality, but not **how**. Your specification is good if someone could read it and understand the user experience of your application and rationale for your design choices. Everything else about how it might be implemented is work for later.

Your specification should have the following sections:

- **Problem**. A good problem description is a logical, substantiated argument that proves the existence of a problem. Your problem description should cite evidence from your user research, as well as any scholarly literature you can find about the problem. This doesn't need to be long; a few paragraphs is usually enough to clearly define the problem you are solving.
- **Solution**. This section must detail every design decision necessary for engineering your solution, including every screen, every error, every algorithmic functionality, and every detail about the textual and visual content of your design (aside from content created by users). If your solution is software, a software engineer should be able to read your specification and build your solution without asking you any questions. Embed mockups of screens throughout the text of this section to visually specify your design. Because of the short timeline, it's okay if these are hand-sketched.

> Note that you only have **one week** to do this. That means that your design really can't be that complicated from an interactive perspective. Keep your solution simple. Our focus in this class will be on something that is architected well, defect-free, and shipping, not something that is multifaceted and powerful.

To write a clear design specification, you need to iteratively evaluate how well the specification specifies its interactive details.

**PMs**: Store your specification in a **GitHub Markdown** document in your GitHub repository. You're welcome to collaborate on drafts of it in a different medium, such as Google Docs, as long as it eventually appears in GitHub, and is submitted as a public link.

### Example Specification

Below is a *very* simple example specification that conveys the structure that I'm looking for, but not the level detail. (I expect your solutions to be more complex and include more detail about every possible state the user might enter). Sketched mockups are acceptable.

#### Problem

Many children in the world still memorize multiplication tables for numbers 0-10. This memorization helps them thrive in a world where small multiples are abundant in everyday tasks. However, paper-based forms of memorization are slow to grade, slow to practice, and thus often quite boring. This takes valuable class time away from elementary school students, while also creating the impression that arithmetic is slow and boring.

#### Solution

We envision a multiplication table game in which players receive a series of 1-digit multiplication problems, including digits 0 through 10 (0 x 0 through 10 x 10). Each successive problem is based on past correct and incorrect answers. When a player correctly answers all possible pairings of digits three times in a row, the player wins. Otherwise, the game continues to present problems that they have yet to answer three times correctly successively.

The interface is simple. There is one main screen for solving multiplication problems:

<figure class="project-figure project-figure--compact">
  <img src="{{ '/assets/images/arithmetic-question.jpeg' | relative_url }}" alt="A hand-drawn multiplication game screen showing seven times four above a numeric keypad.">
  <figcaption>The game's question screen accepts a numeric answer from an on-screen keypad.</figcaption>
</figure>

Players tap the digits to enter a number up to three digits long. They can tap the backspace key to delete a number, all the way back to an empty answer. They can tap the checkmark to enter the number. When backspace is pressed on an empty number, nothing happens. When three digits have been entered, the keypad buttons become disabled by turning gray.

When a player submits a number by tapping the checkmark, the game shows a correct or incorrect screen for 2 seconds before displaying the next problem:

<figure class="project-figure project-figure--compact">
  <img src="{{ '/assets/images/arithmetic-feedback.jpeg' | relative_url }}" alt="Two hand-drawn multiplication game screens showing an incorrect answer with a red X and a correct answer with a green check mark.">
  <figcaption>The feedback screen shows the outcome for two seconds before presenting the next question.</figcaption>
</figure>


After the answer screen , the game selects a new problem by finding a random pairing of digits 0-10 that the player has not yet successively answered 3 times correctly. The order of the digits *does* matter (7 x 3 is different from 3 x 7).

Once the player has won the game, they see the game over screen, which also provides the option of resetting the play history to start the game over:

<figure class="project-figure project-figure--compact">
  <img src="{{ '/assets/images/arithmetic-game-over.jpeg' | relative_url }}" alt="A hand-drawn game completion screen that says You have mastered multiplication and includes a reset button.">
  <figcaption>The completion screen lets the player reset their play history.</figcaption>
</figure>

The game contains no sound, no keyboard support. The game's interface layout is responsive to screen size, but uses the same interface layout for all platforms.

# Requirements

### Translating designs into requirements

You should, by the start of this activity in the project, have a detailed specification of your design, covering every interaction (and likely many of the visual aspects) of your solution to the problem you selected. Your next task is to **translate** your design into a set of unambiguous [requirements](#requirements), each expressed in natural language.

> Writing down requirements is useful for at least three reasons:

- The very act of articulating them will help you notice ambiguous or unstated assumptions about your design.
- Your list of requirements can act as an implementation to-do list.
- Your list of requirements will directly inform your testing plan.
- Your list of requirements will be the basis for a grade later, which is assessed on the proportion of requirements that you've met. (Though this activity isn't about creating the final list you'll be held to; this is just a first draft. You'll have a chance to revise them before you begin your final sprint).

Each requirement should be a **single, precise, verifiable fact** that must be true about your implementation. Here's an example from our arithmetic practice example that violates all of these principles:

*The system should count up all the answers and display them.*

The statement above includes two requirements (counting and displaying), it's vague about what it means by "counting the answers" and "displaying" them, and because it's vague, it's not verifiable. Here's a better version of the counting requirement:

*The system should compute the proportion of correct answers as the total number of correctly answered questions divided by the total number of questions asked.*

That requirement is singular, precise, and verifiable.

Each of your projects has a different number of requirements, so I can't say how long your list needs to be. If I had to guess, I'd say you'll have anywhere from dozens to hundreds. Sound daunting? Here's your motivation: another way to think about requirements is as a complete **to-do list** for your implementation and testing work. The more *complete*, *precise*, *non-conflicting*, and *verifiable* your requirements, the easier it will be to get started, plan your effort, and ensure you can get the work done on time. All of those things are necessary for great engineering (and for a good grade in this class).

Create a **requirements document** in your GitHub repository, written in GitHub markdown. To make the requirements easier to navigate and understand, organize your requirements into sections, grouping sets of related requirements. Each section should be linked to a part of your design specification, when appropriate, so it's easier to understand what the requirements concerned. Each requirement should be ***precise***, ***verifiable***, and ***non-conflicting***. The set of requirements overall should be ***complete*** with respect to your design specification.

To translate your design into requirements, review your design specification. Go through each part of it, identifying places where your specification states that something must be possible and convert all of those into requirements. You may also find that your design specification *doesn't* state that something is required, but you know it is required. Write these down as requirements as well.

# Architecture

You should have detailed **what** your software is going to do from a design perspective. All of those choices you made are about the problem you are solving with the software; those details concern the world. In this phase, you're going to specify **how** you're going to achieve those requirements, defining your software's architecture.

Unlike in building architecture, where there are standards for blueprints, there is no agreed upon way to specify software architectures. There are highly formal tools which precisely detail the components and connectors of a system so that code can even be automatically generated from these architectural specifications ([Shaw et al. 1995](https://ieeexplore.ieee.org/document/385970)). Some architectural specifications are just vague sketched diagrams on a whiteboard ([Cherubini et al. 2007](https://dl.acm.org/doi/10.1145/1240624.1240714)).

To simplify this, we're going to use the architectural concepts relevant to the Model-View-Controller and Client-Server architectures ubiquitous on the web:

- [Client-Server architectures](https://en.wikipedia.org/wiki/Client%E2%80%93server_model) involve two kinds of components—**clients and servers**—exchanging messages with each other.
- [Model-View-Controller architectures](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) involve a **model** to persist and retrieve data, **views** to display data and elicit it from users, and a **controller** to implement the application's logic for passing data back and forth between the model and views, as well as manipulating data.
- In web applications, models, views, and controllers can live on either the client, the server, or both. For example, when you use a **database**, the model is on the server side. But your application might only store data on the client side if it only needs to persist data on the device accessing the site. It might also persist all data on the server, but then send all of the data on the client, so there are actually models on both the client and the server.

Your job, in this phase, is to decide how you're going to organize your clients, servers, models, views, and controllers. To do this, you're going to create two things.

### Description of All Components

First, write a Markdown file in your GitHub repository that specifies **all of the models, controllers, and views in your application**. For each, describe:

1. What the component's **responsibility** is
2. Whether the component resides on the client, the server, or both
3. What other components the component needs to communicate with and precisely what they will communicate.

Here's an example of a description of a **model** component for our arithmetic game example:

> **LearningModel**

    - This component is a model that stores all of the questions the game has asked the player and all of the answers the player has given to the game.
    - The model resides only on the client.
    - Only the **GameController** communicates with the model. It communicates the following:
        - The **GameController** can ask the **LearningModel** to store a question/answer pair
        - The **GameController** can ask the **LearningModel** for the proportion of correct answers
        - The **GameController** can ask the **LearningModel** for all of the stored question/answer pairs.

The architecture of the game would therefore also contain descriptions of the GameController, but also several views components that implement the user interface of the game, such as the view that displays the question, the view that displays the answer, the start screen view, etc.

How many components should you have? There is no right number, but consider a few extremes. If you only had one monolithic component, where there was no encapsulation between any of the data and functionality, you'd have a big "ball of mud" architecture that's going to be hard to understand, and therefore hard to evolve and repair. If you had a thousand little components for every tiny bit of functionality, most of your code would be communicating between components. You want something in the middle, where there's enough division of responsibilities that everyone on your team can understand how the functionality is organized, but not so many that you're writing a lot of extra code just to make things talk to each other.

**Note that you don't have to specify components you aren't building.** For example, if you choose to use something like MongoDB, you don't need to specify MongoDB. But some of your components may need to mention that they're going to communicate with cloud storage to store and retrieve data. Additionally, you'll likely have a client-side model of data in the cloud storage, so your client side components can access the data.

### Stubs For All Components

Once you have all of your components described, create **stubs** to represent all of these components and their functionality as source files. A stub is a *partial implementation* of something in source code, intended to help you architect the larger pieces of an implementation without fully implementing them. For example, here is a stub of a function that takes an age in years and returns an array of strings describing civil rights movements that someone likely experienced in their life:

```java
public List<String> getCivilRightsExperiences(age) {
  // TODO Replace with actual algorithm  
  return Arrays.asList("Voting rights act of 1965");
}
```

Notice how the stub specifies the inputs and outputs, but nothing about how they're computed? It's just a stand-in for functionality you'll eventually write.

None of these components need to have functionality, but they do have to have names, source files, and  all of the function headers, with arguments, return values, preconditions, and postconditions, to specify the specifies the requests that the component can receive from other components. For example, the **LearningModel** model above should have functions defined for the three functions the **GameController** can call on the **MasteryModel**.

Commit all of your stubs to your GitHub repository.

### Approach

While you're producing a document, the real goal of architecture is to make sure everyone on your team has a consistent, detailed understanding of the architecture. If they don't, you'll end up with a ball of mud. To test this, quiz each other on the architecture you have planned: can each of you explain it in detail? If not, keep explaining it to each other until you have the same understanding in your heads and in your document.

# Plan

Now that you've translated your design into requirements, and your requirements into an architecture, it's time to **plan** how you're going to work together to build your application.

## Developing Your Project Plan

**PM's**, lead the authoring of a GitHub page that answers the following questions:

1. **How will you coordinate your work?**
    - Who will coordinate the work?
    - What will their project management practices be?
    - Will you have meetings? How frequently? Who plans their agendas?
2. **What tools will you use to communicate?**
    - For each, articulate the alternatives and why that is the best choice.
3. **Who will own component in your architecture?**
    - Owning them means being responsible for writing them and making sure they are functional and correct.
    - For each component, list the one person who is in charge of getting it done.
4. **What is your timeline?**
    - Include a list of milestones you'll reach and deadlines for each.
5. **How will you verify that you've met your requirements?**
    - For each requirement in your requirements document, detail *how* you will verify it, and if you won't verify it, justify why you won't. This is called an **[acceptance testing plan](https://en.wikipedia.org/wiki/Acceptance_testing)**.
        - If you propose to write a tests, what exact tests will you conduct and what will count as each test passing?
        - If you propose to conduct reviews or inspections, how will you analyze the code?
        - If you write a proof, what property will you prove?
        - If you conduct a review or inspection, what aspects of the code will you inspect to verify the requirement is met?
    - For all of the requirements, how will your verifications be integrated into your process? Will you run automated tests after every build? Before every commit? When will you conduct inspections and who will be involved?

For each answer you provide, **provide a written justification** that explains the rationale behind your decisions, given what you know about what you need to build. I want to incentivize you to think deeply about each of these choices, to make sure your process decision actually makes sense.

To make a *good* plan, brainstorm disasters that might happen and test your plan against them. Illness, injury, API limitations, difficult to fix bugs: how resilient is your plan to all of these crises?

## Approach

**Developers lead**

> Items 1-3 above should be relatively straightforward. Devising a set of milestones and indicating a clear verification plan, however, is more difficult. A significant component is your approach to testing. Describe your testing plan in reasonable detail. From an implementation perspective, you may not have the time to build out all the features that you listed and you should prioritize your design effort with a focus on building a minimum viable product. How you prioritize features and integrate this prioritization into your plan matters.

# Release

In about four weeks, you're going to launch your 1.0 product. Excited? Daunted? We hope both! If you've done a good job preparing for your implementation phase, there are several things that should make your process smooth and uneventful:

- You should know what components you need to build and who is building them.
- You should know how you're going to verify that your product meets its requirements.
- You should know how you're going to coordinate and communicate over the next few weeks.
- You should know what technologies, APIs, platforms, and languages you're going to use.
- You should know how to build your project.
- You should know how you're going to test your project.

**PMs Lead**

First, lead the team in a discussion of the grading criteria. What implications does it have for your work that you haven't already accounted for?

Next, review your plan to make sure everyone agrees on it:

- Who owns what?
- What are your milestones?
- How will you communicate and coordinate your work?
- How will you use your time over the next four weeks?

> **What to Submit**

> At the time of your product’s (beta?) release, you should submit:

- well-documented source code;
- documentation describing how to install and use your software (consider using Docker);
- tests, including automation for running the tests, and for determining code coverage;
- known bugs;
- a contributions statement.
- a demo or a video showing a walkthrough of your product:
    - **Demos will be on December 4, during the regular lecture time in Kaiser 2020/2030**
    - Video submission only needed if live demo cannot be done for any purpose. 

# Evaluate and Triage

## Evaluate

Now that every team has launched, it's time to find out whether these applications are functionally correct. Your job is to **find failures** in other team's applications.

- **Major**. Functionality cannot be used to accomplish the intended task. (Remember that this includes usability issues that prevented someone from being able to understand how to accomplish the intended task).
- **Minor**. Functionality can be used to accomplish the intended task, but requires a workaround or understanding a design choice with poor usability to be used successfully.

For each one, use the application, trying all of its major features, filing bugs **in the team's GitHub Issues page** for each problem you find, marking their severity with the labels above. Expect to spend at least **10** minutes with each application, for just over **1 hour** of testing.

To structure your testing, consider using the Black Box Testing. It gives you a basic outline for how to test systematically and document your findings.

Read the existing list of issues before you file your bug to avoid filing duplicate reports. We won't give credit for issues that a team deems a duplicate. This is an incentive to avoid duplicates, to test thoroughly, and to test early. (When you mark something a duplicate, make sure you're not marking the first submitter's a duplicate—they're the one that deserves credit).

Note that you can fix defects reported by others as soon as they're reported; you don't have to wait until after the evaluation period. Schedule time after the release deadline to triage, diagnose, and repair issues to minimize the potential for other major defects being reported.

## Triage

Now that you have a set of issues reported by your classmates, your team's job is to triage and repair them, releasing a patch. Use the [issue triage strategy](https://www.chromium.org/for-testers/bug-reporting-guidelines/triage-best-practices/). 

> For this term, you do not need to release a patch: triaging the issues is sufficient.

# Reflect

Write a ~**1,000 word statement**, with a paragraph about each question:

- **What worked well about your team's process?** Why?
- **What did not work well about your team's process?** Why?
- **What tasks and activities did you personally do well?** Why do you think you excelled at them?
- **What tasks and activities did you personally do poorly?** Why do you think you struggled with them? What might might you do to improve in the future?
- **Does anyone on your team deserve recognition as an MVP (Most Valuable Player) (optional)?** The MVP should epitomize some combination of leadership, open-mindedness, honesty, resilience, resourcefulness, and persistence. Describe two examples of a time this teammate exhibited these qualities.
- **Are there any teammates you would like to "fire" (optional)?** (If everyone on a team fires the same person, they lose 15% of their project grade.) Justification for firing include major failures to fulfill the duties of their roles:
    - A project manager failing to manage the project.
    - A designer that didn't design.
    - A developer that didn't build.
    - Any teammate that minimally contributed to the team's goals.
    - Any teammate that was severely unresponsive, uncommunicative, or unreliable.

**How to submit it?**
Put your reflections in a filename `reflections.md` after creating a repo using this link: [https://classroom.github.com/a/kWRAavkw](https://classroom.github.com/a/kWRAavkw)
This is to be done individually. 

---

# Milestones

<figure class="project-figure project-figure--wide">
  <img src="{{ '/assets/images/milestone-trail-marker.jpeg' | relative_url }}" alt="A yellow trail marker painted on a rock beside a mountain path, indicating an elevation of 2,000 metres.">
  <figcaption>The milestone schedule divides the project into staged submissions.</figcaption>
</figure>

- The project has a weight of 25, which is divided across the different phases/aspects of project work. 
- Each milestone covers one or more phases of project development, and there is a submission associated with each milestone. 
- We will assign a letter grade/score (between 0 and 10) for each submission.
- Deadline is  EOD (11:59pm) for any milestone date. (E.g., October 27 deadline, means October 27, 11:59pm)

> **Milestone 1 (October 27)**

- [Design your Team](#design-your-team) (points: 3)
- [Design Your Solution](#design-your-solution) (points: 2)

> **Milestone 2 (October 31)**

- [Requirements](#requirements) (points: 2)
- [Architecture](#architecture) (points: 2)

> **Milestone 3 (November 7)**

- [Plan](#plan) (points: 6)

> **Milestone 4 (**~~**November 28**~~ **November 30)**

- [Release](#release) (points: 5)

> **Milestone 5 (December 6)**

- [Evaluate and Triage](#evaluate-and-triage) (points: 2, “Evaluate" only)

> **Milestone 6 (December 9)**

- Triage (point: 1)
- [Reflect](#reflect) (points: 2 -- completed individually)

---

# Notes

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
