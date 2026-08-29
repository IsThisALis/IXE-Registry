# Quick Reference

## Severity Matrix

| Severity | Crash? | Workaround? | Blocks Usage? | Example |
|----------|--------|-------------|---------------|---------|
| **S1** | Yes | No | Yes | Camera NPE on first use |
| **S2** | Maybe | Yes | No | Cleanup not executing |
| **S3** | No | N/A | No | Wrong log message |
| **S4** | No | N/A | No | Typo in README |

## Important Notes

1. **When in doubt, choose the HIGHER severity.** It's easier to downgrade than to explain why a critical bug was marked as minor.

2. **Context matters.** The same bug can be S1 or S2 depending on where it occurs:
   - Memory leak during gameplay → S1
   - Memory leak on exit → S2

3. **Security vulnerabilities are ALWAYS S1**, regardless of exploitability. If there's a potential path traversal or injection, mark it S1 and fix it first.

4. **Recurring issues.** If the same category (e.g., [MEM]) has 3+ S2 issues, consider it an architectural problem and create a meta-task with [ARC].
