package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {

	// Пример
	l1 := &ListNode{2, &ListNode{4, &ListNode{3, nil}}}
	l2 := &ListNode{5, &ListNode{6, &ListNode{4, nil}}}
	result := addTwoNumbers(l1, l2)

	// Вывод результата
	for result != nil {
		fmt.Print(result.Val)
		result = result.Next
	}
	// Ожидаемый вывод: 708

}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{} // фиктивный узел для упрощения работы со списком
	current := dummy     // указатель на текущий узел в результирующем списке
	carry := 0           // переменная для хранения переноса

	// Проходим по всем узлам списков l1 и l2
	for l1 != nil || l2 != nil || carry != 0 {
		var x, y int
		if l1 != nil {
			x = l1.Val // Значение текущего узла в l1
			l1 = l1.Next
		}
		if l2 != nil {
			y = l2.Val // Значение текущего узла в l2
			l2 = l2.Next
		}

		sum := x + y + carry                    // Сумма текущих значений и переноса
		carry = sum / 10                        // Обновляем перенос
		current.Next = &ListNode{Val: sum % 10} // Создаем новый узел с результатом и добавляем его в список
		current = current.Next                  // Переходим к следующему узлу
	}

	return dummy.Next // Возвращаем следующий узел после фиктивного узла
}
