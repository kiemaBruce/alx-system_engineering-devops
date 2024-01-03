#!/usr/bin/env ruby
str = ""
if ARGV.length > 0
	matches = ARGV[0].scan(/School/)
	for match in matches
		str += match
	end
	puts str
end
