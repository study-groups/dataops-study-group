# dataops-study-group
## Currently

Daphne Koller's thesis [From Knowledge to Belief](http://i.stanford.edu/pub/cstr/reports/cs/tr/94/1527/CS-TR-94-1527.pdf)

When acting in the real world, an intelligent agent must make decisions under uncertainty. For example, a doctor may need to decide upon the treatment for a particular patient. The
standard solution to this problem is based on decision theory. It requires the agent to assign
degrees of belief or sub jective probabilities to the relevant assertions. The degrees of belief
assigned should be based on the information available to the agent. A doctor, for example,
may have information about particular patients, statistical correlations between symptoms and
diseases, physical laws, default rules, and more. This thesis describes one approach, called the
random-worlds method, for inducing degrees of belief from very rich knowledge bases.


The random-worlds method is based on the principle of indierence: it treats as equally
likely all the worlds that the agent considers possible. It deals with knowledge bases expressed
in a language that augments rst-order logic with statistical statements. By interpreting default
rules as qualitative statistics, the approach integrates qualitative default reasoning with quantitative probabilistic reasoning. The thesis shows that a large number of desiderata that arise in
direct inference (reasoning from statistical information to conclusions about individuals) and in
default reasoning follow provably from the semantics of random worlds. Thus, random worlds
naturally derives important patterns of reasoning such as specicity, inheritance, indierence to
irrelevant information, and a default assumption of independence. Furthermore, the expressive
power of random worlds and its intuitive semantics allow it to deal well with examples that are
too complex for most other inductive reasoning systems.

The thesis also analyzes the problem of computing degrees of belief according to random
worlds. This analysis uses techniques from nite model theory and zero-one laws. We show
that, in general, the problem of computing degrees of belief is undecidable, even for knowledge
bases with no statistical information. On the other hand, for knowledge bases that involve
only unary predicates, there is a tight connection between the random-worlds method and the
principle of maximum entropy. In fact, maximum entropy can be used as a computational tool
for computing degrees of belief in many practical cases.

## Topics

- [Hosting](./hosting)
- [Scraping](./scraping)
- [Ingestion](./ingestion)
- [Modeling](./modeling)
- [Delivery](./delivery)
- [Presentation](./presentation)

# References
  - [DataOps is Not Just DevOps for Data](https://medium.com/data-ops/dataops-is-not-just-devops-for-data-6e03083157b7) by Chris Bergh
  - [DataOps Manifesto](http://dataopsmanifesto.org/) Sensible checklist for full stack data science.
  - [12 factors app](https://12factor.net/) the philosohpy behind DevOps, and now, DataOps
