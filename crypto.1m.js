#!/usr/bin/env /Users/ubik/.nvm/versions/node/v13.8.0/bin/node
const bitbar = require('bitbar');

bitbar([
	// {
	// 	text: '❤',
	// 	color: bitbar.darkMode ? 'white' : 'red',
	// 	dropdown: false
	// },
	bitbar.separator,
	{
		text: 'Unicorns',
		color: '#ff79d7',
		submenu: [
			{
				text: ':tv: Video',
				href: 'https://www.youtube.com/watch?v=9auOCbH5Ns4'
			},
			{
				text: ':book: Wiki',
				href: 'https://en.wikipedia.org/wiki/Unicorn'
			}
		]
	},
	bitbar.separator,
	'Ponies'
]);