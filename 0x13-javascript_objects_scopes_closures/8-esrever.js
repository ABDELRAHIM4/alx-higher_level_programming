#!/usr/bin/node
exports.esrever = function (list){
	if (list.length == 0)
	{
		return [];
	}
	const reverselist = [];
	for (let x = list.length - 1;x >= 0; x--)
	{
		reverselist.push(list[x]);
	}
	return reverselist;
}
