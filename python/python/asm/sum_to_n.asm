; Implements the same logic as sum_to_n in workloads.py

global _start

section .text

_start:
    mov rbx, 1      ; current i
    mov rcx, 5      ; n
    mov r8, 0       ; total

loop_start:
    add r8, rbx     ; total += i
    inc rbx         ; i += 1
    cmp rbx, rcx    ; compare i with n
    jg done         ; if i > n, stop
    jmp loop_start  ; otherwise continue

done:
    mov rax, 60
    mov rdi, 0
    syscall
