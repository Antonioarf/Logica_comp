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
mov ebx, 2 ; 101
mov [ebp- 4], ebx
PUSH DWORD 0
mov ebx,  [ebp- 4] ; 104
push ebx ;103
mov ebx, 2 ; 105
pop eax ;103
cmp eax, ebx ;103
call binop_je ;103
mov [ebp- 8], ebx
mov ebx,  [ebp- 4] ; 105
push ebx ;104
mov ebx,  [ebp- 8] ; 106
pop eax ;104
add eax, ebx ;104
mov ebx, eax ;104
push ebx ;103
CALL print ;103
pop ebx ;103
mov ebx,  [ebp- 4] ; 107
push ebx ;106
mov ebx,  [ebp- 8] ; 108
pop eax ;106
sub eax, ebx ;106
mov ebx, eax ;106
push ebx ;105
CALL print ;105
pop ebx ;105
mov ebx,  [ebp- 4] ; 109
push ebx ;108
mov ebx,  [ebp- 8] ; 110
pop eax ;108
mul eax, ebx ;108
mov ebx, eax ;108
push ebx ;107
CALL print ;107
pop ebx ;107
mov ebx,  [ebp- 4] ; 111
push ebx ;110
mov ebx,  [ebp- 8] ; 112
pop eax ;110
div eax, ebx ;110
mov ebx, eax ;110
push ebx ;109
CALL print ;109
pop ebx ;109
mov ebx,  [ebp- 4] ; 113
push ebx ;112
mov ebx,  [ebp- 8] ; 114
pop eax ;112
cmp eax, ebx ;112
call binop_je ;112
push ebx ;111
CALL print ;111
pop ebx ;111
mov ebx,  [ebp- 4] ; 115
push ebx ;114
mov ebx,  [ebp- 8] ; 116
pop eax ;114
cmp eax, ebx ;114
call binop_jl ;114
push ebx ;113
CALL print ;113
pop ebx ;113
mov ebx,  [ebp- 4] ; 117
push ebx ;116
mov ebx,  [ebp- 8] ; 118
pop eax ;116
cmp eax, ebx ;116
call binop_jg ;116
push ebx ;115
CALL print ;115
pop ebx ;115

  ; interrupcao de saida
  POP EBP
  MOV EAX, 1
  INT 0x80