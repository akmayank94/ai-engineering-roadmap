# 🔮 Experiment Hypotheses

> This document records my predictions before running each experiment.
>
> The purpose is to compare expectations with actual experimental results and improve my understanding of Large Language Models (LLMs) and tokenization.

---

# Experiment 1 — Prompt Length vs Token Usage

## Research Question

**Does increasing the length of a prompt increase the number of prompt tokens used by an LLM?**

### Prediction

I expect prompt token usage to increase as the prompt becomes longer.

Very short prompts such as **"Hi"** should consume the fewest prompt tokens, while detailed prompts should consume more prompt tokens because they contain more text for the tokenizer to process.

I also expect longer prompts to encourage the model to generate longer responses, increasing the overall token usage.

---

# Experiment 2 — English vs Hindi vs Hinglish

## Research Question

**Does the language of a prompt affect token usage?**

### Prediction

I expect English to consume the fewest prompt tokens.

I predict Hinglish will require more prompt tokens than English but fewer than Hindi because it combines English words with Hindi grammar.

I expect Hindi to consume the highest number of prompt tokens because many tokenizers are optimized primarily for English text, meaning Devanagari script may require additional tokens to represent similar information.

---

# Experiment 3 — Emojis & Special Characters

## Research Question

**Do emojis increase token usage?**

### Prediction

I expect prompts containing emojis to consume more prompt tokens than plain text.

I also predict that different emojis may require different numbers of tokens depending on how the tokenizer represents each Unicode character.

Multiple emojis should consume progressively more prompt tokens.

---

# Experiment 4 — Punctuation Impact

## Research Question

**Does punctuation affect token usage?**

### Prediction

I expect punctuation marks to increase token usage slightly.

Repeated punctuation such as:

```
!!!!
```

or

```
.....
```

may consume additional prompt tokens because they introduce extra characters that need to be tokenized.

However, I do not expect the increase to be significant.

---

# Experiment 5 — max_tokens Comparison

## Research Question

**How does changing `max_tokens` affect the generated response?**

### Prediction

I expect smaller values of `max_tokens` to produce shorter responses.

Whenever the response reaches the specified limit, I expect:

```
finish_reason = length
```

Larger values should allow the model to produce more complete answers.

---

# Experiment 6 — Temperature vs Token Usage

## Research Question

**Does temperature affect token usage or only response creativity?**

### Prediction

I expect temperature to primarily affect creativity and randomness rather than prompt token usage.

Prompt token count should remain unchanged because the input prompt is identical.

Completion token usage may vary slightly because more creative responses can become longer or shorter depending on the generated content.

---

# Experiment 7 — System Prompt Overhead

## Research Question

**Does adding a system prompt increase token usage?**

### Prediction

I expect every system prompt to increase prompt token usage because the system instructions become part of the input sent to the LLM.

Longer system prompts should consume noticeably more prompt tokens than shorter ones.

---

# Experiment 8 — Conversation History Growth

## Research Question

**How does conversation history affect token usage?**

### Prediction

I expect prompt token usage to continuously increase as more conversation history is added.

Since every previous message is included in the request, longer conversations should become progressively more expensive.

This is one of the primary reasons production AI chatbots implement memory management and conversation summarization.

---

# Experiment 9 — Safety Responses

## Research Question

**How do LLMs behave when given unsafe prompts?**

### Prediction

I expect the model to refuse requests involving harmful or dangerous instructions.

Instead of providing unsafe content, I expect the model to generate a safe alternative response.

The response should most likely finish with:

```
finish_reason = stop
```

because the refusal itself is considered a valid completion.

---

# Experiment 10 — Token Cost Calculator

## Research Question

**Can token usage be converted into an estimated API cost?**

### Prediction

I expect a simple mathematical formula to accurately estimate the approximate cost of an API request once the provider's pricing is known.

This experiment should demonstrate how production systems estimate operational expenses before deployment.

---

# 🎯 Goal of These Experiments

Rather than accepting theoretical explanations, this project aims to verify important AI Engineering concepts through practical experimentation.

Each hypothesis will be compared with real experimental results to better understand how modern Large Language Models behave in real-world scenarios.