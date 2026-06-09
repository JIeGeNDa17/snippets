export const chunk = (arr, n) => Array.from({length: Math.ceil(arr.length/n)}, (_, i) => arr.slice(i*n, i*n+n));
