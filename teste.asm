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
PUSH DWORD 0
PUSH DWORD 0
mov ebx, 5 ; 301
mov [ebp- 8], ebx
mov ebx, 2 ; 401
mov [ebp- 4], ebx
mov ebx, 1 ; 501
mov [ebp- 12], ebx
while600:
mov ebx,  [ebp- 4] ; 602
push ebx ;601
mov ebx,  [ebp- 8] ; 604
push ebx ;603
mov ebx, 1 ; 605
pop eax ;603
add eax, ebx ;603
mov ebx, eax ;603
pop eax ;601
cmp eax, ebx ;601
call binop_jl ;601
cmp ebx, 0 ; COMP WHILE
je endwhile600
mov ebx,  [ebp- 12] ; 604
push ebx ;603
mov ebx,  [ebp- 4] ; 605
pop eax ;603
mov eax, ebx ;603
imul ebx ;603
mov [ebp- 12], ebx
mov ebx,  [ebp- 4] ; 704
push ebx ;703
mov ebx, 1 ; 705
pop eax ;703
add eax, ebx ;703
mov ebx, eax ;703
mov [ebp- 4], ebx
jmp while600
endwhile600:
mov ebx,  [ebp- 12] ; 801
push ebx ;800
CALL print ;800
pop ebx ;800

  ; interrupcao de saida
  POP EBP
  MOV EAX, 1
  INT 0x80