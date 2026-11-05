# Codewars Kata: `parts_sums` - Notes

**Goal:** For a list `ls`, return the sum of the whole list, then the sum after removing the first item, and so on, ending with `0`.

```
parts_sums([4, 3, 2, 1])  ->  [10, 6, 3, 1, 0]
```

The result always has **one more item** than the input.

---

## Key Takeaways

1. **Never add or remove items from a list while a `for` loop is walking through it.**
2. A `for` loop keeps a hidden index (0, 1, 2, ...) and does not care that the list is shrinking.
3. The result needs **one extra append** because the answer is one item longer than the input.
4. `sum([])` returns `0`, not blank.

---

## Mistake: looping over the list being shrunk

```python
def parts_sums(ls):
    new_ls = ls[:]
    sum_ls = []
    for i in new_ls:              # BUG: loops over the list we pop from
        sum_ls.append(sum(new_ls))
        if len(new_ls) == 0:
            break
        new_ls.pop(0)
    return sum_ls
```

Trace with `[4, 3, 2, 1]`:

| Trip | Hidden index | `new_ls` at start | Appended | `new_ls` after pop |
|------|--------------|-------------------|----------|--------------------|
| 1 | 0 | `[4, 3, 2, 1]` | 10 | `[3, 2, 1]` |
| 2 | 1 | `[3, 2, 1]` | 6 | `[2, 1]` |
| 3 | 2 | `[2, 1]` | loop stops (index 2 is past the end) | |

Result: `[10, 6]` (expected `[10, 6, 3, 1, 0]`)

The index goes up while the list goes down, so they meet in the middle and the loop ends early.

---

## Fix: loop over the untouched list

```python
def parts_sums(ls):
    new_ls = ls[:]
    sum_ls = []
    for _ in ls:                        # ls never changes, so 4 trips for 4 items
        sum_ls.append(sum(new_ls))      # record BEFORE popping
        new_ls.pop(0)
    sum_ls.append(sum(new_ls))          # new_ls is empty now -> appends 0
    return sum_ls
```

Trace with `[4, 3, 2, 1]`:

| Trip | `new_ls` at start | Appended | `new_ls` after pop |
|------|-------------------|----------|--------------------|
| 1 | `[4, 3, 2, 1]` | 10 | `[3, 2, 1]` |
| 2 | `[3, 2, 1]` | 6 | `[2, 1]` |
| 3 | `[2, 1]` | 3 | `[1]` |
| 4 | `[1]` | 1 | `[]` |
| after loop | `[]` | 0 | `[]` |

Result: `[10, 6, 3, 1, 0]`

---

## Why the append after the loop matters

| Version | Code after loop | Returns |
|---------|-----------------|---------|
| A | nothing | `[10, 6, 3, 1]` (missing the `0`) |
| B | `sum_ls.append(sum(new_ls))` | `[10, 6, 3, 1, 0]` |

- Each append inside the loop records the list **before** that trip's pop.
- The pop on the last trip empties the list, but nothing records that empty state yet.
- Version A never runs `sum()` on the empty list, so no fifth item is added (it is shorter, not blank).
- Version B runs `sum([])`, which is `0`, and appends it.

---

## Best solution: one sum, then subtract

```python
def parts_sums(ls):
    sums = []
    n = sum(ls)          # add everything once
    sums.append(n)
    for i in ls:         # ls is never modified
        n = n - i        # each remaining sum = previous - item just passed
        sums.append(n)
    return sums
```

Trace with `[4, 3, 2, 1]`:

| Step | `i` | `n` | `sums` |
|------|-----|-----|--------|
| before loop | | 10 | `[10]` |
| 1 | 4 | 6 | `[10, 6]` |
| 2 | 3 | 3 | `[10, 6, 3]` |
| 3 | 2 | 1 | `[10, 6, 3, 1]` |
| 4 | 1 | 0 | `[10, 6, 3, 1, 0]` |

**Why it is preferred:**
- Faster: sums the list once, then does one subtraction per trip.
- The fixed version above calls `sum(new_ls)` every trip, which re-adds the whole list and can time out on big inputs.
- The final `0` comes for free from the last subtraction.

---

## `for` vs `while`

- Use `for` when you know the number of trips in advance (one per item).
- Use `while` when you loop on a condition that is re-checked each trip. Shrinking a list is safe here:

```python
while len(new_ls) > 0:
    sum_ls.append(sum(new_ls))
    new_ls.pop(0)
```