# Architecture Notes

## Chosen Python function: `sum_to_n(n)`

### Python version

```python
def sum_to_n(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
```

### Assembly version

```asm
global _start

section .text

_start:
    mov rbx, 1
    mov rcx, 5
    mov r8, 0

loop_start:
    add r8, rbx
    inc rbx
    cmp rbx, rcx
    jg done
    jmp loop_start

done:
    mov rax, 60
    mov rdi, 0
    syscall
```

## Comparison

The Python function uses a loop to add numbers from 1 to n.

The assembly version does the same task, but in smaller steps. The CPU cannot understand a Python `for` loop directly, so the loop has to be broken into instructions.

The loop body in assembly is:
- `add r8, rbx`
- `inc rbx`
- `cmp rbx, rcx`
- `jg done`
- `jmp loop_start`

This shows that one Python loop becomes several assembly instructions.

## Loop condition

In Python, the `for` loop automatically moves through the values from 1 to `n`.

In assembly, the loop condition is controlled manually using `cmp` and `jg`. The processor compares the loop counter with the limit and jumps out of the loop when the counter becomes greater than `n`.

## Registers used

- `rbx` holds the loop counter
- `rcx` holds the limit `n`
- `r8` holds the accumulated result

There is no current list element in this example because `sum_to_n` does not use an array.

## Instructions per iteration

Each iteration of the loop uses 5 main instructions:
1. `add`
2. `inc`
3. `cmp`
4. `jg`
5. `jmp`

This demonstrates how assembly is more explicit than Python, because the programmer must control the loop and branching directly.
