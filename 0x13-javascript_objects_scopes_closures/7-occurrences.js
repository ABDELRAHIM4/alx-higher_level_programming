#!/usr/bin/node
exports.nbOccurences = function (list, searchElement){
	let x = 0;
	for (let y = 0; y < list.length; y++)
	{
		if (list[y] == searchElement)
		{
			x += 1;
		}
	}
	return x;
}
