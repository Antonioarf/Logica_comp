; constantes
SYS_EXIT equ 1
SYS_READ equ 3
SYS_WRITE equ 4
STDIN equ 0
STDOUT equ 1
True equ 1
False equ 0

segment .data

segment .bss  ; variaveis
  res RESB 1

section .text
  global _start

print:  ; subrotina print

  PUSH EBP ; guarda o base pointer
  MOV EBP, ESP ; estabelece um novo base pointer

  MOV EAX, [EBP+8] ; 1 argumento antes do RET e EBP
  XOR ESI, ESI

print_dec: ; empilha todos os digitos
  MOV EDX, 0
  MOV EBX, 0x000A
  DIV EBX
  ADD EDX, '0'
  PUSH EDX
  INC ESI ; contador de digitos
  CMP EAX, 0
  JZ print_next ; quando acabar pula
  JMP print_dec

print_next:
  CMP ESI, 0
  JZ print_exit ; quando acabar de imprimir
  DEC ESI

  MOV EAX, SYS_WRITE
  MOV EBX, STDOUT

  POP ECX
  MOV [res], ECX
  MOV ECX, res

  MOV EDX, 1
  INT 0x80
  JMP print_next

print_exit:
  POP EBP
  RET

; subrotinas if/while
binop_je:
  JE binop_true
  JMP binop_false

binop_jg:
  JG binop_true
  JMP binop_false

binop_jl:
  JL binop_true
  JMP binop_false

binop_false:
  MOV EBX, False
  JMP binop_exit
binop_true:
  MOV EBX, True
binop_exit:
  RET

_start:

  PUSH EBP ; guarda o base pointer
  MOV EBP, ESP ; estabelece um novo base pointer

  ; codigo gerado pelo compilador
PUSH DWORD 0
mov ebx, 5 ; 102
mov [ebp- 4], ebx
while102:
mov ebx,  [ebp- 4] ; 104
push ebx ;103
mov ebx, 10 ; 105
pop eax ;103
cmp eax, ebx ;103
call binop_jl ;103
cmp ebx, 0 ; COMP WHILE
je endwhile102
mov ebx,  [ebp- 4] ; 206
push ebx ;205
mov ebx, 1 ; 207
pop eax ;205
add eax, ebx ;205
mov ebx, eax ;205
mov [ebp- 4], ebx
mov ebx,  [ebp- 4] ; 206
push ebx ;205
CALL print ;205
pop ebx ;205
jmp while102
endwhile102:
mov ebx, 99 ; 105
push ebx ;104
CALL print ;104
pop ebx ;104

  ; interrupcao de saida
  POP EBP
  MOV EAX, 1
  INT 0x80