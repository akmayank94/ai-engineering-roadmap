# 📝 Observations

This document contains my observations, analysis, and conclusions drawn from each experiment.

---

# Experiment 1

## Research Question

Does prompt length affect token usage?

---

## Hypothesis

Longer prompts should consume more prompt tokens than shorter prompts.

---

## Observation

The experiment confirmed that prompt token count increases gradually as the input becomes longer.

Examples:

| Prompt | Prompt Tokens |
|---------|--------------:|
| Hi | 36 |
| Hello | 36 |
| Hello World | 37 |
| Explain AI. | 39 |
| Explain Artificial Intelligence in detail. | 42 |

Longer prompts also encouraged the model to generate longer responses. Since the response limit was set to **100 tokens**, the longer prompts reached this limit and stopped with:

```
finish_reason = length
```

---

## Conclusion

Prompt length has a direct impact on token usage.

Even small increases in prompt size result in additional prompt tokens. Larger prompts also tend to generate longer responses, increasing overall token consumption.

---

# Experiment 2

## Research Question

Does language affect token usage?

---

## Hypothesis

English should consume fewer prompt tokens than Hindi or Hinglish.

---

## Observation

The experiment showed a clear progression:

```
English
     ↓
Hinglish
     ↓
Hindi
```

Prompt token usage increased in the same order.

| Language | Prompt Tokens |
|----------|--------------:|
| English | 40 |
| Hinglish | 44 |
| Hindi | 51 |

For longer prompts:

| Language | Prompt Tokens |
|----------|--------------:|
| English | 43 |
| Hindi | 59 |

The Hindi prompt required **16 additional prompt tokens** for expressing nearly the same meaning.

---

## Production Insight

In multilingual AI applications, language selection can influence API costs.

Applications serving large numbers of users should monitor token usage across different languages to better estimate operational costs.

---

## Conclusion

Language has a measurable effect on token usage.

Among the tested prompts, English proved to be the most token-efficient language, followed by Hinglish and then Hindi.