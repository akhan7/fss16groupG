## Code7: early Termination

Can you learn when enough is enough.

If the code runs in "eras" of, say, 100 evals per era, how to test in era X that there has been no future improvement expected?

- Type1: just compare median performance scores (design challenge: what performance score to use?)
- Type2: Use effect size tests to just if the performance scores are not changing (design challenge: what threshold should you use for a "small effect"?)
- Type2: Use effect size + hypothesis test (bootstrap) to judge no improvement (design challenge: how many bootstraps to use?)

For DE and MWS and SA, code up the Type1,Type2, Type3 comparison operators and use them to:

+ Find the final era computed by DE, MWS, SA (with early termination)
+ Compute the cdom _loss_ numbers between era0 the final era
     + Important implementation note: repeat the above with 20 different baseline populations. For each baseline, run DE,MWS,SA.

     Apply the above for [DTLZ7](http://e-collection.library.ethz.ch/eserv/eth:24696/eth-24696-01.pdf)
     with 2 objectives 10 decisions.

ALso comment on the runtime implications (if any) of using  bootstrap.


## Abstract