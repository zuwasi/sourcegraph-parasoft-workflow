# Demo transcript

## Scene 01

The Rule 7.5 Zero Program. Sourcegraph finds, Parasoft decides. In about three minutes, we take a real C code base from one thousand and ninety five MISRA C 2025 findings to a verified, revertable zero.

## Scene 02

iso14229 is a real open source diagnostic protocol stack. About seven and a half thousand lines of C. A full MISRA C 2025 scan reports one thousand and ninety five findings, and every one of them needs a decision. Nobody clicks through a thousand rows by hand.

## Scene 03

The pilot starts with one rule. MISRA C 2025 Rule 7.5 bans suffixes and minus signs inside INT N C macros. One Sourcegraph query finds every candidate in the seed module. Eleven results, in about a tenth of a second.

## Scene 04

The fix is a versioned script, not a one off patch. Two value preserving transforms: strip the suffix, and move the minus sign outside the macro. Two edge cases are excluded and routed to an expert. The values are identical before and after.

## Scene 05

After the fix, the same guard query returns zero. Even the script's own documentation cannot fool the search.

## Scene 06

Parasoft C/C++test is the judge. The seed verification scan reports zero findings left, while the baseline had eight. Search found the sites; Parasoft decided.

## Scene 07

Now scale up. The whole repository, no seed involved. One thousand and ninety five findings. The biggest mechanical classes are assert macro artifacts, implicit integer tests, and missing unsigned suffixes.

## Scene 08

Each fix is one commit on its own stacked branch. The assert macro rewrite removes one hundred and twenty three findings. Unsigned typedefs remove sixty eight. Explicit comparisons remove thirty four. Reversing any step is one git command.

## Scene 09

One verification scan confirms it. One thousand and ninety five becomes seven hundred and sixty six. Three hundred and twenty nine findings removed by mechanical rewrites, and five rule classes now sit at zero.

## Scene 10

Holding zero. Sourcegraph detects, and the code host enforces. The same query runs on every pull request in under a second. Parasoft runs in the pipeline. Code Monitor watches for regressions.

## Scene 11

The Rule 7.5 Zero Program, by Engineering Software Lab. Thank you for watching.
