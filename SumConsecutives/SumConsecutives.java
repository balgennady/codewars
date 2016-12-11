/*
	You are given a list/array which contains only integers (positive and negative). 
	Вам предоставляется список/массив, содержащий только целые числа (положительные и отрицательные).
	Your job is to sum only the numbers that are the same and consecutive. 
	Ваша работа состоит в том, чтобы подвести только цифры, которые являются одинаковыми и последовательными.
	The result should be one list.
	Результат должен быть один список. 
	Extra credit if you solve it in one line.
	Дополнительный кредит, если вы решите его в одной строке. 
	You can asume there is never an empty list/array and there will always be an integer.
	Вы можете предполагаю, что никогда не пустой список / массив и всегда будет целым.

	[1,4,4,4,0,4,3,3,1] # должен вернуть [1,12,0,4,6,1]

	"""So as you can see sum of consecutives 1 is 1 
	sum of 3 consecutives 4 is 12 
	sum of 0... and sum of 2 
	consecutives 3 is 6 ..."""
	[1,1,7,7,3] # should return [2,14,3]
	[-5,-5,7,7,12,0] # should return [-10,14,12,0]
*/

package br.com.urban.codewars.kyu6; 
 
import java.util.ArrayList; 
import java.util.List; 
 
public class SumConsecutives { 
 
	public static List<Integer> sumConsecutives(List<Integer> s) { 
		
		List<Integer> result = new ArrayList<>(); 
		 
		int checker = s.get(0); 
		int sum = 0; 
		 
		for(int i : s) { 
			if(i == checker) { 
				sum += i; 
			} else { 
				result.add(sum); 
				checker = i; 
				sum = i; 
			} 
		} 
		 
		result.add(sum); 
		 
		return result; 
	} 
}