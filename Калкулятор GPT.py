#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast

# ------------------------------------------------------------
# 1. Функция безопасного вычисления выражения
# ------------------------------------------------------------
def eval_expr(expr: str) -> float:
    """
    Принимает строку, содержащую арифметическое выражение,
    парсит её в AST и вычисляет результат.
    Поддерживаются:
        - числа (целые и плавающие)
        - +, -, *, /, //, %, **  (по приоритету)
        - скобки
        - унарные + и -
    """
    try:
        # Парсим строку в AST в режиме выражения (eval)
        node = ast.parse(expr, mode='eval')
        return _eval(node.body)
    except ZeroDivisionError:
        raise ValueError("Ошибка: деление на ноль")
    except Exception as exc:
        raise ValueError(f"Неверное выражение: {exc}")

# ------------------------------------------------------------
# 2. Рекурсивный разбор узлов AST
# ------------------------------------------------------------
def _eval(node: ast.AST) -> float:
    """
    Рекурсивно вычисляет значение узла AST.
    """
    if isinstance(node, ast.Constant):          # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"Неверный тип константы: {type(node.value)}")

    if isinstance(node, ast.Num):               # Python <3.8
        return node.n

    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Div):
            return left / right
        if isinstance(node.op, ast.FloorDiv):
            return left // right
        if isinstance(node.op, ast.Mod):
            return left % right
        if isinstance(node.op, ast.Pow):
            return left ** right

        raise ValueError(f"Неподдерживаемая бинарная операция: {type(node.op)}")

    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)

        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand

        raise ValueError(f"Неподдерживаемая унарная операция: {type(node.op)}")

    raise ValueError(f"Неподдерживаемый тип узла: {type(node)}")

# ------------------------------------------------------------
# 3. Консольный интерфейс
# ------------------------------------------------------------
def main() -> None:
    print("=== Калькулятор ===")
    print("Введите арифметическое выражение.")
    print("Команды выхода: 'выход', 'q', 'exit', 'quit'.")

    while True:
        try:
            expr = input(">>> ").strip()
        except EOFError:          # Ctrl-D
            break

        if not expr:
            continue

        if expr.lower() in {"выход", "q", "exit", "quit"}:
            print("До свидания!")
            break

        try:
            result = eval_expr(expr)
            print("Ответ:", result)
        except ValueError as err:
            print("Ошибка:", err)

# ------------------------------------------------------------
# 4. Точка входа
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
