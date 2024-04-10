#!/usr/bin/node
const dict =  require ('./101-data.js').dict;
const newdict = Object.values(dict).reduce((acc, users) => {
		acc[users.occurrences].push(user.id);
	});
return acc;
console.log(newdict);
