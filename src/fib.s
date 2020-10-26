   .arch armv7-m
   .eabi_attribute 20, 1
   .eabi_attribute 21, 1
   .eabi_attribute 23, 3
   .eabi_attribute 24, 1
   .eabi_attribute 25, 1
   .eabi_attribute 26, 2
   .eabi_attribute 30, 6
   .eabi_attribute 34, 1
   .eabi_attribute 18, 4
   .file   "fibonacci.c"
   .text
   .align  1
   .global main
   .syntax unified
   .thumb
   .thumb_func
   .fpu softvfp
   .type   main, %function
main:
   @ args = 0, pretend = 0, frame = 16
   @ frame_needed = 0, uses_anonymous_args = 0
   @ link register save eliminated.
   sub sp, sp, #16
   movs    r3, #0
   str r3, [sp, #12]
   movs    r3, #1
   str r3, [sp, #8]
   movs    r3, #0
   str r3, [sp, #4]
.L2:
   ldr r2, [sp, #12]
   ldr r3, [sp, #8]
   add r3, r3, r2
   str r3, [sp, #4]
   ldr r3, [sp, #8]
   str r3, [sp, #12]
   ldr r3, [sp, #4]
   str r3, [sp, #8]
   b   .L2
   .size   main, .-main
   .ident  "GCC: (GNU) 9.2.0"
   .section    .note.GNU-stack,"",%progbits
