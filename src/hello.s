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
	.file	"main.c"
	.text
	.align	1
	.global	main
	.syntax unified
	.thumb
	.thumb_func
	.fpu softvfp
	.type	main, %function
main:
	@ args = 0, pretend = 0, frame = 24
	@ frame_needed = 0, uses_anonymous_args = 0
	@ link register save eliminated.
	sub	sp, sp, #24
	movs	r3, #2
	str	r3, [sp, #12]
	movs	r3, #10
	str	r3, [sp, #8]
	movs	r3, #1
	str	r3, [sp, #20]
	movs	r3, #0
	str	r3, [sp, #16]
	b	.L2
.L3:
	ldr	r3, [sp, #20]
	ldr	r2, [sp, #12]
	mul	r3, r2, r3
	str	r3, [sp, #20]
	ldr	r3, [sp, #16]
	adds	r3, r3, #1
	str	r3, [sp, #16]
.L2:
	ldr	r2, [sp, #16]
	ldr	r3, [sp, #8]
	cmp	r2, r3
	blt	.L3
	movs	r3, #1
	str	r3, [sp, #4]
	ldr	r2, [sp, #4]
	ldr	r3, [sp, #8]
	lsl	r3, r2, r3
	str	r3, [sp, #4]
	ldr	r2, [sp, #20]
	ldr	r3, [sp, #4]
	cmp	r2, r3
	bne	.L4
	movs	r3, #0
	b	.L5
.L4:
	mov	r3, #-1
.L5:
	mov	r0, r3
	add	sp, sp, #24
	@ sp needed
	bx	lr
	.size	main, .-main
	.ident	"GCC: (GNU) 9.2.0"
	.section	.note.GNU-stack,"",%progbits
