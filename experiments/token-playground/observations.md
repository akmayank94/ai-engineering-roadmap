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

---

# Experiment 3

## Research Question

Do emojis and Unicode characters increase token usage?

---

## Hypothesis

Prompts containing emojis should consume more prompt tokens than plain text because emojis are represented using Unicode characters.

Different emojis may also consume different numbers of tokens depending on how the tokenizer represents them.

---

## Observation

The experiment confirmed that adding emojis increased prompt token usage.

Interestingly, different emojis did not consume the same number of prompt tokens.

Examples:

| Prompt | Prompt Tokens |
|---------|--------------:|
| Hello | 36 |
| Hello 😊 | 38 |
| Hello 😊😊😊 | 42 |
| Hello ❤️ | 38 |
| Hello 🚀🚀🚀 | 45 |
| 🔥 AI Engineering 🚀 | 43 |

The Rocket emoji consumed noticeably more prompt tokens than the Smile emoji when repeated multiple times.

This demonstrates that Unicode characters are not tokenized equally.

---

## Production Insight

Applications such as messaging platforms, social media assistants, and customer support bots often process emojis.

Heavy emoji usage can slightly increase API costs when operating at large scale.

---

## Conclusion

Emojis increase prompt token usage.

Different Unicode characters have different tokenization behaviour, meaning visually similar prompts may have different token costs.

---

# Experiment 4

## Research Question

Does punctuation affect token usage?

---

## Hypothesis

Adding punctuation should slightly increase prompt token usage.

Repeated punctuation should require additional prompt tokens.

---

## Observation

The experiment produced an interesting result.

Examples:

| Prompt | Prompt Tokens |
|---------|--------------:|
| Hello | 36 |
| Hello. | 37 |
| Hello... | 37 |
| Hello!!!!! | 37 |
| Hello???? | 37 |
| Hello?!?!?! | 39 |

Although punctuation increased token usage, repeated punctuation did not continue increasing prompt tokens.

Only mixed punctuation (`?!?!?!`) consumed additional prompt tokens.

This suggests that tokenizers recognize many common punctuation patterns as reusable token sequences.

---

## Production Insight

Prompt optimization is more complex than simply counting characters.

Understanding tokenizer behaviour can help developers write shorter and more cost-efficient prompts.

---

## Conclusion

Tokenization depends on learned vocabulary rather than individual characters.

Common punctuation patterns may be compressed into fewer tokens than expected.

---

# Experiment 5

## Research Question

Does temperature affect token usage or only response creativity?

---

## Hypothesis

Temperature should mainly affect creativity while leaving prompt token usage unchanged.

---

## Observation

The prompt token count remained exactly the same for every temperature tested.

Only the generated responses became more creative and varied as the temperature increased.

Because `max_tokens` was fixed at **100**, every response stopped due to:

```
finish_reason = length
```

This prevented response length from varying significantly across different temperature values.

---

## Production Insight

Temperature is primarily a creativity control rather than a cost optimization parameter.

Developers can adjust response style without changing the number of prompt tokens sent to the model.

---

## Conclusion

Temperature changes how the model responds, not how the prompt is tokenized.

Higher temperatures produce more diverse responses while prompt token usage remains constant.

---

# Experiment 6

## Research Question

Does adding a system prompt increase prompt token usage?

---

## Hypothesis

Every system prompt should increase prompt token usage because system instructions become part of every API request.

---

## Observation

The experiment confirmed that every system prompt increased prompt token usage.

Different system personas also changed the tone and behaviour of the generated responses.

| System Prompt | Prompt Tokens |
|--------------|--------------:|
| None | 43 |
| CEO | 50 |
| Comedian | 49 |
| Lawyer | 49 |
| Grandma | 49 |

Although the response style changed dramatically, the increase in prompt tokens was relatively small.

---

## Production Insight

Large production systems send system prompts with every request.

Keeping system prompts concise helps reduce token consumption across millions of API calls.

---

## Conclusion

System prompts introduce measurable prompt overhead while providing powerful control over model behaviour.

Well-designed system prompts balance instruction quality with token efficiency.

---

# Experiment 7

## Research Question

How does conversation history affect prompt token usage?

---

## Hypothesis

Prompt token usage should continuously increase as conversation history grows.

---

## Observation

The experiment showed a significant increase in prompt token usage even with a short conversation.

The five-message conversation required:

| Metric | Value |
|--------|------:|
| Prompt Tokens | 82 |
| Completion Tokens | 11 |
| Total Tokens | 93 |

Unlike single prompts, conversational applications repeatedly send previous messages back to the model, causing prompt token usage to grow over time.

---

## Production Insight

Conversation history is one of the largest contributors to API cost in chatbot applications.

Many production systems periodically summarize or remove older messages to reduce token consumption and remain within the model's context window.

---

## Conclusion

Conversation memory provides context but increases API cost.

Managing conversation history efficiently is an important engineering consideration when building scalable AI assistants.

---

# Experiment 8

## Research Question

How do Large Language Models respond to unsafe prompts?

---

## Hypothesis

The model should refuse harmful requests while providing a safe alternative response.

---

## Observation

Every unsafe prompt resulted in a refusal rather than harmful instructions.

Interestingly, every response finished with:

```
finish_reason = stop
```

instead of an error or interruption.

This indicates that the model successfully generated a complete safety response rather than terminating the request unexpectedly.

---

## Production Insight

Modern LLMs are trained to redirect harmful requests toward safer information.

Application developers should still implement additional guardrails because model-level safety should not be considered the only protection mechanism.

---

## Conclusion

The model consistently refused unsafe requests while maintaining a normal completion flow.

Safety mechanisms operate as part of the model's response generation rather than simply blocking the request.

---

# 🎯 Overall Findings

Across all completed experiments, several consistent patterns emerged:

- Prompt length directly influences prompt token usage.
- Tokenization is vocabulary-based rather than character-based.
- English prompts are more token-efficient than equivalent Hindi prompts.
- Emojis and Unicode characters increase prompt token usage.
- Temperature changes creativity but not prompt tokenization.
- System prompts introduce additional prompt overhead.
- Conversation history significantly increases API cost.
- Modern LLMs safely refuse harmful requests while completing the interaction normally.

## Final Reflection

This project transformed theoretical concepts into measurable observations through practical experimentation.

Instead of assuming how Large Language Models behave, each experiment tested a hypothesis, collected real API data, analyzed the results, and documented engineering insights.

These experiments helped build a stronger intuition about tokenization, prompt engineering, production costs, and scalable AI system design.