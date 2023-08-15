#!/usr/bin/node
const dic = require('./101-data.js').dict;
const myDic = {};
for (const key in dic) {
  if (myDic[dic[key]]) myDic[dic[key]].push(key);
  else myDic[dic[key]] = [key];
}
console.log(myDic);
