#!/usr/bin/node
/*exports.converter = function (base){
	return function (num){
		const table = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
		let result = '';
		if (base == "10")
		{
			result = num;
		}
		else if (base == "16")
		{
			let digit = num % base;
			result = table.charAt(digit);
		}
		return result;
	};
};*/
exports.converter = function (base){
	return function (num){
		return Number(num).toString(base);
	}
};
