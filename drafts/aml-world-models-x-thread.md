# X Thread: The Compliance Stack Is About to Flip

---

**Tweet 1:**
I built an AML engine with 22 rules and a 94.9% detection rate.

Then I realized the whole thing was clapping for itself.

Here's why compliance is about to go through the same phase shift image recognition went through in 2012. 🧵

**Tweet 2:**
Every AML system today does one of three things:

Rules. Classifiers. Or a sad hybrid where the rules do the real job and the classifier is a rubber stamp the vendor put on the invoice.

Rules catch the obvious. Classifiers catch what investigators already know. Nothing catches what hasn't been seen.

**Tweet 3:**
Last week I benchmarked @amazoncloud Chronos-tiny (8M params, runs on a potato) on 5 crypto pairs.

Direction prediction: 52%. Coin flip.

But its uncertainty tracked real volatility perfectly. Before the weirdness, it widened its error bars.

It couldn't tell me WHERE. But it told me HOW MUCH I didn't know.

**Tweet 4:**
That's the entire AML problem restated.

We don't need to predict which transaction is the crime.

We need to predict when our own confidence is about to break. When a customer leaves the envelope the model learned.

That's not classification. That's a world model.

**Tweet 5:**
Every world model (Dreamer V3, Chronos, DINO-WM, IRIS, Genie 3) is three Lego blocks:

1. Encoder (compress raw data to state)
2. Dynamics model (imagine next state)
3. Heads (ask questions of imagined state)

Now read that with AML in your head.

**Tweet 6:**
EU AI Act hits Aug 2. AML = high-risk. Models must be explainable.

World models have a property classifiers don't: they IMAGINE forward.

Ask them to SHOW reasoning: "Roll customer 10 steps. Three most likely futures. Which triggers the flag."

That's a story, not a SHAP plot. Stories pass audits.

**Tweet 7:**
The gap between Phase 1 (rules) and Phase 3 (world models) is the biggest moat in finance right now.

Banks have data, no research.
Labs have research, no regulatory context.
Fintechs build Phase 2 and call it Phase 3.

@Feedzai @amazoncloud @Google DeepMind are moving. Who's next?

Full writeup: bionicbanker.tech/aml-world-models.html
