# LinkedIn Post: The Compliance Stack Is About to Flip

---

I built an AML engine with 28 rules and a 94.9% detection rate.

Then I realized it was clapping for itself.

The rules I wrote AND the tests I ran came from the same head. If the same person writes the detector and the test data, you're not testing detection. You're testing taste.

That's where every bank sits today. Rules catch the obvious. ML classifiers catch what investigators already know how to find. Nothing catches what hasn't been seen yet.

Last week I benchmarked Amazon's Chronos-tiny (8M parameters, runs on a potato) on five crypto pairs. It couldn't predict direction. 52%. Coin flip.

But its uncertainty estimates tracked actual volatility almost perfectly. Before the market moved, the model widened its error bars. It couldn't tell me WHERE. But it could tell me HOW MUCH I didn't know.

That's the entire compliance problem restated.

We don't need to predict which transaction is the crime. We need to predict when our confidence is about to break. When a customer's trajectory leaves the envelope the model learned.

That's not classification. That's a world model.

And world models have one property regulators are going to love: because they imagine forward, you can ask them to SHOW their reasoning. Not a SHAP plot. A story. "Here are the three most likely futures for this customer."

EU AI Act hits August 2. AML is explicitly high-risk. Explainability isn't optional.

@Feedzai just shipped RiskFM. @Amazon built Chronos. The foundation model layer is here.

The banks have the data and none of the research. The labs have the research and none of the regulatory context. That gap is the biggest moat in finance right now.

I wrote up the full thesis: rules to classifiers to world models, the three-phase transition, and why the explainability story decides the next decade.

bionicbanker.tech/aml-world-models.html

#AML #FinancialCrime #AI #Compliance #WorldModels #FinTech

---

**First comment:**

The three phases:
Phase 1 (today): Rules dominant, ML re-ranks alerts. 80% detection on known typologies.
Phase 2 (now): Foundation models like @Feedzai RiskFM. Trained on 70B+ transactions.
Phase 3 (3-5 yrs): World models that predict customer trajectory drift, not just flag transactions.

Who's building Phase 3? That's the question.
